# Vu_Minh_Duc - 23110094

import pygame, sys, numpy as np , random

import tkinter as tk
from collections import deque
from PIL import Image, ImageTk
import heapq

import A_sao
import BFS
import DFS
import DLS
import Greedy
import IDS
import UCS
import beam

found =0
lan_vo = 0

def start_BFS():
    BFS.start_BFS()


def start_DFS():
    DFS.start_DFS()

def ham_tinh_chi_phi():
    return 1
def ham_tinh_heuristic(hang,j,li):
    chi_phi = 1
    for (i, cot) in li:
        if i == hang:
            chi_phi += abs(j - cot)
    return chi_phi


def start_UCS():
    UCS.start_UCS()

def start_DLS():
    DLS.start_DLS()


def start_IDS():
    IDS.start_IDS()

def Greedy_Search():
    Greedy.Greedy_Search()



def start_A_sao():
    A_sao.start_A_sao()



def start_Beam_Search():
    beam.start_Beam_Search()

def start_Backtracking():
    pygame.init()
    man_hinh = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Thuật toán Backtracking 8 con xe")
    am = pygame.mixer.Sound("tieng_co.mp3")
    font = pygame.font.SysFont("Tahoma", 22, bold=True)

    N = 8
    anh_nen = pygame.image.load("BG.png").convert_alpha()
    anh_nen_scale = pygame.transform.scale(anh_nen, (900, 700))
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

    Tap_Gia_Tri = [(i, j) for i in range(N) for j in range(N)]
    Tap_Bien = [{"x1": ()}, {"x2": ()}, {"x3": ()}, {"x4": ()},
                {"x5": ()}, {"x6": ()}, {"x7": ()}, {"x8": ()}]
    x_ngau_nhien = random.sample(range(8), 8)
    gt_nn = random.sample(range(64), 64)
    duong_di = []

    def Tap_Cac_Rang_Buoc(Tap_Bien):
        for x in range(len(Tap_Bien) - 1):
            ten_x = "x" + str(x + 1)
            if Tap_Bien[x][ten_x] != ():
                for y in range(x + 1, len(Tap_Bien)):
                    ten_y = "x" + str(y + 1)
                    if Tap_Bien[y][ten_y] == ():
                        continue
                    if (Tap_Bien[x][ten_x] == Tap_Bien[y][ten_y] or
                            Tap_Bien[x][ten_x][0] == Tap_Bien[y][ten_y][0] or
                            Tap_Bien[x][ten_x][1] == Tap_Bien[y][ten_y][1]):
                        return False
        return True

    Bien_Da_Dc_Chon = []

    def bk(t):
        if t == 8:
            duong_di.append(np.zeros((N, N)))
            for k in range(8):
                x, y = Tap_Bien[k]["x" + str(k + 1)]
                duong_di[-1][x][y] = 1
            print(Tap_Bien)
            return True

        for x in x_ngau_nhien:
            if x not in Bien_Da_Dc_Chon:
                Bien_Da_Dc_Chon.append(x)
                for idx in gt_nn:
                    ten = "x" + str(x + 1)
                    Tap_Bien[x][ten] = Tap_Gia_Tri[idx]
                    if Tap_Cac_Rang_Buoc(Tap_Bien):
                        mang_tam = np.zeros((N, N))
                        for k in range(N):
                            val = Tap_Bien[k]["x" + str(k + 1)]
                            if val != ():
                                mang_tam[val[0]][val[1]] = 1
                        duong_di.append(mang_tam)
                        t += 1
                        if bk(t):
                            return True
                    Tap_Bien[x][ten] = ()
                Bien_Da_Dc_Chon.pop(-1)
        return False

    bk(0)

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


def start_FWCK():
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
    Tap_Bien = [{"x1": ()}, {"x2": ()}, {"x3": ()}, {"x4": ()}, {"x5": ()}, {"x6": ()}, {"x7": ()}, {"x8": ()}]

    def Tap_Cac_Rang_Buoc(Tap_Bien):
        for x in range(len(Tap_Bien) - 1):
            ten_x = "x" + str(x + 1)
            if Tap_Bien[x][ten_x] != ():
                for y in range(x + 1, len(Tap_Bien)):
                    ten_y = "x" + str(y + 1)
                    if Tap_Bien[y][ten_y] == ():
                        continue
                    if Tap_Bien[x][ten_x] == Tap_Bien[y][ten_y] or Tap_Bien[x][ten_x][0] == Tap_Bien[y][ten_y][0] or \
                            Tap_Bien[x][ten_x][1] == Tap_Bien[y][ten_y][1]:
                        return False
        return True

    Bien_Da_Dc_Chon = []
    x_ngau_nhien = []
    while len(x_ngau_nhien) < 8:
        x = random.randint(0, 7)
        if x not in x_ngau_nhien:
            x_ngau_nhien.append(x)

    def Checking_FW(i, ten):
        Tap_Mien = []
        for x in range(len(Tap_Gia_Tri)):
            if Tap_Gia_Tri[x][0] != Tap_Bien[i][ten][0] and Tap_Gia_Tri[x][1] != Tap_Bien[i][ten][1]:
                Tap_Mien.append(Tap_Gia_Tri[x])
        random.shuffle(Tap_Mien)
        return Tap_Mien

    duong_di = []

    def bk(t, Tap_Mien):
        if t == 8:
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
                    ten = "x" + str(x + 1)
                    Tap_Bien[x][ten] = Tap_Mien[idx]
                    Tap_Mien_new = Checking_FW(x, ten)
                    if Tap_Cac_Rang_Buoc(Tap_Bien):
                        mang_tam = np.zeros((N, N))
                        for k in range(N):
                            val = Tap_Bien[k]["x" + str(k + 1)]
                            if val != ():
                                mang_tam[val[0]][val[1]] = 1
                        duong_di.append(mang_tam)
                        t += 1
                        bk(t, Tap_Mien_new)
                        Tap_Bien[x][ten] = ()
                Bien_Da_Dc_Chon.pop(-1)
        return False

    bk(0, Tap_Gia_Tri)

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

def start_MU_1_Phan():
    pygame.init()
    man_hinh = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Trò chơi 8 con xe")
    FPS = pygame.time.Clock()
    li = []  # lưu tọa độ đỉnh (i,j) theo cách sinh 1
    am = pygame.mixer.Sound("tieng_co.mp3")
    panel = pygame.Surface((240, 240))
    panel_1 = pygame.Surface((240, 240))
    Cau_hinh = {}  # lưu cấu hình
    N = 8
    mang_2D = np.zeros((8, 8))
    mang_2D_1 = np.zeros((8, 8))
    mang_2D_2 = np.zeros((8, 8))
    mang = np.zeros((8, 8))
    anh_nen = pygame.image.load("BG.png").convert_alpha(man_hinh)
    anh_nen_scale = pygame.transform.scale(anh_nen, (800, 600))

    def chieu_xe(x, y, mang):
        for i in range(1, N):
            if y + i < N and mang[x][y + i] != 1:
                mang[x][y + i] -= 1
            if y - i >= 0 and mang[x][y - i] != 1:
                mang[x][y - i] -= 1
            if x + i < N and mang[x + i][y] != 1:
                mang[x + i][y] -= 1
            if x - i >= 0 and mang[x - i][y] != 1:
                mang[x - i][y] -= 1

    def go_chieu_hau(x, y, mang):
        for i in range(1, N):
            if y + i < N:
                mang[x][y + i] += 1
            if y - i >= 0:
                mang[x][y - i] += 1
            if x + i < N:
                mang[x + i][y] += 1
            if x - i >= 0:
                mang[x - i][y] += 1

    def de_xe(x, mang):
        global found
        if x == N:
            found += 1
            return
        if 1 in mang[x]:
            de_xe(x + 1, mang)
            return
        for j in range(N):
            if mang[x][j] == 0:
                mang[x][j] = 1
                chieu_xe(x, j, mang)
                de_xe(x + 1, mang)
                if found == 24:
                    break
                go_chieu_hau(x, j, mang)
                mang[x][j] = 0

    x = random.randint(1, 7)
    y = random.randint(1, 7)
    mang_2D[x][y] = 1
    chieu_xe(x, y, mang_2D)
    de_xe(0, mang_2D)

    x = random.randint(1, 7)
    y = random.randint(1, 7)
    mang_2D_1[x][y] = 1
    chieu_xe(x, y, mang_2D_1)
    de_xe(0, mang_2D_1)

    x = random.randint(1, 7)
    y = random.randint(1, 7)
    mang_2D_2[x][y] = 1
    chieu_xe(x, y, mang_2D_2)
    de_xe(0, mang_2D_2)

    def xu_ly_sau_khi_sinh_mang_2D(mang_2D, li):
        for i in range(N):
            for j in range(N):
                if mang_2D[i][j] != 1:
                    mang_2D[i][j] = 0
                else:
                    li.append((i, j))

    xu_ly_sau_khi_sinh_mang_2D(mang_2D, li)
    xu_ly_sau_khi_sinh_mang_2D(mang_2D_1, li)
    xu_ly_sau_khi_sinh_mang_2D(mang_2D_2, li)

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

                    img_scale = pygame.transform.scale(img, (40, 40))
                    img_rect = img_scale.get_rect(center=rect.center)
                    panel.blit(img_scale, img_rect)

    def ve_co_trong(panel_1: pygame.Surface, Cau_hinh, k):
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

    actions = ["dat", "di_chuyen"]

    def Ma_Tran_Ke_Tiep_MU_1_phan(Ma_Tran_Hien_Tai, act):
        if act == "dat":
            if np.sum(Ma_Tran_Hien_Tai) == 8:
                return Ma_Tran_Hien_Tai
            while True:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if 1 not in Ma_Tran_Hien_Tai[x] and 1 not in Ma_Tran_Hien_Tai[:, y]:
                    Ma_Tran_Tam_Thoi = Ma_Tran_Hien_Tai.copy()
                    Ma_Tran_Tam_Thoi[x][y] = 1
                    return Ma_Tran_Tam_Thoi

        elif act == "di_chuyen":
            if np.sum(Ma_Tran_Hien_Tai) == 8:
                return Ma_Tran_Hien_Tai
            while True:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if 1 not in Ma_Tran_Hien_Tai[x] and 1 not in Ma_Tran_Hien_Tai[:, y] and x != 1 and y != 2:
                    while True:
                        x_can_doi = random.randint(0, 7)
                        if 1 in Ma_Tran_Hien_Tai[x_can_doi]:
                            for j in range(8):
                                if 1 == Ma_Tran_Hien_Tai[x_can_doi][j]:
                                    Ma_Tran_Tam_Thoi = Ma_Tran_Hien_Tai.copy()
                                    Ma_Tran_Tam_Thoi[x_can_doi][j] = 0
                                    Ma_Tran_Tam_Thoi[x][y] = 1

                                    return Ma_Tran_Tam_Thoi

    def la_trang_thai_dich(Ma_Tran):
        # (1) Phải có đúng 8 quân xe
        if np.sum(Ma_Tran) != 8:
            return False
        for i in range(8):
            if np.sum(Ma_Tran[i]) > 1:
                return False
            if np.sum(Ma_Tran[:, i]) > 1:
                return False
        if Ma_Tran[1][2] != 1:
            return False

        return True

    def la_tap_con(Tap_Ma_tran_hien_tai):
        return all(la_trang_thai_dich(Ma_Tran) for Ma_Tran in Tap_Ma_tran_hien_tai)

    # ===== TIỆN ÍCH CHO MU_1_PHAN =====
    def serialize_tap(tap):
        """Biến 1 TAP (list các ma trận) thành key bất biến để lưu parent/visited."""
        return tuple(map(bytes, [m.tobytes() for m in tap]))

    def deserialize_tap(key):
        """Biến key (tuple bytes) về lại list ma trận 8x8 float64."""
        mats = []
        for b in key:
            mats.append(np.frombuffer(b, dtype=np.float64).reshape(8, 8))
        return mats

    def ve_tap(surface, tap, x_start, y, caption, cell_size=30, spacing=260):
        """Vẽ cả TAP (nhiều bàn) nằm ngang. Không vẽ tập đích, chỉ Initial/Current/Path."""
        font = pygame.font.SysFont("Tahoma", 22, bold=True)
        text = font.render(caption, True, (255, 255, 0))
        surface.blit(text, (x_start, y - 30))

        for idx, mat in enumerate(tap):
            panel = pygame.Surface((cell_size * 8, cell_size * 8))
            for i in range(8):
                for j in range(8):
                    rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                    color = (215, 168, 110) if (i + j) % 2 == 0 else (141, 85, 36)
                    pygame.draw.rect(panel, color, rect)
                    pygame.draw.rect(panel, (0, 0, 0), rect, 1)
                    if mat[i][j] == 1:
                        img = pygame.image.load("WhiteRook.png").convert_alpha()
                        img_scale = pygame.transform.scale(img, (cell_size, cell_size))
                        img_rect = img_scale.get_rect(center=rect.center)
                        panel.blit(img_scale, img_rect)
            surface.blit(panel, (x_start + idx * spacing, y))

    def MU_1_phan(Trang_Thai_Mang):
        """
        BFS trên TẬP (multi-universe). Mỗi bước tạo TAP mới bằng cách áp dụng act lên TỪNG ma trận.
        Lưu lại parent để truy vết đường đi (chuỗi TAP).
        Trả về: (list_tap_tren_duong_di, list_act_tuong_ung)
        """
        from collections import deque
        q = deque()

        start_tap = [M.copy() for M in Trang_Thai_Mang]
        start_key = serialize_tap(start_tap)

        parent = {start_key: (None, None)}
        visited = {start_key}

        q.append(start_tap)

        while q:
            tap_ht = q.popleft()
            key_ht = serialize_tap(tap_ht)

            if la_tap_con(tap_ht):
                # Truy vết đường đi các TAP
                path_keys = []
                acts = []
                cur = key_ht
                while cur is not None:
                    path_keys.append(cur)
                    p, act = parent[cur]
                    acts.append(act)
                    cur = p
                path_keys.reverse()
                acts.reverse()
                acts = acts[1:]

                path_taps = [deserialize_tap(k) for k in path_keys]
                return path_taps, acts  # đường đi các TẬP + chuỗi hành động

            for act in actions:
                tap_moi = []
                for M in tap_ht:
                    tap_moi.append(Ma_Tran_Ke_Tiep_MU_1_phan(M, act))
                key_new = serialize_tap(tap_moi)
                if key_new not in visited:
                    visited.add(key_new)
                    parent[key_new] = (key_ht, act)
                    q.append(tap_moi)

        # Không tìm thấy (hiếm)
        return [start_tap], []

    mang_bd_1 = np.zeros((8, 8))
    mang_bd_2 = np.zeros((8, 8))
    mang_bd_1[1][2] = 1
    mang_bd_2[1][2] = 1
    mang_bd_1[0][0] = 1
    MANG_BD = [mang_bd_1, mang_bd_2]
    # Tap_Dich = là 1 mảng có ma trận có 1 pt nằm ở ô 12
    m = MU_1_phan(MANG_BD)

    print(mang_2D)
    print(m)
    print(len(Cau_hinh))

    font = pygame.font.SysFont("Tahoma", 24, bold=True)

    duong_di_tap, acts = MU_1_phan(MANG_BD)
    # duong_di_tap: list các TAP (mỗi TAP là list ma trận)
    # acts: list hành động giữa các TAP liên tiếp (chuỗi "dat"/"di_chuyen")

    step = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        man_hinh.blit(anh_nen_scale, (0, 0))

        # Hiển thị TẬP BAN ĐẦU ở hàng trên
        ve_tap(man_hinh, duong_di_tap[0], 60, 80, "TẬP BAN ĐẦU (INITIAL SET)")

        # Hiển thị TAP hiện tại ở hàng dưới (đường đi)
        ve_tap(man_hinh, duong_di_tap[step], 60, 360, f"TẬP HIỆN TẠI (BƯỚC {step}/{len(duong_di_tap) - 1})")

        pygame.display.update()
        am.play()
        pygame.time.delay(900)

        if step < len(duong_di_tap) - 1:
            step += 1
        else:
            # Giữ màn hình cuối cho đến khi tắt
            while True:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

def start_MU_TP():
    import sys
    from collections import deque
    import numpy as np
    import pygame
    import random

    found = 0
    so_hd_1 = 0
    so_hd_2 = 0
    so_hd_3 = 0

    def start_BFS_MU():
        pygame.init()
        man_hinh = pygame.display.set_mode((1400, 750))
        pygame.display.set_caption("Trò chơi 8 con xe - Multi Universe (BFS)")

        am = pygame.mixer.Sound("tieng_co.mp3")

        N = 8

        # ====== Tạo các ma trận đích ======
        def chieu_xe(x, y, mang):
            for i in range(1, N):
                if y + i < N and mang[x][y + i] != 1:
                    mang[x][y + i] -= 1
                if y - i >= 0 and mang[x][y - i] != 1:
                    mang[x][y - i] -= 1
                if x + i < N and mang[x + i][y] != 1:
                    mang[x + i][y] -= 1
                if x - i >= 0 and mang[x - i][y] != 1:
                    mang[x - i][y] -= 1

        def go_chieu_hau(x, y, mang):
            for i in range(1, N):
                if y + i < N: mang[x][y + i] += 1
                if y - i >= 0: mang[x][y - i] += 1
                if x + i < N: mang[x + i][y] += 1
                if x - i >= 0: mang[x - i][y] += 1

        def de_xe(x, mang):
            global found
            if x == N:
                found += 1
                return
            if 1 in mang[x]:
                de_xe(x + 1, mang)
                return
            for j in range(N):
                if mang[x][j] == 0:
                    mang[x][j] = 1
                    chieu_xe(x, j, mang)
                    de_xe(x + 1, mang)
                    if found == 24:
                        break
                    go_chieu_hau(x, j, mang)
                    mang[x][j] = 0

        def sinh_ma_tran():
            global found
            m = np.zeros((N, N))
            x, y = random.randint(0, 7), random.randint(0, 7)
            m[x][y] = 1
            chieu_xe(x, y, m)
            de_xe(0, m)
            for i in range(N):
                for j in range(N):
                    if m[i][j] != 1: m[i][j] = 0
            found = 0
            return m

        mang_2D = sinh_ma_tran()
        mang_2D_1 = sinh_ma_tran()
        mang_2D_2 = sinh_ma_tran()
        mang_2D_3 = np.zeros((8, 8))
        for i in range(8):
            mang_2D_3[i][i] = 1

        Tap_Dich = [mang_2D, mang_2D_1, mang_2D_2, mang_2D_3]

        # ====== Hàm vẽ ======
        def ve_tap(man_hinh, tap, x_start, y_start, caption):
            cell_size = 25
            font = pygame.font.SysFont("Tahoma", 22, bold=True)
            text = font.render(caption, True, (255, 255, 0))
            man_hinh.blit(text, (x_start, y_start - 35))

            panel_spacing = 300  # tăng khoảng cách giữa các ma trận
            for idx, mat in enumerate(tap):
                panel = pygame.Surface((cell_size * 8, cell_size * 8))
                for i in range(N):
                    for j in range(N):
                        rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                        color = (215, 168, 110) if (i + j) % 2 == 0 else (141, 85, 36)
                        pygame.draw.rect(panel, color, rect)
                        pygame.draw.rect(panel, (0, 0, 0), rect, 1)  # viền đen
                        if mat[i][j] == 1:
                            img = pygame.image.load("WhiteRook.png").convert_alpha()
                            img_scale = pygame.transform.scale(img, (cell_size, cell_size))
                            img_rect = img_scale.get_rect(center=rect.center)
                            panel.blit(img_scale, img_rect)
                man_hinh.blit(panel, (x_start + idx * panel_spacing, y_start))

        actions = ["dat", "di_chuyen_hang", "di_chuyen_cot"]

        def Ma_Tran_Ke_Tiep_MU_1(Ma_Tran, act):
            Ma_Tran_Tam = Ma_Tran.copy()
            if act == "dat":
                for x in range(8):
                    for y in range(8):
                        if Ma_Tran_Tam[x][y] == 0 and 1 not in Ma_Tran_Tam[x] and 1 not in Ma_Tran_Tam[:, y]:
                            Ma_Tran_Tam[x][y] = 1
                            return Ma_Tran_Tam
            elif act == "di_chuyen_hang":
                for x in range(8):
                    for y in range(8):
                        if Ma_Tran_Tam[x][y] == 1:
                            for x_new in range(8):
                                if x_new != x and 1 not in Ma_Tran_Tam[x_new]:
                                    M = Ma_Tran_Tam.copy()
                                    M[x][y] = 0
                                    M[x_new][y] = 1
                                    return M
            elif act == "di_chuyen_cot":
                for y in range(8):
                    for x in range(8):
                        if Ma_Tran_Tam[x][y] == 1:
                            for y_new in range(8):
                                if y_new != y and 1 not in Ma_Tran_Tam[:, y_new]:
                                    M = Ma_Tran_Tam.copy()
                                    M[x][y] = 0
                                    M[x][y_new] = 1
                                    return M
            return Ma_Tran_Tam

        def la_tap_con(Tap_HT, Tap_Dich):
            return all(any(np.array_equal(M1, M2) for M2 in Tap_Dich) for M1 in Tap_HT)

        def MU(Tap_Dich, Trang_Thai_BD):
            hang_doi = deque()
            visited = set()
            parent = {}  # Lưu quan hệ cha: parent[state_key] = (parent_key, act)
            key_goc = tuple(map(bytes, [m.tobytes() for m in Trang_Thai_BD]))
            hang_doi.append(key_goc)
            visited.add(key_goc)

            goal_key = None
            actions = ["dat", "di_chuyen_hang", "di_chuyen_cot"]
            duong_di = []

            while hang_doi:
                key_ht = hang_doi.popleft()
                Tap_HT = [np.frombuffer(x, dtype=np.float64).reshape(8, 8) for x in key_ht]
                for act in actions:
                    Tap_Moi = [Ma_Tran_Ke_Tiep_MU_1(M, act) for M in Tap_HT]
                    key_moi = tuple(map(bytes, [m.tobytes() for m in Tap_Moi]))
                    if key_moi not in visited:
                        visited.add(key_moi)
                        parent[key_moi] = (key_ht, act)
                        hang_doi.append(key_moi)

                        if la_tap_con(Tap_Moi, Tap_Dich):
                            duong_di.append(act)
                            goal_key = key_moi
                            break
                if goal_key:
                    break

            key_ht = goal_key
            while key_ht != key_goc:
                key_truoc, act = parent[key_ht]
                duong_di.append(act)
                key_ht = key_truoc
            duong_di.reverse()

            print("\n=== DANH SÁCH HÀNH ĐỘNG SINH RA TẬP ĐÍCH ===")
            print(duong_di)

            # ======== Hiển thị GUI thực hiện các hành động ========
            font = pygame.font.SysFont("Tahoma", 24, bold=True)
            Tap_HT = Trang_Thai_BD.copy()

            man_hinh.fill((30, 30, 30))
            ve_tap(man_hinh, Tap_Dich, 100, 80, "TẬP ĐÍCH (GOAL SET)")
            ve_tap(man_hinh, Trang_Thai_BD, 100, 450, "TẬP BAN ĐẦU (INITIAL)")
            pygame.display.update()
            pygame.time.delay(1000)

            for act in duong_di:
                man_hinh.fill((30, 30, 30))
                ve_tap(man_hinh, Tap_Dich, 100, 80, "TẬP ĐÍCH (GOAL SET)")
                ve_tap(man_hinh, Tap_HT, 100, 450, "TẬP HIỆN TẠI (CURRENT)")
                text = font.render(f"Thực hiện hành động: {act}", True, (255, 200, 0))
                man_hinh.blit(text, (500, 30))
                pygame.display.update()
                pygame.time.delay(1000)
                Tap_HT = [Ma_Tran_Ke_Tiep_MU_1(M, act) for M in Tap_HT]
                am.play()
                pygame.time.delay(2000)

        # ====== Khởi tạo tập ban đầu ======
        mang_bd_1 = np.zeros((8, 8))
        mang_bd_2 = np.zeros((8, 8))
        for i in range(4):
            mang_bd_1[i][i] = 1
            mang_bd_2[i + 4][i + 4] = 1
        MANG_BD = [mang_bd_1, mang_bd_2]

        MU(Tap_Dich, MANG_BD)

        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
        pygame.quit()

    # === GỌI CHƯƠNG TRÌNH ===
    start_BFS_MU()

def start_AND_OR():
        import numpy as np
        pygame.init()
        man_hinh = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Trò chơi 8 con xe")
        li = []  # lưu tọa độ đỉnh (i,j) theo cách sinh 1
        am = pygame.mixer.Sound("tieng_co.mp3")
        panel = pygame.Surface((240, 240))
        panel_1 = pygame.Surface((240, 240))
        Cau_hinh = {}  # lưu cấu hình
        N = 8
        mang_2D = np.zeros((8, 8))
        mang = np.zeros((8, 8))
        anh_nen = pygame.image.load("BG.png").convert_alpha(man_hinh)
        anh_nen_scale = pygame.transform.scale(anh_nen, (800, 600))
        font = pygame.font.SysFont("Arial", 12, bold=True)

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

        x = random.randint(1, 7)
        y = random.randint(1, 7)
        mang_2D[x][y] = 1
        chieu_xe(x, y)
        de_xe(0)

        def xu_ly_sau_khi_sinh_mang_2D(mang_2D, li):
            for i in range(N):
                for j in range(N):
                    if mang_2D[i][j] != 1:
                        mang_2D[i][j] = 0
                    else:
                        li.append((i, j))

        xu_ly_sau_khi_sinh_mang_2D(mang_2D, li)

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

                        img_scale = pygame.transform.scale(img, (40, 40))
                        img_rect = img_scale.get_rect(center=rect.center)
                        panel.blit(img_scale, img_rect)

        def ve_co_trong(panel_1: pygame.Surface, Cau_hinh, k):
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

        import numpy as np

        def AND_OR_GRAPH_SEARCH(ma_tran_ban_dau, ma_tran_dich):
            return OR_SEARCH(ma_tran_ban_dau, ma_tran_dich, [])

        def OR_SEARCH(state, goal, path):
            if np.array_equal(state, goal):
                return []

            if any(np.array_equal(state, p) for p in path):
                return None

            new_path = path + [state]

            for i in range(8):
                if 1 not in state[i]:
                    row_index = i
                    break
            else:
                return None

            for j in range(8):
                if 1 not in state[:, j]:
                    next_states = sinh(state, row_index, j)
                    for ns in next_states:
                        Cau_hinh[ns.tobytes()] = (ns.dtype, ns.shape, state.tobytes(), 1)

                    plan = AND_SEARCH(next_states, goal, new_path)
                    if plan is not None:
                        return [(row_index, j), plan]

            return None

        def AND_SEARCH(states, goal, path):
            plans = []
            for s in states:
                plan = OR_SEARCH(s, goal, path)
                if plan is None:
                    return None
                plans.append(plan)
            return plans

        def sinh(state, row, col):
            results = []
            temp = state.copy()
            temp[row][col] = 1
            results.append(temp)

            if col + 1 < 8:
                temp = state.copy()
                temp[row][col + 1] = 1
                results.append(temp)
            elif row + 1 < 8:
                temp = state.copy()
                temp[row + 1][col] = 1
                results.append(temp)
            return results

        ma_tran_start = np.zeros((8, 8))
        plan = AND_OR_GRAPH_SEARCH(ma_tran_start, mang_2D)
        print("Kế hoạch tìm được:")
        print(plan)

        def xu_ly_cau_hinh(cau_hinh, mang_2D):
            t = mang_2D.tobytes()
            duong_di = []
            tong_chi_phi = []
            while t in cau_hinh:
                dtype, shape, parent, chi_phi = cau_hinh[t]
                arr1d = np.frombuffer(t, dtype=dtype)
                arr2d = arr1d.reshape(shape)
                duong_di.append(arr2d)
                tong_chi_phi.append(chi_phi)
                if parent is None:
                    break
                t = parent
            return duong_di[::-1], tong_chi_phi[::-1]

        cau_hinh, tong_chi_phi = xu_ly_cau_hinh(Cau_hinh, mang_2D)

        count = 0
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            man_hinh.blit(anh_nen_scale, (0, 0))
            ve_8_con_xe(panel)
            man_hinh.blit(panel, (500, 150))

            if count < len(cau_hinh):
                ve_co_trong(panel_1, cau_hinh, count)
                man_hinh.blit(panel_1, (50, 150))
                am.play()
                chi_phi = str(tong_chi_phi[count])
                text = font.render(chi_phi, True, (255, 0, 0))
                text_rect = text.get_rect(center=(400, 100))
                man_hinh.blit(text, text_rect)
                count += 1
                pygame.display.update()
                pygame.time.delay(2500)
            else:
                ve_co_trong(panel_1, cau_hinh, tong_chi_phi, len(cau_hinh) - 1)
                man_hinh.blit(panel_1, (50, 150))
                chi_phi = str(tong_chi_phi[len(cau_hinh) - 1])
                text = font.render(chi_phi, True, (255, 0, 0))
                text_rect = text.get_rect(center=(400, 100))
                man_hinh.blit(text, text_rect)
                pygame.display.update()



def start_Genetic():
    pygame.init()
    man_hinh = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Trò chơi 8 con xe")
    li = []  # lưu tọa độ đỉnh (i,j) theo cách sinh 1
    am = pygame.mixer.Sound("tieng_co.mp3")
    panel = pygame.Surface((240, 240))
    panel_1 = pygame.Surface((240, 240))
    Cau_hinh = {}  # lưu cấu hình
    N = 8
    mang_2D = np.zeros((8, 8))
    mang = np.zeros((8, 8))
    anh_nen = pygame.image.load("BG.png").convert_alpha(man_hinh)
    anh_nen_scale = pygame.transform.scale(anh_nen, (800, 600))
    font = pygame.font.SysFont("Arial", 12, bold=True)

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

    found = 0

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

    x = random.randint(1, 7)
    y = random.randint(1, 7)
    mang_2D[x][y] = 1
    chieu_xe(x, y)
    de_xe(0)

    def xu_ly_sau_khi_sinh_mang_2D(mang_2D, li):
        for i in range(N):
            for j in range(N):
                if mang_2D[i][j] != 1:
                    mang_2D[i][j] = 0
                else:
                    li.append((i, j))

    xu_ly_sau_khi_sinh_mang_2D(mang_2D, li)

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

                    img_scale = pygame.transform.scale(img, (40, 40))
                    img_rect = img_scale.get_rect(center=rect.center)
                    panel.blit(img_scale, img_rect)

    def ve_co_trong(panel_1: pygame.Surface, Cau_hinh, k):
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

    def ham_sinh_ca_the():
        ca_the = np.zeros((8, 8))
        for i in range(8):
            j = random.randint(0, 7)
            ca_the[i][j] = 1
        return ca_the

    def ham_sinh_quan_the(so_ca_the):
        population = []
        seen = set()
        while len(population) < so_ca_the:
            ca_the = ham_sinh_ca_the()
            key = ca_the.tobytes()
            if key not in seen:
                seen.add(key)
                # thêm tuple (board, 0) chứ không chỉ là board
                population.append((ca_the, 0))
        return population

    def ham_tinh_fitness(ca_the, ma_tran_dich):
        # ca_the và ma_tran_dich là numpy arrays 0/1
        return int((ca_the * ma_tran_dich).sum())

    # Kiểm tra goal (fitness = 28)
    def is_goal(board, mang_dich):
        if np.array_equal(board, mang_dich):
            return board
        return None

    def tournament_selection(population, tournament_size=5):
        tournament = random.sample(population, min(tournament_size, len(population)))
        return max(tournament, key=lambda x: x[1])  # t

    def lai(bo, me):
        point = random.randint(1, 7)
        child = np.vstack((bo[:, :point], me[:, point:]))
        return child

    def dot_bien(board):
        new_board = board.copy()
        row = random.randint(0, 7)
        col = np.argmax(new_board[row])
        new_board[row][col] = 0
        new_col = random.randint(0, 7)
        new_board[row][new_col] = 1
        return new_board

    def di_truyen():
        population = ham_sinh_quan_the(5000)
        for the_he in range(100):
            population = [(board, ham_tinh_fitness(board, mang_2D)) for (board, _) in population]
            new_population = []
            new_population.append(max(population, key=lambda x: x[1]))
            while len(new_population) < 100:
                p1 = tournament_selection(population)
                p2 = tournament_selection(population)
                child = lai(p1[0], p2[0])
                if random.random() < 0.1:
                    child = dot_bien(child)
                t = is_goal(child, mang_2D)
                if t is not None:
                    return t
                else:
                    new_population.append((child, 0))

            population = new_population


from PIL import Image, ImageTk

root = tk.Tk()
root.title("Menu Game - AI Search")
root.geometry("800x600")

# ===== HÌNH NỀN =====
img = Image.open("bg_2.png")
img = img.resize((800, 600))
bg_img = ImageTk.PhotoImage(img)
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_img

# ===== CẤU HÌNH CHUNG =====
BUTTON_WIDTH = 18
BUTTON_HEIGHT = 2
BUTTON_BG = "#8B4513"
BUTTON_FG = "white"
FONT = ("Tahoma", 10, "bold")

# ===== CỘT TRÁI: TÌM KIẾM CỔ ĐIỂN =====
tk.Label(root, text="TÌM KIẾM CƠ BẢN", font=("Tahoma", 12, "bold"), bg="#D2B48C").place(x=150, y=120)

button_bfs = tk.Button(root, text="BFS", command=start_BFS, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_bfs.place(x=120, y=160)

button_dfs = tk.Button(root, text="DFS", command=start_DFS, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_dfs.place(x=120, y=200)

button_dls = tk.Button(root, text="DLS", command=start_DLS, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_dls.place(x=120, y=240)

button_ucs = tk.Button(root, text="UCS", command=start_UCS, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_ucs.place(x=120, y=280)

button_ids = tk.Button(root, text="IDS", command=start_IDS, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_ids.place(x=120, y=320)

# ===== CỘT PHẢI: THUẬT TOÁN NÂNG CAO =====
tk.Label(root, text="THUẬT TOÁN NÂNG CAO", font=("Tahoma", 12, "bold"), bg="#D2B48C").place(x=480, y=120)

button_greedy = tk.Button(root, text="Greedy Search", command=Greedy_Search, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_greedy.place(x=460, y=160)

button_astar = tk.Button(root, text="A* Search", command=start_A_sao, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_astar.place(x=460, y=200)

button_beam = tk.Button(root, text="Beam Search", command=start_Beam_Search, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_beam.place(x=460, y=240)

button_backtrack = tk.Button(root, text="Backtracking", command=start_Backtracking, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_backtrack.place(x=460, y=280)

button_fwck = tk.Button(root, text="Forward Checking", command=start_FWCK, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_fwck.place(x=460, y=320)

button_mu1 = tk.Button(root, text="Mù Một Phần", command=start_MU_1_Phan, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_mu1.place(x=460, y=360)

button_mutp = tk.Button(root, text="Mù Toàn Phần", command=start_MU_TP, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_mutp.place(x=460, y=400)

button_andor = tk.Button(root, text="AND-OR Search", command=start_AND_OR, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_andor.place(x=460, y=440)

button_genetic = tk.Button(root, text="Genetic Algorithm", command=start_Genetic, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
button_genetic.place(x=460, y=480)

# ===== NÚT THOÁT =====
exit_button = tk.Button(root, text="THOÁT", command=root.quit, width=15, height=2, bg="red", fg="white", font=("Tahoma", 11, "bold"))
exit_button.place(x=330, y=530)

root.mainloop()

