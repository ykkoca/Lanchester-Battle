import random
import simpy
import math

fe = open("Battle Log.txt", "w")
    
class G:

        redsize = 1600
        redstr = 0.02
        bluesize = 400
        bluestr = 0.32

def log(fe):

        if (G.redsize >= 1 and G.bluesize >=1):
            fe.write("\n%d\t%d\t%.2f\t\t%.2f"
                     %(G.redsize, G.bluesize, G.redstr, G.bluestr))

        elif (G.redsize <= 0.99):
            fe.write("\n%d\t%d\t%.2f\t\t%.2f"
                     %(0, G.bluesize, G.redstr, G.bluestr))

        elif (G.bluesize <= 0.99):

            fe.write("\n%d\t%d\t%.2f\t\t%.2f"
                     %(G.redsize, 0, G.redstr, G.bluestr))

        else:

            fe.write("\n%d\t%d\t%.2f\t\t%.2f"
                     %(0, 0, G.redstr, G.bluestr))
        

def Battle():
    
        fe = open('Battle Log.txt', 'w')
        fe.write("Red Size\tBlue Size\tRedStrength\tBlueStrength")

        log(fe)
        
        while (G.redsize > 0.99 and G.bluesize > 0.99):

            dummyobj = G.redsize
            G.redsize += (G.bluesize * G.bluestr * -1)
            G.bluesize += (dummyobj * G.redstr * -1)

            log(fe)
        
        fe.close()
        
Battle()
