#!/usr/bin/env python3

import json


text_json = '''{
    "demo": "Processing JSON in Python",
    "instructor": "Michael",
    "duration": 5.0
}'''


print(type(text_json), text_json)

data = json.loads(text_json)
print(type(data), data)

instructor = data.get('instructor', 'SUBSITUTE')
print("Your instructor is {}".format(instructor))

data['instructor'] = 'Jeff'

new_json = json.dumps(data)

print(type(new_json), new_json)
