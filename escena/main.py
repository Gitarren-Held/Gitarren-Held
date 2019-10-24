#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
import sys
from director import *
from scene_home import *
 
def main():
    dir = Director()
    scene = SceneHome(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    main()