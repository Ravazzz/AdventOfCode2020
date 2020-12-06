import numpy as np



def input_coordinates():
    n2=int(input("Insert right jumps: "))
    n1=int(input("Insert down jumps: "))
    return n1,n2


def result(trees):
    count=0
    n1,n2=input_coordinates()
    pos=(0,0)
    while True:
        pos=(pos[0]+n1,(pos[1]+n2)%trees.shape[1])
        if pos[0] >= trees.shape[0]:
            break
        if trees[pos]: count+=1
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_file = f.readlines()
    input_file = [line.strip() for line in input_file]
    input_file = [[1 if c == '#' else 0 for c in line] for line in input_file]
    trees = np.array(input_file)
    print(f"Number of trees encountered : {result(trees)}")


