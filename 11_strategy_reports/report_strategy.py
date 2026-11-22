import json
from abc import ABC, abstractmethod
from pathlib import Path


class FormatStrategy(ABC):
    extension = ""

    @abstractmethod
    def render(self, data):
        pass


class PDFFormatStrategy(FormatStrategy):
    extension = ".pdf"

    def render(self, data):
        report = "PDF REPORT\n" + "=" * 50 + "\n"
        for item in data:
            report += f"| {item['name']:20} | {item['value']:10} |\n"
        return report + "=" * 50 + "\nEnd of PDF Report"


class ExcelFormatStrategy(FormatStrategy):
    extension = ".xlsx"

    def render(self, data):
        report = "EXCEL REPORT\n" + "-" * 50 + "\nName\tValue\n"
        for item in data:
            report += f"{item['name']}\t{item['value']}\n"
        return report + "-" * 50 + "\n"


class CSVFormatStrategy(FormatStrategy):
    extension = ".csv"

    def render(self, data):
        report = "name,value\n"
        for item in data:
            report += f"{item['name']},{item['value']}\n"
        return report


class JSONFormatStrategy(FormatStrategy):
    extension = ".json"

    def render(self, data):
        return json.dumps(data, indent=2)


class ReportGenerator:
    def __init__(self, data, strategy=None):
        self.data = data
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def generate_report(self):
        if self._strategy is None:
            raise RuntimeError("no format strategy set, call set_strategy() first")
        return self._strategy.render(self.data)

    def save_report(self, filename, directory=Path(".")):
        if self._strategy is None:
            raise RuntimeError("no format strategy set, call set_strategy() first")
        path = Path(directory) / f"{filename}{self._strategy.extension}"
        path.write_text(self._strategy.render(self.data))
        return path


if __name__ == "__main__":
    sales = [
        {"name": "Q1", "value": 15000},
        {"name": "Q2", "value": 18000},
        {"name": "Q3", "value": 21000},
    ]

    report = ReportGenerator(sales, CSVFormatStrategy())
    print(report.generate_report())

    report.set_strategy(JSONFormatStrategy())
    print(report.generate_report())
