apply_discount = lambda total, percent: total * (1 - percent / 100)


def shop(*prices, **kwargs):
    discount = kwargs.get("discount", 0)
    delivery = kwargs.get("delivery", 0)

    subtotal = sum(prices)
    discounted = apply_discount(subtotal, discount)
    total = discounted + delivery

    print("======= ЧЕК =======")
    for i, price in enumerate(prices, start=1):
        print(f"Товар {i}: {price:.2f} руб.")
    print("-" * 19)
    print(f"Сумма:    {subtotal:.2f} руб.")
    print(f"Скидка {discount}%: -{subtotal - discounted:.2f} руб.")
    print(f"Доставка: {delivery:.2f} руб.")
    print("-" * 19)
    print(f"ИТОГО:    {total:.2f} руб.")


shop(120, 250, 80, discount=10, delivery=40)