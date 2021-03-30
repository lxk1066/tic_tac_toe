# # 判断结果
# def compute():
#     i = 0
#     result = -1
#     # 检查行
#     while (result == -1) and (i < size):
#         num_of_x, num_of_o = 0, 0
#         j = 0
#         while j < size:
#             if board[i][j] == 1:
#                 num_of_x += 1
#             elif board[i][j] == 0:
#                 num_of_o += 1
#             if num_of_o == size:
#                 result = 0
#             elif num_of_x == size:
#                 result = 1
#             j += 1
#         i += 1
#     # 检查列
#     if result == -1:
#         i, j = 0, 0
#         while j < size and result == -1:
#             num_of_x = num_of_o = 0
#             i = 0
#             while i < size:
#                 if board[i][j] == 1:
#                     num_of_x += 1
#                 elif board[i][j] == 0:
#                     num_of_o += 1
#                 if num_of_o == size:
#                     result = 0
#                 elif num_of_x == size:
#                     result = 1
#                 i += 1
#             j += 1
#     # 检查正对角线
#     if result == -1:
#         num_of_o = num_of_x = 0
#         i, j = 0, 0
#         while i < size:
#             if board[i][i] == 1:
#                 num_of_x += 1
#             elif board[i][i] == 0:
#                 num_of_o += 1
#             if num_of_o == size:
#                 result = 0
#             elif num_of_x == size:
#                 result = 1
#             i += 1
#     # 检查斜对角线
#     if result == -1:
#         num_of_o = num_of_x = 0
#         i, j = 0, 0
#         while i < size:
#             if board[i][size-i-1] == 1:
#                 num_of_x += 1
#             elif board[i][size-i-1] == 0:
#                 num_of_o += 1
#             if num_of_o == size:
#                 result = 0
#             elif num_of_x == size:
#                 result = 1
#             i += 1
#     return result
#
# # 主程序
# size = 3
# board = []
# for k in range(3):
#     board.append([])
#     for h in range(3):
#         board[k].append(int(input()))
# print(board)
# print(compute())
