#Գրել class Money որը պետք է ունենա դաշտեր` 
# 1.պահելու համար փողի քանակն ու արժույթի տեսակը։ 
#Եվ ունենա մեթոդներ` 
# 1.փողը այլ արժույթի փոխանակելու
# 2.երկու փողեր իրար գումարելու
# 3.հանելու
# 4.բաժանելու
# 4.փողը թվով բազմապատկելու
# 5.հավասարությունը ստուգելու համար

##exchange
class Exchange:
    def __init__(self):        
        self.changeList = {}
        
    def AddChangeList(self, receiving_amount, available_changes):
        #receiving_amount type is string
        self.changeList[receiving_amount] = available_changes
        
    def ChangeMoney(self, from_this, to_this, money_quantity):      
        if from_this not in self.changeList or to_this not in self.changeList[from_this]:
            #debug Exemption            
            return None
        new_money_quantity = self.changeList[from_this][to_this] * money_quantity   
        return new_money_quantity


class Money:
    
    def __init__(self, exchange):
        self.exchange = exchange
        self._money = {}
        
    def append(self, money, quantity):
        if money in self._money:
            self._money[money] += quantity
        else:
            self._money[money] = quantity
    
    def Change_Money(self, from_money_type, to_money_type, money_quantity):
        if self._money[from_money_type] < money_quantity:           
             return ValueError("Недостаточно средств для конвертации")
        
        new_money = self.exchange.ChangeMoney(from_money_type, to_money_type,money_quantity)
        if(new_money is None):
             raise ValueError("Конвертация невозможна: валюта не поддерживается")
       
        self._money[from_money_type] -= money_quantity;
        self.append(to_money_type, new_money)   
         
         #change seter to dictionery    
    #def exchange_form_to(self, form_currency, to_currency):
 
 
 
changeMoney = Exchange()
 
changeMoney.AddChangeList('USD', {'USD': 1.0, 'EUR': 0.89, 'RUB': 57.0, 'AMD': 398.0})
changeMoney.AddChangeList('EUR', {'USD': 1.12, 'EUR': 1.0, 'RUB': 64.0, 'AMD': 446.0})
changeMoney.AddChangeList('RUB', {'USD': 0.017, 'EUR': 0.0156, 'RUB': 1.0, 'AMD': 6.98})
changeMoney.AddChangeList('AMD', {'USD': 0.0025, 'EUR': 0.00224, 'AMD': 1.0, 'RUB': 0.143})
 
 
print (changeMoney.changeList);
    
myMoney = Money(changeMoney);

myMoney.append('USD',  15);
myMoney.append('AMD',  4500);
myMoney.append('RUB',  0);
myMoney.append('EUR',  40);

myMoney.Change_Money('USD', 'RUB', 12)
print(myMoney._money)

myMoney.Change_Money('RUB', 'AMD', 600)
print(myMoney._money)

