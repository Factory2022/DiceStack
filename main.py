import pygame
import random


#   class Dice:
#    def __init__(self,wert):
#        self.wert = wert

# pygame.mixer.pre_init(44100, -16, 2, 2048)
# pygame.mixer.init()
pygame.init()       # PyGame initialiesieren
width = 1920        # Bildbreite
height = 1080        # Bildhöhe height
color = (25, 40, 25)  # Farbe für den Hintergrund
white = (255, 255, 255)         # Weiß
black = (0, 0, 0)               # schwarz
gray = (50,50,50)               # grau
light_green = (50, 80, 50)      # Helles Grün
dark_green = (20,40,20)         # dunkelgrün
blue = (50, 50, 200)            # blau
dark_blue = (10,10,50)          # dunkelblau
shadow_y = 45
shadow_x = -5

# Test Audio
pygame.mixer.init()
# pygame.mixer.music.load("SPACE 2020 Titel.mp3")
# pygame.mixer.music.play()
klick_sound = pygame.mixer.Sound("acces/stack.mp3")
bad_sound = pygame.mixer.Sound("acces/bad.wav")
good_sound = pygame.mixer.Sound("acces/good.wav")
menu_music = (pygame.mixer.music.load("acces/DiceStackTitle.mp3"))
dice_roll_sound = (pygame.mixer.Sound("acces/DicesFall.mp3"))
# pygame.mixer.music.play()
menu_active = True     # wird das Menü gerade angezeigt

count = 0

x_pos = 0
y_pos = 0
radius = 1
is_clicked = False
click_is_ok = False
color_for_circle = 0

# Test für Rotation der Grafiken
rotation = 0

in_menu = True          # sollte erst auf true stehen!
last_round = False      # wenn ein Spieler 10 Würfel gestapelt hat = True
game_over = False       # wenn ein Spieler 10 Würfel gesetzt hat und der letzte Spieler gesetzt hat = True
game_over_timer = 0     # zählt hoch, bis ins Menü gesprungen wird...
game_over_timer_2 = 0
info = False            # zeigt die Infobox an
new_game = True

fall1, fall2, fall3 = False, False, False   # fällt ein würfel gerade?
f1_x, f2_x, f3_x = 0, 0, 0                  # X-Werte für den fallenden Würfel
f1_y, f2_y, f3_y = -100, -100, -100                  # y-Werte
f1_pos, f2_pos, f3_pos = 0, 0, 0            # an welche Position landet der Würfel
f1_y_max, f2_y_max, f3_y_max = 0, 0, 0        # Endpunkt für den Y wert
fall_y_max = [0,0,0]                        # maximaler Y Wert bis zum Erreichen des Stapels

# für das Menü
player_minus_pos_x = 0      # Player + und minus x und y - daraus wird der Klickbereich errechnet
player_minus_pos_y = 0
player_plus_pos_x = 0
ng_button_x = 0         # neues Spiel Button x und y
ng_button_y = 0
quit_button_x = 0       # Pos vom QUIT-Button
quit_button_y = 0
guide_button_x = 0      # Pos vom Guide-Button
guide_button_y = 0
guide = False           # Anleitung anzeigen
quit_on = False         # wurde QUIT gedrückt?
quit_test = False       # Damit man nicht direkt die Abfrage wieder verlässt


# Liste für die Anleitung in Zeilen
g_txt = ["Anleitung zum Spiel:",
         "Jeder Spieler kann einmal würfeln (auf 'Würfeln' klicken) und die Würfel danach stapeln.",
         "Gültig ist das Setzten wenn der neue Würfel den gleichen Wert wie der untere Würfel hat,",
         "einen Wert höher, oder einen Wert niedrieger ist.",
         "Ist kein stapeln mehr möglich, drückt man auf 'nächster Spieler'.",
         "Wenn ein Spieler 10 Würfel gestapelt hat, wird noch bis zum letzten Spieler gespielt.",
         "Danach endet das Spiel.",
         "Gewonnen hat der Spieler mit den meisten Punkten (Die Augen werden zusammengezählt)."]


dices_in_game = 60      # Anzahl der möglichen Würfel auf dem Spielfeld
space = 0
dice_y = 865
value1, value2, value3 = 0, 0, 0

dice1, dice2, dice3 = 0, 0, 0
dice1_visible = True    # nach dem Anklicken sollen die Würfel verschwinden...
dice2_visible = True    # daher visible
dice3_visible = True

must_roll = True        # nach Spielerwechsel muss gewürfelt werden!
is_rolled = False       # es wurde noch nicht gewürfelt...

roll = False            # rollen die Würfel gerade?
roll_legal = False      # wenn die Würfel gerade rollen, dann kein neues Würfeln möglich!
roll_count = 0          # Zei, die beim würfeln vergeht...

dice_view = [0, 1, 2, 3, 4, 5]  # Augen 1,2,3,4,5,6
dices_set = 0           # Anzahl der gültigen Züge (sind bei drei Würfeln 3 :) )

# Listen definieren
dices_img = []          # Liste für die Grafiken
dice_count = []         # Würfel im Spiel und der Wert
dice_side = []          # Seitenansicht - Wert
dice_top = []           # Topansicht - Wert
dice_side_img = []      # Würfel von der Seite
dice_top_img = []       # Würfel von oben
dice_x_offset = []      # Würfel sollen nicht genau gerade übereinander stehen

players_points = [407, 40, 230, 5, 32, 17]  # Maximal 6 Spieler und die entsprechenden Punkte...
players_maximum = 6
player_active = 1               # gerade aktueller Spieler
players_in_game = 2             # Anzahl der Spieler im Spiel
points_offset = " "             # Leerstellen bei niedrigen Punktestand
next_player_count = 50          # zeigt an, wie lange der NEXT-Butten eine andere Farbe nach dem drücken bekommt
next_player_button = False      # Button ist nicht gedrückt

player_name = ["Spieler 1", "Spieler 2", "Spieler 3", "Spieler 4", "Spieler 5", "Spieler 6"]
enter_name = False
name_clicked = ""
name_at_position  = 0
remind_player = 0
wrong_player  = False
name_selected = [False, False ,False ,False ,False ,False]
merker = 0
merker2 = 10
mark1 = 0
mark2 = 0
testtext = ""
cursor_on = ""       # Spielername mit _ am Ende
cursor_off = ""     # Spielername ohne _
cursor_count = 0    # Zähler zum umschalten von Curso an und - aus
cursor_text =""

# Datei
data = "acces/config.txt"


# Würfellisten füllen :) ' bald nur noch leere Liste erzeugen!
for i in range(0, dices_in_game+1):
    dice_count.append(6)
    dice_x_offset.append(random.randint(-8, 8))
    dice_side.append(random.randint(0, 5))
    dice_top.append(random.randint(0, 5))

def read_data():
    global players_in_game
    file = open(data, "r")
    for i in range(0,6):
        player_name[i] = file.readline()
        player_name[i] = player_name[i][: -1]
        # print (player_name[i])
    players_in_game = int(file.readline())
    file.close()

def write_data():

    file = open(data, "w")
    for i in range(0, 6):
        file.write(player_name[i] + "\n")
    file.write(str(players_in_game) + "\n")
    file.close()

def dice_roll():   # bald nur noch zum löschen!
    global dice1_visible, dice2_visible, dice3_visible
    for i in range(0, len(dice_count)):
        dice_count[i] = (6)
        dice_x_offset[i] = (random.randint(-8, 8))
        dice_side[i] = (random.randint(0, 5))
        dice_top[i] = (random.randint(0, 5))
        dice1_visible = True
        dice2_visible = True
        dice3_visible = True

def dice_roll_3():
    global dice1,dice2,dice3
    dice1 = random.randint(0, 5)
    dice2 = random.randint(0, 5)
    dice3 = random.randint(0, 5)

    # Seiten und oben auswürfeln - keine gleichen Zahlen!

    for i in range(0, 6):
        dice_view[i] = random.randint(0, 5)

    while dice_view[0] == dice1 or dice_view[0] == dice_view[3]:
        dice_view[0] = random.randint(0, 5)

    while dice_view[1] == dice2 or dice_view[1] == dice_view[4]:
        dice_view[1] = random.randint(0, 5)

    while dice_view[2] == dice3 or dice_view[2] == dice_view[5]:
        dice_view[2] = random.randint(0, 5)

    while dice_view[3] == dice1 or dice_view[3] == dice_view[0]:
        dice_view[3] = random.randint(0, 5)

    while dice_view[4] == dice2 or dice_view[4] == dice_view[1]:
        dice_view[4] = random.randint(0, 5)

    while dice_view[5] == dice3 or dice_view[5] == dice_view[2]:
        dice_view[5] = random.randint(0, 5)

# Hier kommt das Menü ***************************************************************************************
def menu():
    global player_minus_pos_x, player_minus_pos_y, ng_button_x, ng_button_y, quit_button_x, quit_button_y
    global player_plus_pos_x, g_txt, mouse_presses, x_pos, y_pos, button_new_game_img, bg_img
    global guide_button_x, guide_button_y, quit_on, menu_active

    if menu_active == True:
        play_bg_music()
        menu_active = False

    screen.fill(black)
    screen.blit(bg_img, (0, 540))
    show_infobox(10,70,1800,80,50,black)
    menu_txt = schrift_gross.render("D I C E   S T A C K", True, (50, 50, 50))
    screen.blit(menu_txt, (405, 105))
    menu_txt = schrift_gross.render("D I C E   S T A C K", True, (255, 255, 255))
    screen.blit(menu_txt, (400, 100))

    sa_x = 400      # x und y Wert für den Text und die Boxen
    sa_y = 350

    show_infobox(sa_x - 10, sa_y - 15, 500, 50, 20, black)
    show_infobox(sa_x + 540, sa_y - 15, 310, 50, 20, gray)

    screen.blit(button_small_up_img, (sa_x + 552, sa_y - 10))
    if mouse_presses[0] and x_pos > player_minus_pos_x and x_pos < player_minus_pos_x + 80:
                if y_pos > player_minus_pos_y and y_pos < player_minus_pos_y + 80:
                   screen.blit(button_small_down_img, (sa_x + 552, sa_y - 10))

    screen.blit(button_small_up_img, (sa_x + 795, sa_y - 10))
    if mouse_presses[0] and x_pos > player_plus_pos_x and x_pos < player_plus_pos_x + 80:
                if y_pos > player_minus_pos_y and y_pos < player_minus_pos_y + 80:
                   screen.blit(button_small_down_img, (sa_x + 795, sa_y - 10))

    player_minus_pos_x = sa_x + 552 # Feld ist 80 x 80 Pixel
    player_minus_pos_y = sa_y-5
    player_plus_pos_x = sa_x + 798

    menu_txt = schrift_klein.render(" Spieleranzahl :    -     " + str(players_in_game) + "     +", True,white)
    screen.blit(menu_txt, (sa_x, sa_y))

# New Game Button anzeigen
    ng_button_x = sa_x # + 100
    ng_button_y = sa_y + 150
    ng_txt = schrift_klein.render(" Neues Spiel beginnen", True, white)

    show_infobox(ng_button_x - 10, ng_button_y- 15, 700, 50, 20, black)
    screen.blit(ng_txt, (ng_button_x, ng_button_y))

# Quit Button anzeigen
    quit_button_x = ng_button_x # + 100
    quit_button_y = ng_button_y + 150
    quit_txt = schrift_klein.render(" Spiel verlassen", True, white)
    show_infobox(quit_button_x - 10, quit_button_y - 15, 700, 50, 20, black)
    screen.blit(quit_txt, (quit_button_x, quit_button_y))

    # Wenn Quit gedrückt wurde
    if quit_on == True:
        show_infobox(quit_button_x - 100, quit_button_y - 200, 1050, 255, 20, black)
        leave_txt = schrift_klein.render("Das Spiel wirklich beenden?", True, white)
        screen.blit(leave_txt, (quit_button_x - 20, quit_button_y - 170))

        # JA - BOX
        show_infobox(quit_button_x - 50, quit_button_y - 70, 400, 100, 20, black)
        leave_txt = schrift_gross.render("JA", True, white)
        screen.blit(leave_txt, (quit_button_x + 75, quit_button_y - 55))

        # NEIN - BOX
        show_infobox(quit_button_x + 520, quit_button_y - 70, 400, 100, 20, black)
        leave_txt = schrift_gross.render("NEIN", True, white)
        screen.blit(leave_txt, (quit_button_x +585, quit_button_y - 55))

# Guide-Button anzeigen

    guide_button_x = quit_button_x  # + 100
    guide_button_y = quit_button_y + 150
    show_infobox(guide_button_x - 10, guide_button_y - 15, 700, 50, 20, black)

    if guide == False:
       guide_txt = schrift_klein.render(" Anleitung anzeigen", True, white)
    else:
        guide_txt = schrift_klein.render("  wieder ausblenden", True, white)

    screen.blit(guide_txt, (guide_button_x, guide_button_y))

# Anleitung
    if guide == True:
        show_guide()

# Spieler anzeigen
    text_x = 1500
    for i in range(1, players_in_game+1):
        if i <= players_in_game:
           show_infobox(text_x -20, i * 100 +250,300,30, 20 , black )

           # text = schrift_mini.render("Spieler" + str(i), True, (200,200,200))
           text = schrift_mini.render(player_name[i-1], True, (200, 200, 200))
           screen.blit(text, ((text_x , i*100 + 275)))
           # pygame.draw.rect(screen, white, (text_x-40,i*100 + 240, 400, 100), 4)



def show_guide():
    show_infobox(180, 335, 1100, 330, 50, black)

    # Text anzeigen
    gx = 220
    gy = 400
    for i in range(0, len(g_txt) - 1):
        guide_txt = schrift_mini.render(g_txt[i], True, white)
        if i == 1:
            gy = gy + 20
        screen.blit(guide_txt, (gx, gy + i * 40))

def show_infobox(x_pos,y_pos,xend,yend,r,color):
    radius = r
    x = x_pos + radius
    y = y_pos + radius
    x_end = xend
    y_end = yend


# Blit in white
    pygame.draw.circle(screen, white, (x, y,), radius, draw_top_left=True)              # weiß
    pygame.draw.circle(screen, white, (x + x_end, y,), radius, draw_top_right=True)
    pygame.draw.circle(screen, white, (x, y + y_end,), radius, draw_bottom_left=True)
    pygame.draw.circle(screen, white, (x + x_end, y + y_end,), radius, draw_bottom_right=True)
    pygame.draw.rect(screen, white, (x - radius, y, x_end + radius*2, y_end))  # langes Rechteck
    pygame.draw.rect(screen, white, (x, y - radius, x_end , y_end + radius *2))  # hohes Rechteck
# Blit in Color x
    pygame.draw.circle(screen, color, (x + 4, y + 4,), radius, draw_top_left=True)  # schwarz
    pygame.draw.circle(screen, color, (x + x_end - 4, y + 4,), radius, draw_top_right=True)
    pygame.draw.circle(screen, color, (x + 4 , y + y_end - 4,), radius, draw_bottom_left=True)
    pygame.draw.circle(screen, color, (x + x_end -4, y + y_end - 4,), radius, draw_bottom_right=True)
    pygame.draw.rect(screen, color, (x - radius + 4, y + 4, x_end - 8 + radius * 2, y_end - 4))  # langes Rechteck
    pygame.draw.rect(screen, color, (x, y - radius +4 , x_end , y_end + radius * 2 - 8))  # hohes Rechteck

def show_last_round():
    show_infobox(200,10,900,30,10, black)

    text = schrift_mini.render("L  E  T  Z  T  E     R  U  N  D  E   !", True, (255, 255, 255))
    screen.blit(text, (450, 22))

def test_dice_fall(value, pushed, this_player):
    global dice1_visible, dice2_visible, dice3_visible, fall1, fall2, fall3, f1_x, f2_x, f3_x, f1_pos, f2_pos, f3_pos
    global fall_y_max
    global dice_top, dice_side, dice1, dice2, dice3, dice_view

    px = this_player
    j = value

    y = j + 10 - player_active*10
    y = y * 80 + 50

    # print ("Y wert = " + str(y))
    if pushed == 1:
        dice1_visible = False
        fall1 = True
        f1_pos = j - 1
        f1_x = x_offset + px * 150
        fall_y_max [0] = y

        dice_side[j-1] = dice_view[0]
        dice_top[j-1] = dice1

    if pushed == 2:
        dice2_visible = False
        fall2 = True
        f2_pos = j - 1
        f2_x = x_offset + px * 150
        fall_y_max[1] = y

        dice_side[j - 1] = dice_view[1]
        dice_top[j - 1] = dice2

    if pushed == 3:
        dice3_visible = False
        fall3 = True
        f3_pos = j - 1
        f3_x = x_offset + px * 150
        fall_y_max[2] = y

        dice_side[j - 1] = dice_view[2]
        dice_top[j - 1] = dice3

def blit_dice_fall():
    global  fall1, fall2, fall3, f1_x, f2_x, f3_x, f1_y, f2_y, f3_y, f1_pos, f2_pos, f3_pos
    global dice3, dice2, dice1, dice_view, fall_y_max
    fall_speed = 40


    if fall1 == True:

        screen.blit(dices_img[dice_count[f1_pos]], (f1_x+dice_x_offset[f1_pos], f1_y))  # Front
        screen.blit(dice_side_img[dice_view[0]], (f1_x+dice_x_offset[f1_pos] + 80, f1_y - 16))  # seite
        screen.blit(dice_top_img[dice1], (f1_x+dice_x_offset[f1_pos] , f1_y - 16))  # top
        f1_y += fall_speed

        if f1_y > fall_y_max[0]:
            fall1 = False
            f1_y = - 100
            f1_pos = -10
            pygame.mixer.Sound.play(klick_sound)


    if fall2 == True:
        screen.blit(dices_img[dice_count[f2_pos]], (f2_x + dice_x_offset[f2_pos], f2_y))  # Front
        screen.blit(dice_side_img[dice_view[1]], (f2_x + dice_x_offset[f2_pos] + 80, f2_y - 16))  # seite
        screen.blit(dice_top_img[dice2], (f2_x + dice_x_offset[f2_pos], f2_y - 16))  # top
        f2_y += fall_speed
        if f2_y > fall_y_max[1]:
            fall2 = False
            f2_y = - 100
            f2_pos = -10
            pygame.mixer.Sound.play(klick_sound)

    if fall3 == True:
        screen.blit(dices_img[dice_count[f3_pos]], (f3_x + dice_x_offset[f3_pos], f3_y))  # Front
        screen.blit(dice_side_img[dice_view[2]], (f3_x + dice_x_offset[f3_pos] + 80, f3_y - 16))  # seite
        screen.blit(dice_top_img[dice3], (f3_x + dice_x_offset[f3_pos], f3_y - 16))  # top
        f3_y += fall_speed
        if f3_y > fall_y_max[2]:
            fall3 = False
            f3_y = - 100
            f3_pos = -10
            pygame.mixer.Sound.play(klick_sound)


def blit_roll_button():
    global roll
    if roll == True:
        light_green = (80, 100, 80)
    else:
        light_green = (50, 100, 50)
    txt_color = (255, 255, 255)
    if roll == False and must_roll == False:
        light_green = dark_green
        txt_color = (100, 100, 100)

    show_infobox(space + 320, dice_y - 10, 300, 82, 10, dark_green) # Rahmen um den Button zeichnen
    # Rechteck zeich.  Ort     Farbe      xa  ya     lx   ly   Stärke / ohne stärke ist das Feld gefüllt!
    #pygame.draw.rect(screen, light_green, (800, 800, 400, 200), 3)
    pygame.draw.rect(screen, light_green, (space + 400, dice_y , 160, 80))

    text = schrift_mini.render("WÜRFELN", True, txt_color)
    screen.blit(text, ((space + 420, dice_y + 25)))

def blit_next_player():
    global next_player_button, must_roll, next_player_count
    text_color = (255,255,255)
    if next_player_button == True:
        color2 = (0,0,100)
    else:
        color2 = blue

    if must_roll == True and next_player_count == 50:
        color2 = (10,10,50)
        text_color = (50,50,50)
    show_infobox(space + 320, dice_y - 115, 300, 82, 10, dark_blue)  # Rahmen um den Button zeichnen
    # Rechteck zeich.  Ort     Farbe      xa  ya     lx   ly   Stärke / ohne stärke ist das Feld gefüllt!
    pygame.draw.rect(screen, color2, (space + 400, dice_y - 105, 160, 80))

    text = schrift_mini.render("NÄCHSTER", True, text_color)
    screen.blit(text, ((space + 415, dice_y-120 + 25)))
    text = schrift_mini.render("SPIELER", True, text_color)
    screen.blit(text, ((space + 430, dice_y - 80 + 25)))

def blit_active_player():
    global must_roll, x_offset, game_over
    if game_over == False:
       # if must_roll == True:
       #     text2 = " Bitte würfeln!"
       # else:
       text2 = player_name[player_active - 1]

       text = schrift_midi.render( text2 , True, black)
       screen.blit(text, ((x_offset + 94 + player_active * 150, 1004)))

       text = schrift_midi.render(text2, True, white)
       screen.blit(text, ((x_offset + 90 + player_active * 150, 1000)))

def blit_circle(x,y,r,col):
    global  x_pos, y_pos, click_is_ok, count

    if click_is_ok == True:
        if color_for_circle == 1:
            pygame.draw.ellipse(screen, (255,0,0), (x-r, y-r, r*2,r*2),5)
            
        if color_for_circle == 2:
            pygame.draw.ellipse(screen, (0,255,0), (x-r, y-r, r*2,r*2),5)


def blit_game_over():
    global players_points, game_over_timer, in_menu, game_over_timer_2, menu_active, game_over
    show_infobox(100, 200, 1600, 300, 50, black)

    text = schrift_gross.render("G A M E   O V E R !", True, (255, 255, 255))
    screen.blit(text, ((400, 280)))

    hi_points = 0
    winner = 0
    # print((str(players_in_game)))
    for i in range(0, players_in_game):
        if players_points[i] > hi_points:
            hi_points = players_points[i]
            winner = i+1

    text = schrift_klein.render("Spieler " + str(winner) + " hat mit " + str(hi_points) + " Punkten gewonnen!", True, (255, 255, 255))
    screen.blit(text, ((350, 450)))

    game_over_timer += 1
    if game_over_timer == 50:
       game_over_timer = 0
       if game_over_timer_2 == 10:
           game_over_timer = 0
           game_over_timer_2 = 0
           in_menu = True
           if menu_active == False:
              menu_active = True
           game_over = False

       game_over_timer_2 += 1
        
    text = schrift_mini.render("Das Spiel geht in " + str(int(10 - game_over_timer_2)) + " Sekunden zurück in das Menü. ", True,white)
    screen.blit(text, (740, 530))

def show_playerpoints():
    # pygame.draw.rect(screen, white, (1200, 0, width - 1200, hight / 3 * 2), 5)
    show_infobox(1200,0, 670, 680,20,black)
    for i in range(1, players_maximum+1):
        if i<players_maximum:
            pygame.draw.line(screen, white, (1200, i*120), (width - 15 , i*120), 5)
        if i <= players_in_game:
            points_offset = "   "
            if len(str(players_points[i - 1])) == 3:
                points_offset = ""
            if len(str(players_points[i - 1])) == 2:
                points_offset = " "
            # text = schrift_mini.render("Spieler " + str (i) +":    " + points_offset + str(players_points[i-1]) + " Punkte.", True, white)
            text = schrift_noch_kleiner.render( player_name[i-1] , True, white)
            text2 = schrift_noch_kleiner.render(": " + points_offset + str(players_points[i - 1]) + " Punkte.", True, white)

            screen.blit(text, ((1010 + 220 , i*120 -75)))
            screen.blit(text2, ((1400 + 220, i * 120 - 75)))

# Punkte zählen - muss noch in eine extra Funktion! Sonst wird bei jedem Frame gerechnet - unnötig!
            players_points[i - 1] = 0
            for j in range(0, 10):
                if dice_count[j+i*10-10] <6:
                    players_points[i-1] = players_points[i-1] + dice_count[j+i*10-10]+1
    # aktiven Spieler markieren
    pygame.draw.rect(screen, light_green, (1215, player_active * 120 - 110 , 680, 105), 5)

def dice_pushed(wert, pushed):
    value = wert
    dice_pushed = pushed

    global player_active, dices_set, dice1_visible, dice2_visible, dice3_visible, color_for_circle, click_is_ok, last_round
    global  fall1, fall2, fall3, f1_x, f2_x, f3_x, f1_y, f2_y, f3_y, f1_pos, f2_pos, f3_pos
    global x_offset, dice_view, dice1, dice2, dice3

    for j in range(0 + player_active * 10 - 10, player_active * 10):

         if dice_count[j] < 6 or j == player_active * 10 - 1:

            test = dice_count[j]

            if dice_count[j] < 6:
                # nun erfolgt der Vergleich, ob der Zug gültig ist...
                # wenn beide Würfel den gleichen Wert haben
                if test == value - 1 and test != 6:
                    dice_count[j-1] = value - 1

                    test_dice_fall(j, dice_pushed, player_active)

                    click_is_ok = True
                    color_for_circle = 2
                    play_good_sound()

                    if j-1 == player_active * 10 - 10:
                        last_round = True
                        next_player(3)

                    break

                # Der neue Würfel ist einen Wert niedriger...
                if test == value - 2:
                    dice_count[j-1] = value - 1

                    if dice_pushed == 1:
                        dice1_visible = False
                    if dice_pushed == 2:
                        dice2_visible = False
                    if dice_pushed == 3:
                        dice3_visible = False
                    click_is_ok = True
                    color_for_circle = 2
                    play_good_sound()

                    if j-1 == player_active * 10 - 10:

                        last_round = True
                        next_player(3)

                    test_dice_fall(j, dice_pushed, player_active)
                    break

                # Der neue Würfel ist einen Wert höher...
                if test == value:
                    dice_count[j-1] = value - 1

                    if dice_pushed == 1:
                        dice1_visible = False
                    if dice_pushed == 2:
                        dice2_visible = False
                    if dice_pushed == 3:
                        dice3_visible = False
                    click_is_ok = True
                    color_for_circle = 2
                    play_good_sound()

                    if j-1 == player_active * 10 - 10:

                        last_round = True
                        next_player(3)

                    test_dice_fall(j, dice_pushed, player_active)
                    break

                # wenn kein Zug möglich ist
                dices_set -= 1
                color_for_circle = 1
                click_is_ok = True
                play_bad_sound()

                break

            # erster Würfel
            if j < player_active * 10:
               dice_count[j] = value - 1

               if dice_pushed == 1:
                   dice1_visible = False
               if dice_pushed == 2:
                   dice2_visible = False
               if dice_pushed == 3:
                   dice3_visible = False
               click_is_ok = True
               color_for_circle = 2
               play_good_sound()

               test_dice_fall(j+1, dice_pushed, player_active)

            if j < player_active * 10 - 9:
                next_player(3)
            # print (j)
            break


def next_player(counter):
    # print (counter)
    global dices_set, player_active, must_roll, last_round, game_over, dice1_visible, dice2_visible, dice3_visible
    if counter == 3:

        dices_set = 0
        player_active += 1

        if player_active > players_in_game and last_round == True:
            game_over = True

        if player_active > players_in_game and last_round == False:
            player_active = 1

        must_roll = True
        dice1_visible = False
        dice2_visible = False
        dice3_visible = False

def play_dice_fall_sound():
    pygame.mixer.Sound.play(dice_roll_sound)

def play_good_sound():
    pygame.mixer.Sound.play(good_sound, maxtime=200)

def play_bad_sound():
    pygame.mixer.Sound.play(bad_sound, maxtime=200)

def play_bg_music():
    pygame.mixer.music.play(fade_ms=200)
    # pygame.mixer.music.play()

def stop_bg_music():
    pygame.mixer.music.fadeout(1000)
    #pygame.mixer.music.stop()

# Namen eingeben
def enter_plyername(name_is, position):
    global cursor_off, cursor_on, cursor_count, cursor_text

    name = name_is
    name_pos = position

    cursor_on = player_name[name_pos]+"_"
    cursor_off = player_name[name_pos]

    # Cursor blinken
    cursor_count += 1
    if cursor_count < 20:
       cursor_text = cursor_on
    else:
         cursor_text = cursor_off

    if cursor_count >= 40:
       cursor_count = 0


    show_infobox(200,440, 1180, 100,40,black)
    text = schrift_klein.render(cursor_text, True, white)
    screen.blit(text, (350, 500))

# **********************************************************************************************************************

# Bildschirmmodus setzen - 1920 x 1080, Fullscreen .pygame.FULLSCREEN
# screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
screen = pygame.display.set_mode((width, height), flags=pygame.SCALED, vsync=True)  # Fenstermodus
pygame.display.set_caption("DICE STACK")
clock = pygame.time.Clock()

# Grafiken laden ************************************************
for i in range(1, 7):
    dice_side_img.append(pygame.image.load("acces/"+str(i)+"-seite.png"))
    dice_top_img.append(pygame.image.load("acces/"+str(i) + "-oben.png"))
    dices_img.append(pygame.image.load("acces/"+str(i)+".png"))

button_up_img = (pygame.image.load("acces/button_up.png"))
button_down_img = (pygame.image.load("acces/button_down.png"))

button_small_up_img = button_up_img
button_small_down_img = button_down_img
button_small_up_img = pygame.transform.scale(button_small_up_img, (80, 80))
button_small_down_img = pygame.transform.scale(button_small_down_img, (80, 80))

button_new_game_img = button_up_img
button_new_game_img = pygame.transform.scale(button_new_game_img, (800, 90))

bg_img = (pygame.image.load("acces/bg_m3.png"))   # Spielfläche - Tisch
arrow_img = (pygame.image.load("acces/Pfeil1.png")) # Pfeil, der auf den Spieler Zeigt
shadow_img = (pygame.image.load("acces/shadow1.png"))

test_img = dices_img[5]
test_img = (pygame.transform.rotate(test_img, 90))

# Schriften definieren...
schrift_gross = pygame.font.Font("freesansbold.ttf", 128)
schrift_klein = pygame.font.Font("freesansbold.ttf", 64 )
schrift_midi = pygame.font.Font("freesansbold.ttf", 36 )
schrift_noch_kleiner = pygame.font.Font("freesansbold.ttf", 28 )
schrift_mini = pygame.font.Font("freesansbold.ttf", 24 )

# Spielernamen und Anzahl laden
read_data()

running = True  # Spiel ist gestartet
dice_roll_3()   # ein mal würfeln, bitte...

# Hauptschleife
while running:

    mouse_presses = pygame.mouse.get_pressed() # [0] True, wenn Maustaste gedrückt wird - solange sie gedrückt wird!
    #if mouse_presses[0]:


    # Tastenabfrage / Mausabfrage
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:  # Gedrückte Maustaste wird erkannt.
            pos  = pygame.mouse.get_pos()
            #print(pos, pos[0], pos[1])
            x_pos = int(pos[0])
            y_pos = int(pos[1])
            radius = 1
            is_clicked = True


            #print(x_pos, y_pos)
            # (space + 400, dice_y , 160, 80))
# Würfeln Button wird gedrückt
            if x_pos > space+400 and x_pos < space +400+160 and roll == False and must_roll == True and in_menu == False and game_over == False:
                if y_pos > dice_y and y_pos < dice_y+80:
                    dice1_visible = True
                    dice2_visible = True
                    dice3_visible = True
                    roll = True
                    roll_count = 0
                    dice_roll_3()
                    click_is_ok = True
                    color_for_circle = 2
                    play_good_sound()
                    play_dice_fall_sound()


# Nächster Spieler wird gedrückt
            if x_pos > space + 400 and x_pos < space + 400 + 160 and roll == False and next_player_button == False and must_roll == False and in_menu == False and game_over == False:
                if y_pos > dice_y -110 and y_pos < dice_y - 25:
                    next_player(3)
                    next_player_count = 0
                    next_player_button = True
                    click_is_ok = True
                    color_for_circle = 2
                    play_good_sound()


# Würfel werden angeklickt
            if y_pos > dice_y and y_pos < dice_y + 80 and must_roll == False and in_menu == False and game_over == False:
                if x_pos > space + dice1 and x_pos < space + dice1 + 80 and dice1_visible == True :

                    dices_set += 1
                    dice_pushed(value1,1)
                    next_player(dices_set)


                if x_pos > space + 100 + dice2 and x_pos < space + dice2 +180 and dice2_visible == True :

                    dices_set += 1
                    dice_pushed(value2,2)
                    next_player(dices_set)


                if x_pos > space + 200 + dice3 and x_pos < space + dice3 + 280 and dice3_visible == True :

                    dices_set += 1
                    dice_pushed(value3,3)
                    next_player(dices_set)


            if in_menu == True and guide == False:
                if menu_active == True:
                    play_bg_music()
                    menu_active = False
                # Player plus und minus
                # Player minus
                if x_pos > player_minus_pos_x and x_pos < player_minus_pos_x + 80 and quit_on == False and enter_name == False:
                    if y_pos > player_minus_pos_y and y_pos < player_minus_pos_y + 80:
                        players_in_game -= 1
                        if players_in_game < 1:
                            players_in_game = 1

                # Player plus
                if x_pos > player_plus_pos_x and x_pos < player_plus_pos_x + 80 and quit_on == False and enter_name == False:
                    if y_pos > player_minus_pos_y and y_pos < player_minus_pos_y + 80:
                        players_in_game += 1
                        if players_in_game > 6:
                            players_in_game = 6

                # Playername ist clicked
                text_x = 1500
                for i in range(1, players_in_game + 1):

                    if i <= players_in_game:
                       if x_pos > text_x -20 and x_pos < text_x + 300:
                            if y_pos > i * 100 + 250 and y_pos < i*100+300:

                               # print(player_name[i-1] + " wurde angeklickt")
                               if mark1 == 0:
                                  mark2 = i-1
                                  mark1 = 1
                                  name_at_position = mark2
                                  name_clicked = player_name[mark2]
                                  # print (mark2)

                               if  enter_name == False and mark2 == i-1:
                                   enter_name = True
                                   for k in range(0, players_in_game):
                                       if player_name[mark2] == "Spieler " + str(k+1):
                                          player_name[mark2] = ""
                               else:
                                   if mark2 == i-1:
                                      if player_name[mark2] == "":
                                         player_name[mark2] = "Spieler " + str(mark2+1)
                                   # print(mark2)
                                   enter_name = False
                                   mark1 = 0



                # New Game Button
                if x_pos > ng_button_x-20 and x_pos < ng_button_x + 775 and quit_on == False and enter_name == False:
                    if y_pos > ng_button_y-20 and y_pos < ng_button_y-20 + 100:
                        value1, value2, value3 = 0, 0, 0
                        dice1, dice2, dice3 = 0, 0, 0
                        dice1_visible = False
                        dice2_visible = False
                        dice3_visible = False
                        must_roll = True
                        last_round = False
                        game_over = False
                        player_active = 1
                        dices_set = 0
                        fall1 = False
                        fall2 = False
                        fall3 = False
                        game_over_timer = 0
                        game_over_timer_2 = 0
                        stop_bg_music()


                        for i in range(0, dices_in_game + 1): # alle Würfel im Stapel löschen
                            dice_count [i] = 6
                            dice_x_offset[i] = random.randint(-8, 8)
                            # dice_side[i] = random.randint(0, 5)
                            # dice_top[i] = random.randint(0, 5)

                        in_menu = False
                        quit_on = False



                # QUIT Button wird geklickt
                if x_pos > quit_button_x - 20 and x_pos < quit_button_x + 875 and quit_on == False and enter_name == False:
                    if y_pos > quit_button_y - 20 and y_pos < quit_button_y - 20 + 100:
                       quit_on = True
                       quit_test = True
                            # running = False

                # Quit = Nein
                if x_pos > guide_button_x + 520 and x_pos < guide_button_x + 920 and quit_on == True and quit_test == False:
                   if y_pos > guide_button_y - 220 and y_pos < guide_button_y - 75:
                      quit_on = False
                      # print("Quit nein!")

                # Quit = JA
                if x_pos > guide_button_x - 50 and x_pos < guide_button_x + 370 and quit_on == True and quit_test == False:
                   if y_pos > guide_button_y - 220 and y_pos < guide_button_y - 75:
                      running = False


                quit_test = False

            if in_menu == True and quit_on == False and enter_name == False:
               if x_pos > guide_button_x - 20 and x_pos < guide_button_x + 775:
                  if y_pos > guide_button_y - 20 and y_pos < guide_button_y - 20 + 100:
                     if guide == True:
                         guide = False
                     else:
                        guide = True



        # Tastaturabfrage für die Steuerung
        if event.type == pygame.KEYDOWN:
            if enter_name == False:
                # ins Menü mit ESC-Taste
                if event.key == pygame.K_ESCAPE:
                    in_menu = True
                    menu_active = True

                #if event.key == pygame.K_g:     # g für ANLEITUNG
                #    if in_menu == True:
                #        if guide == True:
                #            guide = False
                #        else:
                #            guide = True

                #if event.key == pygame.K_l:     #  l = Letzte Runde
                #     if last_round == True:
                #        last_round = False
                #     else:
                #        last_round = True

                #if event.key == pygame.K_n:     #  i = Infobox wird angezeigt
                #    if enter_name == True:
                #        enter_name = False
                #    else:
                #        enter_name = True

                #if event.key == pygame.K_o:     #  o = Game Over
                #     if game_over == True:
                #        game_over = False
                #     else:
                #        game_over = True

                #if event.key == pygame.K_m:
                #    if in_menu == False:
                #        in_menu = True

                #    else:
                #        in_menu = False

            if enter_name == True:
                if event.key == pygame.K_RETURN:    # bei Enter wird die Eingabe abgeschlossen
                    if player_name[mark2] == "":
                        player_name[mark2] = "Spieler " + str(mark2 + 1)
                    enter_name = False
                    mark1 = 0

                elif event.key == pygame.K_BACKSPACE:
                    player_name[mark2] = player_name[mark2][:-1]
                # player_name[i - 1]
                else:
                    if len(player_name[mark2]) < 18 and event.key != pygame.K_ESCAPE and event.key != pygame.K_TAB:
                       player_name[mark2]  += event.unicode
                # print(testtext)


    #Bildschirm löschen
    screen.fill(black)
    screen.blit(bg_img, (0, 540))

    show_playerpoints()


    # Würfel anzeigen
    x_offset = 300 - players_in_game*50
    y_offset = 0
    #for i in range(0, len(dice_count)-1): :
    for i in range(0, players_in_game*10):
        if i %10 ==0 :
            x_offset += 150
            y_offset = 0

        if dice_count[i] < 6 and i != f1_pos and i != f2_pos and i != f3_pos:

            # Schatten blitten
            test = 10-y_offset
            screen.blit(shadow_img, (35+ test*10 + x_offset + dice_x_offset[i], 922 - test *15))  # Shaddow

            screen.blit(dice_side_img[dice_side[i]], (50+80+ x_offset + dice_x_offset[i], y_offset*85 + 100 - 16))  # seite
            screen.blit(dice_top_img[dice_top[i]],   (50 +   x_offset + dice_x_offset[i], y_offset*85 + 100 - 16))  # top
        y_offset += 1

    x_offset = 300 - players_in_game*50
    y_offset = 0
    for i in range(0, players_in_game*10):
        if i % 10 == 0:
            x_offset += 150
            y_offset = 0

        if dice_count[i] < 6 and i != f1_pos and i != f2_pos and i != f3_pos:    # TEST!
            screen.blit(dices_img[dice_count[i]],(50 + x_offset + dice_x_offset[i], y_offset * 85 + 100))  # war i*100 - nicht y_offset
        y_offset += 1
        space = x_offset + 300



    # Aktiver Spieler
    if game_over == False:
        x_offset = 350 - players_in_game * 50
        screen.blit(arrow_img, (x_offset+ player_active*150 , 950)) # Pfeil anzeigen

        text = schrift_klein.render(str(player_active), True, black)
        screen.blit(text, ((x_offset+ 23 + player_active*150 , 970)))



    # Rahmen für die Anzeige zeichnen
    show_infobox(space - 20, dice_y - 10 , 300, 82, 10, black)

    text = schrift_midi.render("Bitte würfeln!", True, (255, 255, 255))
    text2 = schrift_midi.render("- Spieler "+ str(player_active) + " -", True, (255, 255, 255))
    if must_roll == True and roll == False and game_over == False:
       screen.blit(text2, ((space + 40, dice_y )))
       screen.blit(text, ((space + 20 , dice_y + 40)))

    if must_roll == False or roll == True:
        # Würfel im Spiegel anzeigen
        if dice1_visible == True:
           # screen.blit(dices_img[dice_view[3]], ((space + 10, dice_y - 120)))
           screen.blit(dices_img[dice_view[3]], ((space, dice_y)))
        if dice2_visible == True:
           screen.blit(dices_img[dice_view[4]], ((space + 100, dice_y)))
        if dice3_visible == True:
           screen.blit(dices_img[dice_view[5]], ((space + 200, dice_y)))

        value1 = dice_view[3] + 1    # war 3,4 ,5
        value2 = dice_view[4] + 1
        value3 = dice_view[5] + 1

    # Würfel mischen/würfeln
    if roll:
        roll_count +=1
        if roll_count% 5 == 0:
            dice_roll_3()
        if roll_count > 50:
            roll = False
            must_roll = False

    if next_player_button == True:
        next_player_count += 1
        if next_player_count == 50:
            next_player_button = False

    blit_roll_button()      # Würfeln Fläche anzeigen
    blit_next_player()      # Next Player Button anzeigen
    blit_active_player()    # der aktuelle Spieler wird angezeigt
    blit_dice_fall()        # Fallende Würfel anzeigen




    if last_round == True and game_over == False:
        # blit_last_round()
        show_last_round()

    if info == True:
        # x,y,xend,yend,r
        show_infobox(200,500,500,500, 10, black)

    if game_over == True:
        blit_game_over()

    if is_clicked == True:
        blit_circle(x_pos, y_pos, radius, color_for_circle)
        radius +=5
        if radius > 60:
            radius = 0
            is_clicked = False
            click_is_ok = False
            color_for_circle = 0

    if in_menu == True:
       menu()
       # Spieler wurde angeklickt
       if enter_name == True:
           enter_plyername(name_clicked, name_at_position)

    pygame.display.update()
    clock.tick(60)

write_data() # Namen speichern
pygame.quit()

