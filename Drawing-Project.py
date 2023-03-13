import pygame
import time
import random
import json
import os
pygame.init()

display_width = 750
display_height = 750
GameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Drawnar.io')

#xrwmata
mauro = (0,0,0)
light_mauro = (75,75,75)
aspro = (255,255,255)
dark_aspro = (200,200,200)
kokkino = (255,0,0)
kokkino_skouro = (200,0,0)
prasino = (0,255,0)
prasino_skouro = (0,200,0)
mple = (0,0,255)
mple_skouro = (0,0,200)
kitrino = (255,255,0)
galazio = (0,255,255)
mwb = (255,0,255)
portokali_skouro = (255,102,0)
portokali = (255,150,0)
gkri_anoixto = (128,128,128)
gkri_skouro = (80,80,80)
kafe = (139,69,19)
kafe_skouro = (82,54,16)
orange_light = (255,128,0)
orange_dark = (153,76,0)
kafetogkri = (155,122,122)
violeti = (238,130,238)
meso_mwb = (147,112,219)
apalo_mple = pygame.Color("#6AFFFF")

#fonts
font = pygame.font.SysFont("Dejavusans", 20)
bigfont = pygame.font.SysFont('Dejavusans', 30)
terafont = pygame.font.SysFont('Dejavusans',80)
different_font = pygame.font.SysFont('comicsansms',20)

# VARIABLES
colors = {
    portokali_skouro:[500,615],
    kafe_skouro:[540,615],
    kokkino_skouro:[580,615],
    prasino_skouro:[620,615],
    mple_skouro:[660,615],
    portokali:[500,655],
    kafe:[540,655],
    kokkino:[580,655],
    prasino:[620,655],
    mple:[660,655],
    mauro:[500,695],
    galazio:[540,695],
    mwb:[580,695],
    kitrino:[620,695],
    gkri_anoixto:[660,695]
    }

# variable gia na metra to xrono pou prepei na mesolabhsei anamesa sta undo's button clicks(1/4 deuteroleptou)
time_count = 0

# variable pou metra to xrono pou prepei na mesolabhsei anamesas stis allages xrwmatwn epiloghs (2 deut)
time_between_color_changing = 20 #(2 * FPS dhladh)

# variable pou metra ton xrono pou prepei na mesolabhsei protou mporeseis na zwgrafiseis prwth fora afotou exeis epileksei ena neo project
first_time_draw_after_selected_new_file = 0 # tha ftanei mexri to 10 (1 * FPS)

# epilegmeno xrwma
selected_color = aspro
previous_color = None

# epilegmenos fakelos
selected_file = None

# mia lista pou krata ta onomata apo ta project pou dhmiourghthikan se auto to RUN to paixnidou, wste na mhn mporei o xrhsths na ta epileksei
recently_created_projects = []

# to variable to opoio deixnei ean to erase einai energopoihmeno h oxi
activate_erase_button = False

# to variable pou metra ton xrono pou prepei na mesolabhsei protou mporeis na ksanapathseis to erase(1 deut)
time_between_erase_buttons = 0
# energeies
actions = []

# variables pou aforoun th Save Files leitourgia tou paixnidiou
waiting = 0
text = ''
text2 = ''
text3 = ''
text2_bool = False
text3_bool = False
clicked_the_box = False

pick_grid_size = {
    'big_blocks': [True, 325, 250],
    'medium_blocks': [False, 325, 350],
    'small_blocks': [False, 325, 450]
}
# exei ws timh to onoma apo to megethos tou plegmatos
current_grid_size = 'big_blocks'
current_grid_columns = 15
current_grid_rows = 12
# metablhth pou deixnei thn apostash twn blocks
difference = 50


grid2 = [
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro]]

grid_with_small_blocks = [
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro]]


# ena deutero grid se periptwsh pou o xrhsths dokimasei na kanei kainouria zwgrafia,afotou exei kanei load kapoia allh
grid = [
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro],
    [aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro,aspro]]
# exei ws timh to onoma apo th lista poy periexei ta koutakia gia to plegma, analoga to megethos tou plegmatos
current_used_grid = 'grid2'
####################################################FUNCTIONS##############################################################
def save_as(x,y,width,height, color, text_color,font):
    global waiting, clicked_the_box, text, text2, text3, text2_bool, text3_bool, recently_created_projects
    running = True
    text = ''
    text2 = ''
    text3 = ''
    while running:
        text_label = font.render(text, True, text_color)
        text_label2 = font.render(text2, True, text_color)
        text_label3 = font.render(text3, True, text_color) 
        mhnyma_label = font.render('Type in the name of your project.',True, mauro)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # zwgrafizw mia orthogwnia epifaneia pou tha perilambanei to text-box
        GameDisplay.fill(kafetogkri)
        pygame.draw.rect(GameDisplay, color, [x,y,width,height])
        if waiting < 2:
            waiting += 1
        if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
            if click[0] == 1:
                clicked_the_box = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and clicked_the_box == True and waiting == 2:
                if event.key == pygame.K_BACKSPACE:
                    if text3_bool == True and len(text3) >= 1:
                        text3 = text3[:-1]
                    elif text2_bool == True and len(text2) >= 1:
                        text2 = text2[:-1]
                    elif len(text) >= 1:
                        text = text[:-1]
                
                elif event.key == pygame.K_RETURN:
                    final_string = text 
                    if text2 != '':
                        final_string += text2
                    if text3 != '':
                        final_string += text3
                    clicked_the_box = False
                    final_string += '.text'
                    recently_created_projects.append(final_string)
                    new_file = open(final_string,'w')
                    ####for line in grid2:
                    if current_used_grid == 'grid2':
                        for line in grid2:
                            content = json.dumps(line)
                            new_file.write(content+'\n')
                    elif current_used_grid == 'grid_with_small_blocks':
                        for line in grid_with_small_blocks:
                            content = json.dumps(line)
                            new_file.write(content+'\n')
                    list_is_empty = False
                    with open('names_of_files.py', 'r') as Projects:
                        if Projects.readlines() == []:
                            list_is_empty = True
                        if list_is_empty == True:
                            with open('names_of_files.py','w') as Projct:
                                Projct.write(final_string+'\n')
                        elif list_is_empty == False:
                            with open('names_of_files.py','a') as Pro:
                                Pro.write(final_string+'\n')
                    MainMenu()
                else:
                    if text3_bool == True:
                        text3 += event.unicode
                    elif text2_bool == True:
                        text2 += event.unicode
                    else:
                        text += event.unicode
                    waiting = 0
        if text_label.get_width() >= width - 1:
            if text2_bool == False:
                text2_bool = True
        if text_label2.get_width() >= width - 1:
            if text3_bool == False:
                text3_bool = True

        GameDisplay.blit(text_label, (x + 1, y))
        GameDisplay.blit(text_label2, (x + 1 , y + text_label.get_height() + 5))
        GameDisplay.blit(text_label3, (x + 1, y + text_label.get_height() + text_label.get_height() + 5 ))
        GameDisplay.blit(mhnyma_label,(x,y - mhnyma_label.get_height() - 5))
        button('<--Back', font, 0, 720, 60, 30, mauro, gkri_anoixto, gkri_skouro, 'BACK')
        pygame.display.update()

def button(text,font,x,y,width, height, text_color, ac, ic, event=None,extra_item=None, extra_item2=None):
    global activate_erase_button, time_between_erase_buttons, selected_file
    if activate_erase_button == True and event == 'ERASE':
        ac, ic = (225,0,0), (0,255,0)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text_label = font.render(text, True, text_color)
    if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
        pygame.draw.rect(GameDisplay, ac, [x,y,width,height])
        if click[0] == 1:
            if event == 'FILL':
                fill(extra_item)
            elif event == 'RESET':
                reset()
            elif event == 'ERASE':
                erase()
                if time_between_erase_buttons == 10:
                    activate_erase_button = not activate_erase_button
                    time_between_erase_buttons = 0
            elif event == 'UNDO':
                undo()
            elif event == 'NEW_PROJECT':
                selected_file = None
                choose_grid_size()
            elif event == 'BACK':
                MainMenu()
            elif event == 'SAVE AS':
                save_as(300,300,200,50,aspro,mauro,font)
            elif event=='LOAD_FILES':
                load_files()
            elif event == 'LOAD':
                if extra_item2 != 'RECENT':
                    selected_file = extra_item
                    print(selected_file)
                    begin()
            elif event== 'SAVE':
                save()
            elif event == 'DELETE':
                delete(extra_item, extra_item2)

    else:
        pygame.draw.rect(GameDisplay, ic, [x,y,width,height])
    GameDisplay.blit(text_label, (x + int(width/2) - int(text_label.get_width() / 2), y + int(height/2) - int(text_label.get_height()/2)))

def save():
    if selected_file != None:
        new_file = open(selected_file[:-1],'w')
        ###for line in grid2:
        if current_used_grid == 'grid2':
            for line in grid2:
                content = json.dumps(line)
                new_file.write(content+'\n')
        elif current_used_grid == 'grid_with_small_blocks':
            for line in grid_with_small_blocks:
                content = json.dumps(line)
                new_file.write(content+'\n')

def fill(color):
    if current_used_grid == 'grid_with_small_blocks':
        for lista in grid_with_small_blocks:
            count = 0
            for item in lista:
                lista[count] = color
                count += 1
    elif current_used_grid == 'grid2':
        for lista in grid2:
            count = 0
            for item in lista:
                lista[count] = color
                count += 1

def reset():
    global actions
    if current_used_grid == 'grid2':
        for lista in grid2:
            count = 0
            for item in lista:
                lista[count] = aspro
                count += 1
    elif current_used_grid == 'grid_with_small_blocks':
        for lista in grid_with_small_blocks:
            count = 0
            for item in lista:
                lista[count] = aspro
                count += 1
    actions = []

def erase():
    global selected_color
    selected_color = aspro

def undo():
    global time_count
    if len(actions) >= 1 and time_count == 3:
        for key,value in actions[-1].items():
            row = int((value[0] - 1) / difference) 
            col = int((value[1] - 1) / difference)
            if current_used_grid == 'grid_with_small_blocks':
                grid_with_small_blocks[col][row] = value[2]
            elif current_used_grid == 'grid2':
                grid2[col][row] = value[2]
            actions.pop(-1)
        time_count = 0

def MainMenu():
    menu = True
    ouranio_tokso = [kokkino,portokali,kitrino,prasino,mple,meso_mwb,violeti]
    mhnyma_label = terafont.render('Drawnar.io',True, mauro)
    made_by_label = different_font.render("-Made by Dimos Theocharis-",True, mauro)
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        position_y = 0
        for xrwma in ouranio_tokso:
            pygame.draw.rect(GameDisplay, xrwma, [0,position_y,display_width, 107])
            position_y += 107
        GameDisplay.blit(mhnyma_label,(display_width / 2 - mhnyma_label.get_width() / 2, 100))
        GameDisplay.blit(made_by_label,(display_width - made_by_label.get_width(),display_height - made_by_label.get_height()))
        button('Load Files',font, 250, 350, 100, 50, mauro, gkri_anoixto, gkri_skouro,'LOAD_FILES')
        button('New Drawing', font, 400, 350, 100, 50, mauro, gkri_anoixto, gkri_skouro,'NEW_PROJECT')
        pygame.display.update()

def delete(name_of_project,coordinates):
    with open('names_of_files.py','r') as project:
        lista = []
        for line in project.readlines():
            lista.append(line)
        if name_of_project in lista:
            lista.remove(name_of_project)
            
    with open('names_of_files.py','w') as myfile:
        for line in lista:
            myfile.write(line)
    mhnyma_label = bigfont.render('The file was successfully deleted!', True, mauro)
    pygame.draw.rect(GameDisplay, kokkino_skouro,[coordinates[0],coordinates[1], display_width, 100])
    GameDisplay.blit(mhnyma_label,(display_width / 2 - mhnyma_label.get_width() / 2, 100 / 2 - mhnyma_label.get_height() / 2 + coordinates[1]))
    os.remove(name_of_project[:-1])
    pygame.display.update()
    time.sleep(1)
    MainMenu()

def load_files():
    global selected_file
    print(recently_created_projects)
    walk = True
    while walk:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.fill(mauro)
        pos_x = 0
        pos_y = 0
        with open('names_of_files.py','r') as projects:
            for line in projects.readlines():
                recent_file = False
                if line[:-1] in recently_created_projects:
                    recent_file = True
                project_name_label = bigfont.render(line[:-1],True, aspro)
                pygame.draw.rect(GameDisplay,kafe,[pos_x,pos_y,display_width,100])
                if recent_file == True:
                    button('Load', font, 450, (pos_y + 100 / 2) - 25, 100, 50, aspro, gkri_skouro, gkri_skouro, 'LOAD', line, 'RECENT')
                elif recent_file == False:
                    button('Load', font, 450, (pos_y + 100 / 2) - 25, 100, 50, aspro, gkri_anoixto, gkri_skouro, 'LOAD', line)
                button('Delete', font, 600, (pos_y + 100 / 2) - 25,100, 50, aspro, gkri_anoixto, gkri_skouro, 'DELETE',line,[0,pos_y])
                GameDisplay.blit(project_name_label,(pos_x + 20, pos_y + 50 - (project_name_label.get_height() / 2)))
                # mia lista pou tha periexei to periexomeno tou ekastote fakelou sto names_of_files.py
                empty = []
                ################################zwgrafizw mia epeikonish tou ekastote project se mikroterh ekdosh##############################
                additional = 6
                with open(line[:-1],'r') as project:
                    lines_file = project.readlines()
                    if len(lines_file[1]) > 400:
                        additional =  3
                    elif len(lines_file[1]) < 400:
                        additional = 6
                    for line in lines_file:
                        content = json.loads(line)
                        # prosthetw kathe seira tou ekastote fakelou sto empty
                        empty.append(content)
                block_y = 0
                for seira in empty:
                    block_x = 0
                    for element in seira:
                        # zwgrafizw ta koutakia gia thn anaparastash tou fakelou
                        pygame.draw.rect(GameDisplay, tuple(element), [300 + block_x,pos_y + 14 + block_y,additional,additional])
                        block_x += additional
                    block_y += additional
                #ftiaxnw ena perigramma gyrw apo kathe project
                pygame.draw.line(GameDisplay, mauro, (298,pos_y + 12),(392, pos_y + 12),2)
                pygame.draw.line(GameDisplay, mauro, (298,pos_y + 14 + 12 * 6),(392, pos_y + 14 + 12*6),2)
                pygame.draw.line(GameDisplay, mauro, (298, pos_y + 12), (298, pos_y + 14 + 12*6),2)
                pygame.draw.line(GameDisplay, mauro, (390, pos_y + 12), (390, pos_y + 14 + 12*6),2)
                pos_y += 150
        button('<--Back', font, 0, 720, 60, 30, mauro, gkri_anoixto, gkri_skouro, 'BACK')
        pygame.display.update()

def choose_grid_size():
    global current_grid_size
    run = True
    time_between_changing_grid = 0
    clock = pygame.time.Clock()
    FPS = 10
    while run:
        clock.tick(FPS)
        if time_between_changing_grid < 5:
            time_between_changing_grid += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #diastaseis
        grid_label_1 = font.render('15 X 12', True, mauro)
        grid_label_2 = font.render('30 X 24', True, mauro)
        GameDisplay.fill(apalo_mple)
        ################ftiaxnw ena background gia thn othoni epiloghs grid###################
        diff_x = 0
        diff_y = 0
        for x in range(3):
            pygame.draw.rect(GameDisplay, kokkino_skouro, [diff_x, 0, 150, 150])
            pygame.draw.rect(GameDisplay, mauro, [diff_x, 150, 150, 150])
            pygame.draw.rect(GameDisplay, kokkino_skouro, [diff_x, 300, 150, 150])
            pygame.draw.rect(GameDisplay, mauro, [diff_x, 450, 150, 150])
            pygame.draw.rect(GameDisplay, kokkino_skouro, [diff_x, 600, 150, 150])
            diff_x += 300
        diff_x = 150
        diff_y = 0
        color = mauro
        for x in range(5):
            pygame.draw.rect(GameDisplay, color, [diff_x, diff_y, 150,150])
            pygame.draw.rect(GameDisplay, color, [diff_x + 300, diff_y, 150, 150])
            diff_y += 150
            if color == kokkino_skouro:
                color = mauro
            elif color == mauro:
                color = kokkino_skouro
        # ftiaxnw ena perigramma pou tha exei mesa tis epiloges
        pygame.draw.rect(GameDisplay, gkri_anoixto, [275,200,200,350], 5)
        # epiloges
        for key, value in pick_grid_size.items():
            if value[0] == True:
                color_of_block = (164,164,164)
                current_grid_size = key
            elif value[0] == False:
                color_of_block = (50,50,50)
            pygame.draw.rect(GameDisplay, color_of_block, [value[1], value[2], 100, 50])
            pygame.draw.rect(GameDisplay, color_of_block, [value[1], value[2], 100, 50])
            pygame.draw.rect(GameDisplay, color_of_block, [value[1], value[2], 100, 50])
        GameDisplay.blit(grid_label_1,(325 + 50 - grid_label_2.get_width() / 2, 250 + 25 - grid_label_2.get_height() / 2))
        GameDisplay.blit(grid_label_2,(325 + 50 - grid_label_1.get_width() / 2, 450 + 25 - grid_label_1.get_height() / 2))
        button('<--Back', font, 0, 720, 60, 30, mauro, gkri_anoixto, gkri_skouro, 'BACK')
        # change picks
        keys = pygame.key.get_pressed()
        if time_between_changing_grid == 5:
            if keys[pygame.K_DOWN] == True:
                time_between_changing_grid = 0
                if pick_grid_size['small_blocks'][0] == True:
                    pick_grid_size['small_blocks'][0] = False
                    pick_grid_size['big_blocks'][0] = True
                elif pick_grid_size['medium_blocks'][0] == True:
                    pick_grid_size['medium_blocks'][0] = False
                    pick_grid_size['small_blocks'][0] = True
                elif pick_grid_size['big_blocks'][0] == True:
                    pick_grid_size['big_blocks'][0] = False
                    pick_grid_size['medium_blocks'][0] = True
            
            elif keys[pygame.K_UP] == True:
                time_between_changing_grid = 0
                if pick_grid_size['small_blocks'][0] == True:
                    pick_grid_size['small_blocks'][0] = False
                    pick_grid_size['medium_blocks'][0] = True
                elif pick_grid_size['medium_blocks'][0] == True:
                    pick_grid_size['medium_blocks'][0] = False
                    pick_grid_size['big_blocks'][0] = True
                elif pick_grid_size['big_blocks'][0] == True:
                    pick_grid_size['big_blocks'][0] = False
                    pick_grid_size['small_blocks'][0] = True
            
            elif keys[pygame.K_RETURN] == True:
                time_between_changing_grid = 0
                print(current_grid_size)
                begin()

        pygame.display.update()

def begin():
    global grid2, grid, first_time_draw_after_selected_new_file, current_used_grid, current_grid_size, grid_with_small_blocks
    run = True
    FPS = 10
    clock = pygame.time.Clock()
    if selected_file != None:
        # adeiazw to grid2
        ###grid2 = []
        # metablhth pou xrhsimopiw gia na deixnei an to grid einai grid2 h an einai grid_with_small_blocks
        GRID = None
        #current_used_grid = []
        # etoimazw ena deutero list sto opoio tha mpoun oi seires apo to project.readlines(), kathe stoixeio einai se morfh listas omws
        hitaki = []
        # bgazw to /n pou yparxei se kathe seira sto fakelo names_of_files.py
        with open(selected_file[:-1],'r') as selected_project:
            file_lines = selected_project.readlines()
            # blepw an einai project se mikro plegma h se megalo
            if len(file_lines[1]) > 400:
                grid_with_small_blocks = []
                GRID = 'grid_with_small_blocks'
                current_grid_size = 'small_blocks'
            elif len(file_lines[1]) < 400:
                grid2 = []
                GRID = 'grid2'
                current_grid_size = 'big_blocks'
            for line in file_lines:
                content = json.loads(line)
                hitaki.append(content)

#bazw to periexomeno tou hitaki mesa sto list GRID, metatrepontas th morfh kathe stoixeiou se tuple
        for x in hitaki:
            dentro = []
            for y in x:
                dentro.append(tuple(y))
            #grid2.append(dentro)
            if GRID == 'grid_with_small_blocks':
                grid_with_small_blocks.append(dentro)
            elif GRID == 'grid2':
                grid2.append(dentro)
    else:
        fill(aspro)
    first_time_draw_after_selected_new_file = 0

    def redraw():
        GameDisplay.fill(aspro)
        global selected_color, current_grid_columns, current_grid_rows, current_used_grid, grid2, difference, grid_with_small_blocks
        # zwgrafizw ena orthogwnio me diaforetiko xrwma apo to plegma gia na ksexwrizoun ta ergaleia zwgrafikhs
        pygame.draw.rect(GameDisplay, dark_aspro, [0,601,display_width,149])
        # bazw ta koumpia
        button('FILL', font, 150, 620, 100, 50, mauro, gkri_anoixto, gkri_skouro, 'FILL',selected_color)
        button('RESET', font, 150, 680, 100, 50, mauro, gkri_anoixto, gkri_skouro, 'RESET')
        button('ERASE', font, 350, 620, 100, 50, mauro, gkri_anoixto, gkri_skouro, 'ERASE')
        button('UNDO', font, 350, 680, 100, 50, mauro, gkri_anoixto, gkri_skouro, 'UNDO')
        button('<--Back', font, 0, 720, 60, 30, mauro, gkri_anoixto, gkri_skouro, 'BACK')
        button('Save as', font, 0, 690, 60, 30, mauro, gkri_anoixto, gkri_skouro, 'SAVE AS')
        button('Save', font, 0, 660, 60, 30, mauro, gkri_anoixto, gkri_skouro, 'SAVE')
        # ta variables gia na kanw tis grammes gia to plegma ths zwgrafikhs
        start_x = 0
        start_y = 0
        # allazw tis metablhtes twn column kai rows, analoga poio grid exei epilextei
        if current_grid_size == 'small_blocks':
            current_grid_rows, current_grid_columns = 24, 30
            current_used_grid = 'grid_with_small_blocks'
        elif current_grid_size == 'big_blocks':
            current_grid_rows, current_grid_columns = 12, 15
            current_used_grid = 'grid2'
        # h apostash metaksy twn grammwn
        ###difference = int(750/15)
        difference = int(750/current_grid_columns)
        ###for x in range(16):
        for x in range(current_grid_columns + 1):
            pygame.draw.line(GameDisplay, mauro, (start_x,0),(start_x,600))
            start_x += difference
        ###for y in range(13):
        for y in range(current_grid_rows + 1):
            pygame.draw.line(GameDisplay, mauro, (0,start_y),(display_width,start_y))
            start_y += difference
        # zwgrafizw ta koutakia gia ta xrwmata
        for key,value in colors.items():
            pygame.draw.rect(GameDisplay, key, [value[0],value[1],40,40])
        #zwgrafizw ta koutakia tou plegmatos
        pos_x = 1
        pos_y = 1
        #######for lista in grid2:
        if current_used_grid == 'grid_with_small_blocks':
            for lista in grid_with_small_blocks:
                count = 0
                pos_x = 1
                for item in lista:
                    #####pygame.draw.rect(GameDisplay, item [pos_x, pos_y, 49,49])
                    pygame.draw.rect(GameDisplay, item, [pos_x,pos_y,difference - 1,difference - 1])
                    ####pos_x += 50
                    pos_x += difference
                ####pos_y += 50
                pos_y += difference
        elif current_used_grid == 'grid2':
            for lista in grid2:
                count = 0
                pos_x = 1
                for item in lista:
                    #####pygame.draw.rect(GameDisplay, item [pos_x, pos_y, 49,49])
                    pygame.draw.rect(GameDisplay, item, [pos_x,pos_y,difference - 1,difference - 1])
                    ####pos_x += 50
                    pos_x += difference
                ####pos_y += 50
                pos_y += difference
        # zwgrafizw ena perigramma poy tha periexei ta xrwmtata ws synolo
        pygame.draw.line(GameDisplay, mauro,(499,614),(701,614))
        pygame.draw.line(GameDisplay, mauro, (499,735),(701,735))
        pygame.draw.line(GameDisplay, mauro, (499,614), (499, 736))
        pygame.draw.line(GameDisplay, mauro, (700,614), (700, 736))

        #zwgrafizw ena perigramma gia to epilegmeno xrwma
        for key,value in colors.items():
            if key == selected_color:
                pygame.draw.line(GameDisplay, mauro, (value[0],value[1]), (value[0] + 40, value[1]),3)
                pygame.draw.line(GameDisplay, mauro, (value[0],value[1] + 40),(value[0] + 40,value[1] + 40),3)
                pygame.draw.line(GameDisplay, mauro, (value[0], value[1]),(value[0], value[1] +40),3)
                pygame.draw.line(GameDisplay, mauro, (value[0] + 40, value[1]),(value[0] + 40, value[1] + 40),3)
        pygame.display.update()
        
    while run:
        clock.tick(FPS)
        global selected_color, previous_color, actions, time_count, time_between_color_changing, activate_erase_button, time_between_erase_buttons    
        # auksanw to first_time_draw_after_selected_new_file
        if first_time_draw_after_selected_new_file < 1 * FPS:
            first_time_draw_after_selected_new_file += 1
        # auksanw to time_count 
        if time_count < 3:
          time_count +=1
        # auksanw to time_between_color_changing
        if time_between_color_changing < 2 * FPS:
            time_between_color_changing += 1
        # ayksanw to time_between_erase_buttons
        if time_between_erase_buttons < 1 * FPS:
            time_between_erase_buttons += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        element_x = 1
        element_y = 1
        # zwgrafizw
        if click[0] == 1 and first_time_draw_after_selected_new_file == 10:
            if current_used_grid == 'grid2':
                for team in grid2:
                    element_x = 1
                    count = 0
                    for element in team:
                        #########if element_x <= mouse[0] <= element_x + 49 and element_y <= mouse[1] <= element_y + 49:
                        if element_x <= mouse[0] <= element_x + difference - 1 and element_y <= mouse[1] <= element_y + difference - 1:
                            # prosthetw tis energeies sto actions
                            action = {selected_color:[element_x,element_y,team[count]]}
                            if len(actions) == 0:
                                actions.append(action)
                            elif actions[-1] != action and team[count] != selected_color:
                                actions.append(action)
                            team[count] = selected_color
                        element_x += difference
                        count += 1
                    element_y += difference
            elif current_used_grid == 'grid_with_small_blocks':
                 for team in grid_with_small_blocks:
                    element_x = 1
                    count = 0
                    for element in team:
                        #########if element_x <= mouse[0] <= element_x + 49 and element_y <= mouse[1] <= element_y + 49:
                        if element_x <= mouse[0] <= element_x + difference - 1 and element_y <= mouse[1] <= element_y + difference - 1:
                            # prosthetw tis energeies sto actions
                            action = {selected_color:[element_x,element_y,team[count]]}
                            if len(actions) == 0:
                                actions.append(action)
                            elif actions[-1] != action and team[count] != selected_color:
                                actions.append(action)
                            team[count] = selected_color
                        element_x += difference
                        count += 1
                    element_y += difference


        #allazw to epilegmeno xrwma
        for key,value in colors.items():
            if value[0] <= mouse[0] <= value[0] + 40 and value[1] <= mouse[1] <= value[1] + 40:
                if click[0] == 1 and time_between_color_changing == 2 * FPS:
                    previous_color = selected_color
                    selected_color = key
                    time_between_color_changing = 0
                    if activate_erase_button == True:
                        activate_erase_button = False
        redraw()


MainMenu()          



        
