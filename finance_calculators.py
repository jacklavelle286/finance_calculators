import math

#initial choice between bond / investment

choice = input("Welcome to Lavelle Financial ltd. Choose either 'investment or 'bond' from the menu below to proceed. \n investment - to calculate the amount of interest you'll earn on your investment \n bond - to calculate the amount you'll have to pay on a home loan ")

#declaring the choices here as variables to ensure i can use .lower to remove case sensitivity from input

investment_choice = "investment" 
bond_choice = "bond"


#investment option
if choice.lower() == investment_choice.lower(): #this makes sure the user input is not case sensitive
    deposit = int(input("What is your deposit?: £"))
    interest_rate = int(input("What is the interest rate as a percentage?: "))
    number_of_years = int(input("How many years are you investing for?: "))
    compound_choice = "compound" 
    simple_choice = "simple"
    interest = input("Which type of interest do you want, compound or simple?: ")
    if interest.lower() == compound_choice.lower(): #compound investment choice 

        # the code below calcuates the total amount once the interest has been applied
        # formula is = P(1 + r) ^ t where:
        # r’ is the interest entered above divided by 100, (r = interest_rate)
        # 'P' is the amount the user deposits (p = deposit)
        #'t' is the number of years the money is being invested (t = number_of_years)
        # A = total amount once the interest has been applied

        A = number_of_years * math.pow((1 + interest_rate / 100), number_of_years) 
        total_amount_A_rounded_down = round(A , 2) # rounding to two Decimal places for readability
        print(f"The total amount of your investment once the interest has been applied is £{total_amount_A_rounded_down}.") #final output

    elif interest.lower() == simple_choice.lower(): #simple investment choice

         # the code below calcuates the total amount once the interest has been applied
        # formula is = A = P(1 + r * t) where:
        # r’ is the interest entered above divided by 100, (r = interest_rate)
        # 'P' is the amount the user deposits (p = deposit)
        #'t' is the number of years the money is being invested (t = number_of_years)
        # B = total amount once the interest has been applied

        B = deposit * (1 + interest_rate / 100 * number_of_years)
        total_amount_B_rounded_down = round(B, 2) 
        print(f"The total amount of your investment once the interest has been applied is £{total_amount_B_rounded_down}.")
    else: print("You entered an option incorrectly, please try again.")


#bond option
elif choice.lower() == bond_choice.lower(): 

        # the code below calculates the amount that a person will have to be repaid on a home loan each month is calculated as follows:
        # formula is as follows: monthly_repayment = (i * P)/(1 - (1+i)^(-n))
        # 'P' is the present value of the house (p = value_of_house)
        #'i'is the monthly interest rate, calculated by dividing the annual interest rate by 12. (i = monthly_interest_rate)
        #‘n’ is the number of months over which the bond will be repaid. (n = num_of_months)

    value_of_house  = int(input("What is the current value of the house?: £"))
    interest_rate = int(input("What is the interest rate as a percentage?: "))
    num_of_months = int(input("How many months are you planning to take to repay the bond?: "))
    monthly_interest_rate = interest_rate / 12
    monthly_repayment = (monthly_interest_rate * value_of_house) / (1 - (1 + monthly_interest_rate) ** (-num_of_months))
    # monthly_repayment = (monthly_interest_rate * value_of_house) / (1 - (1 + math.pow(monthly_interest_rate , num_of_months)))
    monthly_repayment_rounded_down = round(monthly_repayment , 2) # rounding to two Decimal places for readability
    print(f"Your monthly repayment will be £{monthly_repayment_rounded_down} per month.") #final output

else: print("You have entered an invalid option, please try again.") #if they enter neither "bond" nor  "investment"


    