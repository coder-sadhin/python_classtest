# import math
    # result = 1
    # for i in range(1, n+1):
    #     result *= math.factorial(i)
    # return result
# sys.set_int_max_str_digits()
def fact_of_fact(n):
    ans=1.0
    tmp=1.0
    for i in range(1,n+1):
        tmp=tmp*i
        ans=ans*tmp
    return ans
result = fact_of_fact(int(input()))
print(result)
# n = int(input())
# result = fact_of_fact(n)

