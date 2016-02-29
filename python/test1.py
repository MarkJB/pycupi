import sys
import traceback
from Pylargraph import *

Polargraph = polargraph.Polargraph

with Polargraph() as p:
    try:
        p.moveTo(0, 0)
        p.drawTo(p.config.pixels, 0)
        p.drawTo(p.config.pixels, p.config.heightPixels)
        p.drawTo(0, p.config.heightPixels)
        p.drawTo(0, 0)

        gridX = (p.config.pixels - 20) / 10
        gridY = (p.config.heightPixels - 20) / 10

        x = 10
        while x + gridX < p.config.pixels:
            y = 10
            while y + gridY < p.config.heightPixels:
                p.moveTo(x, y)
                p.drawTo(x + gridX, y)
                p.drawTo(x + gridX, y + gridY)
                p.drawTo(x, y + gridY)
                p.drawTo(x, y)
                y += gridY
            x += gridX
        p.goHome()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("test1 main thread exception : %s" % exc_type)
        traceback.print_tb(exc_traceback, limit=2, file=sys.stdout)
