def arithmetic_operation(tst):
    try:
        nt = tst.split(" ")
        a=int(nt[0])
        b=int(nt[-1])
        if nt[1] == "+":
            return a + b
        elif nt[1] == "-":
            return a - b
        elif nt[1] == "*":
            return a * b
        elif nt[1] == "/" or nt[1] == "//":
            return a / b
    except ZeroDivisionError:
        return -1
    except (ValueError, IndexError):
        return "Error: Invalid input format"
    
print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("12 - 12"))
print(arithmetic_operation("12 * 12"))
print(arithmetic_operation("12 / 0"))
print(arithmetic_operation("12 // /0"))