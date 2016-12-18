import hashlib

# takes in a file name and returns the contents of file
def formatInput(filename):
    dimensions = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def calcAns(secretKey):
    answer = 0
    while True:
        result = hashlib.md5(secretKey + str(answer)).hexdigest()
        if result[:6] == '000000':
            return answer
        else:
            answer += 1

if __name__ == "__main__":
    test1 = 'abcdef'
    test2 = 'pqrstuv'

    part1 = 'iwrupvqb'
    part1ans = 'iwrupvqb346386'
    #print calcAns(test1)
    #print calcAns(test2)
    print calcAns(part1)
    
