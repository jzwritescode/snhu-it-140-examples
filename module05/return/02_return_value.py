###############################################################################
# DESCRIPTION:  This program uses a function that returns a value.
# CREDIT:       Gaddis, T. (2016). Starting Out with C++: 
#               From Control Structures Through Objects. 
#               United Kingdom: Pearson.
###############################################################################

def sum(num1:int, num2:int) -> int:
    """This function returns the sum of its two parameters

    Args:
        num1 (int): First number to be added.
        num2 (int): Second number to be added.

    Returns:
        int: Sum of num1 and num2.
    """
    return (num1 + num2)


def main() -> None:
    """Main function.   NOTE:  Python doesn't support a traditional
                        "main" function like other languages.
    """
    
    value1 = int(20)                    # The first value
    value2 = int(40)                    # The second value
    
    # Call the sum function, passing the contents of
    # value1 and value2 as arguments.  Assign the return
    # value to the total variable.
    total = sum(value1, value2)
    
    # Display the sum of the values
    print("The sum of {val1} and {val2} is {sum}".format(val1=value1, val2=value2, sum=total))
    
# Call "main" function
main()