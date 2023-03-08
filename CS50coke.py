# In a file called coke.py, implement a program that prompts the user to insert a coin, 
# one at a time, each time informing the user of the amount due. Once the user has inputted 
# at least 50 cents, output how many cents in change the user is owed. Assume that the user will 
# only input integers, and ignore any integer that isn’t an accepted denomination.

amount_due = 50

possible_amounts = ["25", "10", "5"]

# Either make input an int or possible_amount a str

while amount_due > 0:
    coin_taken = input("Input a coin: ")
    if coin_taken in possible_amounts:
        coin_taken = int(coin_taken)
        amount_due = amount_due - coin_taken
        if amount_due <= 0:
            amount_due = (amount_due) * (-1) 
            # Would otherwise output "Change owed : -10" for example
            print(f"Change owed: {amount_due}")
            break

        print(f"Amount due: {amount_due}")
        
    else:
        print(f"Amount due: {amount_due}")    


