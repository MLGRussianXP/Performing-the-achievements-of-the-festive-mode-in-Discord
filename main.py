from time import sleep
import pyautogui


key = 'a'
enter = 'enter'


def get_points(amount, chill):
    pyautogui.press(key, amount)
    pyautogui.press(enter)
    sleep(chill)


def get_all_advancements_related_to_points():
    points = ((64, 1), (88, 2), (99, 3), (113, 4), (430, 5), (555, 6), (898, 7), (1337, 8))
    for p in points:
        get_points(*p)

    # 2048 points
    # get 4x
    for _ in range(3):
        pyautogui.press(key, 5)
        pyautogui.press(enter)
    # 2048
    pyautogui.press(key, 512)
    pyautogui.press(enter)


def get_all_advancements_related_to_multipliers():
    for _ in range(7):
        pyautogui.press(key, 5)
        pyautogui.press(enter)


def get_all_advancements_related_to_chat():
    get_all_advancements_related_to_points()
    sleep(7)
    get_all_advancements_related_to_multipliers()


def main():
    print(
        """
        Напишите 1, чтобы выполнить все достижения связанные с множителями в чате\n
        Напишите 2, чтобы выполнить все достижения связанные с очками в чате\n
        Напишите 3, чтобы выполнить все достижения связанные с чатом\n
        Абсолютно все достижения не будут выполнены! Другие нужно будет выполнять вручную.
        """
    )
    instruction = input()
    if instruction in ('1', '2', '3'):
        print(
            """
            ВНИМАНИЕ!!!
            Разработчик за, если таковой будет, "причинённый ущерб"
            вашему компьютеру, ответственности не несёт.
            
            Запустите приложение Discord и зайдите в любой чат, желательно с ботом.\n
            Нажмите Enter (в этой командной строке) и щёлкните по полю ввода в Discord'e.\n
            Через 5 секунд программа начнёт работать. При исполнении не трогайте мышку и клавиатуру,
            чтобы не перейти в другие окна или приложения.
            """
        )
        input()
        for _ in range(5, -1, -1):
            print(_)
            sleep(1)

        if instruction == '1':
            get_all_advancements_related_to_multipliers()
        elif instruction == '2':
            get_all_advancements_related_to_points()
        elif instruction == '3':
            get_all_advancements_related_to_chat()
    else:
        print('Введите корректную команду!')
    input('Нажмите Enter, чтобы выйти')


if __name__ == '__main__':
    main()
