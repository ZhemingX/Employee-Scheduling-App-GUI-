import pygame
import time_month

# background image and compoment image
bg1 = pygame.transform.scale(pygame.image.load("images/bg.jpg"), (800, 700))

time_button_image = pygame.transform.scale(pygame.image.load("images/time_button.png"), (120, 30))

any_button_image = pygame.transform.scale(pygame.image.load("images/time_button.png"), (100, 30))

time_select_pop_image = pygame.transform.scale(pygame.image.load("images/white_rec.png"), (400, 300))
time_select_pop_pos = (400, 250)

depart_button_image = pygame.transform.scale(pygame.image.load("images/depart_button.png"), (120, 40))
depart_select_pop_image = pygame.transform.scale(pygame.image.load("images/white_rec.png"), (600, 600))

depart_button_pop_pos = (400, 400)

day_button_image = pygame.transform.scale(pygame.image.load("images/white_rec.png"), (60, 60))

button_on_image = pygame.transform.scale(pygame.image.load("images/on_b.png"), (50, 30))
button_off_image = pygame.transform.scale(pygame.image.load("images/off_b.png"), (50, 30))

button_out_image = pygame.transform.scale(pygame.image.load("images/time_button.png"), (130, 70))

gen_info_image = pygame.transform.scale(pygame.image.load("images/white_rec.png"), (400, 200))
# font

class GameFont(object):
    def __init__(self, text, font_size, font_color, font_position):
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.font_position = font_position
        self.TextSurface = pygame.font.Font('AaBaoHeZhiFangSuan3.ttf', self.font_size).render(self.text, True, self.font_color)
    
    def draw(self, screen):
        bw, bh = self.TextSurface.get_size()
        cx, cy = self.font_position
        screen.blit(self.TextSurface, (cx - bw/2, cy - bh/2))

def week_font(text, pos):
    return GameFont(text, 18, (178, 34, 34), pos)


# button

class Button(object):

    def __init__(self, pos, image, text, font_size, font_color):
        self.image = image
        self.position = pos
        self.gfont = GameFont(text, font_size, font_color, pos)
        self.depart_select = False
    
    def isOver(self):
		# check whether the mouse is on the button
        mx, my = pygame.mouse.get_pos()
        cx, cy = self.position
        bw, bh = self.image.get_size()
        in_x = cx - bw/2 < mx < cx + bw/2
        in_y = cy - bh/2 < my < cy + bh/2
        
        return in_x and in_y
    
    def draw(self, screen):
        cx, cy = self.position
        bw, bh = self.image.get_size()
        screen.blit(self.image, (cx - bw/2, cy - bh/2))
        self.gfont.draw(screen)

def button_ts(text, pos):
    return Button(pos, time_button_image, text, 16, (0,0,0))

def button_any(text, pos):
    return Button(pos, any_button_image, text, 15, (0,0,0))

def button_d(text, pos):
    return Button(pos, depart_button_image, text, 16, (0,0,0))

def button_out(text, pos):
    return Button(pos, button_out_image, text, 20, (0,0,0))

class FontButton(object):

    def __init__(self, pos, text, font_size, font_color):
        self.gfont = GameFont(text, font_size, font_color, pos)
        self.selected = False

    def isOver(self):
		# check whether the mouse is on the button
        mx, my = pygame.mouse.get_pos()
        cx, cy = self.gfont.font_position
        bw, bh = self.gfont.TextSurface.get_size()
        in_x = cx - bw/2 < mx < cx + bw/2
        in_y = cy - bh/2 < my < cy + bh/2
        
        return in_x and in_y
    
    def draw(self, screen):
        cx, cy = self.gfont.font_position
        bw, bh = self.gfont.TextSurface.get_size()
        if self.selected:
            pygame.draw.rect(screen, (255, 218, 185),[cx - bw/2, cy - bh/2, bw, bh], 6)
        self.gfont.draw(screen)

def year_font_button(text, pos):
    return FontButton(pos, text, 18, (0,0,0))

def month_font_button(text, pos):
    return FontButton(pos, text, 18, (0,0,0))


class DayButton(object):
    
    def __init__(self, pos, image, text, font_size, font_color):
        self.image = image
        self.position = pos
        self.gfont = GameFont(text, font_size, font_color, pos)
        self.day_select = False
    
    def isOver(self):
		# check whether the mouse is on the button
        mx, my = pygame.mouse.get_pos()
        cx, cy = self.position
        bw, bh = self.image.get_size()
        in_x = cx - bw/2 < mx < cx + bw/2
        in_y = cy - bh/2 < my < cy + bh/2
        
        return in_x and in_y
    
    def draw(self, screen, mode_sig):
        cx, cy = self.position
        bw, bh = self.image.get_size()
        screen.blit(self.image, (cx - bw/2, cy - bh/2))
        if self.day_select:
            if mode_sig == 0:
                # mode sig = 0 -> allowed days, mode sig = 1 -> disallowed days
                #print("green")
                pygame.draw.rect(screen, (84, 255, 159),[cx - bw/2, cy - bh/2, bw, bh], 6)
            elif mode_sig == 1:
                pygame.draw.rect(screen, (255, 99, 71),[cx - bw/2, cy - bh/2, bw, bh], 6)
        self.gfont.draw(screen)

def button_day(text, pos):
    return DayButton(pos, day_button_image, text, 20, (0,0,0))


class SwitchButton(object):
    
    def __init__(self, pos):
        self.images = [button_off_image, button_on_image]
        self.position = pos
        self.status = 0
    
    def isOver(self):
		# check whether the mouse is on the button
        mx, my = pygame.mouse.get_pos()
        cx, cy = self.position
        bw, bh = self.images[0].get_size()
        in_x = cx - bw/2 < mx < cx + bw/2
        in_y = cy - bh/2 < my < cy + bh/2
        
        return in_x and in_y
    
    def draw(self, screen):
        cx, cy = self.position
        bw, bh = self.images[0].get_size()
        screen.blit(self.images[self.status], (cx - bw/2, cy - bh/2))



    
# time select pop window
class TimeWindowPop(object):

	def __init__(self):
            self.windowimage = time_select_pop_image
            self.windowpos = time_select_pop_pos
            self.cancelbutton = button_any("取消", (320, 360))
            self.ensurebutton = button_any("确认", (480, 360))
            # year
            self.year_list = [year_font_button("2021", (310, 160)), year_font_button("2022", (310, 200)), year_font_button("2023", (310, 240)), year_font_button("2024", (310, 280))]
            # month
            self.month_list = [
                month_font_button("1", (430,160)),
                month_font_button("2", (480,160)),
                month_font_button("3", (530,160)),
                month_font_button("4", (430,200)),
                month_font_button("5", (480,200)),
                month_font_button("6", (530,200)),
                month_font_button("7", (430,240)),
                month_font_button("8", (480,240)),
                month_font_button("9", (530,240)),
                month_font_button("10", (430,280)),
                month_font_button("11", (480,280)),
                month_font_button("12", (530,280)),
            ]
	def draw(self, screen):
            wx, wy = self.windowimage.get_size()
            screen.blit(self.windowimage, (self.windowpos[0] - wx/2, self.windowpos[1] - wy/2))
            self.cancelbutton.draw(screen)
            self.ensurebutton.draw(screen)  
            for year in self.year_list:
                year.draw(screen)
            for month in self.month_list:
                month.draw(screen)

# day select pop window
class DayWindowPop(object):
    
    def __init__(self, depart_index, name, year, month):
        
        self.depart_index = depart_index
        self.name = name
        self.year = year
        self.month = month
        self.calendar, self.days = time_month.month_list(self.year, self.month)
        self.windowimage = depart_select_pop_image
        self.windowpos = depart_button_pop_pos
        self.caption = GameFont(str(self.year)+"."+str(self.month)+" -- "+self.name, 20, (0,0,0), (400, 140))
        self.mode_sig = 0
        self.week = [
            week_font("Mon", (200, 190)),
            week_font("Tue", (260, 190)),
            week_font("Wed", (320, 190)),
            week_font("Thurs", (395, 190)),
            week_font("Fri", (465, 190)),
            week_font("Sat", (530, 190)),
            week_font("Sun", (590, 190)),
        ]
        self.switch_button = SwitchButton((230, 640))
        self.switch_comment = [week_font("Add", (180, 640)), week_font("Delete", (295, 640))]
        self.cancelbutton = button_any("取消", (500, 640))
        self.ensurebutton = button_any("确认", (620, 640))
        ##
        self.day_choice = []
        for r in range(len(self.calendar)):
            for c in range(7):
                if self.calendar[r][c] != 0:
                    self.day_choice.append(button_day(str(self.calendar[r][c]), (202+c*65, 250+r*65)))
                    
    def draw(self, screen):
        wx, wy = self.windowimage.get_size()
        screen.blit(self.windowimage, (self.windowpos[0] - wx/2, self.windowpos[1] - wy/2))
        self.caption.draw(screen)
        self.switch_button.draw(screen)
        self.switch_comment[0].draw(screen)
        self.switch_comment[1].draw(screen)
        self.cancelbutton.draw(screen)
        self.ensurebutton.draw(screen)
        
        for d in self.week:
            d.draw(screen)
        for day in self.day_choice:
            day.draw(screen, self.mode_sig)

class gen_info_window(object):
    
    def __init__(self, pos):
        self.image = gen_info_image
        self.pos = pos
        self.msg = week_font("doc文件生成中...", pos)
                    
    def draw(self, screen):
        wx, wy = self.image.get_size()
        screen.blit(self.image, (self.pos[0] - wx/2, self.pos[1] - wy/2))
        self.msg.draw(screen)
        

