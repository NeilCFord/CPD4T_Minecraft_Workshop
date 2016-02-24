# import modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import os

# connect python to minecraft
mc = minecraft.Minecraft.create()

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, block.AIR.id)
mc.player.setPos(5, 0, 0)

# build the trap
mc.setBlocks(20, 0, 20, 22, 3, 22, block.WOOL.id, 3)
mc.setBlocks(21, 0, 20, 21, 3, 21, block.AIR.id)
mc.setBlock(21, -1, 21, block.WOOL.id, 14)

while True:
    x, y, z = mc.player.getTilePos()

    # check if player is on the red square and take a photo with the webcam
    # print "Say cheese!" to the chat
    if x == 21 and y == 0 and z == 21:
        mc.postToChat("Say cheese!")
        filename = "image.jpg"
        # os.system() runs a linux command. fswebcam is a program that can take photos os.system("fswebcam --no-banner -r 800x600 -d /dev/video0 " + filename)

        #quit program
        break