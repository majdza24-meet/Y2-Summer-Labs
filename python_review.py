
sumofevens=0
import random
temperatures=[]
Days0fweek=["sunday","monday","tuesday","wednesdy","thursday","friday","saturday"]
for i in range(7):
 temperatures. append (random. randint(26,41))
print(temperatures)
                                              
for i in range(7):
  if temperatures[i]%2==0:
    sumorevens= sumofevens+1
    print(Days0fweek[i])


highest_temp= 25
highest_temp_day='Sunday'

for i in range(7):
  if temperatures[i]>highest_temp:
    highest_temp=temperatures[i]
    highest_temp_day= Days0fweek[i]
print(highest_temp)
print(highest_temp_day)

lowest_temp=41
Lowesttemp_day='Sunday'

for i in range(7):
  if temperatures[i]<lowest_temp:
    lowest_temp=temperatures[i]
    lowesttemp_day= Days0fweek[i]
print(lowest_temp)
print(lowesttemp_day)

sumOfTemps=0
for i in range(7):
  sumOfTemps=+temperatures[i]

avg= sumOfTemps/7
print (avg)
above_avg=[]

for i in range(7):
  if temperatures[i]>avg:
    above_avg.append(Days0fweek[i])
print(above_avg)