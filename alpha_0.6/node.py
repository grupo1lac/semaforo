from datetime import datetime
import numpy as np

###### speed generator ######
def genspeed(slider):
        pi = np.pi
        av_amount = 5
        dev       = 1
        min_dif   = 0
        max_dif   = 30
        av_speed  = -( 1 / ( 1 + np.exp(-((slider-av_amount)*2) ) ) * \
                        (max_dif - min_dif) - max_dif)
        speed     = abs(dev * np.tan(pi * np.random.rand() - (pi / 2)) + av_speed)
        return speed

###### ratio generator ######
def cauchy(x, center, dev):
    return dev / ( dev**2 + (x-center)**2 ) 

def gettime(conversion):
    rate = 24 / ( conversion/60 )
    a=datetime.now().time()
    realt = ( a.hour + a.minute/60 + a.second/60**2 )
    virtualt = (realt*rate) % 24
    return virtualt

def ratio(conversion): # conversion in minutes
    t = gettime(conversion)
    return (cauchy(t, 8, 3) + cauchy(t, 17, 3))*20

###### functions called in labview ######
def get(array):
    return [ratio(array[0]),    \
            genspeed(array[1]), \
            genspeed(array[2]), \
            genspeed(array[3])]