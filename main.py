


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Инициализация пустого словаря для items

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаление товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Получение цены товара по его названию."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновление цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

stores = []

while True:
    doit2 = '3'
    doit1 = input(f"Для добавления нового магазина введите 1 \n"
                  f"Для управления существующим магазином введите 2 \n"
                  f"Для вывода списка магазинов на экран введите 3 \n"
                  f"Для выхода введите 0: ")
    match doit1:
        case '0':
            break
        case '1':
            name = input('Введите название магазина:')
            address = input('Введите адрес магазина:')
            stores.append(Store(name, address))
        case '2':
            market_name = input('Введите название магазина, которым будем управлять:')
            for market in stores:
                if market_name == market.name:
                    name = market
                #else
            while doit2 != '0':
                doit2 = input(f"Для добавления нового товара в ассортимент магазина введите 1 \n"
                      f"Для удаления товара из ассортимента магазина введите 2 \n"
                      f"Для вывода полного списка товаров в магазине на экран введите 3 \n"
                      f"Для изменения цены на товар введите 4 \n"
                      f"Вывести цену конкретного товара на экран введите 5 \n" 
                      f"Для выхода введите 0: ")
                match doit2:
                    case '0':
                        print(f'Управление магазином {name.name} завершено')
                    case '1':
                        new_item = input('Введите название товара:')
                        new_item_price  = input('Введите цену товара:')
                        name.add_item(new_item, new_item_price)
                        print(f'Товар {new_item} введен в ассортимент магазина {name.name} по цене {new_item_price} руб.')
                    case '2':
                        item_to_del = input('Введите название товара:')
                        name.remove_item(item_to_del)
                        print(f'Товар {item_to_del} выведен из ассортимента магазина {name.name}')
                    case '3':
                        for item_to_print in name.items:
                            print(f'{item_to_print} - {name.get_price(item_to_print)} руб.')
                    case '4':
                        item_price_to_change = input('Введите название товара:')
                        item_new_price = input('Введите новую цену товара:')
                        name.update_price(item_price_to_change, item_new_price)
                        print(f'Новая цена товара {item_price_to_change}: {name.get_price(item_price_to_change)} руб.')
                    case '5':
                        item_price_to_print = input('Введите название товара:')
                        print(f'Цена товара {item_price_to_print}: {name.get_price(item_price_to_print)} руб.')
        case '3':
            for market in stores:
                print(f'{market.name}, {market.address}')
        case _:
            print(stores)

