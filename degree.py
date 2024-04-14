import math
 
for degree in range(0, 361, 15):
    angle_radians = math.radians(degree)  # 度をラジアンに変換
    sin_value = round(math.sin(angle_radians), 2)
    cos_value = round(math.cos(angle_radians), 2)
    tan_value = round(math.tan(angle_radians), 2)

    print("sin" + str(degree) + "°の値は" + str(sin_value))
    print("cos" + str(degree) + "°の値は" + str(cos_value))
    print("tan" + str(degree) + "°の値は" + str(tan_value))

    # gitの練習
    # branchをつくって、練習
    # git switch -c UpdateTextの練習