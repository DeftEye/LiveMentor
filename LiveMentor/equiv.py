import json
import csv  

def find_Endpoints(node, key=None, key_String=""):
    if isinstance(node, dict):
        nodes = {}
        for node_Key in node.keys():
            bis_Key_String = (
                node_Key if (key_String == "") else (key_String + "." + str(node_Key))
            )
            nodes.update(find_Endpoints(node[node_Key], node_Key, bis_Key_String))
        return nodes
    elif isinstance(node, list):
        nodes = {}
        str_array = ""
        for elem in node:
            str_array += str(elem) + ", "
        if len(str_array) > 0:
            str_array = str_array[:-2]
            nodes[key] = str(str_array)
        return nodes
    else:
        return {key_String: node}


with open("test.json") as f_input, open("output.csv", "w") as f_output:
    json_data = json.load(f_input, strict=False)
    fieldnames = set()
    for entry in json_data:
        fieldnames.update(find_Endpoints(entry).keys())
    csv_output = csv.DictWriter(f_output, delimiter=",", fieldnames=sorted(fieldnames))
    csv_output.writeheader()
    csv_output.writerows(find_Endpoints(entry) for entry in json_data)