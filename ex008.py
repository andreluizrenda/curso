medida = float(input('Uma distancia em metros: '))
km = medida / 1000
hc = medida / 100
dc = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a:\n {}km, {}hc, {}dc, {}dm, {}cm, e {}mm'.format(medida, km, hc, dc, dm, cm, mm))