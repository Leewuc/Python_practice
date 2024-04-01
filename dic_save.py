import json
with open("./news.txt",'r') as text:
    txt = text.read()
# 저장할 딕셔너리
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "music"],
    "married": False
}
line = txt.split(" ")
for line in txt:
    data[line] = data.get(line,0) + 1
# JSON 파일로 저장
with open("data.json", "w") as file:
    json.dump(data, file)