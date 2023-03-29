def read_phonebook():
    # with open('file_name.txt', 'r', encoding='utf-8') as file:
    #     file.readline()
    f  = open('file_name.txt', 'r')
    res = f.readlines()
    f.close
    return res

def add_contact():
    first_name = input("Введите имя")
    last_name = input("Введите фамилию")
    phone = input("Введите телефон")
    file = open("file_name.txt", 'a')
    file.write(first_name + " ")
    file.write(last_name + " ")
    file.write(phone + "\n")
    file.close() 
    pass

def find():
    # f  = open('file_name.txt', 'r')
    # f.close()
    # return None
    print("Введите данные для поиска: ")
    f = input("")
    print()

    lines = read_phonebook()
    cnt = False
    for line in lines:
        if f in line:
            print("---------------------------------" + "\n")
            print(line)
            print("---------------------------------" + "\n")
            cnt = True
    
    if cnt == False:
        print("Контакт не найден!")
    
    return line



def remove_contact():
    print("Input RM name: ")
    del_name = find()
    
    print(del_name)
    rm = read_phonebook()
    print(rm)

    index = rm.index(del_name)
    print("======================")
    print(index)
    for line in rm:
        if del_name in line:
            del rm[index]
            print(rm)
   
            # ПЕРВОНОЧАЛЬНО ПИСАЛ ДАННУЮ ФУНКЦИЮ В ДРУГОМ ФАЙЛЕ
            # ТАМ ОНА ВПРИНЦИПЕ РАБОТАЛА ХОТЯ Я ТАК И НЕ ПОНЯЛ КАК 
            # РЕАЛИЗОВАТЬ ИМЕННО УДАЛЕНИЕ ОДНОЙ СТРОКИ....
            # А ТУТ Я ВООБЩЕ ПОДВИС...

    # print(lines)

