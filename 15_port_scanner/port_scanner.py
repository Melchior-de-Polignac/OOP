import argparse
import json
import socket
from concurrent.futures import ThreadPoolExecutor


class PortScanner:
    def __init__(self, host="127.0.0.1", timeout=0.5):
        self.host = host
        self.timeout = timeout

    def scan_port(self, port):
        if not 1 <= port <= 65535:
            raise ValueError(f"port out of range: {port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(self.timeout)
            # connect_ex returns 0 when the connection works
            return sock.connect_ex((self.host, port)) == 0

    def scan_range(self, start_port, end_port, workers=50):
        if start_port > end_port:
            raise ValueError("start_port must not exceed end_port")
        ports = range(start_port, end_port + 1)
        # closed ports cost the timeout, so scan in parallel
        with ThreadPoolExecutor(max_workers=workers) as pool:
            results = list(pool.map(self.scan_port, ports))
        return [port for port, is_open in zip(ports, results) if is_open]

    def report(self, start_port, end_port):
        return {
            "host": self.host,
            "open_ports": self.scan_range(start_port, end_port),
        }


def main():
    parser = argparse.ArgumentParser(description="Scan a range of TCP ports.")
    parser.add_argument("-t", "--target", default="127.0.0.1")
    parser.add_argument("-sp", "--start-port", type=int, default=1000)
    parser.add_argument("-ep", "--end-port", type=int, default=8000)
    parser.add_argument("-o", "--output", default="scan_results.json")
    args = parser.parse_args()

    report = PortScanner(args.target).report(args.start_port, args.end_port)
    with open(args.output, "w") as json_file:
        json.dump(report, json_file, indent=4)
    print(f"open ports on {args.target}: {report['open_ports'] or 'none'}")
    print(f"saved to {args.output}")


if __name__ == "__main__":
    main()
