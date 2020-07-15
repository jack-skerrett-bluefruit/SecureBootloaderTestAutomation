def feature_compiler(feature_name, feature_lines):
    with open("D:\\Code\\secureBootloaderAutomatedTests\\behaveTests\\features\\" + feature_name + ".feature", "w+") as w:
        w.write("Feature: ")
        for line in feature_lines:
            line = line.replace("</div>", "")
            line = line.replace("<br>", "")
            line = line.replace("<div>", "")
            line = line.replace("&nbsp;", "")
            line = line.replace("&gt;", ">")
            w.write(line)