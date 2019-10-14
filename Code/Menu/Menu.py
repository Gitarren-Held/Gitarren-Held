import pygame
import pygameMenu.examples.multi_input

def fun():
    pass

menu = pygameMenu.Menu(surface, window...)
menu.add_option(timer_menu.get_title(), timer_menu)         # Add timer submenu
menu.add_option(help_menu.get_title(), help_menu)           # Add help submenu
menu.add_option(about_menu.get_title(), about_menu)         # Add about submenu
menu.add_option('Exit', pygameMenu.events.MENU_EXIT) # Add exit function

help_menu = pygameMenu.TextMenu(surface, window...)
help_menu.add_option('Simple button', fun, align=pygameMenu.locals.ALIGN_LEFT)
help_menu.add_option('Return to Menu', pygameMenu.events.MENU_BACK)


