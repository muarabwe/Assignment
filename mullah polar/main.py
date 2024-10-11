def polar_calculator():
    import math
    Ya = float(input('Enter Y coordinate of a: '))
    Xa = float(input('Enter X coordinate of a: '))
    Dm = float(input('Enter Distance in metres: '))
    Dq = float(input('Enter Direction in degrees: '))
    Q = (Dq/180)*math.pi
    Yb = Ya+Dm*math.sin(Q)
    Xb = Xa+Dm*math.cos(Q)
    print(f'Y Coordinates of b {Yb} m')
    print(f'X Coordinates of b {Yb} m')



polar_calculator()
