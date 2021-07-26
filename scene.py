import pygame
from  gui_component import *
import category

#setting
screen_size = (800, 700)
caption = "medical department auto-schedule"

# scene state
START = "START"
INPROGRESS = "INPROGRESS"
CHECKPRODUCE = "CHECKPRODUCE"
SHOPPROC = "SHOPPROC"
GAMEOVER = "GAMEOVER"

class Scene:
    """background and mouse render"""
    def __init__(self):
		# initial pygame module for further use
        pygame.init()
        
        self.state = START
		# start scene element
        self.startbg = bg1
        self.title = GameFont(u"医院科室自动排班系统", 40, (0,0,0), (400, 50))
        self.screen = pygame.display.set_mode(screen_size, 0, 32)
        pygame.display.set_caption(caption)

        # year, month select button and subwindow
        self.year = 2021
        self.month = 1
        self.time_selected = False
        self.choose_time_button = button_ts("选择时间",(400, 120))
        self.time_window_pop = TimeWindowPop()

        # departments buttons
        self.get_departs = category.get_depart()
        self.depart_cons = [set([]) for i in range(len(self.get_departs))]
        
        self.departs = []
        for (i, d) in enumerate(self.get_departs):
            self.departs.append(button_d(d, (70 + (i % 6) * 130, 180 + (i // 6) * 60)))
        
        # departments subwindow
        self.depart_window = DayWindowPop(0, self.get_departs[0], self.year, self.month)      
        # import button
        self.import_button = button_out("生成排班表", (400, 600))
        
        self.gen_info = gen_info_window((400, 300))
        
        print("Scene inital!")
    
    def draw_start(self):
        self.screen.blit(self.startbg, (0,0))
        self.title.draw(self.screen)
        self.choose_time_button.draw(self.screen)
        self.import_button.draw(self.screen)
        
        for depart in self.departs:
            depart.draw(self.screen)
            
        if self.time_selected:
            full_time = str(self.year) + "." + str(self.month)
            time_display = GameFont(full_time, 22, (0,0,0), (530, 120))
            time_display.draw(self.screen)
    
    def draw_time_select(self):
        self.draw_start()
        self.time_window_pop.draw(self.screen)
    
    def draw_day_select(self):
        self.draw_start()
        self.depart_window.draw(self.screen)
        
    def draw_end(self):
        self.draw_start()  
        self.gen_info.draw(self.screen)          
        


