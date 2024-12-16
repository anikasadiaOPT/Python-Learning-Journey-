# Logical Operators: Used to evaluate multiple conditions.
# 
# 1. OR: At least one condition must be True.
#    Example: True or False → True

# 2. AND: Both conditions must be True.
#    Example: True and False → False
 
# 3. NOT: Inverts the condition.
#    Example: not True → False, not False → True


# Example 1: Deciding whether to buy coffee based on price, budget, and other conditions

price = 1000
budget = 800
in_budget = True 
if price > 1200 or budget > 500 or in_budget:
    print("I will buy coffee")
else:
    print("I won't buy coffee")
    
# Example 2: Determining student scholarship eligibility based on grade and extracurricular activities

# Inputs   
grade = 65
extra_curricular = True

# Scholarship eligibility conditions
if grade <= 100 and extra_curricular:               # AND ensures both conditions must be true.
    print("The student is eligible for the scholarship.")
elif 80 < grade <90 or extra_curricular:            # OR allows either condition to be true.
    print("You have to work on extra_curricular activities")
elif 70 < grade <80 and extra_curricular:
    print("You have to work a little bit hard")
elif 60 < grade <= 70 or not extra_curricular:      # NOT inverts the extracurricular condition.
    print("You need to work harder")
elif 60 < grade <= 70 and not extra_curricular:
    print("Do not lose your hope")
else:
    print("The student is not eligible for the scholarship.")
