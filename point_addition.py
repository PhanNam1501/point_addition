a = 497
b = 1768
p = 9739

P = (493, 5564)
Q = (1539, 4742) 
R = (4403,5202)

p = 9739
def point_addition(P,Q):
    O = (0,0)
    if (P == O) :
        return Q
    elif (Q == O):
        return P
    x1, y1 = P[0], P[1]
    x2, y2 = Q[0], Q[1]
    
    if (x1 == x2 and y1 == -y2) :
        return 0
    
    if P != Q:
        lam = ((y2 - y1) * pow(x2 - x1,-1, p)) % p
    else :
        lam = ((3 * x1**2 + a) * pow(2 * y1,-1, p)) % p
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    summation = (x3, y3)
    return summation
S = point_addition(point_addition(point_addition(P, P), Q), R)
print(S)
    
    
    