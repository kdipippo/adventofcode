def readfileintowords(filename):
  with open(filename) as textFile:
    lines = [line.split() for line in textFile]
  return lines[0][0].split(",")

def dance(programs, moves):
  for i in range(len(moves)):
    if moves[i][0] == "s":
      # SPIN
      end = programs[moves[i][1]:]
      programs = end + programs[:moves[i][1]]

    elif moves[i][0] == "x":
      # EXCHANGE
      programs[moves[i][1]], programs[moves[i][2]] = programs[moves[i][2]], programs[moves[i][1]]

    elif moves[i][0] == "p":
      # PARTNER
      firstParnerLoc = programs.index(moves[i][1])
      secondParnerLoc = programs.index(moves[i][2])
      programs[firstParnerLoc],programs[secondParnerLoc] = programs[secondParnerLoc],programs[firstParnerLoc]
  return programs

def prepMoves(moves):
  for i in range(len(moves)):
    if moves[i][0] == "s":
      # SPIN
      spinSize = -1*int(moves[i][1:])
      moves[i] = ["s",spinSize]

    elif moves[i][0] == "x":
      # EXCHANGE
      exchangeInstr = moves[i][1:].split("/")
      exchangeInstr[0] = int(exchangeInstr[0])
      exchangeInstr[1] = int(exchangeInstr[1])
      moves[i] = ["x",int(exchangeInstr[0]),int(exchangeInstr[1])]

    elif moves[i][0] == "p":
      # PARTNER
      partnerInstr = moves[i][1:].split("/")
      moves[i] = ["p",partnerInstr[0],partnerInstr[1]]
  return moves

def getDanceCycle(programs,moves):
  moves = prepMoves(moves)
  duplicateCounter = 0
  dancePositions = []
  dancePositions.append("".join(programs))
  while True:
    programs = dance(programs,moves)
    if "".join(programs) not in dancePositions:
      dancePositions.append("".join(programs))
    else:
      return dancePositions

def part2(programs,moves):
  dancePositions = getDanceCycle(programs,moves)
  finalPosition = 1000000000%len(dancePositions)
  print dancePositions[finalPosition]

if __name__ == "__main__":
  moves = readfileintowords("input.txt")
  test = ["a","b","c","d","e"]
  testmoves = ['s1','x3/4','pe/b']
  programs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
  #testmoves = prepMoves(testmoves)
  #test = dance(test,testmoves)

  part2(programs,moves)
