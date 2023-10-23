# n = int(input())
# A = []
# for r in range(n):
#     for c in range(n):
#         A[r][c] = 1
# for row in A:
#     print(*row)
#
# n = n = int(input())
# A = [[0]*n for _ in range(n)]
# for row in A:
#     print(*row)

# n, m = int(input()), int(input())  # считываем значения n и m
#
# my_list = [[0] * m for _ in range(n)]
# for row in my_list:
#     print(*row)

def matrix(n = 1, m = None, Value = 0): # тут указаны значения аргументов по умолчанию. далее они могут меняться при передаче в функцию
    if m == None:
        m = n

    my_list = [[Value] * m for _ in range(n)]
    return my_list

print(matrix())   # n=1, m=1(тк m=ничего) v=0 (по умолчанию)
print(matrix(3))  # n=3, m=3(тк m=ничего), v=0 (по умолчанию)
print(matrix(2, 5))  # n=1, m=5, v=0 (по умолчанию)
print(matrix(3, 4, 9))  # n=1, m=4, v=9
