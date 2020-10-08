#birth_year = input('Birth year: ')
#print(type(birth_year))
#age = 2020 - int(birth_year)
#print(type(age))
#int() converts an integer
#float() converts a float
#bool() converts a boolean
#print(age)

weight_lbs = input(' How much do you weigh in pounds? ')
#asks for input of targets weight
kgweight = int(weight_lbs)/2.205
#converts the weight in pounds to kg
print((round(kgweight, 2)))