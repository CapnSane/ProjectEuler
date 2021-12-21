'''
Problem 18



By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

Obs.: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


'''

# n0 = [75]
# n1 = [95, 64]
# n2 = [17, 47, 82]
# n3 = [18, 35, 87, 10]
# n4 = [20, 4, 82, 47, 65]
# n5 = [19, 1, 23, 75, 3, 34]
# n6 = [88, 2, 77, 73, 7, 63, 67]
# n7 = [99, 65, 4, 28, 6, 16, 70, 92]
# n8 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
# n9 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
# n10= [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
# n11= [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
# n12= [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
# n13= [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
# n14= [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

# n = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14]


n0 = [3]
n1 = [7, 4]
n2 = [2, 4, 6]
n3 = [8, 5, 9, 3]

n = [n0, n1, n2, n3]

accum = []

for i in range(len(n)):
  for j in range(0,i+1):
    accum.append(n[i][j])
    # print(f"for i = {i}\n for j = {j}\n n[{i}][{j}] = {n[i][j]}")
x = []
# for i in range(len(accum)):
  # if (accum[i] + accum[i+1]) > (accum[i] + accum[i+2]):
  #   x.append(i+1)
  # else:
  #   x.append(i+2)

print(accum)
