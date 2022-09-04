# numlang-9ee9
A very concise language for processing numbers.

## Introduction

Numlang is a [golfing](https://en.wikipedia.org/wiki/Code_golf) language designed for handling integers, and lists of integers.

`9ee9` is the alternative name for Numlang. It is taken by converting `num` from Base 64 to Hexadecimal.

## Setup and running the code

### Installation

Install `numlang-9ee9` from PyPI:

```
$ pip install numlang-9ee9
```

### Running the code

To run your code, use the `numlang` command, followed by your code in quotes:

```
$ numlang "#Fx"
```

## Tutorial

### Basics

Numlang has 5 variables: `x`, `y`, `i`, `l`, and `n`. You cannot define your own.

`x` and `y` are the input variables (discussed in the User Inputs section)

`i` is the iterating variable (discussed in the Loops section)

`l` is a list which starts as `[]`. You can use methods on it (discussed in the Methods section)

`n` is an integer which starts as `0`. You can perform operations on it (discussed in the Operations section)

The output of the last operation performed is always outputted at the end of the program in Numlang.

### User Inputs

#### Integer

To get a single integer as an input, use `#`.
The input will be converted to an integer, and implicitly stored in the `x` variable

An example program is `#+1`. It will take the input from the user, add one, and output it.

#### List

To get a list of integers as an input, use `$`.
The input must be integers separated by spaces, like `1 2 3 4`.

All elements will be converted to integers. The list will be implicitly stored in the `y` variable.

An example program is `$;{i+1}`. It will go through the list, add one, and output it.

### Loops

To loop, add the iterable, then any code you want to loop in braces.
Each time it loops, the next element of the iterable is implicitly assigned to the `i` variable.

An example program is `#Rx;{i*2}`. It will go through each number from 0 to the input minus one, and multiply by 2.

Note: the closing bracket is unneccesarry if it is at the end. The interpreter will automatically put it in.

### Methods

#### Range

`R` is the Numlang equivalent of `range` in Python. You can use `Rn;` to get the numbers from 0 to `n`.

#### Append

To append to a list, use `A`. Use `yAi;` to append `i` to `y`.

#### Without

Use `W` to exclude all instances of an element from a list. Use `lWx;` to remove all `x`s from `l`

#### Prime

Use `P` to test if a number is prime. Use it as a function: `P(i)`. No semicolon needed.

### Operations

You can use the following operations in Numlang:

* `+` (addition) - e.g. `i+x;`
* `-` (subtraction) - e.g. `i-x;`
* `*` (multiplication) - e.g. `i*x;`
* `/` (integer division / floor division) - e.g. `i/x;`
* `^` (exponentiation / power) - e.g. `i^x;`
* `%` (modulus / remainder) - e.g. `i%x;`

### Conditions

In Numlang conditions take the form `?cond;if_true;`.

An example program is `#R100;{?i%x;i;}`.
It will go through the numbers from 0 to 99, and print those which are multiples of the user input.
