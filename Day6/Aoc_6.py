
def result(input_lines):
    sum=0
    l=set()
    for line in input_lines:
        if line == "\n":
            sum+=len(l)
            l=set()
        line=set(line.strip())
        l=l.union(line)
    return sum


if __name__ == "__main__":
    with open("input.txt","r") as f:
        input_lines=f.readlines()
    print(f"The sum of all answers is: {result(input_lines)}")