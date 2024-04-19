def palindrom(number):
    return number == number[::-1]


def numbers2(number):
    return number[(len(number) // 2) - 2] == number[(len(number) // 2) + 1] and \
    number[(len(number) // 2) - 1] == number[(len(number) // 2)]


for i in range(100000, 999_999 + 1):
     if palindrom(str(i)[-5:]):
         i1 = i + 1
         if palindrom(str(i1)[-5:]):
             i2 = i1 + 1
             if numbers2(str(i2)):
                 i3 = i2 + 1
                 if len(str(i3)) == 6 and palindrom(str(i3)):
                     print(i)