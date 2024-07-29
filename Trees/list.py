
num=-123
number = str(num) #-123
res = []
contains_minus=False
final_result=""
when_to_stop=-1

if (number[0] == "-"):
    contains_minus = True
    when_to_stop=0

for i in range(len(number)-1,when_to_stop,-1): # -,1,2,3
        res.append(number[i])

if(contains_minus):
    final_result = "-"

for i in range(len(res)):
        final_result += res[i]
        
print(final_result)
