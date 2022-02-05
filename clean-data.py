import json

def clean_data():


    with open('data/jobs.json', 'r') as jsonFile:
        data=jsonFile.read()

    # parse file
    obj = json.loads(data)

    print(type(obj))
    print(len(obj))

    return

clean_data()