#import sys
#sys.path.append("/home/user/src/exercise03")
import arithmetic

def correct_num_inputs(operator, num_inputs):
    if operator in ['+', '-', '/','%','pow','*'] and num_inputs == 3:
        return True
    elif operator in ["square","cube"] and num_inputs == 2:
        return True
    else:
        print "Wrong number of operands for %r" % operator
        return False

print "  Enter an equation -- operation followed by operands  delimit by spaces"

keepGoing = True
operand = [0,0]

while keepGoing:
    prompt = raw_input("> ")

    print prompt  

    # split input into elements
    elements = prompt.split(" ")
    operation = elements[0]

    num_inputs = len(elements)
#    print 'operation length is %d' % num_inputs

    if num_inputs == 1 and operation == 'Q':
        break


    elif num_inputs == 2:
        if elements[1].isdigit():
            operand[0] = int(elements[1])
        else:
            print "Please enter only integers"

    elif num_inputs == 3:  
        if elements[1].isdigit():
            operand[0] = int(elements[1])
        else:
            print "Please enter only integers"
        
        if elements[2].isdigit():
            operand[1] = int(elements[2])
        else:
            print "Please enter only integers"

    else:
        print 'wrong # of inputs'

    if correct_num_inputs(operation, num_inputs):

        if operation == "+":   
            print arithmetic.add(operand[0], operand[1])
        elif operation == "-":
            print arithmetic.subtract(operand[0], operand[1])
        elif operation == "*":   
            print arithmetic.multiply(operand[0], operand[1])
        elif operation == "/":
            print arithmetic.divide(operand[0], operand[1])
        elif operation == "pow":
            print arithmetic.power(operand[0], operand[1])
        elif operation == "square":
            print arithmetic.square(operand[0])
        elif operation == "cube":
            print arithmetic.cube(operand[0])
        elif operation == "%":
            print arithmetic.mod(operand[0], operand[1])
        else:
            print "Not yet implemented"



