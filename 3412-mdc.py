def mdc(num1, num2):
    for i in range(1, num1+1):
        if num1%i==0 and num2%i==0:
            mdc = i
    return mdc

num1 = int(input())
num2 = int(input())

print(f'MDC={mdc(num1, num2)}')