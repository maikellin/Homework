def scalar_mult(s, v):
    for i in range(len(v)):
        v[i]=s*v[i]
    return v\

(scalar_mult(5, [1, 2]) == [5, 10])
(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
