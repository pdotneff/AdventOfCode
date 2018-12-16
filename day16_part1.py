file = """Before: [1, 1, 0, 1]
0 1 0 1
After:  [1, 1, 0, 1]

Before: [2, 2, 2, 1]
2 1 2 2
After:  [2, 2, 1, 1]

Before: [1, 3, 2, 2]
1 2 2 0
After:  [4, 3, 2, 2]

Before: [2, 2, 1, 1]
8 0 2 1
After:  [2, 3, 1, 1]

Before: [0, 1, 2, 2]
7 3 1 1
After:  [0, 3, 2, 2]

Before: [1, 2, 2, 0]
8 2 0 1
After:  [1, 3, 2, 0]

Before: [2, 2, 2, 0]
2 1 2 0
After:  [1, 2, 2, 0]

Before: [0, 1, 1, 1]
3 1 0 1
After:  [0, 1, 1, 1]

Before: [2, 3, 2, 2]
15 1 2 2
After:  [2, 3, 6, 2]

Before: [0, 3, 1, 1]
9 0 0 3
After:  [0, 3, 1, 0]

Before: [2, 0, 1, 1]
4 2 3 2
After:  [2, 0, 0, 1]

Before: [1, 1, 3, 3]
6 0 3 3
After:  [1, 1, 3, 0]

Before: [3, 2, 3, 2]
11 1 3 3
After:  [3, 2, 3, 1]

Before: [3, 2, 1, 2]
14 3 3 1
After:  [3, 6, 1, 2]

Before: [1, 0, 1, 2]
10 1 0 1
After:  [1, 1, 1, 2]

Before: [1, 2, 0, 2]
11 1 3 2
After:  [1, 2, 1, 2]

Before: [3, 3, 0, 0]
14 0 3 2
After:  [3, 3, 9, 0]

Before: [2, 0, 2, 3]
6 0 3 1
After:  [2, 0, 2, 3]

Before: [3, 2, 2, 2]
11 1 3 1
After:  [3, 1, 2, 2]

Before: [2, 2, 0, 2]
13 1 2 1
After:  [2, 4, 0, 2]

Before: [2, 2, 2, 0]
8 3 1 3
After:  [2, 2, 2, 2]

Before: [2, 3, 1, 3]
6 0 3 2
After:  [2, 3, 0, 3]

Before: [3, 3, 1, 1]
14 1 3 1
After:  [3, 9, 1, 1]

Before: [2, 2, 1, 3]
6 0 3 2
After:  [2, 2, 0, 3]

Before: [2, 3, 2, 3]
15 3 3 0
After:  [9, 3, 2, 3]

Before: [1, 0, 0, 3]
10 1 0 1
After:  [1, 1, 0, 3]

Before: [1, 3, 1, 3]
15 1 3 3
After:  [1, 3, 1, 9]

Before: [1, 1, 2, 3]
15 1 2 3
After:  [1, 1, 2, 2]

Before: [1, 1, 3, 0]
0 1 0 0
After:  [1, 1, 3, 0]

Before: [1, 2, 3, 2]
13 3 2 2
After:  [1, 2, 4, 2]

Before: [0, 1, 1, 2]
9 0 0 0
After:  [0, 1, 1, 2]

Before: [2, 2, 0, 0]
12 1 1 3
After:  [2, 2, 0, 1]

Before: [1, 0, 2, 3]
6 0 3 2
After:  [1, 0, 0, 3]

Before: [1, 1, 0, 3]
6 0 3 3
After:  [1, 1, 0, 0]

Before: [0, 2, 0, 0]
9 0 0 2
After:  [0, 2, 0, 0]

Before: [0, 2, 2, 3]
5 0 3 0
After:  [3, 2, 2, 3]

Before: [1, 0, 2, 1]
5 1 2 3
After:  [1, 0, 2, 2]

Before: [1, 1, 3, 3]
0 1 0 2
After:  [1, 1, 1, 3]

Before: [2, 0, 3, 1]
12 2 3 0
After:  [0, 0, 3, 1]

Before: [0, 3, 2, 0]
5 0 2 0
After:  [2, 3, 2, 0]

Before: [2, 1, 2, 2]
1 2 2 0
After:  [4, 1, 2, 2]

Before: [1, 2, 1, 3]
6 0 3 2
After:  [1, 2, 0, 3]

Before: [0, 2, 3, 1]
14 1 3 2
After:  [0, 2, 6, 1]

Before: [1, 3, 3, 3]
5 0 3 2
After:  [1, 3, 3, 3]

Before: [3, 1, 0, 3]
14 3 2 3
After:  [3, 1, 0, 6]

Before: [2, 0, 3, 3]
12 3 2 0
After:  [1, 0, 3, 3]

Before: [1, 2, 1, 2]
11 1 3 3
After:  [1, 2, 1, 1]

Before: [2, 1, 2, 1]
1 0 2 1
After:  [2, 4, 2, 1]

Before: [0, 1, 1, 0]
3 1 0 1
After:  [0, 1, 1, 0]

Before: [0, 2, 3, 0]
9 0 0 2
After:  [0, 2, 0, 0]

Before: [3, 1, 2, 3]
15 2 3 3
After:  [3, 1, 2, 6]

Before: [0, 1, 0, 0]
3 1 0 0
After:  [1, 1, 0, 0]

Before: [0, 0, 1, 2]
5 2 3 2
After:  [0, 0, 3, 2]

Before: [0, 2, 2, 2]
8 0 3 1
After:  [0, 2, 2, 2]

Before: [1, 2, 0, 3]
15 0 1 0
After:  [2, 2, 0, 3]

Before: [2, 1, 0, 3]
6 0 3 2
After:  [2, 1, 0, 3]

Before: [0, 2, 3, 2]
11 1 3 1
After:  [0, 1, 3, 2]

Before: [1, 1, 2, 1]
0 1 0 1
After:  [1, 1, 2, 1]

Before: [2, 2, 2, 0]
12 1 1 1
After:  [2, 1, 2, 0]

Before: [3, 1, 2, 2]
1 2 2 2
After:  [3, 1, 4, 2]

Before: [0, 1, 3, 0]
3 1 0 3
After:  [0, 1, 3, 1]

Before: [3, 0, 2, 0]
1 2 2 2
After:  [3, 0, 4, 0]

Before: [2, 3, 3, 2]
15 1 3 2
After:  [2, 3, 6, 2]

Before: [3, 0, 2, 0]
1 2 2 0
After:  [4, 0, 2, 0]

Before: [3, 2, 3, 2]
12 1 1 0
After:  [1, 2, 3, 2]

Before: [2, 3, 3, 2]
13 0 2 0
After:  [4, 3, 3, 2]

Before: [1, 0, 2, 2]
10 1 0 0
After:  [1, 0, 2, 2]

Before: [2, 0, 0, 0]
8 1 0 1
After:  [2, 2, 0, 0]

Before: [0, 2, 2, 1]
12 2 1 0
After:  [1, 2, 2, 1]

Before: [0, 3, 2, 1]
9 0 0 3
After:  [0, 3, 2, 0]

Before: [2, 2, 2, 1]
1 0 2 1
After:  [2, 4, 2, 1]

Before: [0, 1, 2, 3]
3 1 0 2
After:  [0, 1, 1, 3]

Before: [1, 1, 0, 2]
0 1 0 0
After:  [1, 1, 0, 2]

Before: [3, 2, 1, 2]
11 1 3 0
After:  [1, 2, 1, 2]

Before: [3, 1, 3, 3]
8 1 0 0
After:  [3, 1, 3, 3]

Before: [3, 1, 2, 3]
15 0 2 2
After:  [3, 1, 6, 3]

Before: [0, 2, 2, 1]
2 1 2 3
After:  [0, 2, 2, 1]

Before: [1, 1, 0, 2]
0 1 0 3
After:  [1, 1, 0, 1]

Before: [2, 2, 3, 2]
11 1 3 0
After:  [1, 2, 3, 2]

Before: [1, 1, 3, 1]
0 1 0 2
After:  [1, 1, 1, 1]

Before: [1, 2, 3, 0]
8 3 1 0
After:  [2, 2, 3, 0]

Before: [1, 0, 2, 3]
10 1 0 0
After:  [1, 0, 2, 3]

Before: [1, 3, 3, 1]
12 1 2 1
After:  [1, 1, 3, 1]

Before: [0, 1, 2, 2]
3 1 0 0
After:  [1, 1, 2, 2]

Before: [2, 2, 2, 3]
6 0 3 2
After:  [2, 2, 0, 3]

Before: [3, 2, 3, 0]
13 1 2 0
After:  [4, 2, 3, 0]

Before: [0, 1, 0, 1]
9 0 0 2
After:  [0, 1, 0, 1]

Before: [2, 3, 3, 2]
13 3 2 1
After:  [2, 4, 3, 2]

Before: [2, 2, 1, 3]
4 1 2 2
After:  [2, 2, 1, 3]

Before: [1, 3, 0, 1]
8 0 1 2
After:  [1, 3, 3, 1]

Before: [0, 1, 2, 0]
3 1 0 1
After:  [0, 1, 2, 0]

Before: [0, 2, 0, 2]
11 1 3 1
After:  [0, 1, 0, 2]

Before: [3, 2, 3, 1]
14 2 3 3
After:  [3, 2, 3, 9]

Before: [0, 1, 1, 3]
3 1 0 0
After:  [1, 1, 1, 3]

Before: [2, 2, 2, 1]
2 1 2 0
After:  [1, 2, 2, 1]

Before: [0, 2, 1, 2]
4 3 3 3
After:  [0, 2, 1, 0]

Before: [0, 1, 1, 2]
7 3 1 3
After:  [0, 1, 1, 3]

Before: [1, 0, 1, 0]
10 1 0 0
After:  [1, 0, 1, 0]

Before: [3, 2, 2, 1]
12 1 1 3
After:  [3, 2, 2, 1]

Before: [0, 1, 0, 0]
9 0 0 2
After:  [0, 1, 0, 0]

Before: [2, 2, 2, 1]
2 1 2 1
After:  [2, 1, 2, 1]

Before: [1, 3, 0, 3]
2 1 3 0
After:  [1, 3, 0, 3]

Before: [1, 1, 2, 2]
0 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 2, 0, 2]
11 1 3 3
After:  [0, 2, 0, 1]

Before: [0, 2, 3, 2]
11 1 3 0
After:  [1, 2, 3, 2]

Before: [2, 3, 2, 1]
7 3 2 0
After:  [3, 3, 2, 1]

Before: [2, 1, 1, 3]
14 3 2 0
After:  [6, 1, 1, 3]

Before: [1, 1, 3, 2]
0 1 0 0
After:  [1, 1, 3, 2]

Before: [2, 2, 2, 3]
1 0 2 2
After:  [2, 2, 4, 3]

Before: [1, 1, 0, 3]
0 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 0, 3, 0]
10 1 0 2
After:  [1, 0, 1, 0]

Before: [0, 2, 0, 2]
11 1 3 2
After:  [0, 2, 1, 2]

Before: [1, 3, 2, 1]
7 3 2 0
After:  [3, 3, 2, 1]

Before: [2, 2, 1, 0]
14 0 3 2
After:  [2, 2, 6, 0]

Before: [0, 1, 0, 0]
5 0 1 3
After:  [0, 1, 0, 1]

Before: [0, 2, 2, 3]
15 2 3 0
After:  [6, 2, 2, 3]

Before: [3, 3, 0, 3]
15 0 3 0
After:  [9, 3, 0, 3]

Before: [0, 3, 3, 0]
14 2 3 0
After:  [9, 3, 3, 0]

Before: [0, 1, 1, 2]
7 3 1 2
After:  [0, 1, 3, 2]

Before: [1, 3, 1, 3]
2 1 3 0
After:  [1, 3, 1, 3]

Before: [1, 0, 3, 3]
10 1 0 2
After:  [1, 0, 1, 3]

Before: [0, 1, 3, 2]
3 1 0 3
After:  [0, 1, 3, 1]

Before: [0, 1, 3, 1]
3 1 0 2
After:  [0, 1, 1, 1]

Before: [1, 1, 2, 0]
0 1 0 1
After:  [1, 1, 2, 0]

Before: [0, 3, 0, 2]
15 1 3 3
After:  [0, 3, 0, 6]

Before: [0, 2, 1, 1]
4 1 2 2
After:  [0, 2, 1, 1]

Before: [0, 2, 2, 1]
4 3 3 0
After:  [0, 2, 2, 1]

Before: [1, 2, 1, 2]
8 1 0 1
After:  [1, 3, 1, 2]

Before: [1, 2, 2, 0]
15 0 2 1
After:  [1, 2, 2, 0]

Before: [2, 2, 3, 1]
4 3 3 1
After:  [2, 0, 3, 1]

Before: [1, 2, 1, 0]
8 3 1 3
After:  [1, 2, 1, 2]

Before: [3, 0, 2, 2]
8 1 0 2
After:  [3, 0, 3, 2]

Before: [0, 0, 2, 0]
9 0 0 2
After:  [0, 0, 0, 0]

Before: [1, 2, 2, 3]
4 1 0 2
After:  [1, 2, 1, 3]

Before: [2, 1, 2, 2]
1 3 2 1
After:  [2, 4, 2, 2]

Before: [2, 3, 0, 3]
2 1 3 1
After:  [2, 1, 0, 3]

Before: [1, 2, 0, 2]
11 1 3 1
After:  [1, 1, 0, 2]

Before: [3, 1, 0, 2]
7 3 1 1
After:  [3, 3, 0, 2]

Before: [0, 2, 2, 3]
1 1 2 3
After:  [0, 2, 2, 4]

Before: [1, 2, 3, 3]
6 0 3 0
After:  [0, 2, 3, 3]

Before: [2, 0, 2, 1]
7 3 2 0
After:  [3, 0, 2, 1]

Before: [0, 2, 2, 2]
8 0 3 2
After:  [0, 2, 2, 2]

Before: [1, 0, 3, 1]
10 1 0 2
After:  [1, 0, 1, 1]

Before: [0, 1, 2, 1]
4 3 3 2
After:  [0, 1, 0, 1]

Before: [0, 2, 2, 0]
2 1 2 3
After:  [0, 2, 2, 1]

Before: [0, 0, 2, 2]
5 1 2 0
After:  [2, 0, 2, 2]

Before: [1, 0, 0, 3]
10 1 0 3
After:  [1, 0, 0, 1]

Before: [1, 0, 3, 1]
10 1 0 3
After:  [1, 0, 3, 1]

Before: [0, 0, 3, 2]
9 0 0 3
After:  [0, 0, 3, 0]

Before: [1, 0, 1, 3]
10 1 0 2
After:  [1, 0, 1, 3]

Before: [3, 2, 3, 2]
4 3 3 2
After:  [3, 2, 0, 2]

Before: [0, 1, 1, 3]
3 1 0 2
After:  [0, 1, 1, 3]

Before: [1, 2, 3, 3]
4 1 0 1
After:  [1, 1, 3, 3]

Before: [0, 0, 0, 2]
9 0 0 1
After:  [0, 0, 0, 2]

Before: [1, 0, 2, 1]
10 1 0 1
After:  [1, 1, 2, 1]

Before: [1, 2, 3, 2]
5 0 3 2
After:  [1, 2, 3, 2]

Before: [2, 2, 3, 2]
12 1 1 0
After:  [1, 2, 3, 2]

Before: [2, 2, 2, 2]
12 2 1 2
After:  [2, 2, 1, 2]

Before: [2, 2, 2, 3]
1 2 2 1
After:  [2, 4, 2, 3]

Before: [3, 1, 3, 2]
7 3 1 2
After:  [3, 1, 3, 2]

Before: [2, 2, 0, 0]
13 0 2 1
After:  [2, 4, 0, 0]

Before: [0, 2, 1, 3]
15 1 3 1
After:  [0, 6, 1, 3]

Before: [0, 1, 1, 2]
3 1 0 0
After:  [1, 1, 1, 2]

Before: [2, 1, 0, 0]
8 3 0 1
After:  [2, 2, 0, 0]

Before: [0, 1, 3, 3]
15 2 3 0
After:  [9, 1, 3, 3]

Before: [0, 1, 1, 2]
3 1 0 1
After:  [0, 1, 1, 2]

Before: [0, 1, 1, 1]
8 0 2 0
After:  [1, 1, 1, 1]

Before: [1, 2, 2, 3]
12 1 1 3
After:  [1, 2, 2, 1]

Before: [3, 3, 1, 2]
12 1 0 1
After:  [3, 1, 1, 2]

Before: [3, 0, 0, 3]
14 3 2 2
After:  [3, 0, 6, 3]

Before: [3, 3, 3, 1]
12 2 3 3
After:  [3, 3, 3, 0]

Before: [2, 3, 2, 0]
14 2 3 1
After:  [2, 6, 2, 0]

Before: [2, 3, 0, 2]
15 1 3 2
After:  [2, 3, 6, 2]

Before: [3, 2, 3, 2]
11 1 3 1
After:  [3, 1, 3, 2]

Before: [1, 2, 2, 1]
15 3 2 1
After:  [1, 2, 2, 1]

Before: [1, 2, 2, 1]
5 0 2 1
After:  [1, 3, 2, 1]

Before: [1, 2, 3, 3]
6 0 3 2
After:  [1, 2, 0, 3]

Before: [1, 2, 2, 0]
5 0 2 2
After:  [1, 2, 3, 0]

Before: [3, 0, 0, 2]
4 3 3 1
After:  [3, 0, 0, 2]

Before: [1, 2, 1, 3]
8 1 0 2
After:  [1, 2, 3, 3]

Before: [2, 0, 2, 1]
1 2 2 1
After:  [2, 4, 2, 1]

Before: [2, 1, 2, 3]
1 2 2 3
After:  [2, 1, 2, 4]

Before: [1, 1, 0, 1]
14 3 2 1
After:  [1, 2, 0, 1]

Before: [1, 0, 2, 1]
1 2 2 1
After:  [1, 4, 2, 1]

Before: [2, 2, 0, 3]
15 0 3 3
After:  [2, 2, 0, 6]

Before: [3, 0, 2, 2]
1 3 2 0
After:  [4, 0, 2, 2]

Before: [2, 2, 3, 2]
13 3 2 1
After:  [2, 4, 3, 2]

Before: [1, 1, 2, 1]
0 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 2, 3, 2]
11 1 3 2
After:  [0, 2, 1, 2]

Before: [2, 1, 1, 2]
7 3 1 0
After:  [3, 1, 1, 2]

Before: [3, 0, 2, 0]
14 2 3 3
After:  [3, 0, 2, 6]

Before: [2, 2, 0, 2]
14 0 3 3
After:  [2, 2, 0, 6]

Before: [0, 0, 3, 2]
9 0 0 0
After:  [0, 0, 3, 2]

Before: [1, 1, 3, 1]
0 1 0 1
After:  [1, 1, 3, 1]

Before: [1, 1, 1, 1]
0 1 0 1
After:  [1, 1, 1, 1]

Before: [1, 0, 2, 0]
10 1 0 1
After:  [1, 1, 2, 0]

Before: [1, 1, 0, 3]
0 1 0 0
After:  [1, 1, 0, 3]

Before: [0, 1, 0, 2]
13 3 2 1
After:  [0, 4, 0, 2]

Before: [2, 1, 0, 0]
14 1 2 3
After:  [2, 1, 0, 2]

Before: [3, 3, 2, 2]
4 3 3 1
After:  [3, 0, 2, 2]

Before: [0, 2, 0, 0]
12 1 1 3
After:  [0, 2, 0, 1]

Before: [1, 0, 2, 1]
1 2 2 2
After:  [1, 0, 4, 1]

Before: [0, 1, 2, 1]
9 0 0 2
After:  [0, 1, 0, 1]

Before: [1, 1, 3, 2]
0 1 0 2
After:  [1, 1, 1, 2]

Before: [3, 0, 3, 2]
15 0 3 0
After:  [6, 0, 3, 2]

Before: [2, 1, 2, 0]
5 3 2 0
After:  [2, 1, 2, 0]

Before: [3, 2, 2, 2]
1 2 2 2
After:  [3, 2, 4, 2]

Before: [1, 1, 0, 0]
0 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 2, 0, 3]
12 1 1 2
After:  [1, 2, 1, 3]

Before: [2, 2, 2, 0]
1 0 2 1
After:  [2, 4, 2, 0]

Before: [0, 2, 1, 3]
8 0 2 2
After:  [0, 2, 1, 3]

Before: [3, 2, 0, 0]
14 1 3 1
After:  [3, 6, 0, 0]

Before: [0, 2, 2, 3]
15 3 3 3
After:  [0, 2, 2, 9]

Before: [1, 0, 3, 2]
10 1 0 0
After:  [1, 0, 3, 2]

Before: [1, 2, 2, 0]
2 1 2 2
After:  [1, 2, 1, 0]

Before: [0, 0, 3, 3]
9 0 0 1
After:  [0, 0, 3, 3]

Before: [0, 1, 2, 3]
3 1 0 1
After:  [0, 1, 2, 3]

Before: [1, 0, 1, 1]
10 1 0 3
After:  [1, 0, 1, 1]

Before: [2, 0, 2, 3]
6 0 3 0
After:  [0, 0, 2, 3]

Before: [0, 2, 3, 0]
13 1 2 1
After:  [0, 4, 3, 0]

Before: [0, 1, 3, 2]
3 1 0 1
After:  [0, 1, 3, 2]

Before: [1, 1, 0, 3]
6 0 3 0
After:  [0, 1, 0, 3]

Before: [3, 2, 0, 1]
13 1 2 0
After:  [4, 2, 0, 1]

Before: [2, 1, 3, 1]
5 0 1 2
After:  [2, 1, 3, 1]

Before: [1, 1, 3, 2]
0 1 0 1
After:  [1, 1, 3, 2]

Before: [2, 0, 0, 3]
6 0 3 0
After:  [0, 0, 0, 3]

Before: [1, 2, 1, 0]
13 1 2 1
After:  [1, 4, 1, 0]

Before: [2, 2, 1, 2]
11 1 3 3
After:  [2, 2, 1, 1]

Before: [0, 1, 2, 3]
5 1 3 3
After:  [0, 1, 2, 3]

Before: [2, 0, 3, 3]
6 0 3 2
After:  [2, 0, 0, 3]

Before: [2, 2, 1, 0]
12 1 0 0
After:  [1, 2, 1, 0]

Before: [2, 2, 2, 2]
11 1 3 0
After:  [1, 2, 2, 2]

Before: [1, 1, 0, 1]
0 1 0 0
After:  [1, 1, 0, 1]

Before: [0, 2, 2, 2]
11 1 3 0
After:  [1, 2, 2, 2]

Before: [2, 2, 0, 2]
11 1 3 3
After:  [2, 2, 0, 1]

Before: [2, 2, 2, 0]
2 1 2 2
After:  [2, 2, 1, 0]

Before: [3, 1, 1, 2]
7 3 1 3
After:  [3, 1, 1, 3]

Before: [0, 2, 1, 3]
9 0 0 0
After:  [0, 2, 1, 3]

Before: [0, 2, 2, 2]
11 1 3 3
After:  [0, 2, 2, 1]

Before: [3, 3, 3, 1]
7 3 2 2
After:  [3, 3, 3, 1]

Before: [2, 0, 3, 3]
6 0 3 1
After:  [2, 0, 3, 3]

Before: [0, 0, 2, 3]
5 1 3 1
After:  [0, 3, 2, 3]

Before: [3, 3, 2, 0]
5 3 2 2
After:  [3, 3, 2, 0]

Before: [3, 1, 2, 0]
14 2 3 3
After:  [3, 1, 2, 6]

Before: [1, 1, 2, 0]
1 2 2 2
After:  [1, 1, 4, 0]

Before: [1, 3, 1, 1]
4 2 3 1
After:  [1, 0, 1, 1]

Before: [1, 1, 2, 3]
0 1 0 1
After:  [1, 1, 2, 3]

Before: [3, 3, 3, 2]
15 2 3 0
After:  [6, 3, 3, 2]

Before: [1, 1, 0, 1]
0 1 0 3
After:  [1, 1, 0, 1]

Before: [2, 1, 1, 1]
13 0 2 1
After:  [2, 4, 1, 1]

Before: [3, 3, 2, 1]
1 2 2 1
After:  [3, 4, 2, 1]

Before: [0, 2, 2, 3]
2 1 2 3
After:  [0, 2, 2, 1]

Before: [2, 0, 1, 3]
6 0 3 2
After:  [2, 0, 0, 3]

Before: [1, 3, 3, 3]
6 0 3 2
After:  [1, 3, 0, 3]

Before: [0, 1, 0, 2]
7 3 1 3
After:  [0, 1, 0, 3]

Before: [0, 2, 2, 1]
12 2 1 2
After:  [0, 2, 1, 1]

Before: [1, 3, 2, 3]
6 0 3 1
After:  [1, 0, 2, 3]

Before: [1, 3, 1, 3]
15 1 3 2
After:  [1, 3, 9, 3]

Before: [0, 3, 2, 2]
1 2 2 1
After:  [0, 4, 2, 2]

Before: [3, 3, 2, 3]
2 1 3 2
After:  [3, 3, 1, 3]

Before: [0, 0, 2, 3]
5 0 2 0
After:  [2, 0, 2, 3]

Before: [3, 0, 2, 3]
15 2 3 0
After:  [6, 0, 2, 3]

Before: [2, 3, 0, 3]
14 3 2 1
After:  [2, 6, 0, 3]

Before: [2, 0, 2, 1]
1 0 2 2
After:  [2, 0, 4, 1]

Before: [0, 1, 3, 1]
9 0 0 2
After:  [0, 1, 0, 1]

Before: [1, 2, 2, 2]
2 1 2 3
After:  [1, 2, 2, 1]

Before: [0, 0, 3, 1]
9 0 0 0
After:  [0, 0, 3, 1]

Before: [0, 1, 3, 3]
3 1 0 2
After:  [0, 1, 1, 3]

Before: [2, 1, 2, 3]
12 2 0 0
After:  [1, 1, 2, 3]

Before: [1, 2, 3, 2]
11 1 3 2
After:  [1, 2, 1, 2]

Before: [3, 2, 0, 2]
11 1 3 3
After:  [3, 2, 0, 1]

Before: [2, 1, 2, 2]
12 2 0 1
After:  [2, 1, 2, 2]

Before: [0, 1, 0, 2]
13 3 2 2
After:  [0, 1, 4, 2]

Before: [0, 1, 1, 0]
9 0 0 3
After:  [0, 1, 1, 0]

Before: [2, 1, 1, 3]
5 1 3 1
After:  [2, 3, 1, 3]

Before: [0, 2, 2, 2]
1 2 2 1
After:  [0, 4, 2, 2]

Before: [0, 1, 1, 2]
5 0 1 2
After:  [0, 1, 1, 2]

Before: [1, 1, 1, 2]
0 1 0 1
After:  [1, 1, 1, 2]

Before: [3, 3, 1, 2]
12 1 0 0
After:  [1, 3, 1, 2]

Before: [3, 2, 1, 0]
14 0 3 0
After:  [9, 2, 1, 0]

Before: [2, 2, 1, 1]
15 3 1 0
After:  [2, 2, 1, 1]

Before: [1, 3, 2, 1]
7 3 2 2
After:  [1, 3, 3, 1]

Before: [0, 2, 0, 0]
9 0 0 3
After:  [0, 2, 0, 0]

Before: [1, 2, 1, 3]
4 1 0 1
After:  [1, 1, 1, 3]

Before: [1, 1, 3, 2]
15 2 3 1
After:  [1, 6, 3, 2]

Before: [2, 3, 3, 1]
7 3 2 0
After:  [3, 3, 3, 1]

Before: [0, 1, 2, 2]
5 0 1 0
After:  [1, 1, 2, 2]

Before: [3, 1, 0, 2]
7 3 1 0
After:  [3, 1, 0, 2]

Before: [1, 3, 3, 3]
15 2 3 3
After:  [1, 3, 3, 9]

Before: [3, 2, 2, 3]
15 3 3 1
After:  [3, 9, 2, 3]

Before: [0, 0, 0, 2]
9 0 0 2
After:  [0, 0, 0, 2]

Before: [2, 1, 3, 0]
5 1 2 3
After:  [2, 1, 3, 3]

Before: [3, 0, 2, 1]
1 2 2 0
After:  [4, 0, 2, 1]

Before: [1, 0, 2, 3]
10 1 0 3
After:  [1, 0, 2, 1]

Before: [0, 3, 1, 2]
14 3 3 2
After:  [0, 3, 6, 2]

Before: [0, 3, 3, 3]
2 1 3 2
After:  [0, 3, 1, 3]

Before: [0, 2, 2, 0]
5 3 2 3
After:  [0, 2, 2, 2]

Before: [1, 1, 2, 1]
5 2 1 0
After:  [3, 1, 2, 1]

Before: [1, 2, 0, 2]
11 1 3 3
After:  [1, 2, 0, 1]

Before: [3, 0, 2, 1]
7 3 2 3
After:  [3, 0, 2, 3]

Before: [0, 2, 1, 3]
9 0 0 2
After:  [0, 2, 0, 3]

Before: [2, 2, 2, 2]
11 1 3 3
After:  [2, 2, 2, 1]

Before: [1, 3, 2, 3]
1 2 2 0
After:  [4, 3, 2, 3]

Before: [1, 3, 1, 3]
2 1 3 2
After:  [1, 3, 1, 3]

Before: [0, 1, 2, 3]
5 0 3 1
After:  [0, 3, 2, 3]

Before: [2, 2, 1, 2]
11 1 3 1
After:  [2, 1, 1, 2]

Before: [1, 0, 3, 1]
7 3 2 0
After:  [3, 0, 3, 1]

Before: [1, 2, 1, 3]
6 0 3 0
After:  [0, 2, 1, 3]

Before: [3, 2, 2, 2]
2 1 2 0
After:  [1, 2, 2, 2]

Before: [3, 0, 0, 3]
5 1 3 0
After:  [3, 0, 0, 3]

Before: [2, 3, 3, 3]
6 0 3 2
After:  [2, 3, 0, 3]

Before: [1, 2, 3, 2]
11 1 3 0
After:  [1, 2, 3, 2]

Before: [2, 3, 3, 3]
6 0 3 1
After:  [2, 0, 3, 3]

Before: [2, 1, 0, 3]
6 0 3 0
After:  [0, 1, 0, 3]

Before: [3, 2, 3, 1]
4 3 3 1
After:  [3, 0, 3, 1]

Before: [1, 2, 2, 3]
1 2 2 1
After:  [1, 4, 2, 3]

Before: [0, 2, 0, 2]
12 1 1 2
After:  [0, 2, 1, 2]

Before: [3, 3, 1, 3]
2 1 3 3
After:  [3, 3, 1, 1]

Before: [1, 1, 2, 2]
5 1 2 2
After:  [1, 1, 3, 2]

Before: [0, 0, 2, 2]
5 0 2 3
After:  [0, 0, 2, 2]

Before: [0, 1, 3, 1]
9 0 0 0
After:  [0, 1, 3, 1]

Before: [0, 1, 0, 0]
3 1 0 1
After:  [0, 1, 0, 0]

Before: [1, 0, 0, 1]
10 1 0 1
After:  [1, 1, 0, 1]

Before: [1, 1, 1, 3]
0 1 0 0
After:  [1, 1, 1, 3]

Before: [0, 2, 2, 2]
4 3 3 1
After:  [0, 0, 2, 2]

Before: [1, 2, 1, 0]
8 2 1 0
After:  [3, 2, 1, 0]

Before: [0, 1, 2, 1]
3 1 0 3
After:  [0, 1, 2, 1]

Before: [1, 0, 2, 1]
10 1 0 3
After:  [1, 0, 2, 1]

Before: [1, 1, 3, 1]
5 0 2 1
After:  [1, 3, 3, 1]

Before: [2, 3, 2, 1]
4 3 3 2
After:  [2, 3, 0, 1]

Before: [3, 3, 0, 3]
12 1 0 1
After:  [3, 1, 0, 3]

Before: [3, 3, 1, 3]
8 2 0 3
After:  [3, 3, 1, 3]

Before: [1, 3, 3, 1]
7 3 2 2
After:  [1, 3, 3, 1]

Before: [3, 0, 3, 1]
4 3 3 0
After:  [0, 0, 3, 1]

Before: [1, 3, 2, 3]
15 3 2 3
After:  [1, 3, 2, 6]

Before: [3, 2, 2, 0]
2 1 2 2
After:  [3, 2, 1, 0]

Before: [3, 1, 2, 1]
4 3 3 1
After:  [3, 0, 2, 1]

Before: [2, 3, 1, 3]
2 1 3 3
After:  [2, 3, 1, 1]

Before: [2, 2, 0, 3]
6 0 3 1
After:  [2, 0, 0, 3]

Before: [2, 3, 2, 2]
1 0 2 0
After:  [4, 3, 2, 2]

Before: [0, 1, 3, 3]
5 0 3 3
After:  [0, 1, 3, 3]

Before: [2, 0, 3, 3]
12 3 2 2
After:  [2, 0, 1, 3]

Before: [1, 1, 3, 2]
13 3 2 2
After:  [1, 1, 4, 2]

Before: [1, 3, 3, 3]
2 1 3 2
After:  [1, 3, 1, 3]

Before: [3, 2, 2, 2]
14 0 3 1
After:  [3, 9, 2, 2]

Before: [1, 0, 3, 2]
8 1 3 2
After:  [1, 0, 2, 2]

Before: [0, 3, 3, 3]
9 0 0 2
After:  [0, 3, 0, 3]

Before: [3, 2, 0, 1]
4 3 3 0
After:  [0, 2, 0, 1]

Before: [3, 0, 3, 2]
4 3 3 0
After:  [0, 0, 3, 2]

Before: [3, 0, 3, 2]
8 1 2 1
After:  [3, 3, 3, 2]

Before: [0, 2, 1, 1]
8 0 3 0
After:  [1, 2, 1, 1]

Before: [2, 2, 2, 0]
1 1 2 1
After:  [2, 4, 2, 0]

Before: [2, 2, 1, 3]
13 0 2 1
After:  [2, 4, 1, 3]

Before: [0, 1, 3, 1]
3 1 0 0
After:  [1, 1, 3, 1]

Before: [0, 1, 2, 2]
3 1 0 3
After:  [0, 1, 2, 1]

Before: [1, 2, 2, 3]
6 0 3 1
After:  [1, 0, 2, 3]

Before: [3, 2, 0, 3]
12 1 1 2
After:  [3, 2, 1, 3]

Before: [2, 3, 1, 1]
13 0 2 0
After:  [4, 3, 1, 1]

Before: [2, 1, 1, 0]
5 0 1 1
After:  [2, 3, 1, 0]

Before: [3, 3, 2, 3]
15 3 2 3
After:  [3, 3, 2, 6]

Before: [0, 1, 0, 3]
3 1 0 3
After:  [0, 1, 0, 1]

Before: [1, 0, 3, 2]
14 2 3 1
After:  [1, 9, 3, 2]

Before: [0, 2, 3, 1]
7 3 2 0
After:  [3, 2, 3, 1]

Before: [2, 3, 0, 2]
14 1 2 2
After:  [2, 3, 6, 2]

Before: [2, 2, 3, 1]
7 3 2 0
After:  [3, 2, 3, 1]

Before: [0, 3, 3, 3]
12 3 2 2
After:  [0, 3, 1, 3]

Before: [0, 2, 2, 2]
9 0 0 2
After:  [0, 2, 0, 2]

Before: [0, 3, 1, 0]
8 0 1 2
After:  [0, 3, 3, 0]

Before: [0, 3, 3, 0]
9 0 0 0
After:  [0, 3, 3, 0]

Before: [0, 3, 0, 3]
15 3 3 1
After:  [0, 9, 0, 3]

Before: [2, 1, 1, 3]
6 0 3 2
After:  [2, 1, 0, 3]

Before: [2, 0, 0, 3]
15 3 3 1
After:  [2, 9, 0, 3]

Before: [0, 1, 0, 3]
5 0 3 2
After:  [0, 1, 3, 3]

Before: [1, 2, 2, 1]
4 1 0 0
After:  [1, 2, 2, 1]

Before: [0, 2, 3, 2]
15 2 3 0
After:  [6, 2, 3, 2]

Before: [0, 2, 2, 3]
9 0 0 1
After:  [0, 0, 2, 3]

Before: [3, 3, 3, 3]
2 1 3 1
After:  [3, 1, 3, 3]

Before: [1, 0, 2, 3]
10 1 0 1
After:  [1, 1, 2, 3]

Before: [2, 1, 1, 3]
6 0 3 1
After:  [2, 0, 1, 3]

Before: [0, 2, 2, 3]
1 2 2 1
After:  [0, 4, 2, 3]

Before: [1, 1, 1, 1]
0 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 0, 2, 0]
1 2 2 1
After:  [0, 4, 2, 0]

Before: [1, 3, 0, 2]
13 3 2 3
After:  [1, 3, 0, 4]

Before: [1, 1, 0, 0]
0 1 0 2
After:  [1, 1, 1, 0]

Before: [1, 1, 1, 3]
0 1 0 2
After:  [1, 1, 1, 3]

Before: [1, 0, 3, 1]
10 1 0 0
After:  [1, 0, 3, 1]

Before: [2, 2, 1, 2]
11 1 3 0
After:  [1, 2, 1, 2]

Before: [0, 1, 0, 1]
9 0 0 3
After:  [0, 1, 0, 0]

Before: [0, 2, 1, 3]
5 2 3 2
After:  [0, 2, 3, 3]

Before: [1, 2, 2, 0]
1 1 2 3
After:  [1, 2, 2, 4]

Before: [1, 1, 0, 1]
0 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 1, 2, 3]
3 1 0 0
After:  [1, 1, 2, 3]

Before: [0, 0, 2, 1]
14 2 3 1
After:  [0, 6, 2, 1]

Before: [2, 1, 2, 2]
7 3 1 3
After:  [2, 1, 2, 3]

Before: [1, 3, 3, 2]
12 1 2 0
After:  [1, 3, 3, 2]

Before: [3, 2, 2, 3]
1 2 2 2
After:  [3, 2, 4, 3]

Before: [0, 3, 2, 1]
8 0 3 2
After:  [0, 3, 1, 1]

Before: [1, 1, 0, 3]
0 1 0 2
After:  [1, 1, 1, 3]

Before: [3, 2, 1, 2]
11 1 3 2
After:  [3, 2, 1, 2]

Before: [0, 2, 1, 2]
11 1 3 1
After:  [0, 1, 1, 2]

Before: [1, 2, 1, 3]
6 0 3 1
After:  [1, 0, 1, 3]

Before: [2, 2, 2, 3]
2 1 2 2
After:  [2, 2, 1, 3]

Before: [3, 2, 2, 1]
1 1 2 1
After:  [3, 4, 2, 1]

Before: [1, 0, 0, 1]
10 1 0 3
After:  [1, 0, 0, 1]

Before: [0, 1, 0, 1]
3 1 0 3
After:  [0, 1, 0, 1]

Before: [1, 1, 1, 0]
0 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 1, 1, 2]
7 3 1 3
After:  [1, 1, 1, 3]

Before: [3, 3, 1, 3]
2 1 3 0
After:  [1, 3, 1, 3]

Before: [1, 0, 0, 2]
10 1 0 0
After:  [1, 0, 0, 2]

Before: [0, 2, 1, 3]
13 1 2 3
After:  [0, 2, 1, 4]

Before: [1, 0, 2, 0]
10 1 0 3
After:  [1, 0, 2, 1]

Before: [2, 3, 3, 0]
13 0 2 3
After:  [2, 3, 3, 4]

Before: [3, 1, 2, 3]
5 1 3 3
After:  [3, 1, 2, 3]

Before: [1, 1, 1, 3]
0 1 0 1
After:  [1, 1, 1, 3]

Before: [2, 1, 2, 1]
7 3 2 3
After:  [2, 1, 2, 3]

Before: [1, 0, 0, 0]
10 1 0 0
After:  [1, 0, 0, 0]

Before: [1, 1, 0, 2]
0 1 0 1
After:  [1, 1, 0, 2]

Before: [3, 1, 2, 2]
1 2 2 0
After:  [4, 1, 2, 2]

Before: [1, 1, 1, 2]
0 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 2, 3, 2]
11 1 3 1
After:  [1, 1, 3, 2]

Before: [3, 0, 2, 1]
1 2 2 3
After:  [3, 0, 2, 4]

Before: [0, 1, 0, 2]
3 1 0 1
After:  [0, 1, 0, 2]

Before: [1, 0, 3, 3]
10 1 0 3
After:  [1, 0, 3, 1]

Before: [1, 3, 1, 2]
5 0 3 2
After:  [1, 3, 3, 2]

Before: [1, 0, 0, 2]
10 1 0 2
After:  [1, 0, 1, 2]

Before: [1, 1, 1, 3]
6 0 3 3
After:  [1, 1, 1, 0]

Before: [1, 2, 0, 2]
11 1 3 0
After:  [1, 2, 0, 2]

Before: [1, 2, 1, 2]
11 1 3 1
After:  [1, 1, 1, 2]

Before: [0, 0, 2, 0]
9 0 0 3
After:  [0, 0, 2, 0]

Before: [3, 2, 2, 2]
1 3 2 2
After:  [3, 2, 4, 2]

Before: [0, 1, 3, 2]
3 1 0 2
After:  [0, 1, 1, 2]

Before: [2, 2, 1, 2]
11 1 3 2
After:  [2, 2, 1, 2]

Before: [1, 3, 0, 2]
13 3 2 0
After:  [4, 3, 0, 2]

Before: [2, 1, 2, 3]
6 0 3 2
After:  [2, 1, 0, 3]

Before: [0, 2, 1, 2]
11 1 3 2
After:  [0, 2, 1, 2]

Before: [2, 2, 2, 2]
2 1 2 1
After:  [2, 1, 2, 2]

Before: [3, 0, 2, 2]
1 2 2 3
After:  [3, 0, 2, 4]

Before: [0, 0, 3, 2]
13 3 2 0
After:  [4, 0, 3, 2]

Before: [1, 2, 1, 1]
4 1 0 1
After:  [1, 1, 1, 1]

Before: [1, 0, 2, 1]
10 1 0 0
After:  [1, 0, 2, 1]

Before: [2, 0, 2, 3]
6 0 3 3
After:  [2, 0, 2, 0]

Before: [1, 2, 3, 1]
4 3 3 3
After:  [1, 2, 3, 0]

Before: [1, 1, 1, 2]
5 2 3 2
After:  [1, 1, 3, 2]

Before: [1, 2, 3, 0]
14 1 3 1
After:  [1, 6, 3, 0]

Before: [0, 0, 1, 3]
5 2 3 0
After:  [3, 0, 1, 3]

Before: [0, 0, 0, 1]
9 0 0 0
After:  [0, 0, 0, 1]

Before: [2, 1, 3, 1]
5 0 1 3
After:  [2, 1, 3, 3]

Before: [2, 1, 2, 3]
6 0 3 3
After:  [2, 1, 2, 0]

Before: [2, 3, 1, 3]
2 1 3 1
After:  [2, 1, 1, 3]

Before: [1, 2, 1, 2]
4 3 3 3
After:  [1, 2, 1, 0]

Before: [2, 2, 3, 2]
11 1 3 1
After:  [2, 1, 3, 2]

Before: [2, 3, 3, 3]
13 0 2 1
After:  [2, 4, 3, 3]

Before: [1, 3, 2, 3]
6 0 3 2
After:  [1, 3, 0, 3]

Before: [2, 2, 1, 1]
4 1 2 0
After:  [1, 2, 1, 1]

Before: [1, 0, 3, 3]
5 1 3 2
After:  [1, 0, 3, 3]

Before: [3, 3, 2, 1]
7 3 2 1
After:  [3, 3, 2, 1]

Before: [1, 0, 2, 2]
10 1 0 1
After:  [1, 1, 2, 2]

Before: [2, 1, 1, 3]
13 0 2 0
After:  [4, 1, 1, 3]

Before: [1, 1, 0, 0]
0 1 0 0
After:  [1, 1, 0, 0]

Before: [2, 2, 2, 0]
2 1 2 1
After:  [2, 1, 2, 0]

Before: [0, 1, 1, 0]
3 1 0 2
After:  [0, 1, 1, 0]

Before: [1, 1, 2, 2]
1 3 2 3
After:  [1, 1, 2, 4]

Before: [2, 2, 1, 2]
13 3 2 0
After:  [4, 2, 1, 2]

Before: [0, 1, 0, 0]
9 0 0 1
After:  [0, 0, 0, 0]

Before: [1, 3, 1, 1]
14 1 2 2
After:  [1, 3, 6, 1]

Before: [1, 3, 0, 3]
6 0 3 1
After:  [1, 0, 0, 3]

Before: [1, 2, 2, 2]
11 1 3 1
After:  [1, 1, 2, 2]

Before: [1, 2, 0, 1]
12 1 1 2
After:  [1, 2, 1, 1]

Before: [3, 3, 2, 2]
4 3 3 0
After:  [0, 3, 2, 2]

Before: [0, 0, 0, 2]
4 3 3 3
After:  [0, 0, 0, 0]

Before: [1, 1, 2, 0]
0 1 0 2
After:  [1, 1, 1, 0]

Before: [3, 0, 2, 1]
7 3 2 2
After:  [3, 0, 3, 1]

Before: [3, 1, 2, 1]
7 3 2 1
After:  [3, 3, 2, 1]

Before: [0, 0, 2, 2]
1 3 2 2
After:  [0, 0, 4, 2]

Before: [0, 1, 3, 1]
3 1 0 3
After:  [0, 1, 3, 1]

Before: [1, 3, 2, 2]
14 3 3 3
After:  [1, 3, 2, 6]

Before: [1, 3, 3, 0]
8 0 1 0
After:  [3, 3, 3, 0]

Before: [1, 3, 2, 3]
1 2 2 1
After:  [1, 4, 2, 3]

Before: [0, 1, 3, 2]
7 3 1 3
After:  [0, 1, 3, 3]

Before: [3, 3, 2, 2]
15 1 2 2
After:  [3, 3, 6, 2]

Before: [0, 3, 3, 1]
7 3 2 3
After:  [0, 3, 3, 3]

Before: [2, 3, 3, 3]
2 1 3 1
After:  [2, 1, 3, 3]

Before: [1, 1, 3, 1]
14 0 2 2
After:  [1, 1, 2, 1]

Before: [2, 1, 0, 3]
8 1 0 2
After:  [2, 1, 3, 3]

Before: [1, 2, 2, 0]
2 1 2 0
After:  [1, 2, 2, 0]

Before: [1, 0, 0, 0]
10 1 0 2
After:  [1, 0, 1, 0]

Before: [1, 3, 3, 3]
2 1 3 3
After:  [1, 3, 3, 1]

Before: [0, 2, 2, 1]
1 1 2 3
After:  [0, 2, 2, 4]

Before: [1, 2, 2, 3]
6 0 3 3
After:  [1, 2, 2, 0]

Before: [3, 2, 0, 2]
11 1 3 2
After:  [3, 2, 1, 2]

Before: [2, 2, 2, 2]
1 2 2 0
After:  [4, 2, 2, 2]

Before: [1, 0, 0, 1]
4 3 3 1
After:  [1, 0, 0, 1]

Before: [3, 1, 1, 2]
4 3 3 1
After:  [3, 0, 1, 2]

Before: [1, 1, 2, 3]
6 0 3 3
After:  [1, 1, 2, 0]

Before: [0, 3, 1, 3]
9 0 0 2
After:  [0, 3, 0, 3]

Before: [1, 3, 0, 0]
8 2 1 0
After:  [3, 3, 0, 0]

Before: [3, 2, 0, 2]
13 1 2 3
After:  [3, 2, 0, 4]

Before: [0, 0, 1, 2]
13 3 2 2
After:  [0, 0, 4, 2]

Before: [0, 2, 0, 2]
11 1 3 0
After:  [1, 2, 0, 2]

Before: [0, 3, 1, 3]
9 0 0 3
After:  [0, 3, 1, 0]

Before: [2, 2, 0, 2]
11 1 3 0
After:  [1, 2, 0, 2]

Before: [0, 3, 1, 2]
8 2 1 0
After:  [3, 3, 1, 2]

Before: [0, 3, 2, 2]
9 0 0 2
After:  [0, 3, 0, 2]

Before: [3, 2, 0, 2]
13 1 2 2
After:  [3, 2, 4, 2]

Before: [0, 3, 1, 1]
14 1 3 2
After:  [0, 3, 9, 1]

Before: [2, 0, 2, 0]
1 0 2 1
After:  [2, 4, 2, 0]

Before: [3, 2, 3, 2]
11 1 3 0
After:  [1, 2, 3, 2]

Before: [0, 0, 3, 1]
7 3 2 0
After:  [3, 0, 3, 1]

Before: [2, 2, 0, 2]
12 1 1 2
After:  [2, 2, 1, 2]

Before: [0, 3, 2, 1]
8 0 1 0
After:  [3, 3, 2, 1]

Before: [2, 0, 3, 1]
7 3 2 0
After:  [3, 0, 3, 1]

Before: [0, 0, 1, 2]
8 0 3 2
After:  [0, 0, 2, 2]

Before: [1, 1, 3, 0]
0 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 2, 0, 3]
4 1 0 1
After:  [1, 1, 0, 3]

Before: [1, 1, 2, 1]
0 1 0 0
After:  [1, 1, 2, 1]

Before: [2, 3, 2, 3]
6 0 3 3
After:  [2, 3, 2, 0]

Before: [2, 1, 3, 2]
7 3 1 3
After:  [2, 1, 3, 3]

Before: [1, 0, 0, 2]
4 3 3 2
After:  [1, 0, 0, 2]

Before: [0, 0, 1, 1]
4 2 3 2
After:  [0, 0, 0, 1]

Before: [1, 1, 0, 2]
0 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 1, 0, 2]
3 1 0 2
After:  [0, 1, 1, 2]

Before: [2, 2, 0, 1]
13 0 2 0
After:  [4, 2, 0, 1]

Before: [2, 2, 0, 3]
6 0 3 3
After:  [2, 2, 0, 0]

Before: [0, 2, 0, 2]
13 3 2 0
After:  [4, 2, 0, 2]

Before: [2, 2, 2, 2]
1 0 2 3
After:  [2, 2, 2, 4]

Before: [1, 2, 2, 3]
2 1 2 3
After:  [1, 2, 2, 1]

Before: [1, 2, 0, 0]
15 0 1 3
After:  [1, 2, 0, 2]

Before: [2, 2, 0, 2]
11 1 3 1
After:  [2, 1, 0, 2]

Before: [1, 0, 2, 3]
5 0 2 0
After:  [3, 0, 2, 3]

Before: [1, 0, 0, 1]
10 1 0 2
After:  [1, 0, 1, 1]

Before: [3, 1, 1, 1]
14 0 3 2
After:  [3, 1, 9, 1]

Before: [0, 1, 3, 3]
3 1 0 3
After:  [0, 1, 3, 1]

Before: [2, 1, 2, 2]
1 0 2 2
After:  [2, 1, 4, 2]

Before: [0, 2, 2, 1]
12 1 1 0
After:  [1, 2, 2, 1]

Before: [1, 2, 1, 2]
11 1 3 2
After:  [1, 2, 1, 2]

Before: [0, 1, 2, 2]
3 1 0 1
After:  [0, 1, 2, 2]

Before: [2, 2, 3, 2]
11 1 3 3
After:  [2, 2, 3, 1]

Before: [0, 2, 1, 2]
12 1 1 1
After:  [0, 1, 1, 2]

Before: [2, 1, 1, 3]
6 0 3 0
After:  [0, 1, 1, 3]

Before: [1, 2, 1, 3]
8 0 1 3
After:  [1, 2, 1, 3]

Before: [0, 3, 0, 2]
9 0 0 3
After:  [0, 3, 0, 0]

Before: [0, 2, 2, 2]
11 1 3 1
After:  [0, 1, 2, 2]

Before: [0, 1, 0, 2]
3 1 0 0
After:  [1, 1, 0, 2]

Before: [2, 0, 1, 2]
13 0 2 2
After:  [2, 0, 4, 2]

Before: [1, 0, 0, 2]
10 1 0 3
After:  [1, 0, 0, 1]

Before: [3, 1, 3, 2]
14 0 3 3
After:  [3, 1, 3, 9]

Before: [2, 2, 2, 3]
15 2 3 0
After:  [6, 2, 2, 3]

Before: [1, 0, 1, 0]
10 1 0 2
After:  [1, 0, 1, 0]

Before: [0, 2, 1, 0]
9 0 0 3
After:  [0, 2, 1, 0]

Before: [1, 2, 2, 2]
11 1 3 0
After:  [1, 2, 2, 2]

Before: [1, 2, 3, 1]
15 3 1 0
After:  [2, 2, 3, 1]

Before: [0, 0, 3, 1]
8 0 2 2
After:  [0, 0, 3, 1]

Before: [2, 0, 2, 1]
14 0 3 1
After:  [2, 6, 2, 1]

Before: [0, 0, 2, 3]
15 2 3 1
After:  [0, 6, 2, 3]

Before: [1, 2, 2, 0]
12 1 1 2
After:  [1, 2, 1, 0]

Before: [2, 2, 3, 0]
12 1 0 2
After:  [2, 2, 1, 0]

Before: [3, 2, 0, 2]
11 1 3 1
After:  [3, 1, 0, 2]

Before: [2, 2, 2, 3]
6 0 3 3
After:  [2, 2, 2, 0]

Before: [0, 1, 0, 0]
3 1 0 2
After:  [0, 1, 1, 0]

Before: [0, 1, 1, 3]
3 1 0 3
After:  [0, 1, 1, 1]

Before: [2, 0, 0, 3]
6 0 3 1
After:  [2, 0, 0, 3]

Before: [3, 1, 0, 0]
8 1 0 0
After:  [3, 1, 0, 0]

Before: [0, 1, 2, 1]
3 1 0 1
After:  [0, 1, 2, 1]

Before: [1, 0, 1, 0]
10 1 0 3
After:  [1, 0, 1, 1]

Before: [0, 0, 3, 1]
12 2 3 3
After:  [0, 0, 3, 0]

Before: [0, 1, 0, 1]
4 3 3 2
After:  [0, 1, 0, 1]

Before: [1, 0, 2, 1]
7 3 2 2
After:  [1, 0, 3, 1]

Before: [1, 1, 2, 2]
15 0 2 0
After:  [2, 1, 2, 2]

Before: [3, 3, 0, 3]
2 1 3 2
After:  [3, 3, 1, 3]

Before: [1, 0, 3, 3]
10 1 0 0
After:  [1, 0, 3, 3]

Before: [1, 3, 2, 1]
14 2 3 2
After:  [1, 3, 6, 1]

Before: [0, 1, 1, 1]
3 1 0 0
After:  [1, 1, 1, 1]

Before: [3, 3, 0, 1]
4 3 3 3
After:  [3, 3, 0, 0]

Before: [3, 3, 2, 1]
7 3 2 2
After:  [3, 3, 3, 1]

Before: [3, 2, 2, 1]
2 1 2 3
After:  [3, 2, 2, 1]

Before: [1, 1, 1, 3]
6 0 3 0
After:  [0, 1, 1, 3]

Before: [3, 0, 2, 3]
5 1 3 3
After:  [3, 0, 2, 3]

Before: [2, 2, 3, 3]
15 1 3 2
After:  [2, 2, 6, 3]

Before: [1, 2, 1, 2]
8 2 1 3
After:  [1, 2, 1, 3]

Before: [0, 2, 3, 1]
15 3 1 0
After:  [2, 2, 3, 1]

Before: [3, 3, 0, 3]
12 3 0 2
After:  [3, 3, 1, 3]

Before: [2, 2, 2, 2]
11 1 3 2
After:  [2, 2, 1, 2]

Before: [3, 0, 3, 0]
8 1 2 1
After:  [3, 3, 3, 0]

Before: [1, 1, 1, 2]
5 0 3 2
After:  [1, 1, 3, 2]

Before: [0, 3, 3, 2]
9 0 0 2
After:  [0, 3, 0, 2]

Before: [0, 3, 2, 1]
9 0 0 0
After:  [0, 3, 2, 1]

Before: [1, 3, 1, 3]
5 2 3 3
After:  [1, 3, 1, 3]

Before: [2, 1, 3, 3]
6 0 3 3
After:  [2, 1, 3, 0]

Before: [0, 1, 1, 0]
9 0 0 0
After:  [0, 1, 1, 0]

Before: [1, 0, 2, 3]
6 0 3 0
After:  [0, 0, 2, 3]

Before: [3, 3, 3, 1]
7 3 2 0
After:  [3, 3, 3, 1]

Before: [0, 1, 3, 0]
3 1 0 2
After:  [0, 1, 1, 0]

Before: [1, 2, 2, 2]
4 3 3 1
After:  [1, 0, 2, 2]

Before: [3, 2, 2, 2]
11 1 3 3
After:  [3, 2, 2, 1]

Before: [0, 1, 0, 2]
9 0 0 0
After:  [0, 1, 0, 2]

Before: [1, 0, 1, 3]
10 1 0 0
After:  [1, 0, 1, 3]

Before: [3, 3, 2, 3]
2 1 3 1
After:  [3, 1, 2, 3]

Before: [2, 3, 1, 0]
8 3 0 1
After:  [2, 2, 1, 0]

Before: [1, 1, 2, 1]
0 1 0 3
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 3]
15 3 2 1
After:  [3, 6, 2, 3]

Before: [0, 2, 1, 2]
4 1 2 3
After:  [0, 2, 1, 1]

Before: [2, 2, 1, 0]
13 1 2 1
After:  [2, 4, 1, 0]

Before: [1, 0, 3, 3]
10 1 0 1
After:  [1, 1, 3, 3]

Before: [3, 3, 2, 0]
1 2 2 2
After:  [3, 3, 4, 0]

Before: [1, 2, 1, 2]
11 1 3 0
After:  [1, 2, 1, 2]

Before: [1, 3, 1, 3]
6 0 3 3
After:  [1, 3, 1, 0]

Before: [3, 3, 1, 3]
8 2 1 1
After:  [3, 3, 1, 3]

Before: [1, 0, 0, 1]
4 3 3 0
After:  [0, 0, 0, 1]

Before: [1, 2, 2, 2]
11 1 3 3
After:  [1, 2, 2, 1]

Before: [3, 1, 2, 1]
8 1 0 0
After:  [3, 1, 2, 1]

Before: [3, 0, 1, 2]
8 1 3 3
After:  [3, 0, 1, 2]

Before: [1, 1, 3, 3]
0 1 0 3
After:  [1, 1, 3, 1]

Before: [0, 0, 1, 2]
13 3 2 1
After:  [0, 4, 1, 2]

Before: [2, 3, 0, 1]
13 0 2 0
After:  [4, 3, 0, 1]

Before: [1, 2, 2, 0]
2 1 2 1
After:  [1, 1, 2, 0]

Before: [2, 3, 1, 0]
13 0 2 2
After:  [2, 3, 4, 0]

Before: [0, 1, 2, 3]
3 1 0 3
After:  [0, 1, 2, 1]

Before: [2, 3, 2, 2]
15 1 3 1
After:  [2, 6, 2, 2]

Before: [0, 1, 2, 0]
3 1 0 3
After:  [0, 1, 2, 1]

Before: [1, 2, 2, 2]
15 0 2 2
After:  [1, 2, 2, 2]

Before: [1, 2, 2, 1]
12 1 1 2
After:  [1, 2, 1, 1]

Before: [0, 1, 1, 0]
3 1 0 0
After:  [1, 1, 1, 0]

Before: [3, 3, 0, 1]
14 0 3 1
After:  [3, 9, 0, 1]

Before: [1, 0, 2, 1]
10 1 0 2
After:  [1, 0, 1, 1]

Before: [0, 3, 2, 3]
9 0 0 2
After:  [0, 3, 0, 3]

Before: [0, 2, 1, 2]
11 1 3 3
After:  [0, 2, 1, 1]

Before: [2, 0, 1, 3]
6 0 3 1
After:  [2, 0, 1, 3]

Before: [1, 1, 2, 3]
0 1 0 3
After:  [1, 1, 2, 1]

Before: [3, 0, 2, 2]
1 2 2 1
After:  [3, 4, 2, 2]

Before: [1, 3, 2, 0]
5 3 2 3
After:  [1, 3, 2, 2]

Before: [3, 3, 0, 3]
8 2 0 1
After:  [3, 3, 0, 3]

Before: [0, 0, 3, 3]
9 0 0 3
After:  [0, 0, 3, 0]

Before: [0, 3, 1, 3]
8 2 1 3
After:  [0, 3, 1, 3]

Before: [1, 1, 3, 2]
0 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 0, 0, 3]
10 1 0 2
After:  [1, 0, 1, 3]

Before: [2, 0, 1, 2]
13 3 2 3
After:  [2, 0, 1, 4]

Before: [3, 2, 3, 2]
13 1 2 0
After:  [4, 2, 3, 2]

Before: [0, 1, 0, 2]
3 1 0 3
After:  [0, 1, 0, 1]

Before: [1, 1, 3, 1]
0 1 0 0
After:  [1, 1, 3, 1]

Before: [0, 1, 3, 0]
3 1 0 0
After:  [1, 1, 3, 0]

Before: [0, 1, 0, 1]
3 1 0 1
After:  [0, 1, 0, 1]

Before: [3, 2, 1, 2]
4 1 2 2
After:  [3, 2, 1, 2]

Before: [1, 1, 2, 3]
0 1 0 0
After:  [1, 1, 2, 3]

Before: [3, 2, 3, 2]
11 1 3 2
After:  [3, 2, 1, 2]

Before: [0, 1, 3, 1]
3 1 0 1
After:  [0, 1, 3, 1]

Before: [1, 1, 2, 0]
0 1 0 3
After:  [1, 1, 2, 1]

Before: [0, 1, 3, 0]
9 0 0 3
After:  [0, 1, 3, 0]

Before: [2, 2, 3, 1]
14 2 3 2
After:  [2, 2, 9, 1]

Before: [0, 1, 0, 1]
3 1 0 2
After:  [0, 1, 1, 1]

Before: [3, 3, 3, 3]
15 0 3 3
After:  [3, 3, 3, 9]

Before: [2, 1, 2, 3]
6 0 3 0
After:  [0, 1, 2, 3]

Before: [0, 2, 1, 2]
8 0 3 1
After:  [0, 2, 1, 2]

Before: [0, 2, 2, 1]
2 1 2 1
After:  [0, 1, 2, 1]

Before: [1, 0, 1, 2]
10 1 0 0
After:  [1, 0, 1, 2]

Before: [1, 2, 3, 3]
15 1 3 3
After:  [1, 2, 3, 6]

Before: [2, 1, 2, 3]
15 1 2 3
After:  [2, 1, 2, 2]

Before: [1, 2, 2, 1]
14 1 3 3
After:  [1, 2, 2, 6]

Before: [1, 1, 1, 0]
0 1 0 1
After:  [1, 1, 1, 0]

Before: [3, 2, 3, 1]
4 3 3 0
After:  [0, 2, 3, 1]

Before: [0, 2, 2, 2]
11 1 3 2
After:  [0, 2, 1, 2]

Before: [2, 1, 3, 1]
14 3 2 3
After:  [2, 1, 3, 2]

Before: [0, 2, 2, 3]
2 1 2 0
After:  [1, 2, 2, 3]

Before: [0, 1, 3, 3]
5 0 3 2
After:  [0, 1, 3, 3]

Before: [0, 3, 2, 2]
15 1 2 0
After:  [6, 3, 2, 2]

Before: [2, 2, 1, 2]
14 3 3 1
After:  [2, 6, 1, 2]

Before: [2, 2, 2, 2]
11 1 3 1
After:  [2, 1, 2, 2]

Before: [3, 2, 2, 2]
11 1 3 0
After:  [1, 2, 2, 2]

Before: [1, 3, 2, 1]
15 0 2 0
After:  [2, 3, 2, 1]

Before: [1, 2, 0, 0]
15 0 1 2
After:  [1, 2, 2, 0]

Before: [1, 2, 2, 3]
1 1 2 1
After:  [1, 4, 2, 3]

Before: [3, 2, 2, 1]
7 3 2 0
After:  [3, 2, 2, 1]

Before: [3, 2, 2, 0]
12 1 1 2
After:  [3, 2, 1, 0]

Before: [1, 0, 3, 3]
6 0 3 1
After:  [1, 0, 3, 3]

Before: [2, 0, 2, 1]
1 0 2 3
After:  [2, 0, 2, 4]

Before: [2, 0, 1, 2]
13 0 2 0
After:  [4, 0, 1, 2]

Before: [2, 2, 2, 2]
12 2 1 0
After:  [1, 2, 2, 2]

Before: [2, 2, 0, 2]
13 3 2 1
After:  [2, 4, 0, 2]

Before: [3, 3, 3, 0]
14 2 3 1
After:  [3, 9, 3, 0]

Before: [3, 1, 0, 2]
4 3 3 3
After:  [3, 1, 0, 0]

Before: [0, 2, 2, 3]
1 1 2 0
After:  [4, 2, 2, 3]

Before: [0, 1, 1, 2]
9 0 0 1
After:  [0, 0, 1, 2]

Before: [3, 3, 1, 0]
14 1 3 2
After:  [3, 3, 9, 0]

Before: [2, 0, 2, 3]
5 1 2 2
After:  [2, 0, 2, 3]

Before: [1, 1, 1, 2]
0 1 0 0
After:  [1, 1, 1, 2]

Before: [3, 2, 3, 3]
15 1 3 0
After:  [6, 2, 3, 3]

Before: [1, 3, 2, 1]
14 1 3 0
After:  [9, 3, 2, 1]

Before: [2, 0, 2, 2]
1 2 2 0
After:  [4, 0, 2, 2]

Before: [0, 2, 1, 2]
11 1 3 0
After:  [1, 2, 1, 2]

Before: [0, 1, 1, 1]
3 1 0 3
After:  [0, 1, 1, 1]

Before: [1, 0, 1, 0]
10 1 0 1
After:  [1, 1, 1, 0]

Before: [1, 1, 1, 1]
4 3 3 3
After:  [1, 1, 1, 0]

Before: [3, 2, 2, 2]
14 0 3 3
After:  [3, 2, 2, 9]

Before: [0, 1, 2, 1]
9 0 0 0
After:  [0, 1, 2, 1]

Before: [2, 0, 2, 3]
1 2 2 0
After:  [4, 0, 2, 3]

Before: [1, 1, 1, 3]
0 1 0 3
After:  [1, 1, 1, 1]

Before: [0, 1, 0, 3]
3 1 0 1
After:  [0, 1, 0, 3]

Before: [2, 0, 2, 1]
5 1 2 0
After:  [2, 0, 2, 1]

Before: [1, 3, 3, 1]
14 0 2 0
After:  [2, 3, 3, 1]

Before: [1, 0, 0, 3]
6 0 3 1
After:  [1, 0, 0, 3]

Before: [2, 3, 0, 3]
6 0 3 3
After:  [2, 3, 0, 0]

Before: [0, 1, 2, 2]
1 3 2 3
After:  [0, 1, 2, 4]

Before: [3, 1, 2, 3]
1 2 2 2
After:  [3, 1, 4, 3]

Before: [3, 1, 0, 3]
8 2 0 3
After:  [3, 1, 0, 3]

Before: [3, 3, 1, 2]
14 0 3 3
After:  [3, 3, 1, 9]

Before: [3, 0, 3, 2]
4 3 3 3
After:  [3, 0, 3, 0]

Before: [2, 3, 1, 0]
8 2 1 0
After:  [3, 3, 1, 0]

Before: [0, 1, 2, 1]
3 1 0 2
After:  [0, 1, 1, 1]

Before: [0, 1, 3, 2]
3 1 0 0
After:  [1, 1, 3, 2]

Before: [1, 1, 2, 0]
15 0 2 1
After:  [1, 2, 2, 0]

Before: [0, 3, 2, 2]
1 3 2 0
After:  [4, 3, 2, 2]

Before: [1, 0, 1, 2]
10 1 0 3
After:  [1, 0, 1, 1]

Before: [0, 2, 2, 0]
12 1 1 0
After:  [1, 2, 2, 0]

Before: [1, 1, 3, 3]
0 1 0 1
After:  [1, 1, 3, 3]

Before: [1, 0, 2, 0]
10 1 0 2
After:  [1, 0, 1, 0]

Before: [2, 3, 2, 1]
15 1 2 1
After:  [2, 6, 2, 1]

Before: [1, 2, 0, 0]
8 1 0 1
After:  [1, 3, 0, 0]

Before: [3, 2, 1, 2]
11 1 3 3
After:  [3, 2, 1, 1]

Before: [1, 1, 1, 1]
0 1 0 3
After:  [1, 1, 1, 1]

Before: [2, 3, 1, 3]
6 0 3 3
After:  [2, 3, 1, 0]

Before: [0, 2, 1, 3]
13 1 2 2
After:  [0, 2, 4, 3]

Before: [1, 0, 3, 1]
7 3 2 3
After:  [1, 0, 3, 3]

Before: [2, 1, 0, 0]
8 3 0 3
After:  [2, 1, 0, 2]

Before: [1, 1, 1, 2]
0 1 0 2
After:  [1, 1, 1, 2]

Before: [3, 2, 2, 2]
1 3 2 3
After:  [3, 2, 2, 4]

Before: [3, 1, 1, 1]
14 0 3 3
After:  [3, 1, 1, 9]

Before: [2, 2, 3, 3]
6 0 3 0
After:  [0, 2, 3, 3]

Before: [0, 1, 1, 2]
3 1 0 2
After:  [0, 1, 1, 2]

Before: [3, 2, 1, 2]
14 0 3 0
After:  [9, 2, 1, 2]

Before: [2, 0, 3, 1]
7 3 2 3
After:  [2, 0, 3, 3]

Before: [1, 2, 2, 1]
2 1 2 0
After:  [1, 2, 2, 1]

Before: [0, 0, 2, 1]
4 3 3 3
After:  [0, 0, 2, 0]

Before: [3, 2, 3, 3]
12 3 0 3
After:  [3, 2, 3, 1]

Before: [1, 1, 2, 2]
0 1 0 3
After:  [1, 1, 2, 1]

Before: [2, 3, 1, 1]
14 1 3 2
After:  [2, 3, 9, 1]

Before: [1, 0, 2, 1]
15 0 2 1
After:  [1, 2, 2, 1]

Before: [0, 1, 2, 3]
9 0 0 3
After:  [0, 1, 2, 0]

Before: [3, 0, 0, 2]
4 3 3 0
After:  [0, 0, 0, 2]

Before: [3, 0, 3, 1]
7 3 2 3
After:  [3, 0, 3, 3]

Before: [3, 2, 2, 3]
12 2 1 1
After:  [3, 1, 2, 3]

Before: [0, 3, 3, 3]
2 1 3 1
After:  [0, 1, 3, 3]

Before: [1, 0, 0, 0]
10 1 0 1
After:  [1, 1, 0, 0]

Before: [1, 3, 0, 3]
2 1 3 3
After:  [1, 3, 0, 1]

Before: [3, 2, 2, 3]
12 3 0 2
After:  [3, 2, 1, 3]

Before: [1, 1, 2, 0]
0 1 0 0
After:  [1, 1, 2, 0]

Before: [0, 2, 2, 1]
2 1 2 2
After:  [0, 2, 1, 1]

Before: [1, 0, 1, 2]
10 1 0 2
After:  [1, 0, 1, 2]

Before: [1, 0, 3, 0]
14 0 2 2
After:  [1, 0, 2, 0]

Before: [0, 2, 3, 2]
11 1 3 3
After:  [0, 2, 3, 1]

Before: [0, 1, 0, 3]
3 1 0 2
After:  [0, 1, 1, 3]

Before: [3, 3, 2, 1]
12 1 0 0
After:  [1, 3, 2, 1]

Before: [0, 2, 3, 3]
13 1 2 0
After:  [4, 2, 3, 3]

Before: [1, 1, 3, 0]
0 1 0 1
After:  [1, 1, 3, 0]

Before: [1, 2, 2, 2]
2 1 2 2
After:  [1, 2, 1, 2]

Before: [2, 1, 3, 3]
13 0 2 2
After:  [2, 1, 4, 3]

Before: [1, 0, 1, 3]
10 1 0 3
After:  [1, 0, 1, 1]

Before: [2, 1, 3, 2]
7 3 1 1
After:  [2, 3, 3, 2]

Before: [1, 1, 1, 0]
0 1 0 0
After:  [1, 1, 1, 0]

Before: [0, 2, 3, 2]
13 3 2 3
After:  [0, 2, 3, 4]

Before: [3, 2, 2, 3]
12 3 0 3
After:  [3, 2, 2, 1]

Before: [2, 3, 2, 3]
2 1 3 1
After:  [2, 1, 2, 3]

Before: [2, 3, 0, 3]
6 0 3 1
After:  [2, 0, 0, 3]

Before: [2, 2, 2, 3]
1 2 2 0
After:  [4, 2, 2, 3]

Before: [3, 2, 3, 2]
4 3 3 1
After:  [3, 0, 3, 2]

Before: [0, 2, 2, 0]
12 1 1 1
After:  [0, 1, 2, 0]

Before: [2, 2, 3, 2]
11 1 3 2
After:  [2, 2, 1, 2]

Before: [3, 0, 2, 3]
1 2 2 2
After:  [3, 0, 4, 3]

Before: [0, 3, 2, 0]
9 0 0 0
After:  [0, 3, 2, 0]

Before: [0, 2, 3, 1]
9 0 0 2
After:  [0, 2, 0, 1]

Before: [0, 1, 1, 1]
3 1 0 2
After:  [0, 1, 1, 1]

Before: [2, 2, 2, 3]
2 1 2 0
After:  [1, 2, 2, 3]

Before: [0, 1, 2, 3]
15 3 2 0
After:  [6, 1, 2, 3]

Before: [1, 1, 0, 2]
7 3 1 3
After:  [1, 1, 0, 3]

Before: [1, 1, 1, 1]
0 1 0 0
After:  [1, 1, 1, 1]

Before: [1, 2, 3, 3]
15 0 1 3
After:  [1, 2, 3, 2]

Before: [0, 3, 2, 3]
2 1 3 1
After:  [0, 1, 2, 3]

Before: [0, 3, 0, 0]
8 2 1 3
After:  [0, 3, 0, 3]

Before: [2, 0, 2, 3]
1 0 2 0
After:  [4, 0, 2, 3]

Before: [0, 3, 0, 3]
5 0 3 3
After:  [0, 3, 0, 3]

Before: [0, 1, 2, 0]
3 1 0 0
After:  [1, 1, 2, 0]""".strip().split('\n')

import re

def get_digits(line):
    digits = [int(match[0]) for match in re.finditer(r'\d+',line)]
    return digits

def build_lists(data):
    bef_list = []
    codes = []
    after_list = []
    
    for i in range(len(data)):
        if data[i].startswith("B"):
            bef_list.append(get_digits(data[i]))
        elif data[i].startswith("A"):
            after_list.append(get_digits(data[i]))
        elif data[i] is "":
            continue
        else:
            codes.append(get_digits(data[i]))
    return bef_list, codes, after_list

def addr__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] + before[integer][code_2] == after[integer][code_3]):
        return True

def addi__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] + code_2 == after[integer][code_3]):
        return True

def mulr__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] * before[integer][code_2] == after[integer][code_3]):
        return True

def muli__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] * code_2 == after[integer][code_3]):
        return True

def banr__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] & before[integer][code_2] == after[integer][code_3]):
        return True

def bani__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] & code_2 == after[integer][code_3]):
        return True

def borr__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] | before[integer][code_2] == after[integer][code_3]):
        return True

def bori__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] | code_2 == after[integer][code_3]):
        return True

def setr__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if (before[integer][code_1] == after[integer][code_3]):
        return True

def seti__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if code_1 == after[integer][code_3]:
        return True
    
def gtir__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (code_1 > before[integer][code_2])) or (after[integer][code_3] == 0):
        return True

def gtri__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (before[integer][code_1] > code_2)) or (after[integer][code_3] == 0):
        return True

def gtrr_(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (before[integer][code_1] > before[integer][code_2])) or (after[integer][code_3] == 0):
        return True

def eqir__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (code_1 == before[integer][code_2])) or (after[integer][code_3] == 0):
        return True

def eqri__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (before[integer][code_1] == code_2)) or (after[integer][code_3] == 0):
        return True

def eqrr__(before,codes,after,integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (before[integer][code_1] == before[integer][code_2])) or (after[integer][code_3] == 0):
        return True

def main(data):
    before, codes, after = build_lists(data)
    count = 0
    functions = [addr__,addi__,mulr__,muli__,banr__,bani__,borr__,bori__,setr__,seti__,gtir__,gtri__,gtrr_, \
                eqir__,eqri__,eqrr__]
    
    for i in range(len(before)):
        num_func = [x for x in functions if x(before,codes,after,i) == True]
        if len(num_func) >= 3:
            count += 1
    
    print(count) 
    
def part_2_setup(data):
    before, codes, after = build_lists(data)
    func_dict = {}
    functions = [addr__,addi__,mulr__,muli__,banr__,bani__,borr__,bori__,setr__,seti__,gtir__,gtri__,gtrr_, \
                eqir__,eqri__,eqrr__]
    
    for i in range(len(before)):
        num_func = []
        for f,x in enumerate(functions):
            if (x(before,codes,after,i) == True) and (x not in func_dict.values()):
                num_func.append((f,x))
        if len(num_func) == 1:
            func_dict[codes[i][0]] = num_func[0][1]
    return func_dict

main(file)
part_2_setup(file)
