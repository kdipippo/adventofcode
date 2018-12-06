# Advent of Code 2018
Welcome to the writeup file for each of these days where I talk about my solutions in plain English and elaborate on my implementation.

### Day 1
> Completed 12/1/2018

It really occurred to me how many people are working on the puzzles when I place 300th for part 1 after spending a couple minutes on it. Wish I lived maybe in the UK at least for the month of December just so I'm not starting on these problems at midnight and working until 2am.

The puzzle was straightforward, as it usually is. Of course the method I went with for part 2 was the naive implementation: running the loop infinitely until a result is found. This was okay for the smaller inputs, but the larger input took 142.00 seconds, with 146473 inputs added to the prevFreqs list.

However, as suggested by others in the AoC community, I tried changing my impelmentation to use a set instead. This time, the same function took 7.17 seconds. Completely blown away and going to try working sets into my more regular programming vocabulary.

### Day 2
> Completed 12/2/2018

Proud of the solution I was able to program for part 2. I created a custom comparator function and sorted a list of pairs created using a Cartesian product library. After that, it was just a matter of taking the very last pair in that sorted list and intersecting the letters. Solution took 3.24 seconds to run.

### Day 3
> Completed 12/3/2018

Part 1 took 0.115 seconds to execute. The hardest part was just figuring out how to structure the nested for loops to get the expected visualization outcome.

Part 2 took 0.117 seconds to execute. My claim to fame is that I stored claims if they were not overlapping anyone in the process of going through the first round. This reduced the number of claims I was going through the second time by.

### Day 4
> Completed 12/5/2018

Missed a day, so I started and finished this problem on the 5th. This was a very confusing problem in terms of what was being asked. I first understood it as storing the longest streak that each guard had been sleeping (i.e. in the example problem, Guard #10 sleeps for 25 minutes during the first shift, which is similar to 24 minutes being the most frequently asleep minute). After continuing to modify the solution as the problem became more clear, I quickly turned to Classes to keep track of the different Guard attributes. Once part 1 was solved, part 2 took less than a minute by modifying the prior solution. Both parts took roughly 0.0088ms. I obtained the solution by printing out all the relevant guard attributes and then inferring what the correct result was myself without the use of programming (I instead just pulled out a calculator to do this last part).

### Day 5
> Completed 12/5/2018

Very interesting problem. My initial solution with react() was to iterate through the word and merely skip characters when a reaction happened. This ended up being a significant number of loops when the large input happened, resulting in 4.96ms for part 1's runtime with react(). However, once part 2 was revealed, the idea to simply replace the reaction polymers with blank strings sounded more attainable. Initially, I was going to check if a substring existed in the list by using an extended regex. But I wasn't able to figure one out that compiled with any online regex testers. Luckily, Python came in clutch with the any() function, allowing me to do the check very quickly to determine if all reactions were performed. My only performance improvement from this would be to see if any() could return which pair was noticed and just replace that, instead of iterating through the pairs list every time. With replaceReact(), part 1 took 0.44ms, nearly a tenth of the original time. Part 2 with replaceReact() took 11.12ms.
