from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlocks(x-2,y-1,z,x+2,y-1,z,13)
mc.setBlocks(x-1,y-1,z+1,x+1,y-1,z+1,13)
mc.setBlock(x,y-1,z+2,13)