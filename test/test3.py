# import pygame
# from tkinter import *
# from tkinter.messagebox import *
# Tk().wm_withdraw()
#
# showinfo("提示", "游戏仅支持单机，左击为先手，右击为后手！")
# while True:
#     # 判断结果
#     def compute():
#         i = 0
#         result = -1
#         # 检查行
#         while (result == -1) and (i < size):
#             num_of_x, num_of_o = 0, 0
#             j = 0
#             while j < size:
#                 if board[i][j] == 1:
#                     num_of_x += 1
#                 elif board[i][j] == 0:
#                     num_of_o += 1
#                 if num_of_o == size:
#                     result = 0
#                 elif num_of_x == size:
#                     result = 1
#                 j += 1
#             i += 1
#         # 检查列
#         if result == -1:
#             i, j = 0, 0
#             while j < size and result == -1:
#                 num_of_x = num_of_o = 0
#                 i = 0
#                 while i < size:
#                     if board[i][j] == 1:
#                         num_of_x += 1
#                     elif board[i][j] == 0:
#                         num_of_o += 1
#                     if num_of_o == size:
#                         result = 0
#                     elif num_of_x == size:
#                         result = 1
#                     i += 1
#                 j += 1
#         # 检查正对角线
#         if result == -1:
#             num_of_o = num_of_x = 0
#             i, j = 0, 0
#             while i < size:
#                 if board[i][i] == 1:
#                     num_of_x += 1
#                 elif board[i][i] == 0:
#                     num_of_o += 1
#                 if num_of_o == size:
#                     result = 0
#                 elif num_of_x == size:
#                     result = 1
#                 i += 1
#         # 检查斜对角线
#         if result == -1:
#             num_of_o = num_of_x = 0
#             i, j = 0, 0
#             while i < size:
#                 if board[i][size-i-1] == 1:
#                     num_of_x += 1
#                 elif board[i][size-i-1] == 0:
#                     num_of_o += 1
#                 if num_of_o == size:
#                     result = 0
#                 elif num_of_x == size:
#                     result = 1
#                 i += 1
#         return result
#
#     # 画图
#     def paint_tick_one():
#         pygame.draw.lines(screen, black, False, [(43, 92), (87, 147), (87, 147), (169, 75)], 3)
#
#
#     def paint_fork_one():
#         pygame.draw.line(screen, black, [60, 60], [140, 140], 3)
#         pygame.draw.line(screen, black, [140, 60], [60, 140], 3)
#
#
#     def paint_tick_two():
#         pygame.draw.lines(screen, white, False, [(242, 92), (279, 142), (279, 142), (353, 82)], 3)
#
#
#     def paint_fork_two():
#         pygame.draw.line(screen, white, [260, 60], [340, 140], 3)
#         pygame.draw.line(screen, white, [340, 60], [260, 140], 3)
#
#
#     def paint_tick_three():
#         pygame.draw.lines(screen, black, False, [(433, 87), (482, 147), (482, 147), (555, 75)], 3)
#
#
#     def paint_fork_three():
#         pygame.draw.line(screen, black, [460, 60], [540, 140], 3)
#         pygame.draw.line(screen, black, [540, 60], [460, 140], 3)
#
#
#     def paint_tick_four():
#         pygame.draw.lines(screen, white, False, [(43, 299), (87, 350), (87, 350), (169, 281)], 3)
#
#
#     def paint_fork_four():
#         pygame.draw.line(screen, white, [60, 260], [140, 340], 3)
#         pygame.draw.line(screen, white, [140, 260], [60, 340], 3)
#
#
#     def paint_tick_five():
#         pygame.draw.lines(screen, black, False, [(242, 299), (279, 350), (279, 350), (353, 281)], 3)
#
#
#     def paint_fork_five():
#         pygame.draw.line(screen, black, [260, 260], [340, 340], 3)
#         pygame.draw.line(screen, black, [340, 260], [260, 340], 3)
#
#     def paint_tick_six():
#         pygame.draw.lines(screen, white, False, [(433, 299), (482, 350), (482, 350), (555, 281)], 3)
#
#
#     def paint_fork_six():
#         pygame.draw.line(screen, white, [460, 260], [540, 340], 3)
#         pygame.draw.line(screen, white, [540, 260], [460, 340], 3)
#
#
#     def paint_tick_seven():
#         pygame.draw.lines(screen, black, False, [(43, 495), (87, 549), (87, 549), (169, 480)], 3)
#
#
#     def paint_fork_seven():
#         pygame.draw.line(screen, black, [60, 460], [140, 540], 3)
#         pygame.draw.line(screen, black, [140, 460], [60, 540], 3)
#
#
#     def paint_tick_eight():
#         pygame.draw.lines(screen, white, False, [(242, 495), (279, 549), (279, 549), (353, 480)], 3)
#
#
#     def paint_fork_eight():
#         pygame.draw.line(screen, white, [260, 460], [340, 540], 3)
#         pygame.draw.line(screen, white, [340, 460], [260, 540], 3)
#
#
#     def paint_tick_nine():
#         pygame.draw.lines(screen, black, False, [(433, 495), (482, 549), (482, 549), (555, 480)], 3)
#
#
#     def paint_fork_nine():
#         pygame.draw.line(screen, black, [460, 460], [540, 540], 3)
#         pygame.draw.line(screen, black, [540, 460], [460, 540], 3)
#
#
#     # 刷新背景
#     def background():
#         screen.fill([0, 0, 255])
#         pygame.draw.rect(screen, white, [0, 0, 200, 200], 0)
#         pygame.draw.rect(screen, black, [200, 0, 200, 200], 0)
#         pygame.draw.rect(screen, white, [400, 0, 200, 200], 0)
#         pygame.draw.rect(screen, black, [0, 200, 200, 200], 0)
#         pygame.draw.rect(screen, white, [200, 200, 200, 200], 0)
#         pygame.draw.rect(screen, black, [400, 200, 200, 200], 0)
#         pygame.draw.rect(screen, white, [0, 400, 200, 200], 0)
#         pygame.draw.rect(screen, black, [200, 400, 200, 200], 0)
#         pygame.draw.rect(screen, white, [400, 400, 200, 200], 0)
#         pygame.display.update()
#
#
#     # 主程序
#     size = 3
#     n = 0
#     board = []
#     for k in range(3):
#         board.append([])
#         for h in range(3):
#             board[k].append(-1)
#
#     white = [255, 255, 255]
#     black = [0, 0, 0]
#     # count表示用奇偶数的方法区分先后手
#     count = 0
#     pygame.display.init()
#     screen = pygame.display.set_mode([1000, 600])
#     pygame.display.set_caption("MyPygame")
#     # 刷新背景
#     background()
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x = event.pos[0]                         # 鼠标的x坐标
#                 y = event.pos[1]                         # 鼠标的y坐标
#                 print(event.button)
#
#                 if (x >= 1 and x <= 199) and (y >= 1 and y <= 199) and board[0][0] == -1:   # 第一格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_one()
#                         board[0][0] = 1
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_one()
#                         board[0][0] = 0
#                         pygame.display.update()
#                         count += 1
#                 elif (x >= 201 and x <= 399) and (y >= 1 and y <= 199) and board[0][1] == -1:   # 第二格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_two()
#                         board[0][1] = 1
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_two()
#                         board[0][1] = 0
#                         pygame.display.update()
#                         count += 1
#                 elif (x >= 401 and x <= 599) and (y >= 1 and y <= 199) and board[0][2] == -1:   # 第三格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_three()
#                         board[0][2] = 1
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_three()
#                         board[0][2] = 0
#                         pygame.display.update()
#                         count += 1
#                 elif (x >= 1 and x <= 199) and (y >= 201 and y <= 399) and board[1][0] == -1:   # 第四格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_four()
#                         board[1][0] = 1
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_four()
#                         board[1][0] = 0
#                         pygame.display.update()
#                         count += 1
#                 elif (x >= 201 and x <= 399) and (y >= 201 and y <= 399) and board[1][1] == -1:   # 第五格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_five()
#                         board[1][1] = 1
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_five()
#                         board[1][1] = 0
#                         pygame.display.update()
#                         count += 1
#                 elif (x >= 401 and x <= 599) and (y >= 201 and y <= 399) and board[1][2] == -1:   # 第六格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_six()
#                         board[1][2] = 1
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_six()
#                         board[1][2] = 0
#                         pygame.display.update()
#                         count += 1
#                 elif (x >= 1 and x <= 199) and (y >= 401 and y <= 599) and board[2][0] == -1:   # 第七格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_seven()
#                         board[2][0] = 1
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_seven()
#                         board[2][0] = 0
#                         pygame.display.update()
#                         count += 1
#                 elif (x >= 201 and x <= 399) and (y >= 401 and y <= 599) and board[2][1] == -1:   # 第八格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_eight()
#                         board[2][1] = 1
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_eight()
#                         board[2][1] = 0
#                         pygame.display.update()
#                         count += 1
#                 elif (x >= 401 and x <= 599) and (y >= 401 and y <= 599) and board[2][2] == -1:   # 第九格
#                     if event.button == 1 and count % 2 == 0:
#                         paint_tick_nine()
#                         board[2][2] = 1     # 写入数组
#                         pygame.display.update()
#                         count += 1
#                     elif event.button == 3 and count % 2 == 1:
#                         paint_fork_nine()
#                         board[2][2] = 0
#                         pygame.display.update()
#                         count += 1
#                 if compute() == 1:
#                     showinfo("提示", "X WIN!")
#                     n = 2
#                     if askyesno("提示", "是否要重新开始？"):
#                         n = 1
#                 elif compute() == 0:
#                     showinfo("提示", "O WIN!")
#                     n = 2
#                     if askyesno("提示", "是否要重新开始？"):
#                         n = 1
#                 elif count >= 9 and compute() == -1:
#                     if askyesno("提示", "平局！是否要重新开始？"):
#                         n = 1
#                     else:
#                         exit()
#         # 重新开始
#         if n == 1:
#             break
#         # elif n == 2:
#         #     continue
