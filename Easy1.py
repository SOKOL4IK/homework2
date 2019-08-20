fruits = ["яблоко", "банан", "киви", "арбуз"]
result = f" 1. {fruits[0]}\n 2. {fruits[1]}\n 3. {fruits[2]}\n 4. {fruits[3]}"
print(result)

first_list = {1, 2, 3, 4, 5}
second_list = {4, 5, 6, 7} 
print(first_list ^ second_list)

old_list = [55, 4, 22, 32, 10, 5]
new_list = []
last_element = len(old_list)

for i in range(last_element):
    if old_list[i] % 2 == 0:
        new_list.append(old_list[i] / 4)
else:
    new_list.append(old_list[i] * 2)
print(new_list)