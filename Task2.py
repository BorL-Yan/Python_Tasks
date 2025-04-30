# Գրել Time եվ Date կլասներ որոնք ունեն
#   Time class' ժամ,րոպե,վայրկյան
#   Date class տարի, ամիս, օր
# դաշտեր 
# Ինչպես նաև մեթոդներ 
#   1. ժամ/րոպե/վայրկյան ավելացնելու Time֊ի համար, 
#   2. տարի/ամիս/օր ավելացնելու Date֊ի համար։ 

# Ինչպես նաև յուրաքանչյուր կլասի համար սահմանե սեփական Exception class'
#   1. կոնստրուկտորներում մշակել բոլոր դաշտերի արժեքները
#   2. սխալ արժեքների դեպքում մշակել համապատասխան Exception֊ներ

class DateError(Exception):
    pass

class TimeError(Exception):
    pass


class Data:

    month_day = []
    def __init__(self,day, month, year):
        if not (0 <= year):
            self._year = 0
            raise DateError(f"The year should be positive : {year}. It has been assigned 0")
        if not (1 <= month <= 12):
            self._year = 0
            raise DateError(f"The month sent is incorrect : {month}. It has been assigned 0")
        if not (1 <= day <= self._days_in_month(year, month)):
            self._day = 0
            raise DateError(f"The day sent is incorrect : {day}. It has been assigned 0")
        
        self._day = day
        self._month = month
        self._year = year

#region Private Metods
    def _is_lerp_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def _days_in_month(self, year, month):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2  and self._is_lerp_year(year):
            return 29
        return days[month - 1]
    
    def _validate(self):
        if not isinstance(self._year, int) or self._year < 0:
            raise DateError(f"Year must be positive: {self._year}")
        if not isinstance(self._month, int) or self._month < 1 or self._month > 12:
            raise DateError(f"Month must be between 1 and 12: {self._month}")
        if not isinstance(self._day, int) or self._day < 1 or self._day > self._days_in_month(self._year, self._month):
            raise DateError(f"Day must be between 1 and {self._days_in_month(self._year, self._month)}: {self._day}")
#end region

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if not isinstance(value, int) or value < 0:
            raise DateError(f"The day should be positive : {value}.")
        
        self._day = value
        self._validate()
    
    def add_day(self, value):
        if not isinstance(value, int) or value < 0:
            raise DateError(f"The day should be positive : {value}.")
        
        while value > 0:
            month_days = self._days_in_month(self.year, self.month)
            if value > month_days:
                self._day = 1
                self.add_month(1)
                value -= month_days
            else:
                
                self._day = value
                value = 0

        self._validate()



    @property
    def month(self):
        return self._month
    
    @month.setter
    def month(self, value):
        if not isinstance(value, int) or value < 0:
            raise DateError(f"The month should be positive : {value}.")
        
        self._month = value
        self._validate()

    def add_month(self, value):
        if not isinstance(value, int) or value < 0:
            raise DateError(f"The month should be positive : {value}.")
        
        self.add_year( (value - 1) // 12 )
        self._month = (value - 1) % 12 + 1

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value < 0:
            raise DateError(f"The year should be positive : {value}.")
        
        self._year = value
        self._validate()
                

    def add_year(self, value):
        if not isinstance(value, int) or value < 0:
            raise DateError(f"The year should be positive : {value}.")
        
        self._year += value
        self._validate()


  



class Time:
    def __init__(self, date, second, minute, hour):
    
        self._date = date

        if not (0 <= hour <= 24):
            self._hour = hour
        else:
            self._hour = 0
            raise TimeError(f"The hour sent is incorrect : {hour}. It has been assigned 0")
        
        if not (0 <= minute <= 24):
            self._minute = minute
        else:
            self._minute = 0
            raise TimeError(f"The minute sent is incorrect : {minute}. It has been assigned 0")

        if not (0 <= second <= 60):
            self._second = second
        else:
            self._second = 0
            raise TimeError(f"The second sent is incorrect : {second}. It has been assigned 0")

    @property
    def hour(self):
        return self._hour
    
    @hour.setter   
    def hour(self,value):
        self._hour += value
        day = int( self._hour / 24 )
        self._hour %= 24          
        self._date.add_day(day)

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        self._minute += value
        hour = int(self._minute / 60)
        self._minute %= 60
        self.hour =+ hour
    

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        self._second += value
        minute = int(self._second / 60)
        self._second %= 60
        self.minute += minute

    def __str__(self):
        return f"{self._hour}:{self._minute}:{self._second} {self._date.year}-{self._date.month}-{self._date.day}"


time = Time(Data(2023, 10, 1), 0, 0, 0)
print(time.hour)

