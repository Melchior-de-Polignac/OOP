from html import escape

from report_strategy import FormatStrategy


class HTMLFormatStrategy(FormatStrategy):
    extension = ".html"

    def render(self, data):
        rows = "".join(
            f"<tr><td>{escape(str(item['name']))}</td>"
            f"<td>{escape(str(item['value']))}</td></tr>"
            for item in data
        )
        return "<table>\n<tr><th>Name</th><th>Value</th></tr>\n" + rows + "\n</table>"


if __name__ == "__main__":
    from report_strategy import ReportGenerator

    rows = [{"name": "Q1", "value": 15000}, {"name": "<b>", "value": 1}]
    print(ReportGenerator(rows, HTMLFormatStrategy()).generate_report())
