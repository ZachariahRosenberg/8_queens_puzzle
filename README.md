# N Queens Puzzle

From Morning Brew's puzzle section:

<img width="458" alt="mb_queens_puzzle" src="https://user-images.githubusercontent.com/6923376/150577882-688bb0cd-2066-40bc-b0bf-e31954525549.png">

The puzzle can be generalized to find solutions to any `n x n` board.

More details can be found in [Eight Queens Puzzle Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle).

This solution uses the permutation method.

## How to use
1. `git clone https://github.com/ZachariahRosenberg/8_queens_puzzle.git`
2. `python queens_puzzle.py -d 8 -a False`


## Optional arguments
|flag|description|
|:-|:-|
|`-d`,`--dim`|Number of dimensions. For example, `-d 8` will use an 8x8 board.|
|`-a`,`--all`|Whether to return the first solution found or return all found solutions <br /> NOTE: searching for all solutions can take a long time, especially with dim sizes greater than 11|
