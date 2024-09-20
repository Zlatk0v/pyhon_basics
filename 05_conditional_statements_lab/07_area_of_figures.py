# квадрат (square),
# правоъгълник (rectangle),
# кръг (circle)
# триъгълник (triangle)
# •	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# •	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# •	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# •	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.
import math

figure = input() #  (square), (rectangle), (circle), (triangle)

if figure == "square":
    side_a = float(input())
    area = side_a * side_a

elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area=side_a * side_b

elif figure == "circle":
    radius = float(input())
    area = math.pi * radius * radius

else:
    side_a = float(input())
    h_a = float(input())
    area = side_a * h_a / 2

print(f"{area : 3f}")