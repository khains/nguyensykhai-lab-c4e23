def is_inside(x, y):
    if y[0]<=x[0]<=y[0]+y[2] and y[1]<=x[1]<=y[1]+y[3] :
        print("Diem nam trong hcn")
    else:
        print("Diem ko nam trong hcn")
is_inside([200, 120], [140, 60, 100, 200])
