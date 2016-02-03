## Matrix Multiplication

### Description
This program implements 2 types of Matrix Multiplication techniques:
    1. Standard Recursive Matrix Multiplication
    2. Matrix Multiplication using Strassens Algorithm

The program also compares the running time of both algorithms. As expected, the Strassens algorithm runs faster for larger matrix sizes.

That is,
```cmd
Standard Recursive matrix multiplication takes:
T(n) = O(n^3) time.

Strassens algorithm takes:
T(n) = O(n^lg7) = O(n^2.81) time. [Here lg x = Log to base 2 of x]
```

### Requirements

To execute the program, you need to specify the size (N) of the Square Matrix (N x N).
The matrices A,B used for multiplication are auto-generated (N x N each).
Note: Currently, the program only supports matrix of sizes that are power of 2. i.e. N = 2^k


### Usage

```cmd
usage: matrix_multiply.py [-h] SIZE

positional arguments:
  SIZE        Size of Square Matrix for Multiplication. SIZE = 2^k

optional arguments:
  -h, --help  show this help message and exit
```

### Sample Output

```cmd
$ python .\matrix_multiply.py 16

Matrix A:
   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
0 [4, 3, 2, 3, 8, 3, 3, 7, 5, 9, 6, 9, 4, 2, 8, 2]
1 [5, 6, 4, 6, 3, 2, 9, 7, 9, 4, 9, 8, 6, 4, 7, 9]
2 [8, 6, 4, 4, 6, 1, 8, 9, 6, 7, 1, 8, 9, 5, 2, 2]
3 [4, 4, 5, 9, 9, 9, 4, 7, 1, 3, 3, 7, 7, 4, 6, 1]
4 [8, 2, 1, 1, 2, 7, 2, 7, 7, 4, 6, 3, 8, 7, 2, 7]
5 [7, 5, 5, 6, 4, 6, 4, 7, 3, 3, 6, 5, 5, 7, 5, 5]
6 [9, 1, 2, 5, 7, 4, 2, 5, 5, 5, 7, 8, 5, 3, 1, 9]
7 [7, 4, 9, 5, 9, 2, 3, 6, 8, 4, 8, 9, 9, 1, 4, 3]
8 [2, 7, 4, 3, 5, 6, 8, 2, 1, 6, 1, 1, 1, 9, 8, 8]
9 [5, 2, 6, 6, 4, 1, 1, 2, 3, 1, 9, 5, 1, 7, 9, 6]
10 [9, 3, 2, 3, 1, 7, 3, 8, 4, 7, 2, 6, 4, 5, 2, 6]
11 [1, 3, 3, 2, 5, 6, 9, 2, 8, 3, 6, 9, 5, 1, 5, 4]
12 [3, 3, 1, 8, 8, 9, 7, 7, 4, 8, 8, 2, 7, 9, 5, 2]
13 [2, 9, 4, 9, 6, 1, 7, 9, 8, 4, 5, 5, 4, 1, 4, 6]
14 [6, 1, 4, 6, 8, 4, 5, 3, 4, 8, 2, 2, 1, 5, 7, 4]
15 [2, 6, 7, 6, 8, 7, 4, 9, 7, 5, 1, 8, 6, 6, 8, 7]

Matrix B:
   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
0 [4, 6, 3, 6, 3, 2, 2, 6, 4, 4, 2, 9, 2, 6, 5, 4]
1 [5, 7, 5, 2, 3, 8, 1, 3, 6, 1, 3, 9, 8, 1, 2, 5]
2 [8, 6, 1, 4, 8, 7, 2, 4, 8, 5, 9, 6, 6, 2, 1, 2]
3 [4, 7, 7, 1, 5, 9, 3, 4, 7, 8, 3, 8, 7, 5, 3, 1]
4 [6, 3, 1, 5, 4, 8, 7, 1, 7, 6, 7, 7, 4, 8, 5, 4]
5 [6, 3, 8, 9, 4, 2, 6, 9, 2, 8, 4, 1, 4, 1, 6, 2]
6 [1, 3, 4, 9, 9, 8, 4, 9, 8, 5, 6, 3, 2, 8, 3, 5]
7 [8, 4, 7, 4, 7, 6, 9, 3, 3, 4, 7, 9, 4, 3, 6, 6]
8 [9, 5, 6, 4, 7, 4, 1, 9, 6, 7, 1, 7, 1, 5, 9, 8]
9 [1, 3, 1, 7, 4, 8, 2, 8, 2, 2, 1, 5, 8, 5, 9, 7]
10 [9, 3, 3, 6, 3, 3, 4, 6, 9, 2, 2, 4, 1, 2, 4, 2]
11 [3, 8, 6, 5, 2, 9, 3, 3, 6, 4, 1, 6, 2, 4, 4, 7]
12 [3, 8, 9, 9, 5, 4, 5, 2, 4, 7, 5, 2, 7, 1, 3, 8]
13 [9, 2, 9, 7, 1, 4, 5, 9, 1, 5, 2, 9, 3, 6, 4, 8]
14 [1, 1, 8, 2, 1, 5, 9, 2, 8, 7, 9, 3, 8, 1, 8, 5]
15 [7, 4, 1, 2, 7, 7, 9, 6, 7, 3, 7, 6, 6, 1, 3, 2]

Standard Matrix Multiplication:
--- 0.00999999046326 seconds ---

Strassens Matrix Multiplication:
--- 0.00999999046326 seconds ---

 Standard Matrix Multiplication Result ==>
   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
0 [371, 342, 374, 397, 323, 478, 367, 370, 430, 369, 324, 450, 354, 302, 422, 403]
1 [515, 455, 483, 478, 471, 587, 445, 518, 586, 460, 417, 574, 420, 354, 457, 474]
2 [414, 433, 433, 470, 412, 531, 357, 431, 441, 408, 349, 540, 381, 364, 404, 475]
3 [410, 392, 454, 434, 360, 501, 403, 379, 445, 452, 385, 471, 398, 309, 377, 375]
4 [434, 333, 397, 422, 333, 360, 354, 431, 350, 360, 284, 432, 299, 255, 372, 380]
5 [454, 380, 432, 424, 364, 468, 388, 431, 443, 405, 359, 503, 371, 297, 374, 382]
6 [428, 375, 344, 401, 352, 448, 361, 405, 426, 366, 301, 476, 315, 304, 371, 358]
7 [493, 463, 419, 460, 428, 540, 380, 414, 540, 447, 394, 540, 391, 339, 417, 439]
8 [352, 271, 348, 365, 318, 443, 363, 411, 386, 342, 352, 414, 371, 270, 332, 333]
9 [390, 288, 329, 296, 267, 387, 329, 335, 422, 329, 309, 417, 300, 237, 307, 288]
10 [374, 336, 366, 392, 325, 397, 328, 413, 331, 337, 274, 441, 314, 264, 363, 360]
11 [355, 329, 359, 398, 348, 433, 318, 393, 436, 366, 303, 363, 286, 272, 350, 357]
12 [475, 372, 492, 518, 397, 514, 437, 507, 460, 470, 373, 507, 410, 365, 454, 439]
13 [445, 409, 403, 371, 428, 551, 371, 406, 506, 397, 372, 531, 395, 316, 384, 394]
14 [337, 279, 314, 353, 312, 423, 329, 380, 380, 359, 316, 417, 332, 306, 366, 323]
15 [514, 444, 505, 468, 450, 599, 477, 473, 523, 499, 459, 576, 470, 343, 466, 477]

 Strassens Matrix Multiplication Result ==>
   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
0 [371, 342, 374, 397, 323, 478, 367, 370, 430, 369, 324, 450, 354, 302, 422, 403]
1 [515, 455, 483, 478, 471, 587, 445, 518, 586, 460, 417, 574, 420, 354, 457, 474]
2 [414, 433, 433, 470, 412, 531, 357, 431, 441, 408, 349, 540, 381, 364, 404, 475]
3 [410, 392, 454, 434, 360, 501, 403, 379, 445, 452, 385, 471, 398, 309, 377, 375]
4 [434, 333, 397, 422, 333, 360, 354, 431, 350, 360, 284, 432, 299, 255, 372, 380]
5 [454, 380, 432, 424, 364, 468, 388, 431, 443, 405, 359, 503, 371, 297, 374, 382]
6 [428, 375, 344, 401, 352, 448, 361, 405, 426, 366, 301, 476, 315, 304, 371, 358]
7 [493, 463, 419, 460, 428, 540, 380, 414, 540, 447, 394, 540, 391, 339, 417, 439]
8 [352, 271, 348, 365, 318, 443, 363, 411, 386, 342, 352, 414, 371, 270, 332, 333]
9 [390, 288, 329, 296, 267, 387, 329, 335, 422, 329, 309, 417, 300, 237, 307, 288]
10 [374, 336, 366, 392, 325, 397, 328, 413, 331, 337, 274, 441, 314, 264, 363, 360]
11 [355, 329, 359, 398, 348, 433, 318, 393, 436, 366, 303, 363, 286, 272, 350, 357]
12 [475, 372, 492, 518, 397, 514, 437, 507, 460, 470, 373, 507, 410, 365, 454, 439]
13 [445, 409, 403, 371, 428, 551, 371, 406, 506, 397, 372, 531, 395, 316, 384, 394]
14 [337, 279, 314, 353, 312, 423, 329, 380, 380, 359, 316, 417, 332, 306, 366, 323]
15 [514, 444, 505, 468, 450, 599, 477, 473, 523, 499, 459, 576, 470, 343, 466, 477]
```