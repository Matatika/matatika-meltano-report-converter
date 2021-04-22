import unittest
import yaml
import matatika_meltano_report_converter as mmrc


class TestChartjsChartType(unittest.TestCase):
    def setUp(self):
        self.chart_type_bar = "Bar"
        self.chart_type_vertical_bar = "VerticalBar"
        self.chart_type_line = "LineChart"

    def test_chartjs_chart_type_bar(self):
        self.chartjs_type = mmrc.chartjs_chart_type(self.chart_type_bar)
        self.assertEqual(self.chartjs_type, "horizontalBar")

    def test_chartjs_chart_type_vertical_bar(self):
        self.chartjs_type = mmrc.chartjs_chart_type(self.chart_type_vertical_bar)
        self.assertEqual(self.chartjs_type, "bar")

    def test_chartjs_chart_type_line(self):
        self.chartjs_type = mmrc.chartjs_chart_type(self.chart_type_line)
        self.assertEqual(self.chartjs_type, "line")


if __name__ == "__main__":
    unittest.main()