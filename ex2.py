def get_hedgehog(count=10):
    all_str = ""
    for i in range(count):
        str1 = ""
        for j in range(count):
            str1 += "ЁЖИК \t"
        all_str = all_str + str1 + " \n"
    print(all_str)

get_hedgehog(30)