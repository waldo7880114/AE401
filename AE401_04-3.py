from mcpi.minecraft import Minecraft
import time as t
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlocks(x-1,y-1,z+1,x+1,y-1,z-1,19) 
    t.sleep(0.3)