with open("input.txt", "r") as f:
    input_list=f.readlines()


def result(input_list):
    for i,val_i in enumerate(input_list):
        for val_j in input_list[i+1:]:
            if int(val_i)+int(val_j)==2020:
                return int(val_i)*int(val_j)


print(result(input_list))




