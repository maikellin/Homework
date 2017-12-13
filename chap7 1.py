mylist=[0,2,3,7,11,12]
def count_odd(numlist):
    count=0
    for i in numlist:
        if i%2 !=0:
            count+=1
    return count

def sum_even(numlist):
    sum=0
    for i in numlist:
        if i%2 ==0:
            sum+=i
    return sum

thelist=[-2,-5,6,-21,100]
def sum_neg(numlist):
    sum=0
    for i in numlist:
        if i%2 ==0:
            sum=i
    return sum

print(count_odd(mylist))
print(sum_even(mylist))
print(sum_neg(mylist))


            