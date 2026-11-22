from abc import ABC, abstractmethod


class OrderComponent(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class BaseOrder(OrderComponent):
    def __init__(self, base_price):
        self._base_price = base_price

    def get_cost(self):
        return self._base_price

    def get_description(self):
        return f"Base price: {self._base_price:.2f}€"


class OrderDecorator(OrderComponent):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_cost(self):
        return self._wrapped.get_cost()

    def get_description(self):
        return self._wrapped.get_description()


class ExpressShippingDecorator(OrderDecorator):
    COST = 15.00

    def get_cost(self):
        return self._wrapped.get_cost() + self.COST

    def get_description(self):
        return f"{self._wrapped.get_description()}, Express shipping: +{self.COST:.2f}€"


class InsuranceDecorator(OrderDecorator):
    RATE = 0.05

    def get_cost(self):
        return self._wrapped.get_cost() * (1 + self.RATE)

    def get_description(self):
        return f"{self._wrapped.get_description()}, Insurance (5%)"


class GiftWrapDecorator(OrderDecorator):
    COST = 5.00

    def get_cost(self):
        return self._wrapped.get_cost() + self.COST

    def get_description(self):
        return f"{self._wrapped.get_description()}, Gift wrap: +{self.COST:.2f}€"


class DiscountDecorator(OrderDecorator):
    def __init__(self, wrapped, percent):
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        super().__init__(wrapped)
        self._percent = percent

    def get_cost(self):
        return self._wrapped.get_cost() * (1 - self._percent / 100)

    def get_description(self):
        return f"{self._wrapped.get_description()}, Discount ({self._percent:g}%)"


class PremiumMemberDecorator(OrderDecorator):
    RATE = 0.10

    def get_cost(self):
        return self._wrapped.get_cost() * (1 - self.RATE)

    def get_description(self):
        return f"{self._wrapped.get_description()}, Premium member (10%)"


if __name__ == "__main__":
    order = BaseOrder(100)
    order = ExpressShippingDecorator(order)
    order = InsuranceDecorator(order)
    order = GiftWrapDecorator(order)
    order = DiscountDecorator(order, 15)
    order = PremiumMemberDecorator(order)
    print(order.get_description())
    print(order.get_cost())
