# Գրել կլաս Person, որը ունի դաշտեր
# 1 անուն, ազգանուն, տարիք, սեռ։ +
# 2 Ունի մեթոդներ այդ դաշտերը վերադարձնելու համար +

# Գրել կլաս Student , որը ժառանգում է Person֊ից, և ունի դաշտեր
# 1 համալսարան, ֆակուլտետ, կուրս, միջին  գնահատական
# 2 ունի մեթոդ, որը ստանում է հերթական հանձնած քննության գնահատականը, և համապատասխանաբար փոխում է միջին գնահատականը։

class UserError(Exception):
    pass


class Person:
    def __init__(self, fname, last_name, age, gender):
        self.fname = fname
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self,value):
        if isinstance(value, str):
            self._fname = value
        else:
            self._fname = ''
            raise UserError(f"first name must be a string : {value}")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self,value):
        if isinstance(value, str):
            self._last_name = value
        else:
            self._last_name = ''
            raise UserError(f"last name must be a string : {value}")
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if isinstance(value, int) and  value >= 0 :
            self._age = value
        else:
            self._age = 0
            raise UserError(f"age must be a int and positive: {value}")

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self,value):
        if isinstance(value, str):
            self._gender = value
        else:
            self._gender = ''
            raise UserError(f"gender must be a string : {value}")
        
    def __str__(self):
        return f"First name : {self.fname}, Last name : {self.last_name} \nAge : {self.age}, gender : {self.gender}"
        
class Student(Person):
    def __init__(self, fname, last_name, age, gender, university, faculty, year, avarage_score):
        super().__init__(fname, last_name, age, gender)
        self.university = university
        self.faculty = faculty
        self.year = year
        self.avarage_score = avarage_score
        self._examen_quantity = 0



    @property
    def university(self):
        return self._university
    @university.setter
    def university(self,value):
        if isinstance(value, str):
            self._university = value
        else:
            self._university = ''
            raise UserError(f"univeristy must be a string : {value}")
    
    @property
    def faculty(self):
        return self._faculty
    @faculty.setter
    def faculty(self,value):
        if isinstance(value, str):
            self._faculty = value
        else:
            self._faculty = ''
            raise UserError(f"faculty must be a string : {value}")
        
    @property
    def year(self):
        return self._yera
    @year.setter
    def year(self,value):
        if isinstance(value, int) and  value > 0 :
            self._yera = value
        else:
            self._yera = 0
            raise UserError(f"yera must be a int and positive: {value}")

    @property 
    def avarage_score(self):
        return self._avarage_score
    @avarage_score.setter
    def avarage_score(self,value):
        if isinstance(value, (int, float)) and  value >= 0 :
            self._avarage_score = value
        else:
            self._avarage_score = 0
            raise UserError(f"avarage score must be a int and positive: {value}")

    def add_examen_assessment(self, assessment):
        total_points = self.avarage_score * self._examen_quantity + assessment
        self._examen_quantity += 1
        self.avarage_score = total_points / self._examen_quantity
        return self.avarage_score
    
    def __str__(self):
        return f"{super().__str__()} \nUniversity : {self.university}, Faculty : {self.faculty} \nYear: {self.year}, Avarage score: {self.avarage_score}"

person = Person("Anna", "Don", 20, "Female")
print (person)

student = Student("Hayk", "martirosyan", 23, "Male", "EPH", "IKM", 1, 0)
print (student)

student.add_examen_assessment(3.75)
student.add_examen_assessment(2.75)
student.add_examen_assessment(3.5)
print (student)