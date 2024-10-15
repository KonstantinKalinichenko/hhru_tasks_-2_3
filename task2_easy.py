def classify_triangle(input_string: str):
    a, b, c = map(int, input_string.split())
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        if area.is_integer():
            return int(area)
        else:
            return f'{area:.2f}'
    else:
        return 'Не существует'


input_string = input()
result = classify_triangle(input_string)
print(result)
