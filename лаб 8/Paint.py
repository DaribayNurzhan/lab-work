import pygame,sys

pygame.init()
#frames per second
fps = 144
clock = pygame.time.Clock()
#screen size
width = 800
height = 600
active_brush = 0#no size
active_color = 'white'#transparent

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint program')
painting = []#drawn paintings

def draw_menu(size, color):
    pygame.draw.rect(screen, 'gray', [0,0,width, 90])#drawing menu
    pygame.draw.line(screen, 'black', (0,90), (width, 90), 2)
    big_brush = pygame.draw.rect(screen, 'black', [20,20,50,50])#brush sizes
    pygame.draw.circle(screen, 'white', (45,45),20)
    medium_brush = pygame.draw.rect(screen, 'black', [80,20,50,50])
    pygame.draw.circle(screen, 'white', (105,45),15)
    small_brush = pygame.draw.rect(screen, 'black', [140,20,50,50])
    pygame.draw.circle(screen, 'white', (165,45),10)
    rect_brush = pygame.draw.rect(screen, 'black', [200,20,50,50])#rectangle brush
    pygame.draw.rect(screen, 'white', [210,30,30,30])
    brush_list = [big_brush, medium_brush, small_brush, rect_brush]
    if size == 20:#showing which brush is chosen
        pygame.draw.rect(screen, 'green', [20,20,50,50], 3)
    if size == 15:
        pygame.draw.rect(screen, 'green', [80,20,50,50], 3)
    if size == 10:
        pygame.draw.rect(screen, 'green', [140,20,50,50], 3)
    if size == 5:
        pygame.draw.rect(screen, 'green', [200,20,50,50], 3)
    #showing which color is chosen
    pygame.draw.circle(screen, color, (400,45),30)
    pygame.draw.circle(screen, 'darkgray', (400,45),30, 3)
    #colors list
    blue = pygame.draw.rect(screen, (0,0,255), [width-45,20,25,25])
    red = pygame.draw.rect(screen, (255,0,0), [width-45,45,25,25])
    green = pygame.draw.rect(screen, (0,255,0), [width-70,20,25,25])
    yellow = pygame.draw.rect(screen, (255,255,0), [width-70,45,25,25])
    l_blue = pygame.draw.rect(screen, (0,255,255), [width-95,20,25,25])
    black = pygame.draw.rect(screen, (0,0,0), [width-95,45,25,25])
    eraser = pygame.draw.rect(screen, (255,255,255), [width-130,20,25,25])
    color_rect = [blue,red,green,yellow,l_blue,black,eraser]
    rgb_list = [(0,0,255),(255,0,0),(0,255,0), (255,255,0),
                (0,255,255), (0,0,0), (255,255,255) ]

    return brush_list, color_rect, rgb_list
#drawing itself
def draw_painting(paints):
    for paint in paints:
        if paint[2] == 5: #if rectangular shape
            pygame.draw.rect(screen, paint[0], (paint[1][0]-paint[2]//2, paint[1][1]-paint[2]//2, 35, 35))
        else: #circular
            pygame.draw.circle(screen, paint[0], paint[1], paint[2]) 

    


running = True
while running:
    clock.tick(fps)#fps
    screen.fill('white')
    mouse = pygame.mouse.get_pos()#mouse position
    left_click = pygame.mouse.get_pressed()[0]#click for drawing
    #add new shape to painting list on mouse click
    if left_click and mouse[1] > 90:
        painting.append((active_color, mouse, active_brush))
    if mouse[1] > 90:#draw shapes, like showing it 
        if active_brush == 5:  
            pygame.draw.rect(screen, active_color, (mouse[0]-active_brush//2, mouse[1]-active_brush//2, 35, 35))
        else:  
            pygame.draw.circle(screen, active_color, mouse, active_brush)
    
    draw_painting(painting)

    brushes, colors, rgb = draw_menu(active_brush, active_color) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#for closing game
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: #erasing all paintings
            if event.key == pygame.K_SPACE:
                painting = []

        if event.type == pygame.MOUSEBUTTONDOWN:#changing shape, size and color
            for brush in range(len(brushes)):
                if brushes[brush].collidepoint(event.pos):
                    active_brush = 20 - (brush*5)
            
            for color in range(len(colors)):
                if colors[color].collidepoint(event.pos):
                    active_color =  rgb[color]
            
    

    pygame.display.flip()