# shiny-barnacle
My attempt at [Advent of code 2023](https://adventofcode.com/2023).

## Journal

### 2023.12.14
Starting 2 weeks late...
#### Day 1
* First part completed on first go.
* Second part is looking trickier...
* Second part done on first go. Now it's bedtime.

### 2023.12.15
#### Day 2
* First part on first try.
* I feel like I may be over-coding this. It's not like I need to pass a linter of anything. But whatevs...
* Part 2 done on first go. 

### 2023.12.16
#### Day 3
* making sloppy use of string objects...
* got part 1 on second try. Missed an increment.
* Part 2 I got on first go.
* Day 3 complete.

#### Day 4
* Part 1 looks almost too easy. Wonder what the catch is...
* Part 1 done on first go. Part 2 has got to be a doozy right?
* ohhhh boy lol...
* so this is where the recursion begins?
* Ok, so maybe not recursion yet, but I feel recursion coming soon.
* Part 2 done on first go! Totally did not expect that.

#### Day 5
* Part 1 is taking some thought.
* starting more bottom up this time.
* uh-oh, this one is taking awhile to run... Gotta actually start thinking about stuff.
* My first attempt will take an unreal amount of time to run and a ton of RAM. Gotta get smart here...
* First go, right answer. Hell yeah.
* PART 2
* Nearly crashing my computer trying to solve this one.
* switched from max RAM usage to max CPU usage lol.
* Day 5 part 2 looks like one to revisit later.

### 2023.12.17
#### Day 6
* I started writing a function for finding distance from hold time and realized that it forms a quadratic equation and I just need to find the zeros of it.
* hardest part about round 1 was figuring out the best way to "round" the result. Ended up just doing dumb if statements
* part 2 looks pretty easy cuz I did it the mathematic way to begin with.
* Ez ez, done in less than 30 minutes.

#### Day 7
* This one obviously involves sorting.
* Python certainly has sorting algorithms, but it seemed too hard/too much effort to use them, so I just wrote my own quick-sort algorithm.
* I used a few copy.deepcopy() calls, not totally sure if they're needed, but seemed like the thing to do.
* First attempt get's wrong answer (it works on the sample data!!).
* Ok, so the sort doesn't work on the full input data (sad face).
* I think I would like to implement merge sort better than quicksort.
* Second try, got it. Merge sort worked, but was initially confused about my array copying.
* On part 2, missed the first try (it works on the sample!).
* I think I might know what I'm doing wrong....
* Second try, got it! What I was doing was not considering the MAX possible Joker card option.

### 2023.12.19
#### Day 8
* after 20 minutes of coding, the 2 samples work, but I'm nervous to try my answer in the text input lol.
* the program is really chewing on the input lol.
* I just thought of another way to approach this. Once you have a path tried out, if you ever encounter that path again, you know how many steps it takes to get through it. 
* wait, I think I'm actually supposed to start at AAA rather than the first line...
  * Duh that was stupid lol. Program works.
* Ok, part 2 works on sample but is actually taking awhile on the actual input. May need to actually start thinking here...
* I can't believe my solution worked! I actually did a "hand calc" at the end there, but could have totally finished the whole puzzle with code.
