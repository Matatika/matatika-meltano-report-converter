import json
import yaml
import os

from meltano.api.controllers.sql_helper import SqlHelper
from meltano.core.m5o.m5o_collection_parser import M5oCollectionParser, M5oCollectionParserTypes
from meltano.core.m5o.m5o_file_parser import MeltanoAnalysisFileParser

def chartjs_chart_type(chartjs_type):
        # Lowercase first character of chart type
        chartjs_type = chartjs_type[0].lower() + chartjs_type[1:]
        chartjs_type = chartjs_type.replace("Chart", "")
        if chartjs_type == "bar":
            chartjs_type = "horizontalBar"
        if chartjs_type == "verticalBar":
            chartjs_type = "bar"
        return chartjs_type

def generate_query(design_helper, sql_helper, report):
        query_payload = report["query_payload"]
        sql_dict = sql_helper.get_sql(design_helper, query_payload)
        outgoing_sql = sql_dict["sql"]
        return outgoing_sql


def matatika_convert_reports():
    report_list = []
    try:
        report_list = [file for file in os.listdir('./analyze/reports') if file[-4:] == '.m5o']
    except FileNotFoundError:
        print("analyze/reports directory not found in this meltano project.")
    
    for file in report_list:
        with open('./analyze/reports/'+file, 'r') as open_file:
            data = json.load(open_file)
            sql_helper = SqlHelper()
            m5oc = sql_helper.get_m5oc_topic(data["namespace"], data["model"])
            design_helper = m5oc.design(data["design"])
            full_design = design_helper.design
            name = data["name"]
            title = full_design["label"]
            description = full_design["description"]
            visualisation = {
                "chartjs-chart": {
                    "chartType": chartjs_chart_type(data["chart_type"])
                }
                #'google-chart': {"chartType": self.google_chart_type(data["chart_type"]), "options": {"title": title}}
            }

            sql_query = {"query": generate_query(design_helper, sql_helper, data)}

            # If you pass dicts straight to the yaml dump you get the yaml teired layout rather than a json object to pass. 
            # This means that in the yaml the metadata and visulisation will have single quotes around them to avoid the above.
            visualisation_jsonstr = json.dumps(visualisation)
            full_design_jsonstr = json.dumps(full_design)
            dataset = {
                "title": title,
                "questions": title,
                "description": description,
                "metadata": full_design_jsonstr,
                "visualisation": visualisation_jsonstr,
                "query": sql_query["query"],
            }
            

            datasets = {"datasets": {data["slug"]: dataset}}

            with open(f'analyze/reports/{data["slug"]}.yaml', 'w') as output:
                yaml.dump(datasets, output, sort_keys=False, encoding='utf8')




if __name__ == '__init__':
    matatika_convert_reports()