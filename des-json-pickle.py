import json
import pickle

with open('myfav.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
    print(type(res))

with open('myfav.pickle', 'rb') as f:
    res = pickle.load(f)
    print(type(res))