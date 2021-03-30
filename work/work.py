import pygame
from tkinter import *
from tkinter.messagebox import *
Tk().wm_withdraw()

showinfo("提示", "本游戏仅支持单机，左击为先手，右击为后手！")

# ----------------------------------------逻辑部分------------------------------------------------

while True:
    # 判断结果
    def compute():
        i = 0
        result = -1
        # 检查行
        while (result == -1) and (i < size):
            num_of_x, num_of_o = 0, 0
            j = 0
            while j < size:
                if board[i][j] == 1:
                    num_of_x += 1
                elif board[i][j] == 0:
                    num_of_o += 1
                if num_of_o == size:
                    result = 0
                elif num_of_x == size:
                    result = 1
                j += 1
            i += 1
        # 检查列
        if result == -1:
            i, j = 0, 0
            while j < size and result == -1:
                num_of_x = num_of_o = 0
                i = 0
                while i < size:
                    if board[i][j] == 1:
                        num_of_x += 1
                    elif board[i][j] == 0:
                        num_of_o += 1
                    if num_of_o == size:
                        result = 0
                    elif num_of_x == size:
                        result = 1
                    i += 1
                j += 1
        # 检查正对角线
        if result == -1:
            num_of_o = num_of_x = 0
            i, j = 0, 0
            while i < size:
                if board[i][i] == 1:
                    num_of_x += 1
                elif board[i][i] == 0:
                    num_of_o += 1
                if num_of_o == size:
                    result = 0
                elif num_of_x == size:
                    result = 1
                i += 1
        # 检查斜对角线
        if result == -1:
            num_of_o = num_of_x = 0
            i, j = 0, 0
            while i < size:
                if board[i][size-i-1] == 1:
                    num_of_x += 1
                elif board[i][size-i-1] == 0:
                    num_of_o += 1
                if num_of_o == size:
                    result = 0
                elif num_of_x == size:
                    result = 1
                i += 1
        return result

# ---------------------------------------GUI图形部分------------------------------------------
    # 画图
    def paint_tick_one():
        pygame.draw.lines(screen, black, False, [(43, 92), (87, 147), (87, 147), (169, 75)], 3)


    def paint_fork_one():
        pygame.draw.line(screen, black, [60, 60], [140, 140], 3)
        pygame.draw.line(screen, black, [140, 60], [60, 140], 3)


    def paint_tick_two():
        pygame.draw.lines(screen, white, False, [(242, 92), (279, 142), (279, 142), (353, 82)], 3)


    def paint_fork_two():
        pygame.draw.line(screen, white, [260, 60], [340, 140], 3)
        pygame.draw.line(screen, white, [340, 60], [260, 140], 3)


    def paint_tick_three():
        pygame.draw.lines(screen, black, False, [(433, 87), (482, 147), (482, 147), (555, 75)], 3)


    def paint_fork_three():
        pygame.draw.line(screen, black, [460, 60], [540, 140], 3)
        pygame.draw.line(screen, black, [540, 60], [460, 140], 3)


    def paint_tick_four():
        pygame.draw.lines(screen, white, False, [(43, 299), (87, 350), (87, 350), (169, 281)], 3)


    def paint_fork_four():
        pygame.draw.line(screen, white, [60, 260], [140, 340], 3)
        pygame.draw.line(screen, white, [140, 260], [60, 340], 3)


    def paint_tick_five():
        pygame.draw.lines(screen, black, False, [(242, 299), (279, 350), (279, 350), (353, 281)], 3)


    def paint_fork_five():
        pygame.draw.line(screen, black, [260, 260], [340, 340], 3)
        pygame.draw.line(screen, black, [340, 260], [260, 340], 3)

    def paint_tick_six():
        pygame.draw.lines(screen, white, False, [(433, 299), (482, 350), (482, 350), (555, 281)], 3)


    def paint_fork_six():
        pygame.draw.line(screen, white, [460, 260], [540, 340], 3)
        pygame.draw.line(screen, white, [540, 260], [460, 340], 3)


    def paint_tick_seven():
        pygame.draw.lines(screen, black, False, [(43, 495), (87, 549), (87, 549), (169, 480)], 3)


    def paint_fork_seven():
        pygame.draw.line(screen, black, [60, 460], [140, 540], 3)
        pygame.draw.line(screen, black, [140, 460], [60, 540], 3)


    def paint_tick_eight():
        pygame.draw.lines(screen, white, False, [(242, 495), (279, 549), (279, 549), (353, 480)], 3)


    def paint_fork_eight():
        pygame.draw.line(screen, white, [260, 460], [340, 540], 3)
        pygame.draw.line(screen, white, [340, 460], [260, 540], 3)


    def paint_tick_nine():
        pygame.draw.lines(screen, black, False, [(433, 495), (482, 549), (482, 549), (555, 480)], 3)


    def paint_fork_nine():
        pygame.draw.line(screen, black, [460, 460], [540, 540], 3)
        pygame.draw.line(screen, black, [540, 460], [460, 540], 3)


    def paint_circle_first():
        pygame.draw.circle(screen, black, [625, 60], 20, 0)

    def paint_circle_next():
        pygame.draw.circle(screen, black, [625, 145], 20, 0)

    # 刷新背景
    def background():
        screen.fill([199, 193, 245])
        pygame.draw.rect(screen, white, [0, 0, 200, 200], 0)
        pygame.draw.rect(screen, black, [200, 0, 200, 200], 0)
        pygame.draw.rect(screen, white, [400, 0, 200, 200], 0)
        pygame.draw.rect(screen, black, [0, 200, 200, 200], 0)
        pygame.draw.rect(screen, white, [200, 200, 200, 200], 0)
        pygame.draw.rect(screen, black, [400, 200, 200, 200], 0)
        pygame.draw.rect(screen, white, [0, 400, 200, 200], 0)
        pygame.draw.rect(screen, black, [200, 400, 200, 200], 0)
        pygame.draw.rect(screen, white, [400, 400, 200, 200], 0)
        pygame.draw.lines(screen, lightgrey, True, [(600, 0), (650, 0), (650, 200), (600, 200)], 3)
        pygame.draw.lines(screen, lightgrey, True, [(600, 200), (650, 200), (650, 400), (600, 400)], 3)
        pygame.draw.lines(screen, lightgrey, True, [(600, 400), (650, 400), (650, 600), (600, 600)], 3)
        pygame.draw.circle(screen, black, [625, 60], 20, 3)
        pygame.draw.circle(screen, black, [625, 145], 20, 3)
        screen.blit(text1, (610, 225))
        screen.blit(text2, (610, 262))
        screen.blit(text3, (610, 299))
        screen.blit(text4, (609, 336))
        screen.blit(text5, (610, 3))
        screen.blit(text6, (610, 85))
        pygame.display.update()


    # 主程序
    size = 3
    n = 0        # 游戏结束时的临时变量，控制重启游戏
    board = []
    white = [255, 255, 255]
    black = [0, 0, 0]
    bright_green = (0, 255, 0)
    lightgrey = [125, 125, 125]

    for k in range(3):
        board.append([])
        for h in range(3):
            board[k].append(-1)

    # count表示用奇偶数的方法区分先后手
    count = 0
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode([650, 600])
    pygame.display.set_caption("MyPygame")
    my_font = pygame.font.Font("fzlt.ttf", 30)
    text1 = my_font.render("重", True, black)
    text2 = my_font.render("新", True, black)
    text3 = my_font.render("开", True, black)
    text4 = my_font.render("始", True, black)
    text5 = my_font.render("先", True, black)
    text6 = my_font.render("后", True, black)
    text7 = my_font.render("只要心中有梦想的火种，", True, black)
    text8 = my_font.render("终于一天我们会被生活点燃！", True, black)
    # 刷新背景
    background()

    while True:
        for event in pygame.event.get():
            print(pygame.mouse.get_pos())
            mouse = pygame.mouse.get_pos()

            if count != 0:
                if count % 2 == 1:
                    paint_circle_first()
                    pygame.draw.circle(screen, [199, 193, 245], [625, 145], 17, 0)
                else:
                    paint_circle_next()
                    pygame.draw.circle(screen, [199, 193, 245], [625, 60], 17, 0)
            pygame.display.update()

            if 600 <= mouse[0] <= 650 and 200 <= mouse[1] <= 400:
                pygame.draw.lines(screen, [72, 246, 31], True, [(600, 200), (650, 200), (650, 400), (600, 400)], 3)
            else:
                pygame.draw.lines(screen, lightgrey, True, [(600, 200), (650, 200), (650, 400), (600, 400)], 3)
            pygame.display.update()

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标的x坐标
                x = event.pos[0]
                # 鼠标的y坐标
                y = event.pos[1]
                print(x, y)

                if 600 <= mouse[0] <= 650 and 200 <= mouse[1] <= 400 and event.button == 1:
                    n = 1
                    # print("hello")

                if 650 >= mouse[0] >= 600 >= mouse[1] >= 400 and event.button == 1:
                    screen.fill([255, 255, 255])
                    screen.blit(text7, (180, 200))
                    screen.blit(text8, (150, 250))
                pygame.display.update()

                if (1 <= x <= 199) and (1 <= y <= 199) and board[0][0] == -1:   # 第一格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_one()
                            board[0][0] = 1
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_one()
                            board[0][0] = 0
                            pygame.display.update()
                            count += 1
                elif (201 <= x <= 399) and (1 <= y <= 199) and board[0][1] == -1:   # 第二格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_two()
                            board[0][1] = 1
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_two()
                            board[0][1] = 0
                            pygame.display.update()
                            count += 1
                elif (401 <= x <= 599) and (1 <= y <= 199) and board[0][2] == -1:   # 第三格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_three()
                            board[0][2] = 1
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_three()
                            board[0][2] = 0
                            pygame.display.update()
                            count += 1
                elif (1 <= x <= 199) and (201 <= y <= 399) and board[1][0] == -1:   # 第四格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_four()
                            board[1][0] = 1
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_four()
                            board[1][0] = 0
                            pygame.display.update()
                            count += 1
                elif (201 <= x <= 399) and (201 <= y <= 399) and board[1][1] == -1:   # 第五格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_five()
                            board[1][1] = 1
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_five()
                            board[1][1] = 0
                            pygame.display.update()
                            count += 1
                elif (401 <= x <= 599) and (201 <= y <= 399) and board[1][2] == -1:   # 第六格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_six()
                            board[1][2] = 1
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_six()
                            board[1][2] = 0
                            pygame.display.update()
                            count += 1
                elif (1 <= x <= 199) and (401 <= y <= 599) and board[2][0] == -1:   # 第七格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_seven()
                            board[2][0] = 1
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_seven()
                            board[2][0] = 0
                            pygame.display.update()
                            count += 1
                elif (201 <= x <= 399) and (401 <= y <= 599) and board[2][1] == -1:   # 第八格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_eight()
                            board[2][1] = 1
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_eight()
                            board[2][1] = 0
                            pygame.display.update()
                            count += 1
                elif (401 <= x <= 599) and (401 <= y <= 599) and board[2][2] == -1:   # 第九格
                    if n == 0:
                        if event.button == 1 and count % 2 == 0:
                            paint_tick_nine()
                            board[2][2] = 1     # 写入数组
                            pygame.display.update()
                            count += 1
                        elif event.button == 3 and count % 2 == 1:
                            paint_fork_nine()
                            board[2][2] = 0
                            pygame.display.update()
                            count += 1
                if n == 0:
                    if compute() == 1:
                        showinfo("提示", "X WIN!")
                        n = 2
                    elif compute() == 0:
                        showinfo("提示", "O WIN!")
                        n = 2
                    elif count >= 9 and compute() == -1:
                        showinfo("提示", "平局！")
                        n = 2
        # 重新开始
        if n == 1:
            break
