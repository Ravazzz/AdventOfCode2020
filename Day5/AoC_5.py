
def find_seat(l):
    pass


def result(input_lines):
    max_id=0
    l=set()
    for line in input_lines:
        up=127
        down=0
        row=0
        col=0
        for i in range(7):
            if i == 6:
                if line[i] == 'B':
                    row=up
                else:  # if line[i] == 'F':
                    row=down
                up=7
                down=0
                continue
            half=int((up-down)/2)
            if line[i] =='B':
                down+=half
            else: #if line[i] == 'F':
                up-=half

        for i in range(7, 10):
            if i == 9:
                if line[i] == 'R':
                    col = up
                else:  # if line[i] == 'L':
                    col = down
                break
            half = int((up - down) / 2)
            if line[i] == 'R':
                down += half
            else:  # if line[i] == 'L':
                up -= half

        res=row*8+col
        #l.add(res)
        if res > max_id: max_id=res
    #find_seat(l)
    return max_id

if __name__ == "__main__":
    with open("input.txt","r") as f:
        input_lines=f.readlines()
    print(f"The highest Seat ID found is: {result(input_lines)}")