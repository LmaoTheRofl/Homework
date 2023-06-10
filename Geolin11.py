import numpy as np

A = np.array([[[[[3, -2], [1, 1]], [[3, -2], [5, -4]]], [[[6, -4], [2, -1]], [[-6, 2], [-4, -5]]]], [[[[-3, 1], [-2, 2]], [[1, 2], [-1, -1]]], [[[-3, 4], [5, -1]], [[0, 1], [-5, 4]]]]])
Anew1 = np.ones((2, 2, 2, 2, 2))
Anew2 = np.ones((2, 2, 2, 2, 2))
Anew3 = np.ones((2, 2, 2, 2, 2))
Anew4 = np.ones((2, 2, 2, 2, 2))
Anew5 =np.ones((2, 2, 2, 2, 2))
Anew6 = np.ones((2, 2, 2, 2, 2))
Anew7 = np.ones((2, 2, 2, 2, 2))
Anew8 = np.ones((2, 2, 2, 2, 2))
Anew9 = np.ones((2, 2, 2, 2, 2))
Anew10 = np.ones((2, 2, 2, 2, 2))
Anew11 = np.ones((2, 2, 2, 2, 2))
Anew12 = np.ones((2, 2, 2, 2, 2))
Anew13 = np.ones((2, 2, 2, 2, 2))
Anew14 = np.ones((2, 2, 2, 2, 2))
Anew15 = np.ones((2, 2, 2, 2, 2))
Anew16 = np.ones((2, 2, 2, 2, 2))
Anew17 = np.ones((2, 2, 2, 2, 2))
Anew18 = np.ones((2, 2, 2, 2, 2))
Anew19 = np.ones((2, 2, 2, 2, 2))
Anew20 = np.ones((2, 2, 2, 2, 2))
Anew21 = np.ones((2, 2, 2, 2, 2))
Anew22 = np.ones((2, 2, 2, 2, 2))
Anew23 = np.ones((2, 2, 2, 2, 2))
for l in range(2):
    for i in range(2):
        for q in range(2):
            for p in range(2):
                for m in range(2):
                    Anew1[l,i,q,p,m]=A[l,i,m,p,q]
                    Anew2[l, i, q, p, m] = A[l, i, q, p, m]
                    Anew3[l, i, q, p, m] = A[l, i, m, p, q]
                    Anew4[l, i, q, p, m] = A[l, i, m, q, p]
                    Anew5[l, i, q, p, m] = A[l, i, p, q, m]
                    Anew6[l, i, q, p, m] = A[q, i, l, p, m]
                    Anew7[l, i, q, p, m] = A[q, i, m, p, l]
                    Anew8[l, i, q, p, m] = A[q, i, l, m, p]
                    Anew9[l, i, q, p, m] = A[q, i, p, l, m]
                    Anew10[l, i, q, p, m] = A[q, i, p, m, l]
                    Anew11[l, i, q, p, m] = A[q, i, m, l, p]
                    Anew12[l, i, q, p, m] = A[p, i, l, q, m] 
                    Anew13[l, i, q, p, m] = A[p, i, m, q, l]
                    Anew14[l, i, q, p, m] = A[p, i, q, l, m]
                    Anew15[l, i, q, p, m] = A[p, i, m, l, q]
                    Anew16[l, i, q, p, m] = A[p, i, l, m, q]
                    Anew17[l, i, q, p, m] = A[p, i, q, m, l] 
                    Anew18[l, i, q, p, m] = A[m, i, l, p, q] 
                    Anew19[l, i, q, p, m] = A[m, i, q, p, l]
                    Anew20[l, i, q, p, m] = A[m, i, l, q, p]
                    Anew21[l, i, q, p, m] = A[m, i, q, l, p]
                    Anew22[l, i, q, p, m] = A[m, i, p, q, l]
                    Anew23[l, i, q, p, m] = A[m, i, p, l, q] 
sum = A+Anew1+Anew2+Anew3+Anew4+Anew5+Anew6+Anew7+Anew8+Anew9+Anew10+Anew11+Anew12+Anew13+Anew14+Anew15+Anew16+Anew17+Anew18+Anew19+Anew20+Anew21+Anew22+Anew23
res = sum/24
print(res)