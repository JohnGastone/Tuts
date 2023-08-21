# This is Switch conditional statement, it work in corporation with other built in
# python keywords / data structures like if...else and dictionaries

# Creating a switch statement
def switch_case(case):
    switch_dict = {
        "case1": "This is case 1",  # This is the first case of the Switch statement
        "case2": "This is case 2",  # ----||-----
        "case3": "This is case 3"  # ----||-----
    }
    # result = switch_dict.get(case, "case3")
    # print(result)


print(switch_case("case2"))  # Outputs: This is case 3
