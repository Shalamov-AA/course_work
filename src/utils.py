import json


def open_file(text):
    with open("operations.json", encoding="utf-8") as file:
        return json.load(file)


def check_state_and_sorted(data):
    """Проверка на успешность операции с удалением не успешной операции, удалением пустых значений
    и сортировка данных по дате в обратном порядке"""
    for i in reversed(range(len(data))):
        if 0 == len(data[i]) or data[i]["state"] == "CANCELED":
            data.remove(data[i])
    data.sort(key=lambda x: x['date'])
    data.reverse()
    return data


def output_last_operations(data):
    """Вывод последних 5 операций"""
    last_operations = []
    for i in range(5):
        if 'from' in data[i] and 'Счет' in data[i]['from'] and 'Счет' in data[i]['to']:
            """"Перевод со счета на счет"""
            last_operations.append(f"""{data[i]["date"][8:10] + "." + data[i]['date'][5:7] + '.' + data[i]['date'][:4]} \
{data[i]['description']} 
{data[i]['from'][:5] + "**" + data[i]['from'][-4:]} -> \
{data[i]['to'][:5] + "**" + data[i]['to'][-4:]}
{data[i]['operationAmount']['amount']} {data[i]['operationAmount']['currency']['name']}\n""")
        elif 'from' in data[i] and 'Счет' not in data[i]['from'] and 'Счет' in data[i]['to']:
            """Перевод с карточки на счет"""
            last_operations.append(f"""{data[i]["date"][8:10] + "." + data[i]['date'][5:7] + '.' + data[i]['date'][:4]} \
{data[i]['description']} {data[i]['from'][:-17]}
{data[i]['from'][-16:-12] + " " + data[i]['from'][-12:-10] + "** **** " + data[i]['from'][-4:]} -> \
{data[i]['to'][:5] + "**" + data[i]['to'][-4:]}
{data[i]['operationAmount']['amount']} {data[i]['operationAmount']['currency']['name']}\n""")
        elif 'from' in data[i] and 'Счет' not in data[i]['from'] and 'Счет' not in data[i]['to']:
            """Перевод с карточки на карточку"""
            last_operations.append(f"""{data[i]["date"][8:10] + "." + data[i]['date'][5:7] + '.' + data[i]['date'][:4]} \
{data[i]['description']} {data[i]['from'][:-17]}
{data[i]['from'][-16:-12] + " " + data[i]['from'][-12:-10] + "** **** " + data[i]['from'][-4:]} -> \
{data[i]['to'][:-17]} {data[i]['to'][-16:-12] + " " + data[i]['to'][-12:-10] + "** **** " + data[i]['to'][-4:]} 
    {data[i]['operationAmount']['amount']} {data[i]['operationAmount']['currency']['name']}\n""")
        else:
            """Открытие вклада"""
            last_operations.append(f"""{data[i]["date"][8:10] + "." + data[i]['date'][5:7] + '.' + data[i]['date'][:4]}\
 {data[i]['description']}
{data[i]['to'][:5] + "**" + data[i]['to'][-4:]}
{data[i]['operationAmount']['amount']} {data[i]['operationAmount']['currency']['name']}\n""")
    return last_operations
