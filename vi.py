import random
# Запуска только из каталога с исполняем файлом
def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())
def outGallows(number, gallows1):
    gallows = open(gallows1 + str(number)+'.txt', 'r', encoding="utf-8" )
    gallowss = []
    for gallow in gallows.readlines():
        if gallows1 == "gallows":
            print(gallow)
        gallow = gallow.replace("\n","")
        gallowss.append(gallow)
    return gallowss
wordList = outGallows("", "words")
while True:
    print ("Добро Пожаловать в игру виселица")
    word = random.choice(wordList).lower()
    numberGallows, numberIndex, spaceChars, spaceChars0 = -1, [], len(word) * "_" , list(range(len(word)))
    print("Слово среди этих спейсов", spaceChars)
    print("Так же слово стотит из: ", len(spaceChars))
    while True:
        if len(numberIndex) != 0:
            indexWord = -1
            noSpaceChars = "".join(str(numberIndex))
            for i in word:
                indexWord += 1
                if str(indexWord) in noSpaceChars:
                    spaceCharsList = list(spaceChars)
                    spaceCharsList[int(indexWord)] = word[int(indexWord)]
                    spaceChars = ''.join(str(el) for el in spaceCharsList)
        if "_" not in spaceChars:
            print("ПОБЕДА!!!")
            break
        print("Слово", spaceChars)
        print("можно использовать только русские буквы,","\n","если будет несколько символов будет учитыватся только первый")
        char = input("Введите букву: ")
        if char != "":
            if match(char[0].lower()):
                if char[0].lower() in word:
                    n, i, numberIndex  = [],[],[]
                    n = [i.find(char[0].lower()) for i in word]
                    for m, spaceChar0 in zip(n, spaceChars0):
                        if m == 0:
                            numberIndex.append(spaceChar0)
                    print(numberIndex)
                    continue
                else:
                    numberGallows += 1
                    outGallows(numberGallows, "gallows")
