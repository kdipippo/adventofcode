# Advent of Code 2018
Welcome to the writeup file for each of these days where I talk about my solutions in plain English and elaborate on my implementation.

### Day 1
It really occurred to me how many people are working on the puzzles when I place 300th for part 1 after spending a couple minutes on it. Wish I lived maybe in the UK at least for the month of December just so I'm not starting on these problems at midnight and working until 2am.

The puzzle was straightforward, as it usually is. Of course the method I went with for part 2 was the naive implementation: running the loop infinitely until a result is found. This was okay for the smaller inputs, but the larger input took 142.00 seconds, with 146473 inputs added to the prevFreqs list.

However, as suggested by others in the AoC community, I tried changing my impelmentation to use a set instead. This time, the same function took 7.17 seconds. Completely blown away and going to try working sets into my more regular programming vocabulary.

### Day 2
Proud of the solution I was able to program for part 2. I created a custom comparator function and sorted a list of pairs created using a Cartesian product library. After that, it was just a matter of taking the very last pair in that sorted list and intersecting the letters. Solution took 3.24 seconds to run.
