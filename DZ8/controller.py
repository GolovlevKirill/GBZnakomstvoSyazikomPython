import view
import model

def run():
    view.greetings()
    while True:
        print()
        view.menu()
        answer = input('Ответ: ')
        if answer == '1':
            date = model.read_phonebook()
            view.show_phonebook(date)
        elif answer == '2':
            model.add_contact()
        elif answer == '3':
            find_result = model.find()
            view.show_find_result(find_result)
        elif answer == '4':
            model.remove_contact()
        elif answer == '5':
            break