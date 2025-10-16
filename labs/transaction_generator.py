def shadow(limit=200):
    def decorator(func):
        def wrapped(*args, **kwargs):
            gen = func(*args, **kwargs)
            total = 0.0
            try:
                while True:
                    item = next(gen)
                    print(item)  
                    parts = item.split()
                    if len(parts) != 2:
                        yield item
                        continue
                    action, amount_str = parts
                    if action not in ["payment", "refund", "transfer"]:
                        yield item
                        continue
                    try:
                        amount = float(amount_str)
                    except ValueError:
                        yield item
                        continue
                    if action == "refund":
                        total -= amount
                    else:
                        total += amount
                    if total > limit:
                        print("Тіньовий ліміт перевищено. Активую схему")
                    yield item
            except StopIteration:
                return total 

        return wrapped
    return decorator

@shadow(limit=200)
def transaction_generator():
    yield "payment 120"
    yield "refund 50"
    yield "transfer 300"
    yield "refund 170"
    yield "payment 250"
    yield "transfer 90"

if __name__ == "__main__":
    gen = transaction_generator()
    total = None
    while True:
        try:
            next(gen)
        except StopIteration as e:
            total = e.value
            break
    print(f"Фінальна сума: {total}")