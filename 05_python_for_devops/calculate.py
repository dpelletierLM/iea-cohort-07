"""
This module allows uers to enter two values and an operation.
It will calculate the answer based on the values and operater entered
"""

import sys
import operator
import math
def calculate (op_a, op_b, oper):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        
    }
    
    if oper is not "log":
        operation = operations.get(oper)
        try:
            return operation(op_a, op_b)
        except ZeroDivisionError:
            print('You cannot divide by zero.')
        except TypeError:
            print(f"Operand types don't support {oper} operator")
        return None

    else:
        try:
            operation = math.log(op_a,op_b)
        except ZeroDivisionError:
            print('You cannot divide by zero.')
        except TypeError:
            print(f"Operand types don't support {oper} operator")
        except ValueError:
            print("Math domain error.  Base cannot be zero for log operation")
        else:
            return operation
if __name__ == "__main__"        :
    print("Running as a script!")
    print(f"My name is {__name__}")
    args = sys.argv[1:] # Slices args to remove file name which is always put at index 0
    operation = calculate(int(args[0]), int(args[1]), args[2])
    print(f"The answer to your input is {operation}")
else:
    info_entered = input("Enter two numbers seperated by a space and the operation you want to take on them ('+,-,/,*/log'): ")
    info_entered = info_entered.split()
    print(info_entered)
    op_a, op_b, oper = int(info_entered[0]), int(info_entered[1]), info_entered[2]
    operation = calculate(op_a, op_b, oper)
    print(f"The answer to your input is {operation}")
    
