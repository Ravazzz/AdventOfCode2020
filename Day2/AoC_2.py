with open("input.txt", "r") as f:
    input_list=f.readlines()


def min_max_char_txt(item):
    txt=item.split()
    n1=int(txt[0].split("-")[0])
    n2=int(txt[0].split("-")[1])
    c=txt[1][0]
    return n1,n2, c, txt[2]

def find_passwords(input_list):
    corrects_counter = 0
    for i in input_list:
        occ=0
        n1,n2, c, str=min_max_char_txt(i)
        occ=str.count(c)
        if occ >= n1 and occ <= n2:
            corrects_counter+=1

    return corrects_counter





print(f"In the provided input file there are {find_passwords(input_list)} correct passwords!")
print("\n\nEnd")