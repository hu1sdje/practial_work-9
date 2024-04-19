for word in range(10, 100):
    cab = str(word ** 2)
    if len(cab) == 3 and cab[1] == str(word)[0] and cab[2] == str(word)[1]:
        print(cab)
