# Form is Poly+Poly+Poly
# Valid Examples:
# 2x^5
# 3x^4+2x^2+2
# 3
# 2x
# Invalid Examples:
# 2x^
# 2x^4-13
# -2x^5


import random

# Test Case Number
testcase = 0

# Lowest coef & exponent to highest
low = 0
high = 4

coef_low = 1

# Number of polynomials wanted
num_poly = 3

num_generations = 2

start_number = 0

print(num_generations)
for x in range(num_generations):
    result_str = ""
    last_was_zero = False

    for y in range(num_poly):
        coef = random.randrange(coef_low, high)
        expr = random.randrange(low, high)

        # print ('coef' + str(coef))
        # print ('expr' + str(coef))

        # only need coef
        if y != 0:
            result_str += "+"
        if expr == 1:
            if coef == 1:
                result_str += "x"
            else:
                result_str += str(coef) + "x"

        elif expr == 0:
            result_str += str(coef)

        else:
            if coef == 1:
                result_str += "x^" + str(expr)
            else:
                result_str += str(coef) + "x^" + str(expr)

    print(result_str)