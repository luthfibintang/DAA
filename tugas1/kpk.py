kelipatan3 = 3
kelipatan4 = 4
lcm = 1

while True:
    if lcm % kelipatan3 == 0 and lcm % kelipatan4 == 0:
        break
    else:
        lcm += 1

print("KPK dari", kelipatan3, "dan", kelipatan4, "adalah", lcm)
