class Programmer:
    def __init__(self, _name, _status):
        self.name = _name
        self.status = _status
        self.w_time = 0
        self.salery = 0
        self.smap = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.bonus = 0

    def work(self, _t):
        self.salery += (self.smap[self.status] + self.bonus) * _t
        self.w_time += _t

    def info(self):
        # <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
        return f"{self.name} {self.w_time}ч. {self.salery}тгр. {self.status}"

    def rise(self):
        cur_ind_status = list(self.smap.keys()).index(self.status)
        cur_ind_status += 1
        # print(list(self.smap.keys())[1])
        if cur_ind_status < 3:
            self.status = list(self.smap.keys())[int(cur_ind_status)]
        else:
            self.bonus += 1


if __name__ == '__main__':
    programmer = Programmer('Васильев Иван', 'Junior')
    programmer.work(750)
    print(programmer.info())
    programmer.rise()
    programmer.work(500)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
