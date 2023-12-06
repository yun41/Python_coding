import pygame

pygame.init()   #pygame을 사용할 때 기본적으로 초기화해주어야 한다.(반드시)

#화면 크기 설정
screen_width = 480  #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Flash game")

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/juyun/Desktop/과제 모음/파이썬/pygame/background.png")

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():    #pygame모듈 이용할 때 필수
        if event.type == pygame.QUIT:   #창을 닫을 때
            running = False
    #screen.fill((0,255,255)) - 이 방법으로 화면을 채워넣을 수도 있다. r,g,b
    screen.blit(background, (0,0))      #배경 그리기

    pygame.display.update()
#pygame 종료
pygame.quit()
