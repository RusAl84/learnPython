class RedButton:
    def __init__(self):
        self.count_n = 0

    def click(self):
        self.count_n += 1
        print("Тревога!")

    def count(self):
        return str(self.count_n)


if __name__ == '__main__':
    first_button = RedButton()
    second_button = RedButton()
    for time in range(5):
        if time % 2 == 0:
            second_button.click()
        else:
            first_button.click()
    print(first_button.count())
