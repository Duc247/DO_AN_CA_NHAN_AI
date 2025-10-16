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
    FPS = pygame.time.Clock()
    li = []  # lưu tọa độ đỉnh (i,j) theo cách sinh 1
    am = pygame.mixer.Sound("tieng_co.mp3")
    panel = pygame.Surface((240, 240))
    panel_1 = pygame.Surface((240, 240))
    Cau_hinh = {}  # lưu cấu hình
    N = 8
    mang_2D = np.zeros((8, 8))
    mang_2D_1 = np.zeros((8,8))
    mang_2D_2 = np.zeros((8,8))
    mang = np.zeros((8, 8))
    anh_nen = pygame.image.load("BG.png").convert_alpha(man_hinh)
    anh_nen_scale = pygame.transform.scale(anh_nen, (800, 600))

    def chieu_xe(x, y,mang):
        for i in range(1, N):
            if y + i < N and mang[x][y + i] != 1:
                mang[x][y + i] -= 1
            if y - i >= 0 and mang[x][y - i] != 1:
                mang[x][y - i] -= 1
            if x + i < N and mang[x + i][y] != 1:
                mang[x + i][y] -= 1
            if x - i >= 0 and mang[x - i][y] != 1:
                mang[x - i][y] -= 1

    def go_chieu_hau(x, y,mang):
        for i in range(1, N):
            if y + i < N:
                mang[x][y + i] += 1
            if y - i >= 0:
                mang[x][y - i] += 1
            if x + i < N:
                mang[x + i][y] += 1
            if x - i >= 0:
                mang[x - i][y] += 1

    def de_xe(x,mang):
        global found
        if x == N:
            found += 1
            return
        if 1 in mang[x]:
            de_xe(x + 1,mang)
            return
        for j in range(N):
            if mang[x][j] == 0:
                mang[x][j] = 1
                chieu_xe(x, j,mang)
                de_xe(x + 1,mang)
                if found == 24:
                    break
                go_chieu_hau(x, j,mang)
                mang[x][j] = 0

    x = random.randint(1, 7)
    y = random.randint(1, 7)
    mang_2D[x][y] = 1
    chieu_xe(x, y,mang_2D)
    de_xe(0,mang_2D)

    x = random.randint(1, 7)
    y = random.randint(1, 7)
    mang_2D_1[x][y] = 1
    chieu_xe(x, y,mang_2D_1)
    de_xe(0,mang_2D_1)

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

    actions = ["dat","di_chuyen"]
    def Ma_Tran_Ke_Tiep_MU_1_phan(Ma_Tran_Hien_Tai,act):
            if act == "dat":
                if np.sum(Ma_Tran_Hien_Tai) == 8:
                    return Ma_Tran_Hien_Tai
                while True :
                        x = random.randint(0,7)
                        y = random.randint(0, 7)
                        if 1 not in Ma_Tran_Hien_Tai[x] and 1 not in Ma_Tran_Hien_Tai[:,y]:
                            Ma_Tran_Tam_Thoi = Ma_Tran_Hien_Tai.copy()
                            Ma_Tran_Tam_Thoi[x][y] = 1
                            return Ma_Tran_Tam_Thoi

            elif act == "di_chuyen":
                if np.sum(Ma_Tran_Hien_Tai) == 8:
                    return Ma_Tran_Hien_Tai
                while True:
                       x = random.randint(0, 7)
                       y = random.randint(0, 7)
                       if 1 not in Ma_Tran_Hien_Tai[x] and 1 not in Ma_Tran_Hien_Tai[:, y] and x!=1 and y!=2:
                           while True:
                                x_can_doi = random.randint(0,7)
                                if 1 in Ma_Tran_Hien_Tai[x_can_doi]:
                                    for j in range(8):
                                        if 1 == Ma_Tran_Hien_Tai[x_can_doi][j]:
                                            Ma_Tran_Tam_Thoi = Ma_Tran_Hien_Tai.copy()
                                            Ma_Tran_Tam_Thoi[x_can_doi][j] =0
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
                    color = (215,168,110) if (i + j) % 2 == 0 else (141,85,36)
                    pygame.draw.rect(panel, color, rect)
                    pygame.draw.rect(panel, (0,0,0), rect, 1)
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

    mang_bd_1 = np.zeros((8,8))
    mang_bd_2 = np.zeros((8,8))
    mang_bd_1[1][2] =1
    mang_bd_2[1][2] =1
    mang_bd_1[0][0]=1
    MANG_BD = [mang_bd_1,mang_bd_2]
    #Tap_Dich = là 1 mảng có ma trận có 1 pt nằm ở ô 12
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


start_BFS_MU()
