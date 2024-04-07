# Импорт необходимых модулей
import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна и FPS
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60

# Создание игрового окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg_color = (255, 192, 203)

# Установка начальных скоростей платформы и мяча
DEFAULT_PADDLE_SPEED = 20
DEFAULT_BALL_SPEED = 6

paddle_speed = DEFAULT_PADDLE_SPEED
ball_speed = DEFAULT_BALL_SPEED

# Установка размеров платформы
PADDLE_WIDTH = 200
PADDLE_HEIGHT = 25
paddle = pygame.Rect(WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2, WINDOW_HEIGHT - PADDLE_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

# Создание мяча
BALL_RADIUS = 20
ball = pygame.Rect(random.randrange(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS), WINDOW_HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)
dx, dy = 1, -1

# Создание текста "Game Over"
font = pygame.font.SysFont('comicsansms', 40)
game_over_text = font.render('Game Over', True, (255, 255, 255))
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Создание неразрушаемых кирпичей
unbreakable_bricks = [pygame.Rect(10 + 80 * i, 50 + 40 * j, 70, 30) for i in range(10) for j in range(2)]

# Создание бонусного кирпича
bonus_brick = pygame.Rect(200, 100, 60, 30)
bonus_active = False

# Словарь бонусов
bonus_perks = {
    'speed_up': 3,
    'paddle_shrink': 40
}

# Звук при пойманном бонусе
catch_sound = pygame.mixer.Sound(r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\PygameTutorial_3_0\catch.mp3")

# Функция активации бонуса
def activate_bonus(perk):
    global ball_speed, PADDLE_WIDTH
    if perk == 'speed_up':
        ball_speed += bonus_perks[perk]
    elif perk == 'paddle_shrink':
        PADDLE_WIDTH -= bonus_perks[perk]

# Функция главного меню
def main_menu():
    global paddle_speed, ball_speed
    menu_font = pygame.font.SysFont('comicsansms', 30)
    setting_index = 0
    settings = [("Paddle Speed", paddle_speed), ("Ball Speed", ball_speed)]

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    setting_index = (setting_index - 1) % len(settings)
                elif event.key == pygame.K_DOWN:
                    setting_index = (setting_index + 1) % len(settings)
                elif event.key == pygame.K_LEFT:
                    settings[setting_index] = (settings[setting_index][0], max(1, settings[setting_index][1] - 1))
                elif event.key == pygame.K_RIGHT:
                    settings[setting_index] = (settings[setting_index][0], settings[setting_index][1] + 1)
                elif event.key == pygame.K_RETURN:
                    paddle_speed, ball_speed = settings[0][1], settings[1][1]
                    return
                elif event.key == pygame.K_p:
                    pause_menu()

        # Отрисовка меню
        screen.fill(bg_color)
        for i, (setting_name, setting_value) in enumerate(settings):
            color = (0, 255, 0) if i == setting_index else (255, 255, 255)
            text_surface = menu_font.render(f"{setting_name}: {setting_value}", True, color)
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + i * 50))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

# Функция меню паузы
def pause_menu():
    menu_font = pygame.font.SysFont('comicsansms', 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                return

        screen.fill(bg_color)
        pause_text = menu_font.render('Game Paused', True, (0, 0, 0))
        pause_text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        resume_text = menu_font.render('Press P to Resume', True, (0, 0, 0))
        resume_text_rect = resume_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

        screen.blit(pause_text, pause_text_rect)
        screen.blit(resume_text, resume_text_rect)
        pygame.display.update()
        clock.tick(FPS)

# Отображение главного меню
main_menu()

# Основной игровой цикл
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause_menu()

    screen.fill(bg_color)

    # Отрисовка платформы и мяча
    pygame.draw.rect(screen, pygame.Color(234, 250, 177), paddle)
    pygame.draw.circle(screen, pygame.Color(250, 241, 157), ball.center, BALL_RADIUS)

    # Отрисовка неразрушаемых кирпичей
    for brick in unbreakable_bricks:
        pygame.draw.rect(screen, pygame.Color(100, 100, 100), brick)

    # Отрисовка бонусного кирпича, если он активен
    if bonus_active:
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), bonus_brick)

    # Обработка нажатий клавиш и движение мяча и платформы
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WINDOW_WIDTH:
        paddle.right += paddle_speed

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    # Обработка столкновений мяча с краями экрана, платформой и кирпичами
    if ball.centerx < BALL_RADIUS or ball.centerx > WINDOW_WIDTH - BALL_RADIUS:
        dx = -dx
    if ball.centery < BALL_RADIUS + 50:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dy = -dy
        catch_sound.play()  # Воспроизведение звука

    for brick in unbreakable_bricks:
        if ball.colliderect(brick):
            dx, dy = -dx, -dy

    # Обработка столкновения мяча с бонусным кирпичом
    if bonus_active and ball.colliderect(bonus_brick):
        bonus_active = False
        activate_bonus(random.choice(list(bonus_perks.keys())))

    # Обработка завершения игры при падении мяча
    if ball.y > WINDOW_HEIGHT or ball.x > WINDOW_WIDTH:
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, game_over_text_rect)

    pygame.display.update()
    clock.tick(FPS)
