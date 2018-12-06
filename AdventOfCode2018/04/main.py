import time
import operator

class Guard:
    def __init__(self, id, secDiff):
        self.id = id
        self.totalSleep = secDiff
        self.sleepTimes = {}
    def addSleep(self, sleep):
        self.totalSleep += sleep
    def addSleepTimes(self, start, end):
        for i in range(start,end):
            if i in self.sleepTimes:
                self.sleepTimes[i] += 1
            else:
                self.sleepTimes[i] = 1
    def printGuard(self):
        print("Max Guard = " + self.id + "\t\tTotal Sleep = " + str(self.totalSleep) + "\t\tMax Min = " + str(max(self.sleepTimes.iteritems(), key=operator.itemgetter(1))))

def readfileintowords(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def part1(guardshifts):
    guards = {}
    start = 0
    end = 0
    guardshifts.sort()
    for shift in guardshifts:
        print(shift)
    for shift in guardshifts:
        shift = shift.replace("[","").replace("]","").split(" ")
        # ['1518-11-01', '00:00', 'Guard', '10', 'begins', 'shift']
        # ['1518-11-01', '00:05', 'falls', 'asleep']
        # ['1518-11-01', '00:25', 'wakes', 'up']
        if shift[2] == "Guard":
            currGuard = shift[3]
        elif shift[2] == "falls":
            start = int(shift[1].split(":")[1])
        elif shift[2] == "wakes":
            end = int(shift[1].split(":")[1])
            if currGuard in guards:
                guards[currGuard].addSleep(end-start)
            else:
                guards[currGuard] = Guard(currGuard, end-start)
            guards[currGuard].addSleepTimes(start, end)
    for guard in (sorted(guards.values(), key=operator.attrgetter('totalSleep'))):
        guard.printGuard()

if __name__ == "__main__":
    print("#############################")
    inputs = readfileintowords("input.txt")
    start = time.time()
    part1(inputs)
    end = time.time()
    print(end - start)
