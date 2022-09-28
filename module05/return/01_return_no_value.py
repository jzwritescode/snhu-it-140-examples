###############################################################################
# DESCRIPTION:  This program uses a function to perform division. If division
#               by zero is detected, the function returns.
# CREDIT:       Gaddis, T. (2016). Starting Out with C++: 
#               From Control Structures Through Objects. 
#               United Kingdom: Pearson.
###############################################################################

def divide(arg1:float, arg2:float) -> None:
    """ The function divides arg1*
        by arg2 and shows the result. If arg2 is zero, however, the
        function returns without completing the calculation.                                         

    Args:
        arg1 (float): _description_
        arg2 (float): _description_
    """
    
    # Run error check to see if divisor is 0.  If so, display error message
    # and return control back to calling function.  Basically, do nothing...
    if (arg2 == 0.0):
        print("Sorry, I cannot divide by zero.")
        return
    
    quotient = arg1 / arg2
    print("The quotient is {result}".format(result=quotient))
    
def main() -> None:
    """Main function.   NOTE:  Python doesn't support a traditional
                        "main" function like other languages.
    """
    
    print("Enter two numbers and I will divde the first")
    print("number by the second number.\n")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    divide(num1, num2)
    
    
# Call "main" function
main()