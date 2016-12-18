import hashlib

def validHash(result, answers):
    if result[:5] != '00000':
        return False
    if not result[5].isdigit():
        return False
    if int(result[5]) >= 8:
        return False
    if answers[int(result[5])] != '_':
        return False
    return True

def calcHash(secretKey):
    answers = ['_']*8
    answer = 0
    while True:
        result = hashlib.md5(secretKey + str(answer)).hexdigest()
        if validHash(result,answers):
            # [5] = position
            # [6] = character to put in position
            answers[int(result[5])] = result[6]
            print "".join(answers)
        answer += 1
        if answers.count("_") == 0:
            return "".join(answers)

def calcHashTest(indices):
    answers = ['_']*8
    for i in range(len(indices)):
        result = indices[i]
        if validHash(result):
            # [5] = position
            # [6] = character to put in position
            answers[int(result[5])] = result[6]
            print "".join(answers)
        if answers.count("_") == 0:
            return "".join(answers)

if __name__ == "__main__":
    test1 = 'abc'
    testIndices = ['00000155f8105dff7f56ee10fa9b9abd', '000008f82c5b3924a1ecbebf60344e00', '00000f9a2c309875e05c5a5d09f1b8c4', '000004e597bd77c5cd2133e9d885fe7e', '0000073848c9ff7a27ca2e942ac10a4c', '00000a9c311683dbbf122e9611a1c2d4', '000003c75169d14fdb31ec1593915cff', '0000000ea49fd3fc1b2f10e02d98ee96']
    doorID = 'wtnhxymk'
    
    print calcHash(doorID)
    
    
