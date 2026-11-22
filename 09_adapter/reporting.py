import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class LegacyReportGenerator:
    def generate_report(self, data):
        xml = "<report>\n"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        return xml + "</report>"


class AnalyticsDashboard:
    def display(self, json_data):
        print("=== Analytics Dashboard ===")
        for key, value in json.loads(json_data).items():
            print(f"  {key}: {value}")


class ReportGeneratorInterface(ABC):
    @abstractmethod
    def generate(self, data):
        pass


class LegacyReportAdapter(ReportGeneratorInterface):
    def __init__(self, legacy):
        self._legacy = legacy

    def generate(self, data):
        root = ET.fromstring(self._legacy.generate_report(data))
        return json.dumps({child.tag: self._convert(child.text) for child in root})

    @staticmethod
    def _convert(text):
        # xml gives text, so convert numbers back
        if text is None:
            return ""
        for convert in (int, float):
            try:
                return convert(text)
            except ValueError:
                pass
        return text


def show_report(generator, data):
    AnalyticsDashboard().display(generator.generate(data))


if __name__ == "__main__":
    adapter = LegacyReportAdapter(LegacyReportGenerator())
    show_report(adapter, {"total_sales": 150000, "orders": 1234})
    show_report(adapter, {"total_items": 5000, "low_stock": 45})
