import simple_maths as sm
print(sm.addition(1,2,3,4,5,6))
print(sm.average(1,2,3,4,5,6))
print(sm.max_value(1,2,3,4,5,6))



#Lambda example
from functools import reduce
scores = [75, 65, 80, 95, 50]
total = reduce(lambda a, b: a + b, scores)
print(total)