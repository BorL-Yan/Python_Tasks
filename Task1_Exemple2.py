#Գրել class Money որը պետք է ունենա դաշտեր` 
# 1.պահելու համար փողի քանակն ու արժույթի տեսակը։ +
#Եվ ունենա մեթոդներ` 
# 1.փողը այլ արժույթի փոխանակելու +
# 2.երկու փողեր իրար գումարելու +
# 3.հանելու +
# 4.բաժանելու +
# 4.փողը թվով բազմապատկելու 
# 5.հավասարությունը ստուգելու համար


# singlton decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

##exchange
@singleton
class Exchange:
    def __init__(self):        
        self.changeList = {}
        
    def AddChangeList(self, receiving_amount, available_changes):
        if isinstance(receiving_amount, str):
            self.changeList[receiving_amount] = available_changes
            return 0
        else:
            raise ValueError(f"Receiving amount must be a string: {type(receiving_amount)}")
        
    def ChangeMoney(self, from_this, to_this, money_quantity):      
        if from_this not in self.changeList or to_this not in self.changeList[from_this]:
            raise ValueError(f"There is no such thing as money. {from_this}")
        new_money_quantity = self.changeList[from_this][to_this] * money_quantity   
        return new_money_quantity
    
    def is_unavailable(self, currenct):
        return currenct not in self.changeList


    def  __str__(self):
        return f"{self.changeList}" 



class Money:
    def __init__(self, currency, quantity):
        if not isinstance(currency, str):
            raise ValueError("Currency must be a string")
        if not isinstance(quantity, (int, float)):
            raise ValueError("Quantity must be a number")
        
        self._currency = currency
        self._quantity = quantity
        
    @property
    def currency(self):
        return self._currency
    
    @currency.setter
    def currency(self, name):
        if not isinstance(name, str):
            raise ValueError("Currency must be a string")
        self._currency = name
       

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, (int, float)):
            raise ValueError("Quantity must be a number")
        self._quantity = quantity
     
    
    def exchange_from_to(self, to_currency):
        exchange = Exchange()

        if exchange.is_unavailable(self._currency) or exchange.is_unavailable(to_currency):
            raise ValueError(f"Unsupported currency: {self._currency} or {to_currency}")
        
        quantity = exchange.ChangeMoney(self._currency, to_currency, self._quantity)
        self.currency = to_currency
        self.quantity = quantity

    def add(self, currency, quantity):
        new_money = Money(currency, quantity)
        new_money.exchange_from_to(self.currency)
        self.quantity += new_money.quantity
    
    def add_money(self, money):
        if isinstance(money, Money):
            self.add(money.currency, money.quantity)
        else:
            raise ValueError(f"Unsupperted money: {money}")

    def subtract(self, currency, quantity):
        new_money = Money(currency, quantity)
        new_money.exchange_from_to(self.currency)
        self.quantity -= new_money.quantity

    def subtract_money(self,money):
        if isinstance(money, Money):
            self.subtract(money.currency, money.quantity)
        else:
            raise ValueError(f"Unsupperted money: {money}")

    def divide(self, currency, quantity):
        new_money = Money(currency, quantity)
        new_money.exchange_from_to(self.currency)
        self.quantity /= new_money.quantity

    def divide_money(self,money):
        if isinstance(money, Money):
            self.divide(money.currency, money.quantity)
        else:
            raise ValueError(f"Unsupperted money: {money}")

    def multiply(self, value):
        self.quantity *= value

    def isEqual(self, money):
        if isinstance(money, Money):
            return self.quantity == money.quantity
        else:
            raise ValueError(f"Unsupperted money: {money}")


    def __str__(self):
        return f"Currency : {self._currency} \nQuantity : {self._quantity} \n"


def main():
    exchangeMoney = Exchange()
    exchangeMoney.AddChangeList('USD', {'USD': 1.0, 'EUR': 0.89, 'RUB': 57.0, 'AMD': 398.0})
    exchangeMoney.AddChangeList('EUR', {'USD': 1.12, 'EUR': 1.0, 'RUB': 64.0, 'AMD': 446.0})
    exchangeMoney.AddChangeList('RUB', {'USD': 0.017, 'EUR': 0.0156, 'RUB': 1.0, 'AMD': 6.98})
    exchangeMoney.AddChangeList('AMD', {'USD': 0.0025, 'EUR': 0.00224, 'AMD': 1.0, 'RUB': 0.143})

    moneyUSD = Money("USD", 1)
    moneyUSD.exchange_from_to("RUB")
    print(moneyUSD)

    moneyUSD.add_currency("EUR", 1)
    print(moneyUSD)
    

if __name__ == "__main__":
    main()
    
