# Write a program which repeatedly reads numbers until user
# enters 'done'. Then print the total, count and average of the numbers.
# handle input errors with try and except 


def main():

    num = 0
    total = 0.0

    while True:
        
        
            n = input("Please input a number: ")

            if n == 'done':           
                print(num, total, (total / num))
                break
        
            else:
                try:
                    n = float(n)
                except:
                    n = 0
                    num = num - 1 

                    # n = 0 because even though 'except' is used, n stil has a str value and will be used to perform 
                    # calculations, which fails. 
                    # num = num - 1 because the improper input still adds to the count and messes up the calculations

                    print("Please input a number, not a string.")

                num = num + 1
                total = total + n


        # n is floated after checking whether n == "done" because else "done" produces an error
        # (because you can't 'float' a str)
        
main()
