name = 'Taylor Roberts Hasting'
#string = name and that name is Taylor Roberts Hasting
print(name[0:3])
#call the first three characters of the string, "Tay"
print(name[:5])
#Python will call the first 5 letters in the string, name, and assume we start at 0, similar to the above example "Taylo"

print(name[:])
#using this syntax python will clone the  string name.

another = (name[:])
print(another[:])

#########################################

nickname = 'Bobby'
print(nickname[1:-1])
#In this example we call the string Bobby, and then remove the first and last letters from it; eg B and y respectively. 