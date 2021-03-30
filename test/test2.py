import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("事件检测")
# titlelineico = pygame.image.load("img/airplane.ico")  # 导入窗口图标，规格：32x32，格式：.ico
# pygame.display.set_icon(titlelineico)  # 设置窗口图标
window.fill((255, 255, 255))
pygame.display.flip()
y = 200
x = 200
r = 50
flag = False
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = True
            pygame.draw.circle(window, (255, 255, 0), (x, y), r)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            flag = False
            pygame.draw.circle(window, (255, 255, 255), (x, y), r)
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION and flag:
            pygame.draw.circle(window, (255, 255, 255), (x, y), r)
            print(event, flag)
            x, y = event.pos
            pygame.draw.circle(window, (255, 255, 0), (x, y), r)
            pygame.display.update()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     print("鼠标按下 ", event.pos)
