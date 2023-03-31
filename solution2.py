with open ('input.txt', 'r') as f:
    h = f.readlines()
    s = float(h[6])
    m0 = h[0].split()
    m1 = h[2].split()
    m2 = h[4].split() 
    row0 = int(m0[0])
    column0 = int(m0[1])
    row1 = int(m1[0])
    column1 = int(m1[1])
    row2 = int(m2[0])
    column2 = int(m2[1])
    z0 = h[1].split()
    z1 = h[3].split() 
    z2 = h[5].split() 
matrixA = []
matrixB = []
matrixC = []      
tmatrixC = []
resBC = []
multiBCA = [] 
g = 0
t = []
v = 0
if (row1 == column2 and column1 == row2) and (column0 == row1):
    for i in range(row0):          
        a =[]
        for j in range(column0):        
            a.append(float(z0[v]))   
            v += 1  
        matrixA.append(a)
    v = 0 
    for i in range(row1):          
        a =[]
        r = 0 
        for j in range(column1):        
            a.append(float(z1[v]))   
            a[r] = a[r] * s
            r += 1
            v += 1  
        matrixB.append(a)
    v = 0
    for i in range(row2):           
        a =[]
        for j in range(column2):        
            a.append(float(z2[v]))   
            v += 1  
        matrixC.append(a) 
    tmatrixC = [[matrixC[j][i] for j in range(len(matrixC))] for i in range(len(matrixC[0]))]
    resBC = [[tmatrixC[i][j] + matrixB[i][j] for j in range(len(matrixC))] for i in range(len(matrixC[0]))]
    for i in range(len(matrixA)):
        for j in range(len(resBC[0])):
            for k in range(len(resBC)):
               g = g + matrixA[i][k] * resBC[k][j]
            t.append(g) 
            g = 0 
        multiBCA.append(t) 
        t = []   
    output = open('output.txt', 'w')
    output.write(str(1))
    output.write('\n' + str(len(multiBCA)) + ' ' +  str(len(multiBCA[0])))
    res = []
    for x in multiBCA:
        res.extend(x if isinstance(x, list) else [x])
    output.write('\n' + ' '.join(map(str, res)))
    output.flush() 
    output.close()
    print(matrixA)
else:
 output = open('output.txt', 'w')
 output.write(str(0))
 output.flush() 
 output.close()