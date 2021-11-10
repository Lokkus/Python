import json

def count_files(path_to_file):
    counter = 0
    with open(path_to_file, 'r') as file:
        d = json.load(file)
        for key, val in d.items():
            counter += len(val)
    print(counter)


if __name__ == '__main__':
    count_files(r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tests\Splits_read_from_mongo.json')