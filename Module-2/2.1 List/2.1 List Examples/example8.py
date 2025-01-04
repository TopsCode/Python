vowel_list = [] 

name = input("Enter your name : ").lower()

for c in name:
    if c in "aeiou":
        vowel_list.append(c)

print(f"{name} contains {len(vowel_list)} vowels")
