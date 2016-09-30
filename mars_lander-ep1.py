surface_n = int(input())  
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    
    g_modifier = (4 - 3.771)
    t_ctrl = (-v_speed - 30)/g_modifier
    conduct = y + v_speed * t_ctrl + t_ctrl ** 2 * g_modifier / 2
    
    if conduct > 0:
        thurst = "0"
    else:
        thurst = "4"
        
    print("0 {}".format(thurst))