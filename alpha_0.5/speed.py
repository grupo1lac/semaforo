import numpy as np

def genspeed(slider):
        pi = np.pi
        av_amount = 5
        dev       = 1
        min_dif   = 0
        max_dif   = 60
        av_speed  = -( 1 / ( 1 + np.exp(-((slider-av_amount)*2) ) ) * \
                        (max_dif - min_dif) - max_dif)
        speed     = abs(dev * np.tan(pi * np.random.rand() - (pi / 2)) + av_speed)
        return speed