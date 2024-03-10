slova = ["house", "car", "canal", "drought", "anarchy", "knife", "apple"]
stat_word = []
stat_popitki = []
while True:  # цикл для повтора игры
    slova = set(slova)  # перевел список во множество чтобы был рандом
    slova = list(slova)  # перевел множество в список чтобы код работал
    print("Чтобы вывести правила или команды, воспользуйтесь командой - '/help'")
    print(f"Выберите число до {len(slova)} для выбора слова.")
    chislo = input()
    while not chislo.isnumeric():  # цикл для избежения ошибок (проверил что введено число)
        print(f"Выберите число до {len(slova)} для выбора слова.")
        chislo = input()
    chislo = int(chislo)
    if chislo < 1:
        print("Вы выбрали число меньше допустимого, выбралось самое меньшее число")
        chislo = 0
    elif chislo > len(slova):
        print("Вы выбрали число больше допустимого, выбралось самое большее число")
        chislo = len(slova) - 1
    else:
        chislo -= 1
    slovo = slova[chislo].lower()  # выбрал слово из преобразованного ранее списка
    zagad = "." * len(slovo)  # вывел зашифрованное загаданное слово
    print(zagad)
    bukvi_izvesnie = list('qwertyuiopasdfghjklzxcvbnm')
    bukvi_izvesnie.sort()
    bukvi_zagad = set()  # если добавил, сверху удалил
    popitki = 0
    max_popitki = 10
    while True:  # игровой цикл
        bukva = input().lower()
        if bukva == '/kill':  # команда для сдачи
            print(f"Вы сдались, количество попыток: {popitki}")
            break
        elif bukva == "/help" or bukva == "/izves" or bukva == "/zagad":
            if bukva == "/help":  # команда помощи
                print("Ввод осуществляется английскими буквами.")
                print("Команды: '/izves' , '/zagad' ")
                print("'/izves' - команда для показа доступных букв")
                print("'/zagad' - команда для показа уже выбранных букв")
            elif bukva == "/izves":  # команда для показа доступных букв
                print(*bukvi_izvesnie)  # команда для показа уже выбранных букв
            elif bukva == "/zagad":
                print(*bukvi_zagad)
        elif len(bukva) == 1 and bukva in bukvi_izvesnie:
            popitki += 1
            print(f"Оставшиеся попытки: {max_popitki - popitki}")
            bukvi_zagad.add(bukva)
            bukvi_izvesnie.remove(bukva)
            if bukva in slovo:  # замена "." на букву
                temp = ''
                for i in range(len(slovo)):
                    if slovo[i] == bukva:
                        temp += bukva
                    else:
                        temp += zagad[i]
                temp, zagad = zagad, temp
                print(zagad)
            else:
                print("Такой буквы нет")
            if "." not in zagad:
                print(f"Победа, загаданное слово: {slovo} количество попыток: {popitki}")
                break
            if popitki == max_popitki and "." in zagad:  # условие проигрыша (возможное улучшение)
                print("Вы проиграли")
                break
        elif bukva == slovo:
            popitki += 1
            print(f"Оставшиеся попытки: {max_popitki - popitki}")
            print(f"Победа, загаданное слово: {slovo}, количество попыток: {popitki}")
            break

        else:
            print("Проверьте, написали ли Вы букву латинского алфавита.")
            print("Также Вы могли указать букву которую Вы вводили ранее.")
    print("Хотите продолжить игру? \n Введите 'Да' или 'Нет'")
    vibor = input().lower()
    spisok_vibora = ["да", "нет"]
    while vibor not in spisok_vibora:  # цикл для избежения ошибок
        print("Хотите продолжить игру? \n Введите 'Да' или 'Нет'.")
        vibor = input().lower()
    if vibor == "да":
        stat_word.append(slovo)  # подсчет статистики (возможное улучшение)
        stat_popitki.append(popitki)  # подсчет статистики (возможное улучшение)
        slova.remove(slovo)  # удаления слова для повторной игры (возможное улучшение)
        if len(slova) < 1:
            print("Слова кончились, игра окончена.")
            for i in range(len(stat_popitki)):
                print(f"слово: {stat_word[i]}, количество попыток: {stat_popitki[i]}")
    else:
        print("Игра окончена.")
        stat_word.append(slovo)  # подсчет статистики (возможное улучшение)
        stat_popitki.append(popitki)  # подсчет статистики (возможное улучшение)
        slova.remove(slovo)  # удаления слова для повторной игры (возможное улучшение)
        for i in range(len(stat_popitki)):
            print(f"слово: {stat_word[i]}, количество попыток: {stat_popitki[i]}")
        break
