def arithmetic_operation(tst):
    nt = tst.split(" ")
    if int(nt[-1]) == 0:
        return -1
    if nt[1] == "+":
        return int(nt[0]) + int(nt[-1])
    elif nt[1] == "-":
        return int(nt[0]) - int(nt[-1])
    elif nt[1] == "*":
        return int(nt[0]) * int(nt[-1])
    elif nt[1] == "/" or nt[1] == "//":
        return int(nt[0]) / int(nt[-1])
    
print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("12 - 12"))
print(arithmetic_operation("12 * 12"))
print(arithmetic_operation("12 / 0"))
print(arithmetic_operation("12 // 0"))