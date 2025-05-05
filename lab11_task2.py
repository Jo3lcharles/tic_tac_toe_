import doctest

class Product:
    """ A class representing one product """
    
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Constructor

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop._name
        'laptop'
        >>> laptop._price
        2030.5
        >>> laptop._quantity
        2
        """
            
        assert isinstance(name, str), "the name must be a string"
        assert isinstance(price, float) and price > 0, "the price must be a postive float"
        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"
            
        self._name = name
        self._price = price
        self._quantity = quantity
    
    def get_name(self) -> str:
        """
        get the name of the product
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_name()
        'laptop'
        """
        
        return self._name
    
    def get_price(self) -> float:
        """
        get the price of the product
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_price()
        2030.5
        """
        
        return self._price
    
    def get_quantity(self) -> int:
        """
        get the quantity of the product
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_quantity()
        2
        """
        return max(self._quantity,  0)
    
    def add_quantity(self, quantity=1) -> None:
        """
        Add the quantity of the product
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.add_quantity()
        >>> laptop._quantity
        3
        """
        
        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"
        
        self._quantity += quantity
        
    def reduce_quantity(self, quantity=1) -> None:
        """
        Reduce the quantity of the product
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.reduce_quantity()
        >>> laptop._quantity
        1
        """
        
        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"
        
        self._quantity -= quantity
        
class Inventory:
    """ A class representing the inventory """
    
    def __init__(self) -> None:
        """
        Constructor
        
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory._products
        []
        """
        
        self._products = []

    def _find_product(self, name: str) -> Product:
        """
        
        Find the product with the given name. Return None if the product is not found
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory._find_product("laptop") is laptop
        True
        """
        for product in self._products:
            if product.get_name() == name:
                return product
        return None 

    def stock_product(self, product: Product) -> None:
        """
        Add a product to the inventory
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory._products[0] is laptop
        True
        """
        
        assert isinstance(product, Product), "the parameter product must be an instance of the Class Product"

        existing_product = self._find_product(product.get_name())

        if existing_product :
            if existing_product.get_price() != product.get_price():
                raise AssertionError
            else:
                existing_product.add_quantity(product.get_quantity())

        else:
            self._products.append(product)

        
    def sell_product(self, product_name: str, quantity: int) -> None:
        """
        Sell product in inventory
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory.sell_product("laptop", 1)
        >>> laptop._quantity
        1
        """
        
        assert isinstance(product_name, str), "the name must be a string"
        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"        
        
        product = self._find_product(product_name)
        
        if product:
            product.reduce_quantity(quantity)

    def calculate_inventory_value(self) -> float:
        """
        Calcuatel the total value of the current inventory
        
        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory.calculate_inventory_value()
        4061.0
        """
        
        total_value = 0
        
        for product in self._products:
            total_value += (product.get_price() * product.get_quantity())
            
        return total_value

if __name__ == '__main__':
    doctest.testmod()

laptop = Product("laptop", 2030.5, 2)
laptop.reduce_quantity(3)
print(laptop.get_quantity())

laptop = Product("laptop", 2030.5, 2)
retail_store_inventory = Inventory()
retail_store_inventory._products = [laptop]
print(retail_store_inventory._find_product("laptop") is laptop)

laptop = Product("laptop", 2030.5, 2)
retail_store_inventory = Inventory()
retail_store_inventory._products = [laptop]
print(retail_store_inventory._find_product("tablet") == None)

laptop_1 = Product("laptop", 2030.5, 2)
laptop_2 = Product("laptop", 2030.5, 3)
retail_store_inventory = Inventory()
retail_store_inventory.stock_product(laptop_1)
retail_store_inventory.stock_product(laptop_2)
print(retail_store_inventory._find_product("laptop").get_quantity())


laptop_1 = Product("laptop", 2030.5, 2)
laptop_2 = Product("laptop", 102.09, 2)
retail_store_inventory = Inventory()
retail_store_inventory.stock_product(laptop_1)
retail_store_inventory.stock_product(laptop_2)