# 空气动力学数据
import pandas as pd

def load_f16():
    mass = pd.Series({'AXX':9496.0 , 'AYY': 55814.0, 'AZZ': 63100.0, 'AXZ': 982.0})
    mass.AXZ2 = mass.AXZ**2
    mass.XPQ = mass.AXZ*(mass.AXX-mass.AYY+mass.AZZ)
    mass.GAM = mass.AXX*mass.AZZ-mass.AXZ**2
    mass.XQR = mass.AZZ*(mass.AZZ-mass.AYY)+mass.AXZ2
    mass.ZPQ = (mass.AXX-mass.AYY)*mass.AXX+mass.AXZ2
    mass.YPR = mass.AZZ - mass.AXX
    mass.weight_pound = 20490.446
    g0_ftps2 = 32.17
    mass.mass_slug = mass.weight_pound/g0_ftps2
    
    geom = pd.Series({'wing_ft2': 300, 'wingspan_ft': 30, 'chord_ft': 11.32, 'xcgr_mac': 0.35})
    geom.engmomenthx_slugft2ps = 160
    
    params=pd.Series()
    
    params.mass = mass
    params.geom = geom
    params.g0_ftps2 = g0_ftps2

    return params
