# Functions Examples
This folder contains examples for using the return in Python.

## Example 1:  Returning a value
This program uses a function that returns a value.

Key highlights include:

- Line 8:  Type hints.  "num1" and "num2" are variables with an expected type of integer (int).  The function is expected to return an integer.
- Line 18:  Example of a return.  This statement will add two numbers and the result will be returned.
- Line 21:  The "main" function.  In Python, this doesn't exist, but textbooks tend to create a "main" function to help organize code.  Notice there's a return type of "None" as this function will finish without returning a value.
- Line 32:  The variable "total" will hold the return value from Line 18.
- Line 35:  Example of string formatting using placeholder values.


## Example 2: Function that doesn't return a value
This program uses a function to perform division. If division by zero is detected, the function returns.

Key highlights include:

- Line 9:  Type hints.  "arg1" and "arg" are variables that expected floating-point (float) data.  The function will not return anything.
- Lines 21-23:  Error check to see if the divisor is zero.  If so, then display an error message and return control back to the point where the function was called.
- Line 39:  Call to the divide function.  The program will attempt to divide two numbers.  If the divisor is zero, an error will print (Line 22) and the program will return to this point and continue on without doing anything else.

