class Color:
    WARNING = '\033[41m'
    END = '\033[0m'


class DayOfTheWeek:
    def __init__(self, day):
        self.day = day

    def IsAllowed(self):
        if self.day in range(1,8):
            pass
        else:
            print(f"{Color.WARNING}Введено неправильное число!{Color.END}")
            return False
    def IsHoliday(self):
        if self.day in range(1,6):
            print("Да")
        else:
            print("Нет")

def Main():
    print("Программа работает.\nВведите число чтобы узнать является ли день выходным.")
    day = int(input())

    holliday = DayOfTheWeek(day)
    if holliday.IsAllowed():
        pass
    else:
        Main()
    holliday.IsHoliday()

    print("\nДля завершения программы введите Y или y.")
    control = str(input())
    if control == 'Y' or control == 'y':
        pass
    else:
        Main()


if __name__ == "__main__":
    Main()