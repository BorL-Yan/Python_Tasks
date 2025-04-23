#Գրել class Money որը պետք է ունենա դաշտեր` 
# 1.պահելու համար փողի քանակն ու արժույթի տեսակը։ +
#Եվ ունենա մեթոդներ` 
# 1.փողը այլ արժույթի փոխանակելու +
# 2.երկու փողեր իրար գումարելու + ?
# 3.հանելու + ?
# 4.բաժանելու + ?
# 4.փողը թվով բազմապատկելու +
# 5.հավասարությունը ստուգելու համար

##exchange
class Exchange:
    def __init__(self, list):        
        self.changeList = list
        
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


class Money:
    def __init__(self, exchange):
        self.exchange = exchange
        self._money = {}
        
    def append(self, currency, quantity):
        if not isinstance(currency, str):
            raise ValueError("Currency must be a string")
        if not isinstance(quantity, (int, float)):
            raise ValueError("Quantity must be a number")
        
        if currency in self._money:
            self._money[currency] += quantity
        else:
            self._money[currency] = quantity
        return 0
    
    def exchange_form_to_quantity(self, from_currency, to_currency, money_quantity):
        if not isinstance(money_quantity, (int, float)) or money_quantity < 0:
            raise ValueError("Money quantity must be a positive number")
        
        if from_currency not in self._money:
            raise ValueError(f"Source currency {from_currency} not supported")
        if self._money[from_currency] < money_quantity:
            raise ValueError(f"Insufficient funds in {from_currency}: {self._money[from_currency]} available")        
        
        new_money = self.exchange.ChangeMoney(from_currency, to_currency,money_quantity)
        
        if(new_money is None):
            raise ValueError(f"Cannot convert from {from_currency} to {to_currency}")
       
        try:
            self._money[from_currency] -= money_quantity;
            self.append(to_currency, new_money)   
        except Exception as e:
            self._money[from_currency] += money_quantity
            raise ValueError(f"Failed to update balances: {str(e)} ")
        return 0
           
    def exchange_form_to(self, from_currency, to_currency):
        if from_currency not in self._money:
            raise ValueError(f"There is no such thing as money. {from_currency}")

        self.exchange_form_to_quantity(from_currency, to_currency, self._money[from_currency])
        return 0
    
    
    def add_two_currencies(self, currency_1, currency_2):
        new_currency_quantity = self.exchange.ChangeMoney(currency_2, currency_1, self._money[currency_2])

        self.append(currency_1, new_currency_quantity)
        return 0
    
    def add_currency(self, currency, quantity):        
        self.append(currency, quantity)
        return 0
    

    def subtract_two_currenies(self, currency_1, currency_2): 
        new_currency_quantity = self.exchange.ChangeMoney(currency_2, currency_1, self._money[currency_2])
        quantity = self.subtract_currency(currency_1, new_currency_quantity)

        self.append(currency_1, quantity)
        return 0
    
    def subtract_currency(self, currency, quantity):
        if self._money[currency] < quantity:
            ValueError(f"There is not that much money. {self._money[currency]}")
            self._money[currency] = 0
            return abs(self._money[currency] - quantity)

        new_quantity = self._money[currency] - quantity
        self._money[currency] = new_quantity
        return 0

    def devide_two_currencies(self, from_currency, to_currency):
        new_currency_quantity = self.exchange(from_currency, to_currency)
        quantity = self.devide_currency(from_currency, new_currency_quantity)

        return self.devide_currency(to_currency, quantity)


    def devide_currency(self, currency, quantity):
        self._money[currency] /= quantity
        return self._money[currency]
    

    def multiply_currency(self, currency, quantity):
        return self.devide_currency(currency, 1/quantity)
    
    def check_equality_two_currency(self, currency_one, currency_two):
        quantity = self.exchange(currency_one, currency_two)
        return self._money[currency_two] == quantity


def main():
    exchangelist = {'USD': {'USD': 1.0, 'EUR': 0.89, 'RUB': 57.0, 'AMD': 398.0},
                    'EUR': {'USD': 1.12, 'EUR': 1.0, 'RUB': 64.0, 'AMD': 446.0},
                    'RUB': {'USD': 0.017, 'EUR': 0.0156, 'RUB': 1.0, 'AMD': 6.98},
                    'AMD': {'USD': 0.0025, 'EUR': 0.00224, 'AMD': 1.0, 'RUB': 0.143},
                    }
    
    changeMoney = Exchange(exchangelist)
    print (changeMoney.changeList);
    
    myMoney = Money(changeMoney);
    myMoney.append('USD',  15);
    myMoney.append('AMD',  4500);
    myMoney.append('EUR',  40);

    myMoney.exchange_form_to_quantity('USD', 'RUB', 12)
    print(myMoney._money)

    myMoney.exchange_form_to('EUR', 'USD')
    print(myMoney._money)

    myMoney.add_currency('EUR', 12.5)
    print(myMoney._money)

    myMoney.add_two_currencies('USD','EUR')
    print(myMoney._money)

    myMoney.subtract_two_currenies('USD','AMD')
    print(myMoney._money)


 

if __name__ == "__main__":
    main()

