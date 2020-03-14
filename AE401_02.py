from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("You are located on x:" + str(x)+ 
                  " , y:" + str(y) + " , Z:" + str(z))
    import time
    time.sleep(0.1)
    