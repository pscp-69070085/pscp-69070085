"""Hint"""
line_unit = input()
line_tens = input()
line_huns = input()

def check_condition(val, cond_str):
    """check"""
    op, num_str = cond_str.split()
    num = int(num_str)
    if op == "==":
        return val == num
    if op == "!=":
        return val != num
    if op == ">":
        return val > num
    if op == ">=":
        return val >= num
    if op == "<":
        return val < num
    if op == "<=":
        return val <= num
    return False


for i in range(1000):
    h = i // 100
    t = (i // 10) % 10
    u = i % 10
    if (
        check_condition(u, line_unit)
        and check_condition(t, line_tens)
        and check_condition(h, line_huns)
    ):
        print(f"{i:03d}")
