def cal_love(name1,name2):
    combine = name1 + name2
    lower = combine.lower()

    t = lower.count("t")
    r = lower.count("r")
    u = lower.count("u")
    e = lower.count("e")
    first = t + r + u + e

    l = lower.count("l")
    o = lower.count("o")
    v = lower.count("v")
    e = lower.count("e")
    second = l + o + v + e

    score = int(str(first) + str(second))
    print("Your love score is : " , score)

first_name = input("Enter the first name : ")
second_name = input("Enter the second name: ")

cal_love(first_name,second_name)