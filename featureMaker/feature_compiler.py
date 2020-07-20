from pathlib import Path


def json_parser(data):
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
            line = line.replace("</div>", "")
            line = line.replace("<br>", "")
            line = line.replace("<div>", "")
            line = line.replace("&nbsp;", "")
            line = line.replace("&gt;", ">")
            w.write(line)