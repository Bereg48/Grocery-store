class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.__count = count

    def sale(self, sale_count):
        self.__count -= sale_count

    def fill(self, fill_count):
        self.__count += fill_count

    @property
    def count(self):
        return self.__count


class Category:
    def __init__(self, name, products):
        self.name = name
        self.__products = products
        self.__is_active = True

    @property
    def __is_active(self):
        return self.__is_active

    @property
    def products(self):
        return self.__products

    def remove(self, product_index):
        del self.__products[product_index]

    def __add__(self, product_item):
        self.__products.append(product_item)


class Store:

    def __init__(self, categories):
        self.__categories = categories

    @property
    def categories(self):
        tmp = []
        for cat in self.__categories:
            if cat.is_active:
                tmp.append(cat)
        return tmp


if __name__ == '__main__':
    product = Product("Яблоко", 250, 20)
    category = Category("Яблоки", [product])
