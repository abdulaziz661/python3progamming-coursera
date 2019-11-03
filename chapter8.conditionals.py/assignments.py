# percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
# resps = []
# for i in percent_rain:
#     if i > 90:
#         resps.append('Bring an umbrella.')
#     elif i > 80:
#         resps.append('Good for the flowers?')
#     elif i > 50:
#         resps.append('Watch out for clouds!')
#     else:
#         resps.append('Nice day!')
        
# print(resps)

string= ("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)