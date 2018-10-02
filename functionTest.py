def sum(a,b):
    return a + b



c = sum(1,2)
print(c)

def sum2(a,b):
    print("%d와%d의 합: %d" % (a,b,a + b))

sum2(3,4)

print(sum2(3,4))

#designate param regardless of order
def sum3(a,b):
    return a + b

print(sum3(b=4,a=6))




#multiple param
def sum4(*arg):
    sum = 0
    for i in arg :
        sum +=i
    return sum

print(sum4(1,2,3))
print(sum4(0,2,4,6,8))



#multi param2 - *arg
def sum5(choice, *arg):
    if choice == "num":
        result = 0
        for i in arg :
            result += i
    elif choice == "str":
        result = ""
        for i in arg :
            result += i
    return result

print(sum5("num", 1,2,3,4,5))
print(sum5("str", 'a','b','c'))

# keyword param - **kwargs    key = value

def func(**kwarg):
    print(kwarg)

func(a=1)
func(age=99, name='park')


# *arg **kwarg combination
def func(*arg, **kwarg):
    print(arg)
    print(kwarg)

func(1,2,3,a='a',b='b')

# result 
def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
print(result)

#local variable
#lamda 
list = [1,2,3,4,5,6,7]











