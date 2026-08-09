import pygame

from enemy import Enemy
from player import Player
from settings import (
    ADD_ENEMY_EVENT,
    ADD_ENEMY_INTERVAL,
    BACKGROUND_IMAGE,
    BACKGROUND_SPEED,
    CURRENT_LANGUAGE,
    EXPLOSION_FRAME_INTERVAL,
    EXPLOSION_IMAGES,
    ENEMY_EXPLOSION_SOUND,
    ENEMY_EXPLOSION_VOLUME,
    FPS,
    GAME_MUSIC,
    GAME_MUSIC_VOLUME,
    LIGHT_GRAY,
    PLAYER_EXPLOSION_SOUND,
    PLAYER_EXPLOSION_VOLUME,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHOOT_EVENT,
    SHOOT_INTERVAL,
    START_MUSIC,
    START_MUSIC_VOLUME,
    STATUS_GAME_OVER,
    STATUS_PLAYING,
    STATUS_START,
    WHITE,
    YELLOW,
    get_text,
)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# TODO 5.1：在主循环开始前加载背景图片，并使用 convert() 转换图片格式。
# background_image = pygame.image.load(?).convert()

# TODO 5.4：在主循环开始前加载全部爆炸图片，使用 convert_alpha() 保留透明通道，并按配置列表中的顺序保存这些序列帧。
# explosion_images = [pygame.image.load(?).convert_alpha() for ? in ?]

background_y = 0
clock = pygame.time.Clock()
title_font = pygame.font.SysFont("Microsoft YaHei", 56)
normal_font = pygame.font.SysFont("Microsoft YaHei", 28)
pygame.display.set_caption(get_text(CURRENT_LANGUAGE, "caption"))
pygame.time.set_timer(ADD_ENEMY_EVENT, ADD_ENEMY_INTERVAL)
pygame.time.set_timer(SHOOT_EVENT, SHOOT_INTERVAL)

# TODO 5.3：预先加载敌机爆炸和玩家坠毁音效，并分别设置配置中指定的音量。音效只能加载一次，不要在碰撞循环中重复读取文件。
# 分别创建两个 Sound 对象，后续在对应碰撞发生时直接调用 play()。
# enemy_explosion_sound = pygame.mixer.Sound(?)
# player_explosion_sound = ?
# enemy_explosion_sound.set_volume(?)



def play_music(filename, volume):
    """循环播放背景音乐"""
    # TODO 5.3：根据 filename 参数加载背景音乐，根据 volume 参数设置音量，
    # 然后让音乐无限循环播放。pygame.mixer.music 同一时间只播放一首背景音乐，
    # 因此再次调用本函数时会自然切换到新的音乐。
    # pygame.mixer.music.load(?)
    # pygame.mixer.music.set_volume(?)
    # pygame.mixer.music.play(-1)


def draw_text(text, font, color, center):
    """在指定中心位置绘制文字"""
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect(center=center)
    screen.blit(text_image, text_rect)


def draw_text_topright(text, font, color):
    """在指定右上角位置绘制文字"""
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect(topright=(SCREEN_WIDTH - 20, 15))
    screen.blit(text_image, text_rect)


def draw_game_screen(player, enemies, bullets, explosions, score):
    """绘制游戏画面"""
    # TODO 5.2：在所有游戏对象之前绘制两张上下首尾相接的背景图片。
    # 要求：分别绘制在 background_y 和 background_y - 背景高度的位置，形成连续滚动效果。
    # 第一张图片向下移动露出空白时，第二张图片应刚好从上方补上，不能出现明显断层。
    # height = background_image.get_height()
    # screen.blit(background_image, (0, ?))
    # screen.blit(background_image, (0, ?))
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    player.draw(screen)
    # TODO 5.4：绘制每个爆炸动画当前帧，并让图片中心对准敌机被击毁时的中心。爆炸绘制在游戏对象之后、得分文字之前。
    # 可以先根据 frame 取得当前图片，再使用 get_rect(center=...) 计算居中的绘制区域。
    # for explosion in explosions:
    #     image = explosion_images[?]
    #     screen.blit(image, image.get_rect(center=?))
    score_text = get_text(CURRENT_LANGUAGE, "score", score=score)
    draw_text_topright(
        score_text,
        normal_font,
        WHITE
    )


def reset_game():
    """重新开始一局游戏"""
    return Player(), [], [], [], 0


def update_explosions(explosions):
    """更新爆炸动画并移除已经播放完的动画"""
    # TODO 5.4：更新每个爆炸的计时器；达到切帧间隔后切换到下一张图片。
    # 最后只返回尚未播放完的动画，避免无效对象不断累积。
    # 每次切帧后应将计时器归零；当前帧编号达到图片总数时，说明动画已经播放完成。
    # for explosion in explosions:
    #     ?
    #     if explosion["timer"] >= ?:
    #         ?
    #         ?
    # return [item for item in explosions if item["frame"] < len(explosion_images)]
    return explosions


def is_mask_collision(sprite1, sprite2):
    """精细碰撞判定： 判断两张图片的非透明部分是否碰撞"""
    offset_x = sprite2.rect.x - sprite1.rect.x
    offset_y = sprite2.rect.y - sprite1.rect.y
    return sprite1.mask.overlap(sprite2.mask, (offset_x, offset_y)) is not None


def main():
    global background_y
    # 调用 reset_game() 创建首局数据，并将初始状态设为 STATUS_START。
    player, enemies, bullets, explosions, score = reset_game()
    game_state = STATUS_START
    # TODO 5.3：进入开始界面时，调用上面的音乐播放函数，
    # 传入开始音乐路径和对应音量，使开始界面音乐持续循环。
    # play_music(?, ?)

    running = True
    while running:
        # TODO 5.2：非结束状态下更新背景纵向偏移量；移动完整张图片的高度后重置为 0。
        # 要求：开始界面和游戏中持续滚动，游戏结束后停止滚动。
        # 更新时让 background_y 增加 BACKGROUND_SPEED，并用背景图片高度判断是否完成一次循环。
        # if game_state != ?:
        #     background_y += ?
        #     if ? >= background_image.get_height():
        #         ? = 0

        # 3. 处理退出事件
        for event in pygame.event.get():
            # 收到退出事件时结束主循环。
            if event.type == pygame.QUIT:
                running = False

            # 重置游戏数据并进入 STATUS_PLAYING。
            if event.type == pygame.KEYDOWN:
                if game_state == STATUS_START or game_state == STATUS_GAME_OVER:
                    # TODO 5.3：开始或重新开始游戏时，调用音乐播放函数，
                    # 传入游戏音乐路径和音量，用游戏音乐替换开始界面音乐。
                    # play_music(?, ?)
                    player, enemies, bullets, explosions, score = reset_game()
                    game_state = STATUS_PLAYING
            if game_state == STATUS_PLAYING and event.type == ADD_ENEMY_EVENT:
                enemies.append(Enemy())
            if game_state == STATUS_PLAYING and event.type == SHOOT_EVENT:
                bullets.append(player.shoot())

        if game_state == STATUS_START:
            draw_game_screen(player, enemies, bullets, explosions, score)
            title_text = get_text(CURRENT_LANGUAGE, "title")
            prompt_text = get_text(CURRENT_LANGUAGE, "start_prompt")
            draw_text(title_text, title_font, WHITE, (SCREEN_WIDTH / 2, 300))
            draw_text(prompt_text, normal_font, LIGHT_GRAY, (SCREEN_WIDTH / 2, 390))
            pygame.display.update()
            clock.tick(FPS)
            continue  # 使用 continue 跳过后续战斗逻辑。

        # 刷新画面、限制帧率，并使用 continue 跳过战斗逻辑。
        if game_state == STATUS_GAME_OVER:
            draw_game_screen(player, enemies, bullets, explosions, score)
            game_over_text = get_text(CURRENT_LANGUAGE, "game_over")
            final_score_text = get_text(CURRENT_LANGUAGE, "final_score", score=score)
            restart_text = get_text(CURRENT_LANGUAGE, "restart_prompt")
            draw_text(game_over_text, title_font, WHITE, (SCREEN_WIDTH / 2, 300))
            draw_text(final_score_text, normal_font, LIGHT_GRAY, (SCREEN_WIDTH / 2, 390))
            draw_text(restart_text, normal_font, YELLOW, (SCREEN_WIDTH / 2, 450))
            pygame.display.update()
            clock.tick(FPS)
            continue

        # 4. 获取键盘按键，并更新飞机
        keys = pygame.key.get_pressed()
        player.update(keys)
        for enemy in enemies:
            enemy.update()
        for bullet in bullets:
            bullet.update()
        enemies = [enemy for enemy in enemies if not enemy.is_out_of_screen()]
        bullets = [bullet for bullet in bullets if not bullet.is_out_of_screen()]

        # 5. 检查子弹和敌人的碰撞
        hit_enemies = []
        hit_bullets = []
        for bullet in bullets:
            for enemy in enemies:
                if enemy in hit_enemies:
                    continue
                if bullet.rect.colliderect(enemy.rect):
                    hit_bullets.append(bullet)
                    hit_enemies.append(enemy)
                    score += 10
                    # TODO 5.3：敌机被击毁时播放一次爆炸音效。
                    # TODO 5.4：在敌机中心创建爆炸动画，记录固定中心位置、当前帧 0 和计时器 0。
                    # 将新动画加入 explosions 列表，使多个敌机同时被击毁时能够分别播放动画。
                    # 动画只负责显示，不能再次增加分数或参与碰撞检测。
                    # explosions.append({
                    #     "center": enemy.rect.center,
                    #     "frame": 0,
                    #     "timer": 0,
                    # })
                    break
        bullets = [bullet for bullet in bullets if bullet not in hit_bullets]
        enemies = [enemy for enemy in enemies if enemy not in hit_enemies]
        explosions = update_explosions(explosions)

        # 6. 检查玩家是否撞到敌人
        for enemy in enemies:
            if is_mask_collision(player, enemy):
                # TODO 5.3：玩家坠毁时播放一次坠毁音效并停止背景音乐。
                # ?
                # pygame.mixer.music.stop()

                # TODO 5.4：进入游戏结束状态前清空尚未播放完的爆炸动画。
                # 这些操作应放在状态改变的位置，避免每一帧重复触发。
                # 

                # 完成声音和动画状态处理后，再把 game_state 修改为 STATUS_GAME_OVER。
                game_state = STATUS_GAME_OVER
                break

        # 7. 绘制画面
        draw_game_screen(player, enemies, bullets, explosions, score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
