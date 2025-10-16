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
                    color = (215,168,110) if (i + j) % 2 == 0 else (141,85,36)
                    pygame.draw.rect(panel, color, rect)
                    pygame.draw.rect(panel, (0,0,0), rect, 1)  # viền đen
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
    mang_bd_1 = np.zeros((8,8))
    mang_bd_2 = np.zeros((8,8))
    for i in range(4):
        mang_bd_1[i][i] = 1
        mang_bd_2[i+4][i+4] = 1
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
