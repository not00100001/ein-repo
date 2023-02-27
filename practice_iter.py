list1 = ["dalai", "lama", "llama"]

my_first_iter = iter(list1)

my_second_iter = iter(list1)

print(my_first_iter)

print("")

print(next(my_first_iter), "\n\n")

# with this you can also add multiple blank lines if you find it prettier

print("""An iterator retains state internally. It knows which values have been
obtained already. So when you call next(), it knows what value to return next""", "\n\n")

print(next(my_second_iter))
print(next(my_first_iter))

# note how you can define multiple iters and use them as you see fit
