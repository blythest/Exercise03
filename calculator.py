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

def create_operand_array(elements):
    operands_local = ["E","E"]
    num_inputs = len(elements)
    for i in range(1,num_inputs):
        if elements[i].isdigit():
            operands_local[i-1] = int(elements[i])
    return operands_local
    
def valid_input(operands):
    print len(operands)
    for i in operands:
        print i,operands[i-1]
        if operands[i] == 'E':
            return False
        else:
            return True


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
    operand = create_operand_array(elements)
    print operand


    if (correct_num_inputs(operation, num_inputs) and valid_input(operand)):

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






