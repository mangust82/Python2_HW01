#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c -
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
def chek_triangle(a,b,c):
    if b>= a + c or a>= b + c or c>= a + b:
        return print('Такого треугольника не существует')
    elif a<= b + c or b<= a + c or c<= a + b:
        return print('Такой треугольник существует')
    elif a==b==c:
        return print('Треугольник равносторонний')
    elif a==b or a==c or b==c:
        return print('Треугольник равнобедренный')
    else:
        return print('Треугольник разносторонний')

a = (int(input('Введите а:')))
b = (int(input('Введите b:')))
c = (int(input('Введите c:')))
result = chek_triangle(a,b,c)
print(result)
