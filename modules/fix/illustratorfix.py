

def fix(polar):
    # If your angle is greater than 0 and lesser than 90 and your rotation is not 0
    # and polar is positive - then calculate conversion and apply rotation
    if 0 < polar < 90:
        polar = 90 - polar
    # If your angle is greater than 0 and lesser than 90 and your rotation is not 0
    # and polar is negative - then calculate conversion and apply rotation
    elif 0 < abs(polar) < 90:
        polar = abs(polar) + 90
    # If your angle is greater than 90 and lesser than 180 and your rotation is not 0
    # then calculate conversion and apply rotation
    elif 90 < polar < 180:
        polar = polar - 90
    # If your angle is greater than 90 and lesser than 180 and your rotation is not 0
    # and polar is negative - then calculate conversion and apply rotation
    elif 90 < abs(polar) < 180:
        polar = 270 - abs(polar)
    return polar
