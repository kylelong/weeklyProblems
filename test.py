# import json

# data = {
#     "name": "Kyle",
#     "languages": ["Python", "TypeScript", "Italian"],
#     "projects": {
#         "web": ["Next.js", "React"],
#         "mobile": ["React Native"]
#     }
# }
# print(data)
# formatted_json = json.dumps(data, indent=4)
# print(formatted_json)

# tomato

s = {"t": 2, "o": 2, "m": 2, "a": 2}
v = list(s.values())
print(len(set(v)))
mode = max(v)
keys = sorted([k for k in s.keys() if s[k] >= mode])