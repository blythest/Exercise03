import arithmetic

keepGoing = True

while keepGoing:
    print "Please enter a pre-fix equation using integers. "
    
    prompt = raw_input()
    
    elements = prompt.split(" ")

    operation = elements[0]

    double_ops = ["+","-","*","/","%","pow"]
    single_ops = ["cube","square"]
    
    #Checking that the values are numbers in two value expresions
    if operation in double_ops:
        try:
            int(elements[1])
            int(elements[2])
        except ValueError: 
            print "Integers, please!"
            continue

    #Checking that the value is a number in one value expressions
    elif operation in single_ops:
        try:
            int(elements[1])
        except ValueError:
            print "Integers, please!"
            continue

    #Dealing with extra values for two value expressions
    if operation in double_ops:
        if len(elements) >= 4:
            print "Expression takes only two values."
            continue

    #Dealing with extra values for one value expressions
    if operation in single_ops: 
        if len(elements) >= 3:
          print "Expression takes one value."
          continue

    if operation == "q":
        break
    
    elif operation == "+":
        print arithmetic.add(int(elements[1]),int(elements[2]))

    elif operation == "-":
        print arithmetic.subtract(int(elements[1]),int(elements[2]))
    
    elif operation == "*":
        print arithmetic.multiply(int(elements[1]),int(elements[2]))

    elif operation == "/":
        print arithmetic.divide(float(elements[1]),float(elements[2]))

    elif operation == "%":
        print arithmetic.mod(int(elements[1]),int(elements[2]))

    elif operation == "square":
        print arithmetic.square(int(elements[1]))

    elif operation == "cube":
        print arithmetic.cube(int(elements[1]))

    elif operation == "pow":
        print arithmetic.power(int(elements[1]),int(elements[2]))

    else:
         print "Invalid input."