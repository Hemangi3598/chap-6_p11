# wapp to keep a track on food ordered bt ks and ss
# [] ==> list : is a data type to store the elements

order = []

print(type(order))

res = input(" do u want to order something y/n ")
while res == "y":
	name = input("enter food name ")
	order.append(name)
	res = input(" do u want to order more y/n ")
print(order)