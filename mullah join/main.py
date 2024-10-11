
def compute_join():
    import math
    from idlelib.query import Query
    Ya = float(input('Enter Y coordinate of a'))
    Xa = float(input('Enter X coordinate of a'))
    Yb = float(input('Enter Y Coordinate of b'))
    Xb = float(input('Enter X Coordinate for b'))
    Y = Yb - Ya
    X = Xb - Xa
    r = math.sqrt(X**2 + Y**2)
    Q = math.degrees(math.atan2(Y, X))
    A1 = math.degrees(Q)
    A2 = 180 -  math.degrees(Q)
    A3 = 180 +  math.degrees(Q)
    A4 = 360 - math.degrees(Q)
    if Y > 0 and X > 0:
        print(f'join AB: {r} m, {A1} degrees')
    elif Y < 0 and X > 0:
        print(f'Join AB: {r} m, {A2} degrees ')
    elif Y < 0 and X < 0:
        print(f'Join AB: {r} m, {A3} degrees')
    else:
        print(f'Join AB: {r} m, {A4} degrees')

compute_join()
