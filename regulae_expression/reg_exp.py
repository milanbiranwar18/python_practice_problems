import re


def reg_prac():
    my_str = "hello 20125-8996 hdbdj idd ncidn"

    patt = re.compile(r'\d{5}-\d{4}')

    matches = patt.findall(my_str)

    for mat in matches:
        print(mat)


def reg_prac1():
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)

    print(x)

    if x:
        print("YES! We have a match!")
    else:
        print("No match")

    x = re.findall("ai", txt)
    print(x)


if __name__ == '__main__':
    reg_prac()
    reg_prac1()
