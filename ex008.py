m = float(input('Digite uma distancia em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('a medida {} em metros corressponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m, km, hm, dam, dm, cm, mm))
