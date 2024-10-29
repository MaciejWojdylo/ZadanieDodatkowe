#a)
wysoki_meszczyzna = [0,0.25,0.5,0.75,1]
ans_not_meszczyzna = []
for person in wysoki_meszczyzna:
    ans_not_meszczyzna.append(1-person)
print(ans_not_meszczyzna)
#b) wysoki mężczyzna (∩ and czyli min) średni mężczyzna
wysoki_meszczyzna = [0, 0, 0, 0.25, 0.5, 1]
sredni_meszczyzna = [0, 1, 0.5, 0.25, 0, 0]
ans_wysoki_and_sredni = []
for i in range(0,len(wysoki_meszczyzna)):
    ans_wysoki_and_sredni.append(min(wysoki_meszczyzna[i],sredni_meszczyzna[i]))
print(ans_wysoki_and_sredni)
#c)
#d)
ans_wysoki_or_sredni = []
for i in range(0,len(wysoki_meszczyzna)):
    ans_wysoki_or_sredni.append(max(wysoki_meszczyzna[i],sredni_meszczyzna[i]))
print(ans_wysoki_or_sredni)

