with open('input.txt' , 'r') as f:
    h = f.readline().split()
a = float(h[0])#  1
b = float(h[1])#  1
c = float(h[2])#  2
d = float(h[3])#  2
p = float(h[4])#  1
q = float(h[5])#  2
x = float()
y = float()
s = float()
t = float()
det0 = (a*d) - (b*c)
file = open('output.txt' , 'w') 
if det0 != 0:
    det1 = (p*d) - (b*q)
    det2 = (a*q) - (p*c)
    x = det1/det0
    y = det2/det0
    file.write(str('2' + ' ' + str(x) + ' ' + str(y))) #2
elif (a != 0 and c != 0 and b != 0 and d != 0) and (a * d == b * c) and (p * c == q * a):
    s = -(a/b)
    t = p/b
    file.write(str('1' + ' ' + str(s)  + ' ' +  str(t))) #1 
elif (a == 0 and b == 0 and p ==0) and (c != 0 and d != 0):
    s = -(c/d)
    t = q/d 
    file.write(str('1' + ' ' + str(s)  + ' ' +  str(t))) #1
elif (c == 0 and d == 0 and q ==0) and (a != 0 and b != 0):
    s = -(a/b)
    t = p/b 
    file.write(str('1' + ' ' + str(s)  + ' ' +  str(t))) #1
elif (c != 0 and a != 0) and (b == 0 and d == 0) and (q/c == p/a):
    x = q/c
    file.write(str('3' + ' ' + str(x))) #3 
elif (a != 0 and c == 0 and b == 0 and d == 0 and q == 0):
    x = p/a 
    file.write(str('3' + ' ' + str(x))) #3
elif (c != 0 and a == 0 and b == 0 and d == 0 and p == 0):
    x = q/c  
    file.write(str('3' + ' ' + str(x))) #3
elif (d != 0 and b != 0) and (a == 0 and c ==0) and (q/d == p/b):
    y = q/d 
    file.write(str('4' + ' ' +  str(y))) #4
elif (d != 0 and b == 0) and (a == 0 and c ==0) and p == 0:
    y = q/d 
    file.write(str('4' + ' ' +  str(y))) #4
elif (b != 0 and d == 0) and (a == 0 and c ==0) and q == 0:
    y = p/b
    file.write(str('4' + ' ' +  str(y))) #4
elif a == 0 and b == 0 and c == 0 and d ==0  and p ==0  and q == 0:
    file.write(str('5')) #5 
else:
    file.write(str('0'))#0
file.close()
