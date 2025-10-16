import pygame, sys, numpy as np , random

import tkinter as tk
from collections import deque
from PIL import Image, ImageTk
import heapq
found = 0

def start_BFS():
    pygame.init()
    man_hinh = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Trò chơi 8 con xe")
    li=[]   # lưu tọa độ đỉnh (i,j) theo cách sinh 1
    am = pygame.mixer.Sound("tieng_co.mp3")
    panel = pygame.Surface((240, 240))
    panel_1= pygame.Surface((240, 240))
    Cau_hinh = {} # lưu cấu hình
    N = 8
    mang_2D = np.zeros((8, 8))
    mang = np.zeros((8, 8))
    anh_nen = pygame.image.load("BG.png").convert_alpha(man_hinh)
    anh_nen_scale = pygame.transform.scale(anh_nen,(800,600))
    def chieu_xe(x, y):
        for i in range(1, N):
            if y + i < N and mang_2D[x][y + i] != 1:
                mang_2D[x][y + i] -= 1
            if y - i >= 0 and mang_2D[x][y - i] != 1:
                mang_2D[x][y - i] -= 1
            if x + i < N and mang_2D[x + i][y] != 1:
                mang_2D[x + i][y] -= 1
            if x - i >= 0 and mang_2D[x - i][y] != 1:
                mang_2D[x - i][y] -= 1

    def go_chieu_hau(x, y):
        for i in range(1, N):
            if y + i < N:
                mang_2D[x][y + i] += 1
            if y - i >= 0:
                mang_2D[x][y - i] += 1
            if x + i < N:
                mang_2D[x + i][y] += 1
            if x - i >= 0:
                mang_2D[x - i][y] += 1

    def de_xe(x):
        global found
        if x == N:
            found += 1
            return
        if 1 in mang_2D[x]:
            de_xe(x + 1)
            return
        for j in range(N):
            if mang_2D[x][j] == 0:
                mang_2D[x][j] = 1
                chieu_xe(x, j)
                de_xe(x + 1)
                if found == 24:
                    break
                go_chieu_hau(x, j)
                mang_2D[x][j] = 0

    x = random.randint(1,7)
    y = random.randint(1,7)
    mang_2D[x][y] = 1
    chieu_xe(x,y)
    de_xe(0)

    def xu_ly_sau_khi_sinh_mang_2D(mang_2D,li):
        for i in range(N):
            for j in range(N):
                if mang_2D[i][j] != 1:
                    mang_2D[i][j] = 0
                else:
                    li.append((i,j))

    xu_ly_sau_khi_sinh_mang_2D(mang_2D,li)

    def ve_8_con_xe(panel: pygame.Surface):
        panel.fill("White")
        cell_size = 30
        for i in range(N):
            for j in range(N):
                rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                if (i + j) % 2 == 0:
                    pygame.draw.rect(panel, (245, 238, 220), rect)
                else:
                    pygame.draw.rect(panel, (169, 121, 86), rect)
                if mang_2D[i][j] == 1:
                    if (i + j) % 2 == 0:
                        img = pygame.image.load("chess-knight-white.png").convert_alpha()
                    else:
                        img = pygame.image.load("chess-knight-Black.png").convert_alpha()

                    img_scale= pygame.transform.scale(img,(40,40))
                    img_rect = img_scale.get_rect(center=rect.center)
                    panel.blit(img_scale,img_rect)



    def ve_co_trong(panel_1: pygame.Surface,Cau_hinh,k):
        panel_1.fill("White")
        cell_size = 30
        for i in range(N):
            for j in range(N):
                rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                if (i + j) % 2 == 0:
                    pygame.draw.rect(panel_1, (215, 168, 110), rect)  # ô sáng
                else:
                    pygame.draw.rect(panel_1, (141, 85, 36), rect)  # ô tối

                if Cau_hinh[k][i][j] == 1:
                    if (i + j) % 2 == 0:
                        img = pygame.image.load("WhiteRook.png").convert_alpha()
                    else:
                        img = pygame.image.load("BlackRook.png").convert_alpha()

                    img_scale = pygame.transform.scale(img, (30, 30))
                    img_rect = img_scale.get_rect(center=rect.center)
                    panel_1.blit(img_scale, img_rect)
    def Ma_Tran_Ke_Tiep_BFS(Ma_Tran_Hien_Tai, hang_doi, visited,li,cau_hinh):
        N = range(8)
        for i in N:
                if 1 in Ma_Tran_Hien_Tai[i]:   # kiểm tra hàng i
                    continue
                for j in N:
                    if 1 in Ma_Tran_Hien_Tai[:, j]:  # kiểm tra cột j+-
                        continue
                    t = (i,j)
                    if t in li:
                        Ma_Tran_Tam_Thoi = Ma_Tran_Hien_Tai.copy()
                        Ma_Tran_Tam_Thoi[i][j] = 1
                        if Ma_Tran_Tam_Thoi.tobytes() not in visited:
                            hang_doi.append(Ma_Tran_Tam_Thoi)
                            visited.add(Ma_Tran_Tam_Thoi.tobytes())
                            cau_hinh[Ma_Tran_Tam_Thoi.tobytes()] = (Ma_Tran_Hien_Tai.dtype, Ma_Tran_Hien_Tai.shape, Ma_Tran_Hien_Tai.tobytes())

    def Ma_Tran_Ke_Tiep_BFS_1(Ma_Tran_Hien_Tai, hang_doi,hang, visited, cau_hinh):
        N = range(8)
        for j in N:
            if 1 not in Ma_Tran_Hien_Tai[:,j]:
                    Ma_Tran_Tam_Thoi = Ma_Tran_Hien_Tai.copy()
                    Ma_Tran_Tam_Thoi[hang][j] = 1
                    if Ma_Tran_Tam_Thoi.tobytes() not in visited:
                        hang_doi.append(Ma_Tran_Tam_Thoi)
                        visited.add(Ma_Tran_Tam_Thoi.tobytes())
                        cau_hinh[Ma_Tran_Tam_Thoi.tobytes()] = (Ma_Tran_Hien_Tai.dtype, Ma_Tran_Hien_Tai.shape, Ma_Tran_Hien_Tai.tobytes())

    def BFS(Ma_Tran_Dich, Trang_Thai_Mang,cau_hinh):
        hang_doi = deque()
        hang_doi.append(Trang_Thai_Mang)
        visited = set()
        visited.add(Trang_Thai_Mang.tobytes())
        t = 0
        while hang_doi:
            Ma_tran_hien_tai = hang_doi.popleft() # dequeue
            if np.array_equal(Ma_tran_hien_tai, Ma_Tran_Dich):
                return Ma_tran_hien_tai
            for i in range(8):
                if 1 not in Ma_tran_hien_tai[i]:
                    t = i
                    break
            Ma_Tran_Ke_Tiep_BFS_1(Ma_tran_hien_tai, hang_doi,t, visited,cau_hinh)
        return None

    m = BFS(mang_2D,mang,Cau_hinh)

    print(mang_2D)
    print(m)

    def xu_ly_cau_hinh(cau_hinh, mang_2D):
        t = mang_2D.tobytes()
        duong_di = []
        while t in cau_hinh:
            dtype, shape, parent = cau_hinh[t]
            arr1d = np.frombuffer(t, dtype=dtype)
            arr2d = arr1d.reshape(shape)
            duong_di.append(arr2d)
            if parent is None:
                break
            t = parent
        return duong_di[::-1]


    cau_hinh = xu_ly_cau_hinh(Cau_hinh,mang_2D)

    count =0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        man_hinh.blit(anh_nen_scale, (0, 0))
        ve_8_con_xe(panel)
        man_hinh.blit(panel, (500, 150))

        if count < len(cau_hinh):
            ve_co_trong(panel_1,cau_hinh,count)
            man_hinh.blit(panel_1, (50, 150))
            am.play()
            count+=1
            pygame.display.update()
            pygame.time.delay(2500)
        else:
            ve_co_trong(panel_1, cau_hinh, len(cau_hinh)-1)
            man_hinh.blit(panel_1, (50, 150))
            pygame.display.update()