meds = [
    {"name": "Магне-В6", "quantity": 50, "category": "vitamin", "temperature": 19},
    {"name": "Пфайзер", "quantity": 10, "category": "vaccine", "temperature": 2},
    {"name": "Асперин", "quantity": 100, "category": "antibiotic", "temperature": 27},
    {"name": "Флемоксин", "quantity": 20, "category": "antibiotic", "temperature": 21},
]

results = []

for med in meds:
    name = med["name"]
    quantity = med["quantity"]
    category = med["category"]
    temperature = med["temperature"]

    if not isinstance(quantity, int) or not isinstance(temperature, (int, float)):
        results.append(f"{name}: Помилка даних")
        continue

    if temperature < 5.0:
        temp_status = "Надто холодно"
    elif temperature > 25.0:
        temp_status = "Надто жарко"
    else:
        temp_status = "Норма"

    match category:
        case "antibiotic":
            category_status = "Рецептурний препарат"
        case "vitamin":
            category_status = "Вільний продаж"
        case "vaccine":
            category_status = "Потребує спецзберігання"
        case _:
            category_status = "Невідома категорія"


    results.append(f"{name}: {category_status}, {temp_status}")

for result in results:
    print(result)