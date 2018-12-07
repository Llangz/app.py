from math import sqrt, pow,ceil,floor,factorial
# number functions
num = 10
print(10 **2)
print(10**0.097)
print('sqrt is', sqrt(num))
print('power is', pow(2,5))
print('ceiling', ceil(8.25))
print('floor', floor(8.999999))
print('normal round', round(8.6353))
print()
print('Factorial of 5 is', factorial(5))

rounded = floor(8.5468798)
# job of a function is to give back returns
print(rounded)

results = rounded**2
print(results)

res = floor(7.85) * pow(2, 0.8) / sqrt(10.34)
print(res)

x = '10'
y= '12.88'
print(int (x) * float (y))

sentence = "The quick brown fox jumped over a lazy dog"

print(sentence.upper())

upper_cased = sentence.upper()

print(upper_cased * 5)
print(sentence + upper_cased)
# join the sentence

print(sentence.capitalize())
print(sentence.swapcase())
print(sentence.casefold())


new_sentence = sentence.replace('fox','rabbit' )
print(new_sentence)
#  chaining functions
new_sentence2 = sentence.lower().replace("lazy" , "super lazy").capitalize().replace("brown" , "grey")
print(new_sentence2)



