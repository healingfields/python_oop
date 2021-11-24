import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validations
        assert price >= 0, f"price {price} must be positive or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} must be positive or equal to zero"

        # assignements
        print(f"instance created : {name}")
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # actions
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price += self.__price * increment_value

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("the name is toooo long")
        else:
            self.__name = value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            print(items)
        for item in items:
            Item(item.get('name'), float(item.get('price')), int(item.get('quantity')))

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_total_price(self):
        return self.__price * self.quantity

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
            hello!
            we have {self.name} {self.quantity} times . 
            Regards , Idriss    
        """

    def __send(self):
        pass

    def send_mail(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
