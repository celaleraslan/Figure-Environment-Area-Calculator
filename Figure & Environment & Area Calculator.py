pi = 3.14
def square_perimeter(square_edge):
    perimeter = square_edge*4
    print("Perimeter of the square:",perimeter)

def square_area(square_edge):
    area = square_edge*square_edge
    print("Area of the square:",area)

def rectangle_perimeter(short_edge,long_edge):
    perimeter = (short_edge+long_edge)*2
    print("Perimeter of the rectangle:",perimeter)

def rectangle_area(short_edge,long_edge):
    area = short_edge*long_edge
    print("Area of the rectangle:",area)

def triangle_perimeter(edge1,edge2,edge3):
    perimeter = edge1+edge2+edge3
    return perimeter
    print("Perimeter of the triangle:",perimeter)

def triangle_area(edge1,edge2,edge3):
    u = triangle_perimeter(edge1,edge2,edge3)/2
    area = (u*(u-edge1)*(u-edge2)*(u-edge3))**(1/2)
    print("Area of the triangle:",area)

def circle_circumference(diameter):
    circumference = 2*pi*(diameter/2)
    print("Circumference of the circle:",circumference)

def circle_area(diameter):
    area = pi*((diameter/2)**2)
    print("Area of the circle:",area)

while(True):
    print("""Welcome to Figure & Environment & Area Calculator
         Calculated Figures:
         Square
         Rectangle
         Triangle
         Circle
         Enter 'q' to exit the program. """)
    figure = input("Please choose a figure:")
    if(figure == "q"):
        print("Program is closing...")
        break
    elif(figure == "square" or figure == "Square"):
        while(True):
            print("Calculation methods:\n"
                  "1-)Perimeter\n"
                  "2-)Area")
            calculation_type = input("Please enter the calculation type:")
            if(calculation_type == "1"):
                square_edge = int(input("Please enter the edge of the square:"))
                square_perimeter(square_edge)
                break
            elif(calculation_type == "2"):
                square_edge = int(input("Please enter the edge of the square:"))
                square_area(square_edge)
                break
            else:
                print("Missing or incorrect key.")
    elif figure == "rectangle" or figure == "Rectangle":
        while True:
            print("Calculation methods:\n"
                  "1-)Perimeter\n"
                  "2-)Area")
            calculation_type = input("Please enter the calculation type:")
            if calculation_type == "1":
                edge1 = int(input("Enter the short edge of the rectangle:"))
                edge2 = int(input("Enter the long edge of the rectangle:"))
                triangle_perimeter(edge1,edge2)
                break
            elif(calculation_type == "2"):
                edge1 = int(input("Enter the short edge of the rectangle:"))
                edge2 = int(input("Enter the long edge of the rectangle:"))
                triangle_area(edge1,edge2)
                break
            else:
                print("Missing or incorrect key.")
    elif(figure == "triangle" or figure == "Triangle"):
        while (True):
            print("Calculation methods:\n"
                  "1-)Perimeter\n"
                  "2-)Area")
            calculation_type = input("Please enter the calculation type:")
            if(calculation_type == "1"):
                edge1 = int(input("Enter the edge of the triangle:"))
                edge2 = int(input("Enter the edge of the triangle:"))
                edge3 = int(input("Enter the edge of the triangle:"))
                if(edge1 == edge2 or edge1 == edge3 or edge2 == edge3):
                    print("The triangle you entered is isosceles.")
                elif(edge1 == edge2 == edge3):
                    print("The triangle you entered is equilateral.")
                triangle_perimeter(edge1,edge2,edge3)
                break
            elif(calculation_type == "2"):
                edge1 = int(input("Enter the edge of the triangle:"))
                edge2 = int(input("Enter the edge of the triangle:"))
                edge3 = int(input("Enter the edge of the triangle:"))
                if(edge1 == edge2 or edge1 == edge3 or edge2 == edge3):
                    print("The triangle you entered is isosceles.")
                elif(edge1 == edge2 == edge3):
                    print("The triangle you entered is equilateral.")
                triangle_area(edge1,edge2,edge3)
                break
            else:
                print("Missing or incorrect key.")
    elif(figure == "circle" or figure == "Circle"):
        while (True):
            print("Calculation methods:\n"
                  "1-)Circumference\n"
                  "2-)Area")
            calculation_type = input("Please enter the calculation type:")
            if(calculation_type == "1"):
                diameter = int(input("Enter the diameter of the circle:"))
                circle_circumference(diameter)
                break
            elif(calculation_type == "2"):
                diameter = int(input("Enter the diameter of the circle:"))
                circle_area(diameter)
                break
            else:
                print("Missing or incorrect key.")
    else:
        print("Please choose the correct figure.")
