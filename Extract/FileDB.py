import datetime


def new_Entry(alnum):
    now = datetime.datetime.now()
    s = str(now.day) + "/" + str(now.hour) + "/" + str(now.minute)
    l = list()
    l.append(alnum)
    l.append(s)
    l.append("NONE")
    write_File_Entry(l)


def check_Entry(alnum):
    l = read_File()
    count = 0
    flag = 0
    time_list = list()
    for i in range(0, len(l), 3):
        if l[i] == alnum:
            count = count + 1
            s = "In-Time : " + str(l[i + 1]) + "  and  Out-Time : " + str(l[i + 2])
            time_list.append(s)
            if l[i + 2] == "NONE":
                flag = 1
    return time_list, count, flag


def read_File():
    f = open("apogee.txt", "r")
    l = list()
    lines = list()
    lines = f.readlines()
    for line in lines:
        l1 = line.split()
        l.append(l1[0])
        l.append(l1[1])
        l.append(l1[2])
    f.close()
    return l


def write_File_Entry(l):
    f = open("apogee.txt", "a")
    s = str(l[0]) + "          " + str(l[1]) + "          " + str(l[2]) + "\n"
    f.write(s)
    f.close()


def write_File(l):
    f = open("apogee.txt", "w")
    for i in range(0, len(l), 3):
        s = str(l[i]) + "          " + str(l[i + 1]) + "          " + str(l[i + 2]) + "\n"
        f.write(s)
    f.close()


def exit_Entry(alnum):
    l = read_File()
    for i in range(0, len(l), 3):
        if l[i] == alnum and l[i + 2] == "NONE":
            now = datetime.datetime.now()
            s = str(now.day) + "/" + str(now.hour) + "/" + str(now.minute)
            l[i + 2] = s
    write_File(l)

    # new_Entry("AJSF&^%&^")
    # li = list()
    # li,c,f = check_Entry("AJSF&^%&^")
    # print li,c,f
    # exit_Entry("AJSF&^%&^")
