import json
import yaml
import os

from meltano.api.controllers.sql_helper import SqlHelper


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
    try:
        report_list = [
            file for file in os.listdir("./analyze/reports") if file[-4:] == ".m5o"
        ]
    except FileNotFoundError:
        print("analyze/reports directory not found in this meltano project.")
        exit(1)

    for file in report_list:
        with open("./analyze/reports/" + file, "r") as open_file:
            data = json.load(open_file)
            sql_helper = SqlHelper()
            m5oc = sql_helper.get_m5oc_topic(data["namespace"], data["model"])
            design_helper = m5oc.design(data["design"])
            full_design = design_helper.design
            name = data["name"]
            title = full_design["label"]
            description = full_design["description"]
            visualisation = {
                "chartjs-chart": {"chartType": chartjs_chart_type(data["chart_type"])}
            }

            sql_query = generate_query(design_helper, sql_helper, data)

            # If you pass dicts straight to the yaml dump you get the yaml teir-ed layout rather than a json object to pass.
            # This means that in the yaml the metadata and visulisation will have single quotes around them to avoid the above tier-ing.
            visualisation_jsonstr = json.dumps(visualisation)

            try:
                matatika_metadata_str = matatika_metadata_builder(
                    full_design, sql_query
                )
            except KeyError as err:
                print(f"{err} ERROR")
                exit(1)

            dataset = {
                "version": 0.2,
                "source": None,
                "title": title,
                "questions": None,
                "description": description,
                "metadata": matatika_metadata_str,
                "visualisation": visualisation_jsonstr,
                "query": sql_query,
            }

            if not os.path.exists("converted_meltano_reports/"):
                os.mkdir("converted_meltano_reports/")

            with open(f'converted_meltano_reports/{data["slug"]}.yaml', "w") as output:
                yaml.dump(dataset, output, sort_keys=False, encoding="utf8")


def matatika_metadata_builder(full_design, sql_query):

    matatika_metadata = {
        "name": None,
        "label": None,
        "related_table": {"columns": [], "aggregates": []},
    }

    matatika_metadata["name"] = full_design["name"]

    matatika_metadata["label"] = full_design["label"]

    for column in full_design["related_table"]["columns"]:
        if column["name"] in sql_query:
            matatika_metadata["related_table"]["columns"].append(
                {
                    "name": column["name"],
                    "description": column["description"],
                    "label": column["label"],
                }
            )

    for aggregate in full_design["related_table"]["aggregates"]:
        if aggregate["name"] in sql_query:
            matatika_metadata["related_table"]["aggregates"].append(
                {
                    "name": aggregate["name"],
                    "description": aggregate["description"],
                    "label": aggregate["label"],
                }
            )

    matatika_metadata_str = json.dumps(matatika_metadata)
    return matatika_metadata_str


if __name__ == "__init__":
    matatika_convert_reports()