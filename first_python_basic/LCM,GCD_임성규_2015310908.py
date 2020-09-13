
def GCD(x, y):
    if y > x:
        tmp = x
        x = y
        y = tmp
    while y > 0:
        z = y
        y = x % y
        x = z
    print(x)

# 유클리드 호제법을 이용한 GCD 함수


def LCM(x, y):

    multi_num = (x*y)
    if y > x:
        tmp = x
        x = y
        y = tmp
    while y > 0:
        z = y
        y = x % y
        x = z
    # GCD값 =  x

    lcd_num = multi_num // x
    # 주어진 두 수를 곱한 값에 GCD를 나누어준 값이 LCD

    print(lcd_num)


num_1, num_2 = map(int, input().split())
# 두 수 입력받기

print("GCD = ", end="")
GCD(num_1, num_2)
print("LCM = ", end="")
LCM(num_1, num_2)

# 구해낸 GCD, LCD 출력


'''
GCD는 유클리드호제법을,
LCM는 두 수를 곱한값에서 GCD를 나눠준 값이 LCM라는 것을 이용하여 각각의 함수를 만들어 주었습니다.
'''
