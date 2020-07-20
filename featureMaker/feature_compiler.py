from pathlib import Path
from html import unescape
import re

def strip_html(line):
    if not line: 
        return line
    html_tags = re.compile(r"<[^>]*>")
    line = html_tags.sub("", line)
    return unescape(line.replace("&nbsp;", " "))

def json_formatter(data):
    feature_lines = [] 
    feature_name = data["Items"][0]["TestPlans"]["Items"][0]["Name"]
    feature_lines.append(feature_name + "\n")

    for item in data["Items"]:
            feature_lines.append("\n    ")
            feature_lines.append(item["Name"] + "\n")
            for items in item["TestSteps"]["Items"]:
                feature_lines.append("        " + items["Description"] + "\n")

    feature_compiler(feature_name, feature_lines)

def feature_compiler(feature_name, feature_lines):
    feature_name += ".feature"
    base_path = Path(__file__).parent
    file_path = (base_path / "../features/" / feature_name).resolve()

    with open(file_path, "w+") as w:
        w.write("Feature: ")
        for line in feature_lines:
            line = strip_html(line)
            w.write(line)