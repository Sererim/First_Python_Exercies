from COLOR import Color


class DayOfTheWeek:
    def __init__(self, day):
        self.day = day

    def isallowed(self):
        if self.day in range(1, 8):
            pass
        else:
            print(f"{Color.WARNING}Введено неправильное число!{Color.END}")
            return False

    def isholiday(self):
        if self.day in range(1, 6):
            print("Да")
        else:
            print("Нет")


def main():
    print("Программа работает.\nВведите число чтобы узнать является ли день выходным.")
    day = int(input())

    holliday = DayOfTheWeek(day)
    if holliday.isallowed():
        pass
    else:
        main()
    holliday.isholiday()

    print("\nДля завершения программы введите Y или y.")
    control = str(input())
    if control == 'Y' or control == 'y':
        pass
    else:
        main()


if __name__ == "__main__":
    main()
