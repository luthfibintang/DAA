kelipatan3 = 3
kelipatan4 = 4
kpk = 1

while True:
    if kpk % kelipatan3 == 0 and kpk % kelipatan4 == 0:
        break
    else:
        kpk += 1

print("KPK dari", kelipatan3, "dan", kelipatan4, "adalah", kpk)