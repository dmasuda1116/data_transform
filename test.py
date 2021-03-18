import cv2
def f2s(V):
    a=[]
    for i in range(len(V)):
        a.append(str(V[i]))
    return a

def s2f(V):
    a=[]
    for i in range(len(V)):
        a.append(float(V[i]))
    return a


def reverse(Vs,height,width):
    
    Vs=s2f(Vs)
    R=[width-Vs[0]-Vs[2],Vs[1],Vs[2],Vs[3],width-Vs[4],Vs[5],width-Vs[6],Vs[7],width-Vs[8],Vs[9],width-Vs[10],Vs[11],width-Vs[12],Vs[13]]
    R=f2s(R)
    return R
def transpose(Vs,height,width):
    Vs=s2f(Vs)
    T=[width-Vs[0]-Vs[2],height-Vs[1],Vs[2],Vs[3],width-Vs[4],height-Vs[5],width-Vs[6],height-Vs[7],width-Vs[8],height-Vs[9],width-Vs[10],height-Vs[11],width-Vs[12],height-Vs[13]]
    T=f2s(T)
    return T

f2 = open('furuta.txt', 'r', encoding='UTF-8')
tx=f2.read()
#print(tx)
tx2=tx.split('# ')
tx2=tx2[1:]
print('==1==')
print(len(tx2))
#print((tx2[:3]))
output_file='test_.txt'
print('==2==')
print(tx2[0].split()[0])
folder_name='new_pics/'
io=' -1 -1 -1'
z=' '
for i in range(len(tx2)):
    pic_name = tx2[i].split()[0].split('/')[1]
    im=cv2.imread(pic_name)
    imr=cv2.flip(im, 1)
    imt=cv2.flip(im, -1)
    print('==3==')
    cv2.imwrite('R_' + pic_name, imr)
    cv2.imwrite('T_' + pic_name, imt)

    print(pic_name)
    height, width, channels = im.shape[:3]
    print(height, width, channels)
    s_tx2=tx2[i].split('\n')
    s_tx2=s_tx2[1:]
    print(type(height))
    for j in range(len(s_tx2)-1):
        v=s_tx2[j].split()
        print('==4==')
        print(v)
        print('==5==')
        print(len(v))
        x,y,w,h,x_re,y_re,x_le,y_le,x_rn,y_rn,x_ln,y_ln,x_m,y_m=v[0],v[1],v[2],v[3],v[4],v[5],v[7],v[8],v[79],v[80],v[82],v[83],v[88],v[89]
        Vs=[x,y,w,h,x_re,y_re,x_le,y_le,x_rn,y_rn,x_ln,y_ln,x_m,y_m]
        #print(tx2[i].split()[0])
        print('==6==')
        print(Vs)
        R=reverse(Vs,height,width)
        if j==0:
            with open(output_file, 'a', encoding='UTF-8') as f:
                f.writelines('# '+ folder_name + 'R_' + pic_name+'\n')
            with open(output_file, 'a', encoding='UTF-8') as f:
                f.writelines(R[0]+z+R[1]+z+R[2]+z+R[2]+z+R[4]+z+R[5]+' 0.0'+z+R[6]+z+R[7]+' 0.0'+23*io+z+R[8]+z+R[9]+z+R[10]+z+R[11]+io+z+R[12]+z+R[13]+54*io+' 1\n')
        else:
            with open(output_file, 'a', encoding='UTF-8') as f:
                f.writelines(R[0]+z+R[1]+z+R[2]+z+R[2]+z+R[4]+z+R[5]+' 0.0'+z+R[6]+z+R[7]+' 0.0'+23*io+z+R[8]+z+R[9]+z+R[10]+z+R[11]+io+z+R[12]+z+R[13]+54*io+' 1\n')
"""
        T=transpose(Vs,height,width)
        if j==0:
            with open(output_file, 'a', encoding='UTF-8') as f:
                f.writelines('# '+ folder_name + 'T_' + pic_name+'\n')
            with open(output_file, 'a', encoding='UTF-8') as f:
                f.writelines(T[0]+z+T[1]+z+T[2]+z+T[2]+z+T[4]+z+T[5]+' 0.0'+z+T[6]+z+T[7]+' 0.0'+23*io+z+T[8]+z+T[9]+z+T[10]+z+T[11]+io+z+T[12]+z+T[13]+54*io+' 1\n')
        else:
            with open(output_file, 'a', encoding='UTF-8') as f:
                f.writelines(T[0]+z+T[1]+z+T[2]+z+T[2]+z+T[4]+z+T[5]+' 0.0'+z+T[6]+z+T[7]+' 0.0'+23*io+z+T[8]+z+T[9]+z+T[10]+z+T[11]+io+z+T[12]+z+T[13]+54*io+' 1\n')
"""

#print(23*io)
#print(54*io+' 1')