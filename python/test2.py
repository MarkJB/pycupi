import sys
import traceback
from Pylargraph import *
from Pylargraph.generators.spiral import generateSpiral

Polargraph = polargraph.Polargraph

with Polargraph() as p:
    try:
        d = 100.0
        for x in range(100, 2500, 240):
            p.moveTo(x, 100)
            for j in generateSpiral(x, 100, 100, d, 1000, 2):
                p.drawTo(j[0], j[1])
            p.moveTo(x, 350)
            for j in generateSpiral(x, 350, 100, d, 1000, 4):
                p.drawTo(j[0], j[1])
            p.moveTo(x, 590)
            for j in generateSpiral(x, 590, 100, d, 1000, 8):
                p.drawTo(j[0], j[1])
            p.moveTo(x, 830)
            for j in generateSpiral(x, 830, 100, d, 1000, 16):
                p.drawTo(j[0], j[1])
            d += 100.0
        p.goHome()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("test1 main thread exception : %s" % exc_type)
        traceback.print_tb(exc_traceback, limit=2, file=sys.stdout)
