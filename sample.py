import xmltodict,json,yaml
with open('sample.json', 'r') as file_j:
    data_j = json.load(file_j)

with open('sample.yaml', 'w') as file_y:
    data_y = yaml.dump(data_j, file_y)
with open('sample.xml', 'w') as file_x:
    file_x.write(xmltodict.unparse(data_j))