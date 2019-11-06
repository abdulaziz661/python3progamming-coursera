#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.

#Hard-coded answers will receive no credit.


rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

num_rainy_months = []

my_list = rainfall_mi.split(",")

num_rainy_months = 0

print(my_list)

 

for num in my_list:

    if float(num) > 3.0:

        num_rainy_months += 1

print(num_rainy_months)

#The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.

#Hard-coded answers will receive no credit.


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
2
​
3
# Write your code here.
4
words = sentence.split()
5
same_letter_count = 0
6
for word in words:
7
    if word[0] == word[-1]:
8
        same_letter_count += 1
9
print(same_letter_count)   

#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
#HINT 1: Use the accumulation pattern!

#HINT 2: the in operator checks whether a substring is present in a string.

#Hard-coded answers will receive no credit.


items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num = 0

for i in items:

    if "w" in i[0:]:

        

        acc_num += 1

    print(acc_num)

    s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

 = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels = sum([1 for i in s if i in vowels])
print(num_vowels)