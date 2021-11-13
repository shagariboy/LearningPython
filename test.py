list1 = [1,2,3]
list2 = []
for v in list1:
    list2.insert(0,v)
    
print(list2)    
    
    
    
vals = [0,1,2]
vals.insert(0,1)
del vals[1]    
print(sum(vals))

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
    
    
    
a = 1
b = 2
print(a == b)      


j = 0
while j <= 3:
    j += 2
    print("*")
    
t = [[3-x for x in range (3)] for y in range (3)]
s = 0
for t in range(3):
    s += t[x][y]
print(s)        


z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)


oL = [[0,1,2,3] for i in range(2)]
print(oL[2][0])

list = [1,2,3]
for v in range(len(list)):
     list.insert(1, list[v])
print(list)     


l = [1,2,3,4]
print(l[-3:-2])