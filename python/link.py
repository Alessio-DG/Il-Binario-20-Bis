import json

l = []

with open("roba_notizie.txt") as f:
    print(f[:])
    l.extend(json.load(f.read()))
    print(l)
    #print(json.dumps(parsed_json, indent=4, sort_keys=True,  default=str))