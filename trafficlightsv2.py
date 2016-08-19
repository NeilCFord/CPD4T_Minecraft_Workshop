# import modules
import mcpi.minecraft as minecraft
from time import sleep

# connect python to minecraft
mc = minecraft.Minecraft.create()

# create CONSTANTS for block and light colours
AIR = 0
STONE = 1
WOOL = 35
FENCE = 85
BLACK = 15
RED = 14
AMBER = 4
GREEN = 5

# clear area in middle of map and move player there
mc.setBlocks(-60, 0, -60, 60, 50, 60, AIR)
mc.setBlocks(-60, -1, -60, 60, -1, 60, STONE)
mc.player.setPos(5, 0, 0)

# create the pole
for i in range(3):
    mc.setBlock(10, i, 0, FENCE)

mc.setBlock(10, 5, 0, WOOL, BLACK)
mc.setBlock(10, 4, 0, WOOL, BLACK)
mc.setBlock(10, 3, 0, WOOL, BLACK)

# wait three seconds before starting sequence
sleep(3)

# traffic light sequence
while True:
    # turn on red
    mc.setBlock(10, 5, 0, WOOL, RED)
    # wait three seconds
    sleep(3)

    # turn on amber
    mc.setBlock(10, 4, 0, WOOL, AMBER)
    # wait half a second
    sleep(0.5)

    # turn off red & amber, turn on green
    mc.setBlock(10, 5, 0, WOOL, BLACK)
    mc.setBlock(10, 4, 0, WOOL, BLACK)
    mc.setBlock(10, 3, 0, WOOL, GREEN)
    # wait three seconds
    sleep(3)

    # turn off green
    mc.setBlock(10, 3, 0, WOOL, BLACK)
    # turn on amber
    mc.setBlock(10, 4, 0, WOOL, AMBER)
    # wait one second
    sleep(1)

    # turn off amber
    mc.setBlock(10, 4, 0, WOOL, BLACK)
