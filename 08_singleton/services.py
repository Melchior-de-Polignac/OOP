from config_manager import ConfigManager


def start_application():
    config = ConfigManager.get_instance()
    message = f"Starting {config.get('app.name')} (debug={config.get('app.debug')})"
    print(message)
    return message


def connect_database():
    config = ConfigManager.get_instance()
    message = (
        f"Connecting to database at {config.get('database.host')}"
        f":{config.get('database.port')}"
    )
    print(message)
    return message


def send_email(to, subject):
    config = ConfigManager.get_instance()
    message = (
        f"Sending email from {config.get('email.sender')} "
        f"via {config.get('email.smtp_host')}"
    )
    print(message)
    return message


def process_payment(amount):
    config = ConfigManager.get_instance()
    message = f"Processing {amount}€ in {config.get('payment.environment')} mode"
    print(message)
    return message


if __name__ == "__main__":
    start_application()
    connect_database()
    send_email("user@test.com", "Welcome")
    process_payment(99.99)
