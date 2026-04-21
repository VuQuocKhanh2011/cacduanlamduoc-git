def calculate(role, base, bonus):
    if role == "Manager":
        return base + bonus + 2000
    elif role == "Developer":
        return base + bonus + 1000
    else:
        return base + bonus