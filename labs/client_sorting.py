clients = [
    {"name": "Danya", "amount": 2000, "status": "clean"},
    {"name": "Мaria", "amount": 532, "status": "suspicious"},
    {"name": "Dima", "amount": 1200, "status": "clean"},
    {"name": "Makar", "amount": "450", "status": "suspicios"},
    {"name": "Vika", "amount": 50, "status": "fraud"},
    {"name": "Stas", "amount": "75", "status": "fraud"}
]

results = []

for client in clients:
    name = client["name"]
    amount = client["amount"]
    status = client["status"]

    if not isinstance(amount, (int, float)):
        results.append(f"{name}: Фальшиві дані")
        continue

    if amount < 100:
        category = "Дрібнота"
    elif 100 <= amount <= 999:
        category = "Середнячок"
    else:  
        category = "Великий клієнт"

    match status:
        case "clean":
            decision = "Працювати без питань"
        case "suspicious":
            decision = "Перевірити документи"
        case "fraud":
            decision = "У чорний список"
        case _:
            decision = "Невідомий статус"

    results.append(f"{name}: {category}, {decision}")

for result in results:
    print(result)