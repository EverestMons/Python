str = "If monkeys like bananas, then I must be a monkey!"
new_str = str.replace("monkey","aligator")
print new_str

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[7]

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
new_z = z[:5]
z.remove(-2)
z.remove(2)
z.remove(6)
z.remove(7)
z[0]=new_z
print z
