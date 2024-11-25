conditions = {"length": False, "has_uppercase": False, "has_onedigit": False}

def strength(password):
    if len(password) > 7:
        conditions["length"] = True
    for i in password:
        if i.isupper():
            conditions["has_uppercase"] = True
        if i.isdigit():
            conditions["has_onedigit"] = True

    # Determine if all conditions are met
    if all(conditions.values()):
        return "Strong Password"
    else:
        return "Weak Password"


user_input = input("Enter password: ")
print(strength(user_input))





