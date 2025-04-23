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


class Data:
    def __init__(self):
        pass

class Time:
    def __init__(self, date, second, minute, hour):
        try:
            self._date = date
            self.append_hour(hour)
            self.append_minute(minute)
            self.append_second(second)
        except Exception as e:
            print (f" Exeption : {str(e)} ")
            return -1

    def append_hour(self, hour):
        if hour < 0 or hour > 24:
            raise ValueError(f"invalidate value: {hour}")
        self._hour = hour
        return 0 
    
    def append_hour(self, minute):
        if minute < 0 or minute > 60:
            raise ValueError(f"invalidate value: {minute}")
        self._minute = minute
        return 0 
    
    def append_hour(self, second):
        if second < 0 or second > 60:
            raise ValueError(f"invalidate value: {second}")
        self._second = second
        return 0 
    
    def add_hour(self, hour):
        self._hour += hour
        day = int( self._hour / 24 )
        self._hour %= 24          
        self._date.add_day(day)
        return 0


    def add_minute(self, minute):
        self._minute += minute
        hour = int(self._minute / 24)
        self._minute %= 60
        self.add_hour(hour)
        return 0


    def add_second(self, second):
        self._second += second
        minute = int(self._second / 24)
        self._second %= 60
        self.add_minute(minute)
        return 0


