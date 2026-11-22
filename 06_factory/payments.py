from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    method = ""
    error_message = "Invalid payment details"

    def process(self, amount, details):
        if not self.validate(details):
            return {"success": False, "error": self.error_for(details)}
        fee = round(self.fee(amount), 2)
        return {
            "success": True,
            "method": self.method,
            "amount": round(amount + fee, 2),
            "fee": fee,
        }

    @abstractmethod
    def validate(self, details):
        pass

    @abstractmethod
    def fee(self, amount):
        pass

    def error_for(self, details):
        return self.error_message


class CreditCardProcessor(PaymentProcessor):
    method = "credit_card"

    def validate(self, details):
        card = details.get("card_number", "")
        cvv = details.get("cvv", "")
        return len(card) == 16 and len(cvv) == 3

    def error_for(self, details):
        if len(details.get("card_number", "")) != 16:
            return "Invalid card number"
        return "Invalid CVV"

    def fee(self, amount):
        return amount * 0.029


class BankTransferProcessor(PaymentProcessor):
    method = "bank_transfer"
    error_message = "Invalid IBAN"

    def validate(self, details):
        return len(details.get("iban", "")) >= 15

    def fee(self, amount):
        return 1.50


class PayPalProcessor(PaymentProcessor):
    method = "paypal"
    error_message = "Invalid PayPal email"

    def validate(self, details):
        return "@" in details.get("email", "")

    def fee(self, amount):
        return amount * 0.034 + 0.30


class PaymentFactory:
    def __init__(self):
        self._processors = {
            "credit_card": CreditCardProcessor,
            "bank_transfer": BankTransferProcessor,
            "paypal": PayPalProcessor,
        }

    def register(self, payment_type, processor_class):
        self._processors[payment_type] = processor_class

    def get_processor(self, payment_type):
        processor_class = self._processors.get(payment_type)
        if processor_class is None:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()


if __name__ == "__main__":
    factory = PaymentFactory()
    print(factory.get_processor("paypal").process(100, {"email": "user@example.com"}))
    print(factory.get_processor("paypal").process(100, {"email": "nope"}))
    try:
        factory.get_processor("bitcoin")
    except ValueError as error:
        print(error)
