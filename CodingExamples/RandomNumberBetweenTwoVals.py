import random as rd

def generate_random_no_between_two_values(lwr, upr):
    random_no = rd.randint(lwr,upr)
    return random_no


lwr_bound = int(input("Enter the lower bound: "))
upr_bound = int(input("Enter the upper bound: "))
rand = generate_random_no_between_two_values(lwr_bound, upr_bound)
print(f"Between the lower bound {lwr_bound} and the upper bound {upr_bound} we have randomly generated the number: {rand}")