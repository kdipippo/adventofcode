import hashlib

def calcHash(secretKey):
    answers = []
    answer = 0
    while True:
        result = hashlib.md5(secretKey + str(answer)).hexdigest()
        if result[:5] == '00000':
            answers.append(result)
            print "Index",len(answers),"found"
        answer += 1
        if len(answers) == 8:
            #return answers
            return "".join(answers)

if __name__ == "__main__":
    test1 = 'abc'
    doorID = 'wtnhxymk'
    
    print calcHash(doorID)
    
