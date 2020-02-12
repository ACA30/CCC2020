# CCC2020
A compilation of my code from the 2020 CCC Junior Contest.

## [Problem J1 - Dog Treats](https://github.com/ACA30/CCC2020/blob/master/j1-dogtreats.py)
**Problem Description**\
Barley the dog loves treats. At the end of the day he is either happy or sad depending on the number and size of treats he receives throughout the day. The treats come in three sizes: small, medium, and large. His happiness score can be measured using the following formula:

> 1 × *S* + 2 × *M* + 3 × *L*

where *S* is the number of small treats, *M* is the number of medium treats and *L* is the number of large treats.\
If Barley’s happiness score is 10 or greater then he is happy. Otherwise, he is sad. Determine whether Barley is happy or sad at the end of the day.

**Input Specification**\
There are three lines of input. Each line contains a non-negative integer less than 10. The first line contains the number of small treats, *S*, the second line contains the number of medium treats, *M*, and the third line contains the number of large treats, *L*, that Barley receives in a day.

**Output Specification**\
If Barley’s happiness score is 10 or greater, output `happy`. Otherwise, output `sad`.

## [Problem J2 - Epidemology](https://github.com/ACA30/CCC2020/blob/master/j2-epidemology.py)
**Problem Description**\
People who study epidemiology use models to analyze the spread of disease. In this problem, we use a simple model.\
When a person has a disease, they infect exactly *R* other people but only on the very next day. No person is infected more than once. We want to determine when a total of more than *P* people have had the disease.

**Input Specification**\
There are three lines of input. Each line contains one positive integer. The first line contains the value of *P*. The second line contains *N*, the number of people who have the disease on Day 0. The third line contains the value of R. Assume that *P* ≤ 10^7 and *N* ≤ *P* and *R* ≤ 10.

**Output Specification**\
Output the number of the first day on which the total number of people who have had the disease is greater than *P*.

## [Problem J3 - Art](https://github.com/ACA30/CCC2020/blob/master/j3-art.py)
**Problem Description**\
Mahima has been experimenting with a new style of art. She stands in front of a canvas and, using her brush, flicks drops of paint onto the canvas. When she thinks she has created a masterpiece, she uses her 3D printer to print a frame to surround the canvas.\
Your job is to help Mahima by determining the coordinates of the smallest possible rectangular frame such that each drop of paint lies inside the frame. Points on the frame are not considered inside the frame.

**Input Specification**\
The first line of input contains the number of drops of paint, *N*, where 2 ≤ *N* ≤ 100 and *N* is an integer. Each of the next *N* lines contain exactly two positive integers *X* and *Y* separated by one comma (no spaces). Each of these pairs of integers represents the coordinates of a drop of paint on the canvas. Assume that *X* < 100 and *Y* < 100, and that there will be at least two distinct points. The coordinates (0, 0) represent the bottom-left corner of the canvas.\
For 12 of the 15 available marks, *X* and *Y* will both be two-digit integers.

**Output Specification**\
Output two lines. Each line must contain exactly two non-negative integers separated by a single comma (no spaces). The first line represents the coordinates of the bottom-left corner of the rectangular frame. The second line represents the coordinates of the top-right corner of the rectangular frame.

## [Problem J4 - Cyclic Shifts](https://github.com/ACA30/CCC2020/blob/master/j4-cyclic-shifts.py)
**Problem Description**\
Thuc likes finding cyclic shifts of strings. A *cyclic shift* of a string is obtained by moving characters from the beginning of the string to the end of the string. We also consider a string to be a cyclic shift of itself. For example, the cyclic shifts of `ABCDE` are:

> ABCDE, BCDEA, CDEAB, DEABC, and EABCD.

Given some text, *T*, and a string, *S*, determine if *T* contains a cyclic shift of *S*.

**Input Specification**\
The input will consist of exactly two lines containing only uppercase letters. The first line will be the text *T*, and the second line will be the string *S*. Each line will contain at most 1000 characters.\
For 6 of the 15 available marks, *S* will be exactly 3 characters in length.

**Output Specification**\
Output `yes` if the text, *T*, contains a cyclic shift of the string, *S*. Otherwise, output `no`.

## [Problem J5/S2 - Escape Room](https://github.com/ACA30/CCC2020/blob/master/j5-escaoe-room.py)
*I didn't manage to solve this question, so the code in my file is from [Ewpratten's repository](https://github.com/Ewpratten/ccc-2020).*

**Problem Description**\
You have to determine if it is possible to escape from a room. The room is an *M*-by-*N* grid with each position (cell) containing a positive integer. The rows are numbered 1, 2, ..., *M* and the columns are numbered 1, 2, ..., *N*. We use (*r, c*) to refer to the cell in row r and column c.\
You start in the top-left corner at (1, 1) and exit from the bottom-right corner at (*M, N*). If you are in a cell containing the value *x*, then you can jump to any cell (*a, b*) satisfying *a × b = x*. For example, if you are in a cell containing a 6, you can jump to cell (2, 3).\
Note that from a cell containing a 6, there are up to four cells you can jump to: (2, 3), (3, 2), (1, 6), or (6, 1). If the room is a 5-by-6 grid, there isn’t a row 6 so only the first three jumps would be possible.

**Input Specification**\
The first line of the input will be an integer *M* (1 ≤ *M* ≤ 1000). The second line of the input will be an integer *N* (1 ≤ *N* ≤ 1000). The remaining input gives the positive integers in the cells of the room with *M* rows and *N* columns. It consists of M lines where each line contains *N* positive integers, each less than or equal to 1 000 000, separated by single spaces.\
For 1 of the 15 available marks, *M* = 2 and *N* = 2.\
For an additional 2 of the 15 available marks, *M* = 1.\
For an additional 4 of the 15 available marks, all of the integers in the cells will be unique.\
For an additional 4 of the 15 available marks, *M* ≤ 200 and *N* ≤ 200.

**Output Specification**\
Output `yes` if it is possible to escape from the room. Otherwise, output `no`.