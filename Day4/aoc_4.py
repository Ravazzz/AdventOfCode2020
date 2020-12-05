
class Passport():
    def __init__(self):
        self.byr=""
        self.iyr=""
        self.eyr=""
        self.hgt=""
        self.hcl=""
        self.pid=""
        self.cid=""

def checkValidity(fields):
    #if p.byr == "" or p.iyr=="" or p.eyr=="" or p.hgt=="" or p.hcl=="" or p.pid=="": #or p.cid==""
    s_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return s_fields.issubset(set(fields.keys()))


def result(input_file):
    #p=Passport()
    count_valids=0
    fields={}
    for line in input_file:
        if line == "\n":
            if checkValidity(fields):
                count_valids+=1
            fields = {}
            #p=Passport()

        tup=line.split()
        for s in tup:
            key, values=s.split(":")
            fields[key]=values

    if checkValidity(fields):
        count_valids += 1

    return count_valids


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_file=f.readlines()

    print(f"There are {result(input_file)} valid passports")