
data_set = [[0.0, 0.0], [1.0, 1.0], [1.0, 2.0], [2.0, 1.0]]

new_data_set = [[0 for col in range(4)] for row in range(3)]


def error_func_piece(x, y):

    return ((y - **2)


error_function=[]

for i in range(4):

    error_function.insert(i, error_func_piece(data_set[i][0], data_set[i][1]))


print(error_function)




'''
1. quadratic model 구현
2. error function 구현 (data set 대입 까지)
3. 미분해서 w값 구하기
4. 구한 w값을 가진 quadratic model 출력

'''
