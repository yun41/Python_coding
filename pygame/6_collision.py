import pygame

pygame.init()   #pygame을 사용할 때 기본적으로 초기화해주어야 한다.(반드시)

#화면 크기 설정
screen_width = 480  #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Flash game")

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/juyun/Desktop/과제 모음/파이썬/pygame/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/juyun/Desktop/과제 모음/파이썬/pygame/character.png")
character_size = character.get_rect().size  #이미지 크기를 구해옴
character_width = character_size[0]         #캐릭터의 가로 크기
character_height = character_size[1]        #캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2          #캐릭터를 가로의 길이의 절반에 해당하는 곳에 위치
character_y_pos = screen_height - character_height     #캐릭터를 세로의 길이의 가장 아래에 위치

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#적(enemy) 캐릭터
enemy = pygame.image.load("C:/Users/juyun/Desktop/과제 모음/파이썬/pygame/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width) / 2
enemy_y_pos = (screen_height - enemy_height) / 2


#이벤트 루프
running = True
while running:
    dt = clock.tick(60)     #게임화면의 초당 프레임 수

    for event in pygame.event.get():    #pygame모듈 이용할 때 필수
        if event.type == pygame.QUIT:   #창을 닫을 때
            running = False

        if event.type == pygame.KEYDOWN:    #키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:  #왼쪽으로 이동
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #화면 벗어나지 않게 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    
    #screen.fill((0,255,255)) - 이 방법으로 화면을 채워넣을 수도 있다. r,g,b
    screen.blit(background, (0,0))      #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()
#pygame 종료
pygame.quit()
