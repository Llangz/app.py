# def say_hi () :
#     """It prints Hi Guest"""
#     print("Hi Guest")
#
# def greet (name) :
#     """It greets someone by their name"""
#     print("Hi",name)
# # call a function==using a function
#
# def converter(amount_kes, rounded="No", accuracy = 0):
#     usd = amount_kes/102
#     if rounded == "Yes":
#         usd = round (usd, accuracy)
#     print(usd, "USD")

# def converter2(amount, to, accuracy=0):
#     if to == "USD":
#         result = amount/102
#     elif to=="GBP":
#         result = amount/143
#     elif to=="UGX":
#         result = amount*36
#     elif to=="ZAR":
#         result = amount/7.8
#     else:
#         print("we don't support that currency")
#     try:
#         print(round(result, accuracy))
#     except:
#         pass

#     distance converter that converts a value in meters to feet, cm, km, yard, inches
# 100 meters equals to 0.1kms

def converter3(number, to, accuracy = 4):
    amount = number
    meter = number





    if to=="feet":
        ans = amount/3.28084
    elif to=="cm":
        ans = amount*100
    elif to=="km":
        ans = amount/0.001
    elif to=="yard":
        ans=amount*1.09361
    elif to=="inches":
        ans = amount*39.3701
    else:
        print("we don't support that SI unit")

        print(amount)



# tests if a word is a palindrome







# say_hi()
# say_hi()
# greet("Tom")
# greet("Jane")
# greet()

# converter(10000)
# converter(10000, rounded="Yes")
# converter(10000, rounded="Yes", accuracy=2)