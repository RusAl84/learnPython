def print_sey_hi(name):
    print(f"Привет {name}!")
    # print("Привет " + name)


if __name__ == '__main__':
    default_name = "Вася"
    names = []
    for num in range(1, 5, 1):    
        names.append(f"{default_name} {num:03}")
    names.append("Дашенька")
    for name in names:
        print_sey_hi(name)
