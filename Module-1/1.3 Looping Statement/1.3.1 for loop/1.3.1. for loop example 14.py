# accept 5 numbers from user and perform addition of even nos and perform addition of odd nos 

even_sum = 0 
odd_sum = 0 

for i in range(1,6):
    num = int(input("Enter a number : "))
    if num%2 == 0:
        even_sum += num 
    else:
        odd_sum += num 

print(f"even sum = {even_sum}")
print(f"odd sum = {odd_sum}")