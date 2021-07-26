import sys
import pygame
from pygame.locals import QUIT
from gui_component import *
import scene
import employee_scheduling
import py_doc

scene = scene.Scene()

# scene state
START = "START"
TIME_SELECT = "TIME_SELECT"
DAY_SELECT = "DAY_SELECT"
GENERATE = "GENERATE"

while True:
    if scene.state == START:
        for event in pygame.event.get():
            scene.draw_start()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if scene.choose_time_button.isOver():
                    scene.state = TIME_SELECT
                    scene.draw_start()
                elif scene.import_button.isOver():
                    scene.state = GENERATE
                    scene.draw_end()
                else:
                    for i in range(len(scene.departs)):
                        if scene.departs[i].isOver():
                            scene.departs[i].depart_select = True
                            scene.depart_window = DayWindowPop(i, scene.get_departs[i], scene.year, scene.month)
                            for j in range(len(scene.depart_window.day_choice)):
                                if j not in scene.depart_cons[i]:
                                    scene.depart_window.day_choice[j].day_select = True
                            scene.state = DAY_SELECT
                            break
                    scene.draw_start()
                    
        #scene.draw_start()
    
    elif scene.state == TIME_SELECT:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if scene.time_window_pop.cancelbutton.isOver():
                    scene.state = START
                elif scene.time_window_pop.ensurebutton.isOver():
                    flag1 = False
                    for year in scene.time_window_pop.year_list:
                        if year.selected:
                            flag1 = True
                            scene.year = year.gfont.text
                            break
                    flag2 = False
                    for month in scene.time_window_pop.month_list:
                        if month.selected:
                            flag2 = True
                            scene.month = month.gfont.text
                            break
                    if flag1 and flag2:
                        scene.time_selected = True
                    scene.state = START
                else:
                    for year in scene.time_window_pop.year_list:
                        if year.isOver():
                            for other_year in scene.time_window_pop.year_list:
                                other_year.selected = False
                            year.selected = True
                    for month in scene.time_window_pop.month_list:
                        if month.isOver():
                            for other_month in scene.time_window_pop.month_list:
                                other_month.selected = False
                            month.selected = True
        
        scene.draw_time_select()
    
    elif scene.state == DAY_SELECT:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if scene.depart_window.cancelbutton.isOver():
                    scene.departs[scene.depart_window.depart_index].depart_select = False
                    scene.state = START
                    
                elif scene.depart_window.ensurebutton.isOver():
                    # count and assign to depart cons
                    depart_index = scene.depart_window.depart_index
                    if scene.depart_window.mode_sig == 0:
                        for (i,d) in enumerate(scene.depart_window.day_choice):
                            if not d.day_select:
                                scene.depart_cons[depart_index].add(i)
                    elif scene.depart_window.mode_sig == 1:
                        for (i,d) in enumerate(scene.depart_window.day_choice):
                            if d.day_select:
                                scene.depart_cons[depart_index].add(i)
                    scene.departs[scene.depart_window.depart_index].depart_select = False
                    #print(scene.depart_cons[depart_index])
                    scene.state = START
                    
                elif scene.depart_window.switch_button.isOver():
                    
                    if scene.depart_window.mode_sig == 0:
                        scene.depart_window.mode_sig = 1
                        scene.depart_window.switch_button.status = 1
                    elif scene.depart_window.mode_sig == 1:
                        scene.depart_window.mode_sig = 0
                        scene.depart_window.switch_button.status = 0
                    #print(scene.depart_window.mode_sig)
                    scene.depart_cons[scene.depart_window.depart_index] = set([])
                    for d in scene.depart_window.day_choice:
                            d.day_select = False
                else:
                    for d in scene.depart_window.day_choice:
                        if d.isOver():
                            if d.day_select:
                                d.day_select = False
                            else:
                                d.day_select = True
                
        scene.draw_day_select()
    
    elif scene.state == GENERATE:
        scene.draw_end()
        # generate output file
        (if_valid, res) = employee_scheduling.schedule_departs(len(scene.get_departs), 6, scene.depart_window.days, scene.depart_cons)
        if not if_valid:
            sys.exit()
        # print(scene.get_departs)
        # print()
        # print(scene.depart_cons)
        # print()
        # print(res)
        py_doc.create_doc(scene.year, scene.month, res, scene.get_departs)
        scene.state = START
    pygame.display.update()





