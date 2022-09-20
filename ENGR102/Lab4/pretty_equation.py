# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sumit Nalavade
# Section:      524
# Assignment:   Lab 4.14
# Date:         19 September 2022
#

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

# Each case is different which is why there are so many if statements
if (a != 0 and b != 0 and c != 0):
    if(a == 1):
        a = ""
    elif(a == -1):
        a = "- "
    elif(a < 0):
        a = f"- {a * -1}"

    if(b == 1):
        b = "+ "
    elif(b == -1):
        b = "- "
    elif(b < 0):
        b = f"- {b * -1}"
    else:
        b = f"+ {b}"

    if(c == 1):
        c = "+ 1"
    elif(c == -1):
        c = "- 1"
    elif(c < 0):
        c = f"- {c * -1}"
    else:
        c = f"+ {c}"

    print(f'The quadratic equation is {a}x^2 {b}x {c} = 0')

elif (a == b or b == 0) and c != 0 or (a == 0 or c == 0) and b != 0 or (b == 0 or c == 0) and a != 0:
    if(a == 0):
        if(b == 1):
            b = ""
        elif(b == -1):
            b = "- "
        elif(b < 0):
            b = f"- {b * -1}"
    
        if(c == 1):
            c = "+ 1"
        elif(c == -1):
            c = "- 1"
        elif(c < 0):
            c = f"- {c * -1}"
        else:
            c = f"+ {c}"
        
        print(f'The quadratic equation is {b}x {c} = 0')
    elif(b == 0):
        if a == 1:
            a = ""
        elif a == -1: 
            a = "- "
        elif a < 0:
            a = f"- {a * -1}"
        
        if c == 1:
            c = "+ 1"
        elif c == -1: 
            c = "- 1"
        elif c < 0:
            c = f"- {c * -1}"
        elif c > 0:
            c = f"+ {c}"

        if(c == 0):
            print(f'The quadratic equation is {a}x^2 = 0')
        else:
            print(f'The quadratic equation is {a}x^2 {c} = 0')

    elif c == 0:
        if a == 1:
            a = ""
        elif a == -1: 
            a = "- "
        elif a < 0:
            a = f"- {a}"
        
        if b == 1:
            b = "+ "
        elif b == -1:
            b = "- "
        elif b < 0:
            b = f"- {b}"
        elif b > 0:
            b = f"+ {b}"

        print(f'The quadratic equation is {a}x^2 {b}x = 0')  
