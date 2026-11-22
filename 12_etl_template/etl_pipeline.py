import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class DataPipeline(ABC):
    label = ""
    required_fields = ()

    def __init__(self, source):
        self.source = source
        self.data = None

    def run(self):
        self.connect()
        try:
            self.data = self.extract()
            print(f"Extracted {len(self.data)} records")
            self.transform(self.data)
            self.validate(self.data)
            self.load(self.data)
        finally:
            self.cleanup()  # runs even if validation fails
        return f"{self.label} Pipeline finished"

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    def validate(self, data):
        print("Validating data...")
        for record in data:
            if any(field not in record for field in self.required_fields):
                raise ValueError("Invalid record structure")
        print("Validation passed")

    def load(self, data):
        print("Loading data to destination...")
        print(f"Loaded {len(data)} records successfully")

    def cleanup(self):
        print("Cleaning up resources...")
        self.data = None
        print("Cleanup complete")


class CSVPipeline(DataPipeline):
    label = "CSV"
    required_fields = ("id", "name")

    def connect(self):
        print(f"Connecting to CSV file: {self.source}")

    def extract(self):
        return [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25},
        ]

    def transform(self, data):
        for record in data:
            record["age"] = int(record["age"])
            record["name"] = record["name"].upper()


class APIPipeline(DataPipeline):
    label = "API"
    required_fields = ("user_id", "username")

    def connect(self):
        print(f"Connecting to API: {self.source}")

    def extract(self):
        return [
            {"user_id": 101, "username": "charlie", "score": 85},
            {"user_id": 102, "username": "diana", "score": 92},
        ]

    def transform(self, data):
        for record in data:
            record["score"] = int(record["score"])
            record["username"] = record["username"].lower()
            record["grade"] = "A" if record["score"] >= 90 else "B"


class DatabasePipeline(DataPipeline):
    label = "Database"
    required_fields = ("product_id", "price")

    def connect(self):
        print(f"Connecting to database: {self.source}")

    def extract(self):
        return [
            {"product_id": 501, "product_name": "Laptop", "price": 1200},
            {"product_id": 502, "product_name": "Mouse", "price": 25},
        ]

    def transform(self, data):
        for record in data:
            record["price"] = float(record["price"])
            record["product_name"] = record["product_name"].title()
            record["tax"] = record["price"] * 0.2


class XMLPipeline(DataPipeline):
    label = "XML"
    required_fields = ("order_id", "customer")

    SAMPLE = (
        "<orders>"
        '<order id="7"><customer>  dupont </customer><total>40</total></order>'
        '<order id="8"><customer>martin</customer><total>15.5</total></order>'
        "</orders>"
    )

    def connect(self):
        print(f"Opening XML file: {self.source}")

    def extract(self):
        root = ET.fromstring(self.SAMPLE)
        return [
            {
                "order_id": int(order.get("id")),
                "customer": order.findtext("customer"),
                "total": order.findtext("total"),
            }
            for order in root
        ]

    def transform(self, data):
        for record in data:
            record["customer"] = record["customer"].strip().title()
            record["total"] = float(record["total"])


if __name__ == "__main__":
    for pipeline in (
        CSVPipeline("users.csv"),
        APIPipeline("https://api.example.com/users"),
        DatabasePipeline("postgresql://localhost/mydb"),
        XMLPipeline("orders.xml"),
    ):
        print(pipeline.run())
