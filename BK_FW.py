import sys
from collections import deque

import numpy as np
import pygame

import random
found = 0
def start_BFS_MU():
    pygame.init()
    man_hinh = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Trò chơi 8 con xe")
    am = pygame.mixer.Sound("tieng_co.mp3")
    panel = pygame.Surface((240, 240))
    panel_1 = pygame.Surface((240, 240))
    Cau_hinh = {}  # lưu cấu hình
    N = 8
    mang_2D = np.zeros((8, 8))
    mang = np.zeros((8, 8))
    anh_nen = pygame.image.load("BG.png").convert_alpha(man_hinh)
    anh_nen_scale = pygame.transform.scale(anh_nen, (800, 600))
    cell_size = 60
    def ve_ban_co(mang):
        panel = pygame.Surface((cell_size * N, cell_size * N))
        for i in range(N):
            for j in range(N):
                rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                color = (215, 168, 110) if (i + j) % 2 == 0 else (141, 85, 36)
                pygame.draw.rect(panel, color, rect)
                pygame.draw.rect(panel, (0, 0, 0), rect, 1)
                if mang[i][j] == 1:
                    img = pygame.image.load("WhiteRook.png").convert_alpha()
                    img_scale = pygame.transform.scale(img, (cell_size - 8, cell_size - 8))
                    img_rect = img_scale.get_rect(center=rect.center)
                    panel.blit(img_scale, img_rect)
        man_hinh.blit(panel, (180, 100))
        pygame.display.update()
        am.play()
        pygame.time.delay(600)
    Tap_Gia_Tri = [(i, j) for i in range(8) for j in range(8)]
    print(Tap_Gia_Tri)
    Tap_Bien = [{"x1":()},{"x2":()},{"x3":()},{"x4":()},{"x5":()},{"x6":()},{"x7":()},{"x8":()}]
    def Tap_Cac_Rang_Buoc(Tap_Bien):
        for x in range(len(Tap_Bien)-1):
            ten_x = "x" + str(x + 1)
            if Tap_Bien[x][ten_x] != ():
                for y in range(x+1,len(Tap_Bien)):
                    ten_y = "x"+str(y+1)
                    if Tap_Bien[y][ten_y] ==  ():
                        continue
                    if Tap_Bien[x][ten_x] == Tap_Bien[y][ten_y] or Tap_Bien[x][ten_x][0] == Tap_Bien[y][ten_y][0] or Tap_Bien[x][ten_x][1] == Tap_Bien[y][ten_y][1]  :
                        return False
        return True
    Bien_Da_Dc_Chon = []
    x_ngau_nhien = []
    while len(x_ngau_nhien) <8:
        x = random.randint(0, 7)
        if x not in x_ngau_nhien:
            x_ngau_nhien.append(x)

    def Checking_FW(i,ten):
        Tap_Mien = []
        for x in range(len(Tap_Gia_Tri)):
            if Tap_Gia_Tri[x][0]  != Tap_Bien[i][ten][0] and Tap_Gia_Tri[x][1] != Tap_Bien[i][ten][1]:
                Tap_Mien.append(Tap_Gia_Tri[x])
        random.shuffle(Tap_Mien)
        return Tap_Mien

    duong_di = []
    def bk(t,Tap_Mien):
        if t ==8:
            duong_di.append(np.zeros((N, N)))
            for k in range(8):
                x, y = Tap_Bien[k]["x" + str(k + 1)]
                duong_di[-1][x][y] = 1
            print(Tap_Bien)
            return True
        for x in x_ngau_nhien:
            if x not in Bien_Da_Dc_Chon:
                Bien_Da_Dc_Chon.append(x)
                for idx in range(len(Tap_Mien)):
                    ten= "x"+str(x+1)
                    Tap_Bien[x][ten] = Tap_Mien[idx]
                    Tap_Mien_new = Checking_FW(x,ten)
                    if Tap_Cac_Rang_Buoc(Tap_Bien):
                        mang_tam = np.zeros((N, N))
                        for k in range(N):
                            val = Tap_Bien[k]["x" + str(k + 1)]
                            if val != ():
                                mang_tam[val[0]][val[1]] = 1
                        duong_di.append(mang_tam)
                        t+=1
                        bk(t,Tap_Mien_new)
                        Tap_Bien[x][ten] = ()
                Bien_Da_Dc_Chon.pop(-1)
        return False

    bk(0,Tap_Gia_Tri)



    def xu_ly_cau_hinh(cau_hinh, mang_2D):
        t = mang_2D.tobytes()
        duong_di = []
        while t in cau_hinh:
            parent, dtype, shape = cau_hinh[t]
            arr1d = np.frombuffer(t, dtype=dtype)
            arr2d = arr1d.reshape(shape)
            duong_di.append(arr2d)

            if parent is None:
                break
            t = parent
        return duong_di[::-1]

    for buoc, Mang_HT in enumerate(duong_di):
        man_hinh.blit(anh_nen_scale, (0, 0))
        ve_ban_co(Mang_HT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


start_BFS_MU()
