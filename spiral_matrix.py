'''
给你一个m行n列的矩阵matrix，请按照顺时针螺旋顺序，返回矩阵中的所有元素。
示例 1：输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]输出：[1,2,3,6,9,8,7,4,5]
示例 2：输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''

import numpy as np

def drive_pts(mat,start_pts, end_pts,flag):
    global num
    print("="*20)
    # print(start_pts)
    # print(end_pts)
    if flag == 0:
        # 右
        row_idx = start_pts[0]
        start_col_idx = start_pts[1]
        end_col_idx = end_pts[1]
        for j in range(start_col_idx, end_col_idx+1):
            # print(str(row_idx) +", " +  str(j) )
            print(mat[row_idx, j])
            num += 1

    elif flag == 1:
        # 下
        col_idx = start_pts[1]
        start_row_idx = start_pts[0]
        end_row_idx = end_pts[0]
        for i in range(start_row_idx,end_row_idx+1):
            # print(str(i) +", " +  str(col_idx))
            print(mat[i,col_idx])
            num += 1

    elif flag ==2:
        # 左
        row_idx = start_pts[0]
        start_col_idx = start_pts[1]
        end_col_idx = end_pts[1]
        for j in range(start_col_idx, end_col_idx-1, -1):
            # print(str(row_idx) +", " +  str(j))
            print(mat[row_idx,j])
            num += 1

    elif flag ==3:
        # 上
        col_idx = start_pts[1]
        start_row_idx = start_pts[0]
        end_row_idx = end_pts[0]
        for i in range(start_row_idx, end_row_idx-1, -1):
            # print(str(i) +", " + str(col_idx))
            print(mat[i,col_idx])
            num += 1

# matrix = np.mat([[1,2,3],[4,5,6],[7,8,9]])
matrix = np.mat([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(matrix)
row, col = matrix.shape

num = 0

turns = 0
row_footsteps = [i for i in range(row)]
col_footsteps = [i for i in range(col)]

while num < row * col:
    flag = turns % 4
    if flag == 0 :
        walk_row = row_footsteps.pop(0)
        start_pts = [walk_row,col_footsteps[0]]
        end_pts = [walk_row,col_footsteps[-1]]
    elif flag == 1 :
        walk_col = col_footsteps.pop(-1)
        start_pts = [row_footsteps[0], walk_col]
        end_pts = [row_footsteps[-1], walk_col]
    elif flag == 2:
        walk_row = row_footsteps.pop(-1)
        start_pts = [walk_row, col_footsteps[-1]]
        end_pts = [walk_row, col_footsteps[0]]
    elif flag == 3:
        walk_col = col_footsteps.pop(0)
        start_pts = [row_footsteps[-1], walk_col]
        end_pts = [row_footsteps[0], walk_col]

    # print(start_pts)
    # print(end_pts)
    # print(flag)
    drive_pts(matrix, start_pts, end_pts, flag)
    turns += 1


