def get_magic_triangle(n):
    triangle = []
    trow = [1]
    y = [0]
    for x in range(n):
        triangle.append(trow)
        trow = [left+right for left, right in zip(trow+y, y+trow)]

    return triangle


print(get_magic_triangle(5))
