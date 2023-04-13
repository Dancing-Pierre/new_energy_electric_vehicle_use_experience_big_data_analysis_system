import time
import requests
import json


def start_requests(page):
    url = 'https://openapi.diandong.com/car/serieList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    body = {
        'serie_id': '23-39-55-76-79-81-86-87-101-120-127-139-147-177-189-193-195-200-202-204-206-207-209-212-214-222-223-224-292-338-383-455-471-488-575-580-587-598-601-608-614-616-626-633-646-648-649-526-660-664-665-667-668-669-673-699-700-682-711-717-719-724-658-727-729-732-733-734-736-744-747-758-773-775-777-756-457-768-779-797-798-799-803-813-816-818-820-824-825-829-830-769-794-845-738-846-848-850-853-854-855-857-858-859-861-863-864-865-867-868-874-879-881-884-885-886-887-889-891-893-901-902-907-916-919-920-928-937-938-939-951-961-963-964-967-973-977-981-984-985-989-991-997-998-1012-1030-1038-1055-1059-1060-1061-1063-986-1067-1069-1070-1071-1074-1075-1077-1080-1082-1085-1087-1089-1091-1098-1102-1104-1114-1117-1118-1122-1126-1129-1130-1132-1133-1134-1138-1140-1141-1147-1148-1151-1152-1155-1156-1157-1158-1163-1164-1165-1171-1174-1178-1180-1181-1183-1185-1189-1190-1191-1192-1194-1195-1196-1197-1198-1200-1203-1208-1210-1211-1213-1215-1216-1217-1218-1220-1187-1223-1224-1225-1226-1227-1228-1229-1230-1231-1232-1233-1235-1237-1239-1240-1241-1242-1244-1246-1248-1249-1252-1253-1254-1259-1265-1266-1272-1284-1295-1306-1320-1321-1322-1325-1326-1327-1336-1338-1343-1345-1346-1347-1348-1349-1351-1352-1354-1356-1362-1363',
        'sort': '',
        'page': page,
        'size': 8,
    }
    kwargs = {
        "data": body,
        "headers": headers,
        "timeout": 120
    }
    res = requests.post(url, **kwargs)
    print(res.text)
    save_data(page, res.text)
    return res.text


def parse_data(data):
    result = json.loads(data)
    return result.get('data').get('list')


def save_data(page, json_data):
    with open('app_car/data/{}.txt'.format(page), 'w', encoding='utf-8') as f:
        f.write(json_data)
    with open('static/page.txt', 'w', encoding='utf-8') as f:
        f.write(str(page+1))


def start_read_data(page):
    with open('app_car/data/{}.txt'.format(page), 'r', encoding='utf-8') as f:
        o = f.read()
    return o


def read_page():
    with open('static/page.txt', 'r', encoding='utf-8') as f:
        o = f.read()
    return int(o) if o else 23

