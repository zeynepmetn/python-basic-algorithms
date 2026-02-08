letters = [chr(harf) for harf in range(ord('a'), ord('z') + 1 )]
digits = [int(sayi) for sayi in range(1,27)]
all_letters_digits = {}
result = []

for letter,digit in zip(letters, digits): # zip
    all_letters_digits[letter] = digit

s = input("girdi: ")
k = int(input("how many times: "))

new_value = 0
for letter in s:
    for letter2 in all_letters_digits.keys():
        if letter == letter2:
            new_value += all_letters_digits[letter2]
count = 0
while count < k:
    for digit in str(new_value):
        new_value = 0
        new_value += int(digit)
        count += 1
print(new_value)