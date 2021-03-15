f_ = open('furuta_choice.txt', 'r', encoding='UTF-8')
t=f_.read()
t2=t.split()
print(len(t2))
print(t2)


f2 = open('furuta.txt', 'r', encoding='UTF-8')
tx=f2.read()
#print(tx)
tx2=tx.split('# ')
tx2=tx2[1:]
print(len(tx2))
#print((tx2[:3]))
output_file='out.txt'
print(tx2[0].split()[0])

for i in range(len(tx2)):
    if tx2[i].split()[0].split('/')[1] in t2:
        print('!')
        print(tx2[i].split()[0])
        with open(output_file, 'a', encoding='UTF-8') as f:
            f.writelines('# '+ tx2[i])        

