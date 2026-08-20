import csv

with open(r"C:\Users\Manu\Downloads\data.csv", "r") as file:
    header = file.readline().strip().split(",")
    content = file.readlines()
    column_index = header.index("name")

    def extract_names(content):
        unique_names = set()
        for line in content[1:]:
            line = line.strip().split(",")
            unique_names.add(line[1])
        return unique_names

    try:
        if content:
            unique_names = extract_names(content)
            print(list(unique_names))
    except Exception as e:
        print(e)
        raise Exception
