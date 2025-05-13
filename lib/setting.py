class Human:
    species='homo sapiens'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getAge(self):
        print("retrieving age")
        return self.age    
    
    def setAge(self,age):
        if(type(age) in (int,float)) and(0<=age<=120):
            print(f"setting up age to {age}")
            self._age=age
        else:
            print('age must be a number between 0 to 120')    
        # sets up the set and get compiles them
    age =property(getAge,setAge)

bakari=Human('bakari',24)
bakari.age=24
bakari.name='bakari'
# print(f"My name is {bakari.name} , {bakari.age} years old")


# joe=Human('joe')
# print(joe.name)
# joe.species='habilis'
# print(joe.species)
# print(getattr(joe,'name'))
# setattr(ken,'name')
# print()