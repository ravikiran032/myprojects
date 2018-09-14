'''
Created on Jul 29, 2018

@author: ravi
'''
import json
def main():
    json_string={
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
    }
    
    te=json_string['children']
    #te.append({'age': 10, 'firstName':'ravi'})
    iter(te[0]).next()["rrere"]="well"
    #json_string['children']=te
    
    print(te)
if __name__ == '__main__':
    main()