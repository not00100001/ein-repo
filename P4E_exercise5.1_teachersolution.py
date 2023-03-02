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
                    print("Please input a number, not a string.")
                    continue
                # 'continue' skips the current iteration of the loop and the control flow of the program 
                # goes to the next iteration.
                num = num + 1
                total = total + n


        # n is floated after checking whether n == "done" because else "done" produces an error
        # (because you can't 'float' a str)
        
main()
