def area_circle(radius, rounded = False):
    result = 3.142 * radius**2
    if rounded == True:
        result = round(result)
    print(result)

area_circle(15 , rounded=True)
area_circle(190)
