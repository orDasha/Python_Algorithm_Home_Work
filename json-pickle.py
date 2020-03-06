import json
import pickle

my_favourite_group = {
'group_name': 'FPG',
'tracks': ['Думай!', 'Ботинки', 'My way'],
'Albums': [{'alb_name': 'Родина','year': 2001}, {'alb_name': 'Рок','year': 2006}]
}

print(type(my_favourite_group))

json_res = json.dumps(my_favourite_group)
pickle_res = pickle.dumps(my_favourite_group)

with open('myfav.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

with open('myfav.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)