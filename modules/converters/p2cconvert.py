import math


def convert(maindata):
    polar = maindata.polar
    alpha = maindata.alpha
    radius = maindata.radius
    # Calculations
    p = polar * math.pi / 180
    a = alpha * math.pi / 180
    x = radius * math.sin(p) * math.cos(a)
    y = radius * math.sin(p) * math.sin(a)
    z = radius * math.cos(p)
    # Result
    return x, y, z
