# check whether a person is eligible for voting or not

def check_eligibility(age):
    if age < 18:
        print("You are not eligible for Voting!!!")
    else:
        print("Your are eligible for Voting!!!")


inp = int(input("Enter your age: "))
check_eligibility(inp)