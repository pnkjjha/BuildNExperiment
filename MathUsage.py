#Pankaj Jha
#12/10/23
# These modules are preinstalled modules with Python Standard library 
import math
#import cmath

def toDegree( rad ): #block code is indicated by : whether it is if or while (loop) or funcion
    """ This is docustring; first line of the module, used by auto documentaion software. 
        Multiline strings are enclosed in three consecutive quotes
    """
    degree = (rad/math.pi)*180
    return degree

# conversion of one data tpe to another
radian = input("Enter the malue of the angle in Radian\n")

#if data is of a particular type
if isinstance(radian, float):
    print(f"{radian} is float data type")
else:
    print(f"{radian} is not a float \n", flush = True)
    # Data type conversion
    radian = float(radian)

#call the module toDegree
print(f"The {radian} is {toDegree(radian)} in degrees")


