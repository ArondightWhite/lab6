import sys

stores = []

while True:
    command = input(">>> ").lower()

    if command == "exit":
        break

    elif command == "add":
        store = input("Название Магазина ")
        product = input("Название Товара ")
        price = int(input("Цена "))
        store_d = {
                'store': store,
                'product': product,
                'price': price,
            }
        stores.append(store_d)
        if len(stores) > 1:
            stores.sort(key=lambda item: item.get('store', ''))

    elif command.startswith('list '):

        storesname = command.split(' ', maxsplit=1)[1]

        for i in stores:
            if storesname.lower() in i.values() or storesname.upper() in i.values() or storesname.title() in i.values():
                print(f"{i['store']}: {i['product']} {i['price']}")

    elif command == "list":
        for i in stores:
            print(f"{i['store']}: {i['product']} {i['price']}")

    else:
        print(f"Неизвестная команда {command}", file=sys.stderr)
