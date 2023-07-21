# calculate the electricity bill

def calculate_electric_bill(unit):
    total_cost = 0
    if unit <= 200:
        total_cost = (unit - 100) * 5
    elif unit > 200:
        total_cost = (100 * 5) + ((unit - 200) * 10)

    return total_cost


inp = int(input("Enter unit: "))
cost = calculate_electric_bill(inp)
print("Bill amount: ", cost)