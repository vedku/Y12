def height():
    height = input("How tall are you? (M):")
    return height

def weight():
    weight = int(input("How much do you weigh? (kg):"))
    return weight

weight = weight()
height = height()
BMI = weight/height**2
