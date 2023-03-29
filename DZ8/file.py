f  = open('tryfile.txt', 'r')

lines = f.readlines()
f.close
print(lines)
del_name = input("Input RM name: ")
print(del_name)
print(type(del_name))
for line in lines:
    # # res = f.readlines()
    # print(line)
    # print(del_name)
    if del_name in line:
        print("ffff")
        print(lines)
        index = lines.index(del_name + "\n")
        print(index)
        del lines[index]
        # ПОСЛЕ УДАЛЕНИЯ СТРОКИ КАК ВАРИАНТ
        # МОЖНО ОЧИСТИТЬ ФАЙЛ И ДОБАВИТЬ В 
        # НЕГО ОТРЕДАКТИРОВАННЫЙ СПИСОК

print(lines)
