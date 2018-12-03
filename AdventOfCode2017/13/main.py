import copy

def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  firewalls = []
  maxWall = int(lines[-1][0].replace(":",""))
  currLine = 0
  for i in range(maxWall+1):
    firewall = []
    firewall.append(i)
    if (int(lines[currLine][0].replace(":","")) == i):
      firewall.append(int(lines[currLine][1]))   # DEPTH
      firewall.append(0)                  #SCANNER LOCATION
      firewall.append(True)               #True if S is descending, False if S is ascending
      currLine += 1
    else:
      firewall.append("...")
    firewalls.append(firewall)
  return firewalls

def moveScanners(firewalls):
  for i in range(len(firewalls)):
    if firewalls[i][1] != "...":
      # if we are at the start, move downward, set to descending
      # if we are at the end, move upward, set to ascending
      # if we are descending, move downward
      # if we are ascending, move upward
      if firewalls[i][2] == 0:
        firewalls[i][2] += 1
        firewalls[i][3] = True
      elif firewalls[i][2] == (firewalls[i][1]-1):
        firewalls[i][2] -= 1
        firewalls[i][3] = False
      elif firewalls[i][3] == True:
        firewalls[i][2] += 1
      elif firewalls[i][3] == False:
        firewalls[i][2] -= 1

def printFirewalls(time, firewalls):
  print "Picosecond " + str(time) + ":"
  for i in range(len(firewalls)):
    print firewalls[i]
  print ""

def checkPacket(packet,firewalls):
  currFirewall = firewalls[packet]
  if currFirewall[1] != "...":
    if currFirewall[2] == 0:
      return currFirewall[0] * currFirewall[1]
  return 0

def packetWasHit(packet,firewalls):
  currFirewall = firewalls[packet]
  if currFirewall[1] != "...":
    if currFirewall[2] == 0:
      return True
  return False

def part1(firewalls):
  severity = 0
  #printFirewalls(0,firewalls)
  for packet in range(0,len(firewalls)):
    severity += checkPacket(packet,firewalls)
    moveScanners(firewalls)
    #printFirewalls(packet,firewalls)
  print "Severity = " + str(severity)

def wasStrollSuccessful(firewalls):
  #printFirewalls(offset,firewalls)
  for packet in range(0,len(firewalls)):
    if packetWasHit(packet,firewalls):
      return False
    moveScanners(firewalls)
  return True

def part2(firewalls):
  offset = 1417000
  for i in range(offset):
    moveScanners(firewalls)
    if i%1000 == 0:
      print str(i) + " and loading..."
  while True:
    #tempFirewalls = copy.deepcopy(firewalls)
    tempFirewalls = [x[:] for x in firewalls]
    if wasStrollSuccessful(tempFirewalls):
      print "we made it!! offset = " + str(offset)
      return
    if offset%1000 == 0:
      print "curr offset = " + str(offset)
    offset += 1
    moveScanners(firewalls)

if __name__ == "__main__":
  inputs = readfileintowords("input.txt")
  #printFirewalls(0,inputs)
  part2(inputs)
