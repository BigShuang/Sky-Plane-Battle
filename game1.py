import pygame

# 1. 游戏基本设置
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
FPS = 60

PLAYER_IMAGE = "assets/player1.png"
PLAYER_SPEED = 10

class Player:
    """玩家飞机"""
    def __init__(self):
        # 加载飞机图片
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()

        # 飞机初始位置：屏幕底部中间
        self.x = (SCREEN_WIDTH - self.rect.width) / 2
        self.y = SCREEN_HEIGHT - self.rect.height

        # 飞机速度，数值越大移动越快
        self.speed = PLAYER_SPEED

    def move(self, keys):
        """根据键盘按键移动飞机"""
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

    def stay_in_screen(self):
        """限制飞机不能飞出屏幕"""
        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH - self.rect.width:
            self.x = SCREEN_WIDTH - self.rect.width
        if self.y < 0:
            self.y = 0
        if self.y > SCREEN_HEIGHT - self.rect.height:
            self.y = SCREEN_HEIGHT - self.rect.height

    def update(self, keys):
        """更新飞机状态"""
        self.move(keys)
        self.stay_in_screen()
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def draw(self, screen):
        """绘制飞机"""
        screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("飞机大战 基础版1")
clock = pygame.time.Clock()

# 2. 创建玩家飞机
player = Player()

running = True
while running:
    # 3. 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. 获取键盘按键，并更新飞机
    keys = pygame.key.get_pressed()
    player.update(keys)

    # 5. 绘制画面
    screen.fill((20, 28, 44))
    player.draw(screen)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
