


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

# Пример использования
store = Store("Магазин 'Свет'","ул. Светлая, д. 15")

store.add_item("яблоки", 0.5)
store.add_item("бананы", 0.75)

print(store.get_price("яблоки"))  # Выведет 0.5
print(store.get_price("орехи"))  # Выведет None, так как такого товара нет

store.update_price("бананы", 0.80)
print(store.get_price("бананы"))  # Выведет 0.8

store.remove_item("бананы")
print(store.get_price("бананы"))  # Выведет None, так как товар был удален
