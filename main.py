import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720]) #variavel tamanho da janela do jogo
title = pygame.display.set_caption("Soccer Pong") #variavel titulo do jogo na janela

win = pygame.image.load("assets/win.png")

score1 = 0
score1_imag = pygame.image.load("assets/score/0.png")
score2 = 0
score2_imag = pygame.image.load("assets/score/0.png")

field = pygame.image.load("assets/field2.png") #variavel imagem de fundo(campo)

#pausar jogo
pause_image = pygame.image.load("assets/pause.png") #pause
game_paused = False

#variavel jogador1
player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_moveup = False
player1_movedown = False

#variavel jogador2
player2 = pygame.image.load("assets/player2.png")
player2_y = 310
player2_moveup = False
player2_movedown = False

#variavel bola
ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -10
ball_dir_y = 3
ball_speed = 0
bounce = 0

def restartGame():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score2_imag
    global score1_imag
    global ball_speed
    global bounce
    ball_x = 617
    ball_y = 337
    ball_dir = -10
    ball_dir_y = 3
    ball_speed = 0
    bounce = 0
    score1 = 0
    score1_imag = pygame.image.load("assets/score/0.png")
    score2 = 0
    score2_imag = pygame.image.load("assets/score/0.png")


def move_player(): #funcao de mover player1 adiciondo -10 +10 ou 0 de movimento
    global player1_y

    if player1_moveup:
        player1_y -= 15
    else:
        player1_y += 0

    if player1_movedown:
        player1_y += 15
    else:
        player1_y += 0
    #fazer player1 nao passar da borda, definindo limite
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

def move_player2(): #funcao de mover player2 automaticamente junto com a bola
    global player2_y
   # player2_y = ball_y  mexer automaticamente player 2 atras da bola(se preferir jogar solo)

    if player2_moveup:
        player2_y -= 15
    else:
        player2_y += 0

    if player2_movedown:
        player2_y += 15
    else:
        player2_y += 0
        # fazer player2 nao passar da borda, definindo limite
    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 575:
        player2_y = 575


#funcao mover bola,chamando variaveis dentro da funcao (global pq esta modificando para + 1)
def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score2_imag
    global score1_imag
    global ball_speed
    global bounce

    ball_x += ball_dir   #sempre adicionar +1 de movimento em x
    ball_y += ball_dir_y #sempre adiciona valor de ball_dir_y

    #colisão da bola
    if ball_x < 120:
        if player1_y - 23 < ball_y:      #posição do jogador1 em y é menor que a posi da bola em y, tem que se metade to tamnho da bola para pegar a ponta
            if player1_y + 146 > ball_y: #posição do jogador1 em y é maior que a posi da bola em y, inverte sentido da bola quando colidir
                bounce += 1
                ratio = ((player1_y + 60) - ball_y) / 20 # -3 a 3
                ball_dir_y -= ratio * abs(ratio)
                ball_dir *= -1
                ball_dir += bounce

    if ball_x > 1100:
        if player2_y - 23 < ball_y:       #posição do jogador2 em y é menor que a posi da bola em y, tem que se metade to tamnho da bola para pegar a ponta
            if player2_y + 146 > ball_y:  #posição do jogador2 em y é maior que a posi da bola em y, inverte sentido da bola quando colidir
                bounce += 1
                ratio = ((player2_y + 60) - ball_y) / 20 # -3 a 3
                ball_dir_y -= ratio * abs(ratio)
                ball_dir *= -1
                ball_dir -= bounce

    #bola nao passar da borda
    if ball_y > 685:
        ball_dir_y *= -1 #sempre que bater na borda,vai inverter a posição
    elif ball_y <= 0:
        ball_dir_y *= -1 #sempre vai inverter a posição quando bater

    if ball_x < -50:     #bola volta para o meio, quando fosse gol
        ball_speed += 2
        ball_x = 617
        ball_y = 337
        ball_dir_y = 3
        ball_dir = -10 #(ball_dir-ball_speed)*(-1)
        score2 += 1       #adiciona +1 no placar quando bola sai da tela
        bounce = score1 + score2
        score2_imag = pygame.image.load("assets/score/" + str(score2) + ".png") #adiciona mais um número ao placar(prox imagem)

    elif ball_x > 1320:
        ball_speed += 2
        ball_x = 617
        ball_y = 337
        ball_dir_y = 3
        ball_dir = 10 #(ball_dir+ball_speed)*(-1)
        score1 += 1      #adiciona +1 no placar quando bola sai da tela
        bounce = score1 + score2
        score1_imag = pygame.image.load("assets/score/" + str(score1) + ".png") #adiciona mais um número ao placar(prox imagem)


#funcao para melhorar o aspecto do curso, todas as funcoes de imagem estao aqui
def draw():

    if score1 >= 9 or score2 >= 9:
        window.blit(score1_imag, (500, 50))
        window.blit(score2_imag, (710, 50))
        window.blit(win, (300, 330))
    elif game_paused:
        window.blit(pause_image, (0, 0))
    else:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_imag, (500, 50))
        window.blit(score2_imag, (710, 50))
        move_ball()
        move_player()
        move_player2()



#condicao loop de repetição para a janela do jogo continuar aberta
loop = True
while loop:

    #evento para fechar a janela
    for events in pygame.event.get(): #pra cada evento(events) dentro do evento ele vai pegar. Se evento for de fechar a janela loop = false
        if events.type == pygame.QUIT: #Se evento for de fechar a janela, loop = false
            loop = False

        #para cada evento de segurar tecla w ou s, mover o player1 no eixo y
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True

        #para cada evento de soltar tecla w ou s, para o player1 no eixo y
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

        # para cada evento de segurar tecla w ou s, mover o player1 no eixo y
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                player2_moveup = True
            if events.key == pygame.K_DOWN:
                player2_movedown = True

        # para cada evento de soltar tecla w ou s, para o player1 no eixo y
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_UP:
                player2_moveup = False
            if events.key == pygame.K_DOWN:
                player2_movedown = False

        # press R to restart
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_r: # and (score1 >= 9 or score2 >= 9):
                restartGame()

        # press space to pause
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE and score1 < 9 and score2 < 9:
                game_paused = not (game_paused)

    draw()
    pygame.display.update() #manter janela atualizada(aberta) sempre, vai executar o while enquanto loop = true
