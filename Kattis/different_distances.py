while True:
    try:
        x1, y1, x2, y2, p = map(float, input().split())
        print("{:.10f}".format((abs(x1-x2)**p + abs(y1-y2)**p)**(1/p)))
    except:
        break
