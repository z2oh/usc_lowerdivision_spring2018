import sys
from random import randint
MAX_EXCEPT = 25
MIN_RANGE = 100

start = randint(0, 999)
end = randint(start + start//10, start*10)
if(end-start) < MIN_RANGE:
    end += MIN_RANGE
num_exc = (end-start)//10
if(num_exc) > MAX_EXCEPT:
    num_exc = MAX_EXCEPT

excepts = []
while len(excepts) != num_exc:
    val = randint(start+2, end-2)
    for k in range(val-2,val+3):
        if k in excepts:
            continue
    excepts.append(val)
excepts.sort()

#start = 8;
#end = 20;
#excepts = [10,13,16]
#excepts = []

sys.stdout.write("{} {} ".format(start, end))
for i in range(len(excepts)):
    sys.stdout.write("{} ".format(excepts[i]))
sys.stdout.write("\n")
