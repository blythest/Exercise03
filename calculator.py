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
operand1 = 0
operand2 = 0

while keepGoing:
    prompt = raw_input("> ")

    print prompt  

    # split input into words
    words = prompt.split(" ")
    operation = words[0]

    num_inputs = len(words)
    print 'operation length is %d' % num_inputs

    if num_inputs == 1 and operation == 'Q':
        break

    elif num_inputs == 2:
        operand1 = int(words[1])

    elif num_inputs == 3:
        operand1 = int(words[1])
        operand2 = int(words[2])

    else:
        print 'wrong # of inputs'

    if correct_num_inputs(operation, num_inputs):

        if operation == "+":   
            print arithmetic.add(operand1, operand2)
        elif operation == "-":
            print arithmetic.subtract(operand1, operand2)
        elif operation == "*":   
            print arithmetic.multiply(operand1, operand2)
        elif operation == "/":
            print arithmetic.divide(operand1, operand2)
        elif operation == "pow":
            print arithmetic.power(operand1, operand2)
        elif operation == "square":
            print arithmetic.square(operand1)
        elif operation == "cube":
            print arithmetic.cube(operand1)
        elif operation == "%":
            print arithmetic.mod(operand1, operand2)
        else:
            print "Not yet implemented"



