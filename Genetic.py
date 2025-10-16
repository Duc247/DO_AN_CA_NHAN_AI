import pygame, sys, numpy as np , random
found = 0
lan_vo = 0





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