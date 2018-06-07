def add_vectors(u, v):
    new_list=[]
    for i in range(len(u)):
        new_list.append(u[i]+v[i])
        return new_list\

(add_vectors([1, 1], [1, 1]) == [2, 2])
(add_vectors([1, 2], [1, 4]) == [2, 6])
(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
