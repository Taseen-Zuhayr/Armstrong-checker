a = int(input("Input a number here : "))
add = 0
temp = a

while temp>0:
    digit = temp%10
    add += digit**3
    temp//=10

if a==add:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")