class person:
    def __init__(self,name,age = 21, gender = 'male'):
        self.name=name
        self.age=age
        self.gender=gender
    def showInfo(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Gender: ',self.gender)
    def __str__(self):
        return self.name
eva = person('Eva',10,'male')
eva.showInfo()
print(eva)
print('------------------------')
adam = person('Adam')
adam.showInfo()
print('------------------------')
cain = person('Cain',1)
cain.showInfo()
