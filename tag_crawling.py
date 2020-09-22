from pixivpy3 import *
import json

api = PixivAPI()
with open('pw.json') as f:
    pw = json.load(f)
api.login(pw['username'], pw['password'])

tag = 'ツイ腐テ'

result = []
n = 1

while True:
    json_result = api.search_works(tag, mode='tag', page=n)
    res = json_result.response
    if res is None:
        break
    result.extend(res)
    n += 1

print(len(result))

with open('result_'+tag+'.json', 'w') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)