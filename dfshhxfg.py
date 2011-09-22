#===================================================================================================================================================================
#    0.1 - It begins
#===================================================================================================================================================================

import random
import os, pygame
from pygame.locals import *
from RokkitTanx import *
pygame.init() #eehhh

RGIRL = pygame.image.load("rgirl.png")
RGIRLFLY = pygame.image.load("rgirlfly.png")
RGIRLFLY2 = pygame.image.load("rgirlfly2.png")

BGIRL = pygame.image.load("bgirl.png")
BGIRLFLY = pygame.image.load("bgirlfly.png")
BGIRLFLY2 = pygame.image.load("bgirlfly2.png")

GGIRL = pygame.image.load("ggirl.png")
GGIRLFLY = pygame.image.load("ggirlfly.png")
GGIRLFLY2 = pygame.image.load("ggirlfly2.png")

YGIRL = pygame.image.load("ygirl.png")
YGIRLFLY = pygame.image.load("ygirlfly.png")
YGIRLFLY2 = pygame.image.load("ygirlfly2.png")


RGUY = pygame.image.load("rguy.png")
RGUYFLY = pygame.image.load("rguyfly.png")
RGUYFLY2 = pygame.image.load("rguyfly2.png")

BGUY = pygame.image.load("bguy.png")
BGUYFLY = pygame.image.load("bguyfly.png")
BGUYFLY2 = pygame.image.load("bguyfly2.png")

GGUY = pygame.image.load("gguy.png")
GGUYFLY = pygame.image.load("gguyfly.png")
GGUYFLY2 = pygame.image.load("gguyfly2.png")

YGUY = pygame.image.load("yguy.png")
YGUYFLY = pygame.image.load("yguyfly.png")
YGUYFLY2 = pygame.image.load("yguyfly2.png")
                                

#===================================================================================================================================================================
#    0.2 - I own this world
#===================================================================================================================================================================
class World():
    def __init__(self,WIDTH,HEIGHT):
        pygame.init()#ehhhh?
        pygame.font.init()
                
        self.WIDTH = 1024
        self.HEIGHT = 768
        
        pygame.mouse.set_visible(False)
        
        self.sprite_chosen = False
        self.sprite_chosen1 = False
        self.sprite_chosen2 = True
        self.start_game = False
        self.start1_game = False
        
        self.single_rgirl = False
        self.single_rguy = False
        self.single_bgirl = False
        self.single_bguy = False
        self.single_ggirl = False
        self.single_gguy = False
        self.single_ygirl = False
        self.single_yguy = False
        
        self.multi_rgirl = False
        self.multi_rguy = False
        self.multi_bgirl = False
        self.multi_bguy = False
        self.multi_ggirl = False
        self.multi_gguy = False
        self.multi_ygirl = False
        self.multi_yguy = False
        
        self.multi2_rgirl = False
        self.multi2_rguy = False
        self.multi2_bgirl = False
        self.multi2_bguy = False
        self.multi2_ggirl = False
        self.multi2_gguy = False
        self.multi2_ygirl = False
        self.multi2_yguy = False

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), 0, 32)
        pygame.display.set_caption( "Rokkit Tanx" )
        
        
        #Music
        pygame.mixer.music.load("Menu Music.wav")
        
 
#===================================================================================================================================================================
#    0.3 - Drawings I made
#===================================================================================================================================================================       
#    0.3.1 - This is the cursor
        self.cursor_image = pygame.image.load("Crosshairs.png" )
        self.cursor_rect = self.cursor_image.get_rect()
        
#    0.3.2 - Main Screen Background
        self.background_image = pygame.image.load("menu.png" )
        self.background_rect = self.background_image.get_rect()

#    0.3.3 - Background for all other screens       
        self.background2_image = pygame.image.load("Background.png" )
        self.background2_rect = self.background_image.get_rect()

#    0.3.4 - Buttons
        self.single1_image = pygame.image.load("Single1.png" )
        self.single2_image = pygame.image.load("Single2.png" )
        self.cur_single = self.single1_image
        self.single_rect = self.single1_image.get_rect().move(25,300)
        
        self.multi1_image = pygame.image.load("Multi1.png" )
        self.multi2_image = pygame.image.load("Multi2.png" )
        self.cur_multi = self.multi1_image
        self.multi_rect = self.multi1_image.get_rect().move(25,400)
        
        self.credit1_image = pygame.image.load("Credit1.png" )
        self.credit2_image = pygame.image.load("Credit2.png" )
        self.cur_credit = self.credit1_image
        self.credit_rect = self.credit1_image.get_rect().move(25,520)
        
        self.extra1_image = pygame.image.load("Extra1.png" )
        self.extra2_image = pygame.image.load("Extra2.png" )
        self.cur_extra = self.extra1_image
        self.extra_rect = self.extra1_image.get_rect().move(25,630)
        
        self.next_image = pygame.image.load("Next.png" )
        self.next2_image = pygame.image.load("Next2.png" )
        self.cur_next = self.next_image
        self.next_rect = self.next_image.get_rect().move(800,670)
        
        self.back_image = pygame.image.load("Back.png" )
        self.back2_image = pygame.image.load("Back2.png" )
        self.cur_back = self.back_image
        self.back_rect = self.back_image.get_rect().move(0,670)
        
        self.start_image = pygame.image.load("start1.png" )
        self.start2_image = pygame.image.load("start2.png" )
        self.start3_image = pygame.image.load("start.png" )
        self.cur_start = self.start_image
        self.start_rect = self.start_image.get_rect().move(800,670)

#    0.3.5 - Single Player Images        
        self.sp_image = pygame.image.load("SP.png" )
        self.sp_rect = self.sp_image.get_rect().move(165,-20)
        
        self.controls_image = pygame.image.load("Controls.png" )
        self.controls_rect = self.controls_image.get_rect().move(60,270)
        
        self.charsel_image = pygame.image.load("CS.png" )
        self.charsel_rect = self.charsel_image.get_rect().move(60,270)
        
#    0.3.6 - Credits Images        
        self.cred_image = pygame.image.load("CRDTS.png" )
        self.cred_rect = self.cred_image.get_rect().move(60,270)
        
        self.creds_image = pygame.image.load("Creds.png" )
        self.creds_rect = self.creds_image.get_rect().move(300,-15)
        
#    0.3.7 - Extras Images        
        self.xtra_image = pygame.image.load("Xtra.png" )
        self.xtra_rect = self.xtra_image.get_rect().move(320,-20)
        
        self.tank_image = pygame.image.load("Tank.png" )
        self.tank_rect = self.tank_image.get_rect().move(500,300)
        
        self.pt_image = pygame.image.load("Physics Test.png" )
        self.pt2_image = pygame.image.load("Physics Test 2.png" )
        self.cur_pt = self.pt_image
        self.pt_rect = self.pt_image.get_rect().move(0,400)
        
        self.gp_image = pygame.image.load("Group Photo.png" )
        self.gp2_image = pygame.image.load("Group Photo 2.png" )
        self.cur_gp = self.gp_image
        self.gp_rect = self.gp_image.get_rect().move(0,525)
        
        self.grp_image = pygame.image.load("Group.png" )
        self.grp_rect = self.grp_image.get_rect().move(60,270)
        
        self.crown_image = pygame.image.load("Crown.png" )
        self.crown_rect = self.crown_image.get_rect().move(225,-20)
        
#===================================================================================================================================================================        
#    0.4 - Multiplayer Stuff        
#===================================================================================================================================================================        
       
        self.mp_image = pygame.image.load("MP.png" )
        self.mp_rect = self.mp_image.get_rect().move(50,-10)
        
        self.mcs_image = pygame.image.load("MCS.png" )
        self.mcs_rect = self.mcs_image.get_rect().move(60,270)
        
        self.start1_image = pygame.image.load("start1.png" )
        self.start12_image = pygame.image.load("start2.png" )
        self.start13_image = pygame.image.load("start.png" )
        self.cur_start1 = self.start1_image
        self.start1_rect = self.start1_image.get_rect().move(800,670)
        
#    0.4.1 - Red Sprites 1
        self.arb_image = pygame.image.load("CSRB.png" )
        self.arb2_image = pygame.image.load("CSRBY.png" )
        self.arb3_image = pygame.image.load("CSRBG.png" )
        self.cur_arb = self.arb_image
        self.arb_rect = self.arb_image.get_rect().move(200,350)
        
        self.arg_image = pygame.image.load("CSRG.png" )
        self.arg2_image = pygame.image.load("CSRGY.png" )
        self.arg3_image = pygame.image.load("CSRGG.png" )
        self.cur_arg = self.arg_image
        self.arg_rect = self.arg_image.get_rect().move(125,350)
        
#    0.4.2 - Blue Sprites 1       
        self.abb_image = pygame.image.load("CSBB.png" )
        self.abb2_image = pygame.image.load("CSBBY.png" )
        self.abb3_image = pygame.image.load("CSBBG.png" )
        self.cur_abb = self.abb_image
        self.abb_rect = self.abb_image.get_rect().move(400,350)
        
        self.abg_image = pygame.image.load("CSBG.png" )
        self.abg2_image = pygame.image.load("CSBGY.png" )
        self.abg3_image = pygame.image.load("CSBGG.png" )
        self.cur_abg = self.abg_image
        self.abg_rect = self.abg_image.get_rect().move(325,350)
        
#    0.4.3 - Green Sprites 1       
        self.agb_image = pygame.image.load("CSGB.png" )
        self.agb2_image = pygame.image.load("CSGBY.png" )
        self.agb3_image = pygame.image.load("CSGBG.png" )
        self.cur_agb = self.agb_image
        self.agb_rect = self.agb_image.get_rect().move(600,350)
        
        self.agg_image = pygame.image.load("CSGG.png" )
        self.agg2_image = pygame.image.load("CSGGY.png" )
        self.agg3_image = pygame.image.load("CSGGG.png" )
        self.cur_agg = self.agg_image
        self.agg_rect = self.agg_image.get_rect().move(525,350)

#    0.4.4 - Yellow Sprites 1       
        self.ayb_image = pygame.image.load("CSYB.png" )
        self.ayb2_image = pygame.image.load("CSYBY.png" )
        self.ayb3_image = pygame.image.load("CSYBG.png" )
        self.cur_ayb = self.ayb_image
        self.ayb_rect = self.ayb_image.get_rect().move(800,350)
        
        self.ayg_image = pygame.image.load("CSYG.png" )
        self.ayg2_image = pygame.image.load("CSYGY.png" )
        self.ayg3_image = pygame.image.load("CSYGG.png" )
        self.cur_ayg = self.ayg_image
        self.ayg_rect = self.ayg_image.get_rect().move(725,350)
        
#    0.4.5 - Red Sprites 2
        self.brb_image = pygame.image.load("CSRB.png" )
        self.brb2_image = pygame.image.load("CSRBY.png" )
        self.brb3_image = pygame.image.load("CSRBG.png" )
        self.cur_brb = self.brb3_image
        self.brb_rect = self.brb_image.get_rect().move(200,525)
        
        self.brg_image = pygame.image.load("CSRG.png" )
        self.brg2_image = pygame.image.load("CSRGY.png" )
        self.brg3_image = pygame.image.load("CSRGG.png" )
        self.cur_brg = self.brg3_image
        self.brg_rect = self.brg_image.get_rect().move(125,525)
        
#    0.4.6 - Blue Sprites 2       
        self.bbb_image = pygame.image.load("CSBB.png" )
        self.bbb2_image = pygame.image.load("CSBBY.png" )
        self.bbb3_image = pygame.image.load("CSBBG.png" )
        self.cur_bbb = self.bbb3_image
        self.bbb_rect = self.bbb_image.get_rect().move(400,525)
        
        self.bbg_image = pygame.image.load("CSBG.png" )
        self.bbg2_image = pygame.image.load("CSBGY.png" )
        self.bbg3_image = pygame.image.load("CSBGG.png" )
        self.cur_bbg = self.bbg3_image
        self.bbg_rect = self.bbg_image.get_rect().move(325,525)
        
#    0.4.7 - Green Sprites 2       
        self.bgb_image = pygame.image.load("CSGB.png" )
        self.bgb2_image = pygame.image.load("CSGBY.png" )
        self.bgb3_image = pygame.image.load("CSGBG.png" )
        self.cur_bgb = self.bgb3_image
        self.bgb_rect = self.bgb_image.get_rect().move(600,525)
        
        self.bgg_image = pygame.image.load("CSGG.png" )
        self.bgg2_image = pygame.image.load("CSGGY.png" )
        self.bgg3_image = pygame.image.load("CSGGG.png" )
        self.cur_bgg = self.bgg3_image
        self.bgg_rect = self.bgg_image.get_rect().move(525,525)

#    0.4.8 - Yellow Sprites 2       
        self.byb_image = pygame.image.load("CSYB.png" )
        self.byb2_image = pygame.image.load("CSYBY.png" )
        self.byb3_image = pygame.image.load("CSYBG.png" )
        self.cur_byb = self.byb3_image
        self.byb_rect = self.byb_image.get_rect().move(800,525)
        
        self.byg_image = pygame.image.load("CSYG.png" )
        self.byg2_image = pygame.image.load("CSYGY.png" )
        self.byg3_image = pygame.image.load("CSYGG.png" )
        self.cur_byg = self.byg3_image
        self.byg_rect = self.byg_image.get_rect().move(725,525)

#===================================================================================================================================================================        
#    0.5 - Character Selection Sprites        
#===================================================================================================================================================================        
#    0.5.1 - Red Sprites
        self.rb_image = pygame.image.load("CSRB.png" )
        self.rb2_image = pygame.image.load("CSRBY.png" )
        self.rb3_image = pygame.image.load("CSRBG.png" )
        self.cur_rb = self.rb_image
        self.rb_rect = self.rb_image.get_rect().move(200,475)
        
        self.rg_image = pygame.image.load("CSRG.png" )
        self.rg2_image = pygame.image.load("CSRGY.png" )
        self.rg3_image = pygame.image.load("CSRGG.png" )
        self.cur_rg = self.rg_image
        self.rg_rect = self.rg_image.get_rect().move(125,475)
        
#    0.5.2 - Blue Sprites        
        self.bb_image = pygame.image.load("CSBB.png" )
        self.bb2_image = pygame.image.load("CSBBY.png" )
        self.bb3_image = pygame.image.load("CSBBG.png" )
        self.cur_bb = self.bb_image
        self.bb_rect = self.bb_image.get_rect().move(400,475)
        
        self.bg_image = pygame.image.load("CSBG.png" )
        self.bg2_image = pygame.image.load("CSBGY.png" )
        self.bg3_image = pygame.image.load("CSBGG.png" )
        self.cur_bg = self.bg_image
        self.bg_rect = self.bg_image.get_rect().move(325,475)
        
#    0.5.3 - Green Sprites        
        self.gb_image = pygame.image.load("CSGB.png" )
        self.gb2_image = pygame.image.load("CSGBY.png" )
        self.gb3_image = pygame.image.load("CSGBG.png" )
        self.cur_gb = self.gb_image
        self.gb_rect = self.gb_image.get_rect().move(600,475)
        
        self.gg_image = pygame.image.load("CSGG.png" )
        self.gg2_image = pygame.image.load("CSGGY.png" )
        self.gg3_image = pygame.image.load("CSGGG.png" )
        self.cur_gg = self.gg_image
        self.gg_rect = self.gg_image.get_rect().move(525,475)

#    0.5.4 - Yellow Sprites        
        self.yb_image = pygame.image.load("CSYB.png" )
        self.yb2_image = pygame.image.load("CSYBY.png" )
        self.yb3_image = pygame.image.load("CSYBG.png" )
        self.cur_yb = self.yb_image
        self.yb_rect = self.yb_image.get_rect().move(800,475)
        
        self.yg_image = pygame.image.load("CSYG.png" )
        self.yg2_image = pygame.image.load("CSYGY.png" )
        self.yg3_image = pygame.image.load("CSYGG.png" )
        self.cur_yg = self.yg_image
        self.yg_rect = self.yg_image.get_rect().move(725,475)
        
        
        
        self.cur_screen = 0

#===================================================================================================================================================================
#    0.6 - This draws stuff
#===================================================================================================================================================================
    def draw(self):
        
#    0.6.1 - Main Screen        
        if self.cur_screen == 0:
            self.screen.blit(self.background_image, self.background_rect)
            self.screen.blit(self.cur_single, self.single_rect)
            self.screen.blit(self.cur_multi, self.multi_rect)
            self.screen.blit(self.cur_credit, self.credit_rect)
            self.screen.blit(self.cur_extra, self.extra_rect)
            self.screen.blit(self.cursor_image, self.cursor_rect)
            
#    0.6.2 - Single Player Controls            
        elif self.cur_screen == 1:
            self.screen.blit(self.background2_image, self.background2_rect)
            self.screen.blit(self.sp_image, self.sp_rect)
            self.screen.blit(self.controls_image, self.controls_rect)
            self.screen.blit(self.cur_next, self.next_rect)
            self.screen.blit(self.cur_back, self.back_rect)
            self.screen.blit(self.cursor_image, self.cursor_rect)
            
#    0.6.3 - Multiplayer Character Select
        elif self.cur_screen == 2:
            self.screen.blit(self.background2_image, self.background2_rect)
            self.screen.blit(self.mcs_image, self.mcs_rect)
            self.screen.blit(self.mp_image, self.mp_rect)
            self.screen.blit(self.cur_back, self.back_rect)
            self.screen.blit(self.cur_arb, self.arb_rect)
            self.screen.blit(self.cur_arg, self.arg_rect)
            self.screen.blit(self.cur_abb, self.abb_rect)
            self.screen.blit(self.cur_abg, self.abg_rect)
            self.screen.blit(self.cur_agb, self.agb_rect)
            self.screen.blit(self.cur_agg, self.agg_rect)
            self.screen.blit(self.cur_ayb, self.ayb_rect)
            self.screen.blit(self.cur_ayg, self.ayg_rect)
            self.screen.blit(self.cur_brb, self.brb_rect)
            self.screen.blit(self.cur_brg, self.brg_rect)
            self.screen.blit(self.cur_bbb, self.bbb_rect)
            self.screen.blit(self.cur_bbg, self.bbg_rect)
            self.screen.blit(self.cur_bgb, self.bgb_rect)
            self.screen.blit(self.cur_bgg, self.bgg_rect)
            self.screen.blit(self.cur_byb, self.byb_rect)
            self.screen.blit(self.cur_byg, self.byg_rect)
            self.screen.blit(self.cur_start1, self.start1_rect)
            self.screen.blit(self.cursor_image, self.cursor_rect)
            
#    0.6.4 - Credits            
        elif self.cur_screen == 3:
            self.screen.blit(self.background2_image, self.background2_rect)
            self.screen.blit(self.cred_image, self.cred_rect)
            self.screen.blit(self.creds_image, self.creds_rect)
            self.screen.blit(self.cur_back, self.back_rect)
            self.screen.blit(self.cursor_image, self.cursor_rect)

#    0.6.5 - Extras
        elif self.cur_screen == 4:
            self.screen.blit(self.background2_image, self.background2_rect)
            self.screen.blit(self.tank_image, self.tank_rect)
            self.screen.blit(self.cur_pt, self.pt_rect)
            self.screen.blit(self.cur_gp, self.gp_rect)
            self.screen.blit(self.xtra_image, self.xtra_rect)
            self.screen.blit(self.cur_back, self.back_rect)
            self.screen.blit(self.cursor_image, self.cursor_rect)
            
#    0.6.6 - Single Player Character Select
        elif self.cur_screen == 5:
            self.screen.blit(self.background2_image, self.background2_rect)
            self.screen.blit(self.sp_image, self.sp_rect)
            self.screen.blit(self.cur_back, self.back_rect)
            self.screen.blit(self.cur_start, self.start_rect)
            self.screen.blit(self.charsel_image, self.charsel_rect)
            self.screen.blit(self.cur_rb, self.rb_rect)
            self.screen.blit(self.cur_rg, self.rg_rect)
            self.screen.blit(self.cur_bb, self.bb_rect)
            self.screen.blit(self.cur_bg, self.bg_rect)
            self.screen.blit(self.cur_gb, self.gb_rect)
            self.screen.blit(self.cur_gg, self.gg_rect)
            self.screen.blit(self.cur_yb, self.yb_rect)
            self.screen.blit(self.cur_yg, self.yg_rect)
            self.screen.blit(self.cursor_image, self.cursor_rect)
        
#    0.6.7 - Group Photo        
        elif self.cur_screen == 6:
            self.screen.blit(self.background2_image, self.background2_rect)
            self.screen.blit(self.grp_image, self.grp_rect)
            self.screen.blit(self.crown_image, self.crown_rect)
            self.screen.blit(self.cur_back, self.back_rect)
            self.screen.blit(self.cursor_image, self.cursor_rect)
        
#    0.6.8 - Physics Test       
        elif self.cur_screen == 7:
            #self.screen.blit(self.background2_image, self.background2_rect)
            self.screen.blit(self.cursor_image, self.cursor_rect)
        pygame.display.flip()

#===================================================================================================================================================================
#    0.7 - I use this for the buttons
#===================================================================================================================================================================        
    def main_loop(self):
        game_over = False
        
        pygame.mixer.music.play(-1)
                
        while not game_over:
            events = pygame.event.get()
            for event in events:
                    if event.type == QUIT:
                        exit()
                    elif event.type ==  MOUSEMOTION:
                        p = event.pos
                        self.cursor_rect.center = p
                        
#    0.7.1 - Buttons on Main Screen
                        if self.cur_screen == 0:
                            if self.single_rect.collidepoint(p):
                                self.cur_single = self.single2_image
                            else:
                                self.cur_single = self.single1_image
                            if self.multi_rect.collidepoint(p):
                                self.cur_multi = self.multi2_image
                            else:
                                self.cur_multi = self.multi1_image
                            if self.credit_rect.collidepoint(p):
                                self.cur_credit = self.credit2_image
                            else:
                                self.cur_credit = self.credit1_image
                            if self.extra_rect.collidepoint(p):
                                self.cur_extra = self.extra2_image
                            else:
                                self.cur_extra = self.extra1_image
                                
#    0.7.2 - Buttons on Credits
                        elif self.cur_screen == 3:
                            if self.back_rect.collidepoint(p):
                                self.cur_back = self.back2_image
                            else:
                                self.cur_back = self.back_image                                
                                                                
#    0.7.3 - Buttons on Single Player Controls
                        elif self.cur_screen == 1:
                            if self.next_rect.collidepoint(p):
                                self.cur_next = self.next2_image
                            else:
                                self.cur_next = self.next_image
                            if self.back_rect.collidepoint(p):
                                self.cur_back = self.back2_image
                            else:
                                self.cur_back = self.back_image
                                
#    0.7.4 - Buttons on Extras
                        elif self.cur_screen == 4:
                            if self.back_rect.collidepoint(p):
                                self.cur_back = self.back2_image
                            else:
                                self.cur_back = self.back_image
                            if self.gp_rect.collidepoint(p):
                                self.cur_gp = self.gp2_image
                            else:
                                self.cur_gp = self.gp_image
                            if self.pt_rect.collidepoint(p):
                                self.cur_pt = self.pt2_image
                            else:
                                self.cur_pt = self.pt_image
                            
#    0.7.5 - Buttons on Single Player Character Selection
                        elif self.cur_screen == 5:
                            if self.back_rect.collidepoint(p):
                                self.cur_back = self.back2_image
                            else:
                                self.cur_back = self.back_image
                            if self.start_rect.collidepoint(p)and self.start_game:
                                self.cur_start = self.start2_image
                            elif not self.start_rect.collidepoint(p)and self.start_game:
                                self.cur_start = self.start_image
                            elif not self.start_game:
                                self.cur_start = self.start3_image    
                                
#        0.7.5.1 - Buttons of Red Sprites                            
                            if self.rb_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_rb = self.rb2_image
                            elif not self.rb_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_rb = self.rb_image
                            
                            if self.rg_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_rg = self.rg2_image
                            elif not self.rg_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_rg = self.rg_image

#        0.7.5.2 - Buttons of Blue Sprites                            
                            if self.bg_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_bg = self.bg2_image
                            elif not self.bg_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_bg = self.bg_image
                            
                            if self.bb_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_bb = self.bb2_image
                            elif not self.bb_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_bb = self.bb_image

#        0.7.5.3 - Buttons of Green Sprites                            
                            if self.gg_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_gg = self.gg2_image
                            elif not self.gg_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_gg = self.gg_image
                            
                            if self.gb_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_gb = self.gb2_image
                            elif not self.gb_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_gb = self.gb_image

#        0.7.5.4 - Buttons of Yellow Sprites
                            if self.yg_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_yg = self.yg2_image
                            elif not self.yg_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_yg = self.yg_image
                            
                            if self.yb_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_yb = self.yb2_image
                            elif not self.yb_rect.collidepoint(p) and not self.sprite_chosen:
                                self.cur_yb = self.yb_image
                                
#    0.7.6 - Buttons on Multiplayer Character Selection
                        elif self.cur_screen == 2:
                            if self.back_rect.collidepoint(p):
                                self.cur_back = self.back2_image
                            else:
                                self.cur_back = self.back_image
                            if self.start1_rect.collidepoint(p)and self.start1_game:
                                self.cur_start1 = self.start12_image
                            elif not self.start1_rect.collidepoint(p)and self.start1_game:
                                self.cur_start1 = self.start1_image
                            elif not self.start1_game:
                                self.cur_start1 = self.start13_image    
                                
#        0.7.6.1 - Buttons of Red Sprites                            
                            if self.arb_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_arb = self.arb2_image
                            elif not self.arb_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_arb = self.arb_image
                            
                            if self.arg_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_arg = self.arg2_image
                            elif not self.arg_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_arg = self.arg_image

#        0.7.6.2 - Buttons of Blue Sprites                            
                            if self.abg_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_abg = self.abg2_image
                            elif not self.abg_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_abg = self.abg_image
                            
                            if self.abb_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_abb = self.abb2_image
                            elif not self.abb_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_abb = self.abb_image

#        0.7.6.3 - Buttons of Green Sprites                            
                            if self.agg_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_agg = self.agg2_image
                            elif not self.agg_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_agg = self.agg_image
                            
                            if self.agb_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_agb = self.agb2_image
                            elif not self.agb_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_agb = self.agb_image

#        0.7.6.4 - Buttons of Yellow Sprites
                            if self.ayg_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_ayg = self.ayg2_image
                            elif not self.ayg_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_ayg = self.ayg_image
                            
                            if self.ayb_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_ayb = self.ayb2_image
                            elif not self.ayb_rect.collidepoint(p) and not self.sprite_chosen1:
                                self.cur_ayb = self.ayb_image
                                
#        0.7.6.5 - Buttons of Red Sprites 2                           
                            if self.brb_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_brb = self.brb2_image
                            elif not self.brb_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_brb = self.brb_image
                            
                            if self.brg_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_brg = self.brg2_image
                            elif not self.brg_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_brg = self.brg_image

#        0.7.6.6 - Buttons of Blue Sprites 2                           
                            if self.bbg_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_bbg = self.bbg2_image
                            elif not self.bbg_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_bbg = self.bbg_image
                            
                            if self.bbb_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_bbb = self.bbb2_image
                            elif not self.bbb_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_bbb = self.bbb_image

#        0.7.6.7 - Buttons of Green Sprites 2                           
                            if self.bgg_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_bgg = self.bgg2_image
                            elif not self.bgg_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_bgg = self.bgg_image
                            
                            if self.bgb_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_bgb = self.bgb2_image
                            elif not self.bgb_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_bgb = self.bgb_image

#        0.7.6.8 - Buttons of Yellow Sprites 2
                            if self.byg_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_byg = self.byg2_image
                            elif not self.byg_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_byg = self.byg_image
                            
                            if self.byb_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_byb = self.byb2_image
                            elif not self.byb_rect.collidepoint(p) and not self.sprite_chosen2:
                                self.cur_byb = self.byb_image
                            
#    0.7.7 - Buttons on Group Photo
                        elif self.cur_screen == 6:
                            if self.back_rect.collidepoint(p):
                                self.cur_back = self.back2_image
                            else:
                                self.cur_back = self.back_image                               
#===================================================================================================================================================================
#    0.8 - Screen Changing Buttons
#===================================================================================================================================================================
                    elif event.type == MOUSEBUTTONDOWN:
                        p = event.pos
                        if self.cur_screen == 0:
                            if self.single_rect.collidepoint(p):
                                self.cur_screen = 1
                            elif self.multi_rect.collidepoint(p):
                                self.cur_screen = 2
                            elif self.credit_rect.collidepoint(p):
                                self.cur_screen = 3
                            elif self.extra_rect.collidepoint(p):
                                self.cur_screen = 4
                        elif self.cur_screen == 1:
                            if self.next_rect.collidepoint(p):
                                self.cur_screen = 5
                            elif self.back_rect.collidepoint (p):
                                self.cur_screen = 0
                        elif self.cur_screen == 3:
                            if self.back_rect.collidepoint (p):
                                self.cur_screen = 0
                        elif self.cur_screen == 4:
                            if self.back_rect.collidepoint (p):
                                self.cur_screen = 0
                            elif self.gp_rect.collidepoint (p):
                                self.cur_screen = 6
                            elif self.pt_rect.collidepoint (p):
                                pygame.display.quit()
                                pygame.quit()
                                import PhysicsObject
                                PhysicsObject.main()
                                pygame.quit()
                                pygame.init()
                                self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), 0, 32)
                                pygame.display.set_caption( "Rokkit Tanx" )
                                #this is horrible
#                                print "HALP HALP HALP HALP"
#                                newWorld = World("This Doesn't","Do Anything")
#                                newWorld.main_loop()
#                                return
                        elif self.cur_screen == 6:
                            if self.back_rect.collidepoint (p):
                                self.cur_screen = 4

#===================================================================================================================================================================
#    0.9 - Single Player Crap
#===================================================================================================================================================================
                        elif self.cur_screen == 5:
                            if self.back_rect.collidepoint (p):
                                self.cur_screen = 1
                                self.sprite_chosen = False
                                self.start_game = False
                                self.single_rgirl = False
                                self.single_rguy = False
                                self.single_bgirl = False
                                self.single_bguy = False
                                self.single_ggirl = False
                                self.single_gguy = False
                                self.single_ygirl = False
                                self.single_yguy = False
                            elif self.start_rect.collidepoint (p) and self.start_game == True:
                                pygame.display.quit()
                                pygame.quit()
                                
                                
                                if self.single_rgirl:
                                    regular = RGIRL
                                    fly = RGIRLFLY
                                    fly2 = RGIRLFLY2
                                elif self.single_bgirl:
                                    regular = BGIRL
                                    fly = BGIRLFLY
                                    fly2 = BGIRLFLY2
                                elif self.single_ggirl:
                                    regular = GGIRL
                                    fly = GGIRLFLY
                                    fly2 = GGIRLFLY2
                                elif self.single_ygirl:
                                    regular = YGIRL
                                    fly = YGIRLFLY
                                    fly2 = YGIRLFLY2
                                    
                                elif self.single_rguy:
                                    regular = RGUY
                                    fly = RGUYFLY
                                    fly2 = RGUYFLY2
                                elif self.single_bguy:
                                    regular = BGUY
                                    fly = BGUYFLY
                                    fly2 = BGUYFLY2
                                elif self.single_gguy:
                                    regular = GGUY
                                    fly = GGUYFLY
                                    fly2 = GGUYFLY2
                                else:# self.single_yguy:
                                    regular = YGUY
                                    fly = YGUYFLY
                                    fly2 = YGUYFLY2
                                
                                
                                game = RokkitTanx(
                                  [Player(WINDOW_WIDTH/2,WINDOW_HEIGHT*1/4,
                                         regular,
                                         fly,
                                         fly2,
                                         Vector(0,10))]
                                )
                                game.start()
                                
                                
#    0.9.1 - Red Sprite Selection
                            elif self.rb_rect.collidepoint (p) and not self.sprite_chosen:
                                self.cur_rb = self.rb2_image
                                self.cur_rg = self.rg3_image
                                self.cur_bg = self.bg3_image
                                self.cur_bb = self.bb3_image
                                self.cur_gb = self.gb3_image
                                self.cur_gg = self.gg3_image
                                self.cur_yb = self.yb3_image
                                self.cur_yg = self.yg3_image
                                self.sprite_chosen = True
                                self.start_game = True
                                self.single_rgirl = True
                            
                            elif self.rg_rect.collidepoint (p) and not self.sprite_chosen:
                                self.cur_rg = self.rg2_image
                                self.cur_rb = self.rb3_image
                                self.cur_bg = self.bg3_image
                                self.cur_bb = self.bb3_image
                                self.cur_gb = self.gb3_image
                                self.cur_gg = self.gg3_image
                                self.cur_yb = self.yb3_image
                                self.cur_yg = self.yg3_image
                                self.sprite_chosen = True
                                self.start_game = True
                                self.single_rguy = True
                                
#    0.9.2 - Blue Sprite Selection                            
                            elif self.bb_rect.collidepoint (p) and not self.sprite_chosen:
                                self.cur_bb = self.bb2_image
                                self.cur_bg = self.bg3_image
                                self.cur_rg = self.rg3_image
                                self.cur_rb = self.rb3_image
                                self.cur_gb = self.gb3_image
                                self.cur_gg = self.gg3_image
                                self.cur_yb = self.yb3_image
                                self.cur_yg = self.yg3_image
                                self.sprite_chosen = True
                                self.start_game = True
                                self.single_bgirl = True
                            
                            elif self.bg_rect.collidepoint (p) and not self.sprite_chosen:
                                self.cur_bg = self.bg2_image
                                self.cur_bb = self.bb3_image
                                self.cur_rg = self.rg3_image
                                self.cur_rb = self.rb3_image
                                self.cur_gb = self.gb3_image
                                self.cur_gg = self.gg3_image
                                self.cur_yb = self.yb3_image
                                self.cur_yg = self.yg3_image
                                self.sprite_chosen = True
                                self.start_game = True
                                self.single_bguy = True
                                
#    0.9.3 - Green Sprite Selection                            
                            elif self.gg_rect.collidepoint (p) and not self.sprite_chosen:
                                self.cur_bg = self.bg3_image
                                self.cur_bb = self.bb3_image
                                self.cur_rg = self.rg3_image
                                self.cur_rb = self.rb3_image
                                self.cur_gg = self.gg2_image
                                self.cur_gb = self.gb3_image
                                self.cur_yb = self.yb3_image
                                self.cur_yg = self.yg3_image
                                self.sprite_chosen = True
                                self.start_game = True
                                self.single_gguy = True
                                
                            elif self.gb_rect.collidepoint (p) and not self.sprite_chosen:
                                self.cur_bg = self.bg3_image
                                self.cur_bb = self.bb3_image
                                self.cur_rg = self.rg3_image
                                self.cur_rb = self.rb3_image
                                self.cur_gg = self.gg3_image
                                self.cur_gb = self.gb2_image
                                self.cur_yb = self.yb3_image
                                self.cur_yg = self.yg3_image
                                self.sprite_chosen = True
                                self.start_game = True
                                self.single_ggirl = True
                            
#    0.9.4 - Yellow Sprite Selection                            
                            elif self.yb_rect.collidepoint (p) and not self.sprite_chosen:
                                self.cur_bg = self.bg3_image
                                self.cur_bb = self.bb3_image
                                self.cur_rg = self.rg3_image
                                self.cur_rb = self.rb3_image
                                self.cur_gg = self.gg3_image
                                self.cur_gb = self.gb3_image
                                self.cur_yb = self.yb2_image
                                self.cur_yg = self.yg3_image
                                self.sprite_chosen = True
                                self.start_game = True
                                self.single_ygirl = True
                                
                            elif self.yg_rect.collidepoint (p) and not self.sprite_chosen:
                                self.cur_bg = self.bg3_image
                                self.cur_bb = self.bb3_image
                                self.cur_rg = self.rg3_image
                                self.cur_rb = self.rb3_image
                                self.cur_gg = self.gg3_image
                                self.cur_gb = self.gb3_image
                                self.cur_yb = self.yb3_image
                                self.cur_yg = self.yg2_image
                                self.sprite_chosen = True
                                self.start_game = True
                                self.single_yguy = True

#===================================================================================================================================================================
#    1.0 - Multilayer Crap
#=================================================================================================================================================================== 

                        elif self.cur_screen == 2:
                            if self.back_rect.collidepoint (p):
                                self.cur_screen = 0
                                self.sprite_chosen1 = False
                                self.sprite_chosen2 = True
                                self.start1_game = False
                                self.cur_brb = self.brb3_image
                                self.cur_brg = self.brg3_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_bbg = self.bbg3_image    
                                self.cur_bgb = self.bgb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg3_image
                                self.multi_rgirl = False
                                self.multi_rguy = False
                                self.multi_bgirl = False
                                self.multi_bguy = False
                                self.multi_ggirl = False
                                self.multi_gguy = False
                                self.multi_ygirl = False
                                self.multi_yguy = False
        
                                self.multi2_rgirl = False
                                self.multi2_rguy = False
                                self.multi2_bgirl = False
                                self.multi2_bguy = False
                                self.multi2_ggirl = False
                                self.multi2_gguy = False
                                self.multi2_ygirl = False
                                self.multi2_yguy = False
                            elif self.start1_rect.collidepoint (p) and self.start1_game == True:
                                
                                pygame.display.quit()
                                pygame.quit()
                                
                                if self.multi_rgirl:
                                    regular1 = RGIRL
                                    fly1 = RGIRLFLY
                                    fly21 = RGIRLFLY2
                                elif self.multi_bgirl:
                                    regular1 = BGIRL
                                    fly1 = BGIRLFLY
                                    fly21 = BGIRLFLY2
                                elif self.multi_ggirl:
                                    regular1 = GGIRL
                                    fly1 = GGIRLFLY
                                    fly21 = GGIRLFLY2
                                elif self.multi_ygirl:
                                    regular1 = YGIRL
                                    fly1 = YGIRLFLY
                                    fly21 = YGIRLFLY2
                                    
                                elif self.multi_rguy:
                                    regular1 = RGUY
                                    fly1 = RGUYFLY
                                    fly21 = RGUYFLY2
                                elif self.multi_bguy:
                                    regular1 = BGUY
                                    fly1 = BGUYFLY
                                    fly21 = BGUYFLY2
                                elif self.multi_gguy:
                                    regular1 = GGUY
                                    fly1 = GGUYFLY
                                    fly21 = GGUYFLY2
                                else:# self.multi_yguy:
                                    regular1 = YGUY
                                    fly1 = YGUYFLY
                                    fly21 = YGUYFLY2
                                
                                
                                if self.multi2_rgirl:
                                    regular2 = RGIRL
                                    fly2 = RGIRLFLY
                                    fly22 = RGIRLFLY2
                                elif self.multi2_bgirl:
                                    regular2 = BGIRL
                                    fly2 = BGIRLFLY
                                    fly22 = BGIRLFLY2
                                elif self.multi2_ggirl:
                                    regular2 = GGIRL
                                    fly2 = GGIRLFLY
                                    fly22 = GGIRLFLY2
                                elif self.multi2_ygirl:
                                    regular2 = YGIRL
                                    fly2 = YGIRLFLY
                                    fly22 = YGIRLFLY2
                                    
                                elif self.multi2_rguy:
                                    regular2 = RGUY
                                    fly2 = RGUYFLY
                                    fly22 = RGUYFLY2
                                elif self.multi2_bguy:
                                    regular2 = BGUY
                                    fly2 = BGUYFLY
                                    fly22 = BGUYFLY2
                                elif self.multi2_gguy:
                                    regular2 = GGUY
                                    fly2 = GGUYFLY
                                    fly22 = GGUYFLY2
                                else:# self.multi2_yguy:
                                    regular2 = YGUY
                                    fly2 = YGUYFLY
                                    fly22 = YGUYFLY2
                                
                                
                                game = RokkitTanx(
                                  [Player(WINDOW_WIDTH/2,WINDOW_HEIGHT*1/4,
                                         regular1,
                                         fly1,
                                         fly21,
                                         Vector(0,10))
                                    ,Player(WINDOW_WIDTH*1/4,WINDOW_HEIGHT*1/4,
                                        regular2,
                                        fly2,
                                        fly22,
                                        Vector(0,10))
                                  ]
                                )
                                game.start()
                                
#    1.1 - Red Sprite Selection
                            elif self.arb_rect.collidepoint (p) and not self.sprite_chosen1:
                                self.cur_arb = self.arb2_image
                                self.cur_arg = self.arg3_image
                                self.cur_abg = self.abg3_image
                                self.cur_abb = self.abb3_image
                                self.cur_agb = self.agb3_image
                                self.cur_agg = self.agg3_image
                                self.cur_ayb = self.ayb3_image
                                self.cur_ayg = self.ayg3_image
                                self.sprite_chosen1 = True
                                self.sprite_chosen2 = False
                                self.multi_rgirl = True
                            
                            elif self.arg_rect.collidepoint (p) and not self.sprite_chosen1:
                                self.cur_arg = self.arg2_image
                                self.cur_arb = self.arb3_image
                                self.cur_abg = self.abg3_image
                                self.cur_abb = self.abb3_image
                                self.cur_agb = self.agb3_image
                                self.cur_agg = self.agg3_image
                                self.cur_ayb = self.ayb3_image
                                self.cur_ayg = self.ayg3_image
                                self.sprite_chosen1 = True
                                self.sprite_chosen2 = False
                                self.multi_rguy = True
                                
#    1.2 - Blue Sprite Selection                            
                            elif self.abb_rect.collidepoint (p) and not self.sprite_chosen1:
                                self.cur_abb = self.abb2_image
                                self.cur_abg = self.abg3_image
                                self.cur_arg = self.arg3_image
                                self.cur_arb = self.arb3_image
                                self.cur_agb = self.agb3_image
                                self.cur_agg = self.agg3_image
                                self.cur_ayb = self.ayb3_image
                                self.cur_ayg = self.ayg3_image
                                self.sprite_chosen1 = True
                                self.sprite_chosen2 = False
                                self.multi_bgirl = True
                            
                            elif self.abg_rect.collidepoint (p) and not self.sprite_chosen1:
                                self.cur_abg = self.abg2_image
                                self.cur_abb = self.abb3_image
                                self.cur_arg = self.arg3_image
                                self.cur_arb = self.arb3_image
                                self.cur_agb = self.agb3_image
                                self.cur_agg = self.agg3_image
                                self.cur_ayb = self.ayb3_image
                                self.cur_ayg = self.ayg3_image
                                self.sprite_chosen1 = True
                                self.sprite_chosen2 = False
                                self.multi_bguy = True
                                
#    1.3 - Green Sprite Selection                            
                            elif self.agg_rect.collidepoint (p) and not self.sprite_chosen1:
                                self.cur_abg = self.abg3_image
                                self.cur_abb = self.abb3_image
                                self.cur_arg = self.arg3_image
                                self.cur_arb = self.arb3_image
                                self.cur_agg = self.agg2_image
                                self.cur_agb = self.agb3_image
                                self.cur_ayb = self.ayb3_image
                                self.cur_ayg = self.ayg3_image
                                self.sprite_chosen1 = True
                                self.sprite_chosen2 = False
                                self.multi_gguy = True
                                
                            elif self.agb_rect.collidepoint (p) and not self.sprite_chosen1:
                                self.cur_abg = self.abg3_image
                                self.cur_abb = self.abb3_image
                                self.cur_arg = self.arg3_image
                                self.cur_arb = self.arb3_image
                                self.cur_agg = self.agg3_image
                                self.cur_agb = self.agb2_image
                                self.cur_ayb = self.ayb3_image
                                self.cur_ayg = self.ayg3_image
                                self.sprite_chosen1 = True
                                self.sprite_chosen2 = False
                                self.multi_ggirl = True
                            
#    1.4 - Yellow Sprite Selection                            
                            elif self.ayb_rect.collidepoint (p) and not self.sprite_chosen1:
                                self.cur_abg = self.abg3_image
                                self.cur_abb = self.abb3_image
                                self.cur_arg = self.arg3_image
                                self.cur_arb = self.arb3_image
                                self.cur_agg = self.agg3_image
                                self.cur_agb = self.agb3_image
                                self.cur_ayb = self.ayb2_image
                                self.cur_ayg = self.ayg3_image
                                self.sprite_chosen1 = True
                                self.sprite_chosen2 = False
                                self.multi_ygirl = True
                                
                            elif self.ayg_rect.collidepoint (p) and not self.sprite_chosen1:
                                self.cur_abg = self.abg3_image
                                self.cur_abb = self.abb3_image
                                self.cur_arg = self.arg3_image
                                self.cur_arb = self.arb3_image
                                self.cur_agg = self.agg3_image
                                self.cur_agb = self.agb3_image
                                self.cur_ayb = self.ayb3_image
                                self.cur_ayg = self.ayg2_image
                                self.sprite_chosen1 = True
                                self.sprite_chosen2 = False
                                self.multi_yguy = True
                                
#    1.5 - Red Sprite Selection 2
                            elif self.brb_rect.collidepoint (p) and not self.sprite_chosen2:
                                self.cur_brb = self.brb2_image
                                self.cur_brg = self.brg3_image
                                self.cur_bbg = self.bbg3_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_bgb = self.bgb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg3_image
                                self.sprite_chosen2 = True
                                self.start1_game = True
                                self.multi2_rgirl = True
                            
                            elif self.brg_rect.collidepoint (p) and not self.sprite_chosen2:
                                self.cur_brg = self.brg2_image
                                self.cur_brb = self.brb3_image
                                self.cur_bbg = self.bbg3_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_bgb = self.bgb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg3_image
                                self.sprite_chosen2 = True
                                self.start1_game = True
                                self.multi2_rguy = True
                                
#    1.6 - Blue Sprite Selection 2                          
                            elif self.bbb_rect.collidepoint (p) and not self.sprite_chosen2:
                                self.cur_bbb = self.bbb2_image
                                self.cur_bbg = self.bbg3_image
                                self.cur_brg = self.brg3_image
                                self.cur_brb = self.brb3_image
                                self.cur_bgb = self.bgb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg3_image
                                self.sprite_chosen2 = True
                                self.start1_game = True
                                self.multi2_bgirl = True
                            
                            elif self.bbg_rect.collidepoint (p) and not self.sprite_chosen2:
                                self.cur_bbg = self.bbg2_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_brg = self.brg3_image
                                self.cur_brb = self.brb3_image
                                self.cur_bgb = self.bgb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg3_image
                                self.sprite_chosen2 = True
                                self.start1_game = True
                                self.multi2_bguy = True
                                
#    1.7 - Green Sprite Selection 2                            
                            elif self.bgg_rect.collidepoint (p) and not self.sprite_chosen2:
                                self.cur_bbg = self.bbg3_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_brg = self.brg3_image
                                self.cur_brb = self.brb3_image
                                self.cur_bgg = self.bgg2_image
                                self.cur_bgb = self.bgb3_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg3_image
                                self.sprite_chosen2 = True
                                self.start1_game = True
                                self.multi2_gguy = True
                                
                            elif self.bgb_rect.collidepoint (p) and not self.sprite_chosen2:
                                self.cur_bbg = self.bbg3_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_brg = self.brg3_image
                                self.cur_brb = self.brb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_bgb = self.bgb2_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg3_image
                                self.sprite_chosen2 = True
                                self.start1_game = True
                                self.multi2_ggirl = True
                            
#    1.8 - Yellow Sprite Selection 2                           
                            elif self.byb_rect.collidepoint (p) and not self.sprite_chosen2:
                                self.cur_bbg = self.bbg3_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_brg = self.brg3_image
                                self.cur_brb = self.brb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_bgb = self.bgb3_image
                                self.cur_byb = self.byb2_image
                                self.cur_byg = self.byg3_image
                                self.sprite_chosen2 = True
                                self.start1_game = True
                                self.multi2_ygirl = True
                                
                            elif self.byg_rect.collidepoint (p) and not self.sprite_chosen2:
                                self.cur_bbg = self.bbg3_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_brg = self.brg3_image
                                self.cur_brb = self.brb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_bgb = self.bgb3_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg2_image
                                self.sprite_chosen2 = True
                                self.start1_game = True
                                self.multi2_yguy = True
                                                
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            if self.cur_screen != 0:
                                self.cur_screen = 0
                                self.sprite_chosen = False
                                self.sprite_chosen1 = False
                                self.sprite_chosen2 = True
                                self.start_game = False
                                self.cur_brb = self.brb3_image
                                self.cur_brg = self.brg3_image
                                self.cur_bbb = self.bbb3_image
                                self.cur_bbg = self.bbg3_image    
                                self.cur_bgb = self.bgb3_image
                                self.cur_bgg = self.bgg3_image
                                self.cur_byb = self.byb3_image
                                self.cur_byg = self.byg3_image
                                self.single_rgirl = False
                                self.single_rguy = False
                                self.single_bgirl = False
                                self.single_bguy = False
                                self.single_ggirl = False
                                self.single_gguy = False
                                self.single_ygirl = False
                                self.single_yguy = False
                                self.multi_rgirl = False
                                self.multi_rguy = False
                                self.multi_bgirl = False
                                self.multi_bguy = False
                                self.multi_ggirl = False
                                self.multi_gguy = False
                                self.multi_ygirl = False
                                self.multi_yguy = False        
                                self.multi2_rgirl = False
                                self.multi2_rguy = False
                                self.multi2_bgirl = False
                                self.multi2_bguy = False
                                self.multi2_ggirl = False
                                self.multi2_gguy = False
                                self.multi2_ygirl = False
                                self.multi2_yguy = False
            self.draw()
#===================================================================================================================================================================
#    1.1 - Im not sure what this does
#===================================================================================================================================================================            

if __name__ == "__main__":
    the_world = World(400,400)
    the_world.main_loop()
