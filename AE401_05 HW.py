from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z,=mc.player.getTilePos()
num=0
try:
    
    blockType = int(input("請輸入要蓋牆壁和天花板的方塊ID:"))
    mc.setBlock(x,y,z,blockType)
    mc.postToChat("blockType"+str(blockType))
    mc.setBlocks(x-10,y-5,z-10,x+10,y+5,z+10,blockType)
    mc.setBlocks(x-9,y-4,z-9,x+9,y+4,z+9,0)
    plockType = int(input("請輸入要蓋地下室地板的方塊ID:"))
    mc.setBlocks(x-11,y-5,z-11,x+11,y-5,z+11,plockType)
    qlockType = int(input("請輸入要蓋一樓地板的方塊ID:"))
    mc.setBlocks(x-11,y,z-11,x+11,y,z+11,qlockType)
    mc.setBlocks(x,y+2,z+10,x,y+1,z+10,0)
    dlockType = int(input("請輸入要蓋一樓燈泡的方塊ID169或89:"))
    mc.setBlocks(x+10,y+4,z+10,x-10,y+4,z-10,dlockType)
    klockType = int(input("請輸入要蓋一樓燈泡的方塊ID169或89:"))
    mc.setBlocks(x+10,y-2,z+10,x-10,y-2,z-10,klockType)
    
    
except:
    print("只能輸入數字")
