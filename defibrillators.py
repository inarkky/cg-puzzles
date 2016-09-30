import math


R = 6371
dst = []
lst = []
lon = input()
lat = input()
n = int(input())


def madeinchina(ln, lt, lon_tmp, lat_tmp):
    x = (lon_tmp - ln) * math.cos( 0.5*(lat_tmp+lt) )
    y = lat_tmp - lt
    d = R * math.sqrt( x*x + y*y )
    return d


def worldwidedist(a):
    b = a.split(";")
    tmp1 = math.radians(float(b[4].replace(",", ".")))
    tmp2 = math.radians(float(b[5].replace(",", ".")))
    
    tmp3 = math.radians(float(lon.replace(",", ".")))
    tmp4 = math.radians(float(lat.replace(",", ".")))
    
    distance = madeinchina(tmp1, tmp2, tmp3, tmp4) 
    return distance


for i in range(n):
    defib = input()
    dst.append( worldwidedist(defib) );
    lst.append( defib );

val, idx = min((val, idx) for (idx, val) in enumerate(dst))
print(lst[idx].split(";")[1])
