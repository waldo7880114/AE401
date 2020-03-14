# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:02:58 2020

@author: user
"""
from mcpi.minecraft import  Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
print(pos)

x = -100
y = 100
z = 1001

mc.player.setTilePos(x,y,z)
