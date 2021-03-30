# # import pygame
# # from time import sleep
#
# i = 0
# j = 0
# size = 3
# board = []
# result = -1
#
# for k in range(3):
#     board.append([])
#     for h in range(3):
#         board[k].append(int(input()))
#
# print(board)
# # 检查行
# while (result == -1) and (i < size):
#     numOfx, numOfo = 0, 0
#     j = 0
#     while j < size:
#         if board[i][j] == 1:
#             numOfx += 1
#         elif board[i][j] == 0:
#             numOfo += 1
#         if numOfo == size:
#             result = 0
#         elif numOfx == size:
#             result = 1
#         j += 1
#     i += 1
#
# # 检查列
# if result == -1:
#     i, j = 0, 0
#     while j < size and result == -1:
#         numOfx = numOfo = 0
#         i = 0
#         while i < size:
#             if board[i][j] == 1:
#                 numOfx += 1
#             elif board[i][j] == 0:
#                 numOfo += 1
#             if numOfo == size:
#                 result = 0
#             elif numOfx == size:
#                 result = 1
#             i += 1
#         j += 1
#
# # 检查正对角线
# if result == -1:
#     numOfo = numOfx = 0
#     i, j = 0, 0
#     while i < size:
#         if board[i][i] == 1:
#             numOfx += 1
#         elif board[i][i] == 0:
#             numOfo += 1
#         if numOfo == size:
#             result = 0
#         elif numOfx == size:
#             result = 1
#         i += 1
#
# # 检查斜对角线
# if result == -1:
#     numOfo = numOfx = 0
#     i, j = 0, 0
#     while i < size:
#         if board[i][size-i-1] == 1:
#             numOfx += 1
#         elif board[i][size-i-1] == 0:
#             numOfo += 1
#         if numOfo == size:
#             result = 0
#         elif numOfx == size:
#             result = 1
#         i += 1
#
# print("赢家：", result)
