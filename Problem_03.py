sentence = input("Enter your sentence: ")
e_counter = 0

for e in sentence:
    if 'e' in e:
        e_counter = e_counter + 1

print(f"the letter 'e' appears {e_counter} times in the sentence.")
