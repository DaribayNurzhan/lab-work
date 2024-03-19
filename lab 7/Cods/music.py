import pygame

pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("MUZZ.com")

bg_image = pygame.image.load(r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\lab 7\detaly\pngtree-png-music-player-background-png-image_8468984.png"     )
icon = pygame.image.load(r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\lab 7\detaly\png-transparent-music-android-music-video-google-play-music-player-disc-jockey-music-library-singer.png")
pygame.display.set_icon(icon)

_songs = [
    r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\lab 7\detaly\jeltoksan., Taspay, Aidhn - Aitkym Kelgeni.mp3",
    r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\lab 7\detaly\y2mate.com - Ariana Grande  Justin Bieber  Stuck with U Official Video.mp3",
    r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\lab 7\detaly\y2mate.com - Coldplay X BTS  My Universe Official Video.mp3",
    r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\lab 7\detaly\y2mate.com - Dua Lipa  Break My Heart Official Video.mp3",
    r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\lab 7\detaly\y2mate.com - Giveon  Heartbreak Anniversary Official Music Video.mp3",
    r"C:\Users\satzh\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\пп\lab 7\detaly\y2mate.com - Jack Harlow  First Class Official Music Video.mp3"
]
current_song_index = 0
pygame.mixer.music.load(_songs[current_song_index])

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(_songs)
    pygame.mixer.music.load(_songs[current_song_index])
    pygame.mixer.music.play()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(_songs)
    pygame.mixer.music.load(_songs[current_song_index])
    pygame.mixer.music.play()


running = True
while running:
    bg_x = (screen.get_width() - bg_image.get_width()) / 2
    bg_y = (screen.get_height() - bg_image.get_height()) / 2
    screen.blit(bg_image, (bg_x, bg_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                previous_song()
    
    pygame.display.update()