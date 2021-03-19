import cv2
import numpy as np
import random

def f2s(V):#converting float list to str list
    a=[]
    for i in range(len(V)):
        a.append(str(V[i]))
    return a

def s2f(V):#converting str list to float list
    a=[]
    for i in range(len(V)):
        a.append(float(V[i]))
    return a

def reverse(Vs,height,width):#Converting the coordinates for reversing pics, flipping right to left
    Vs=s2f(Vs)
    R=[width-Vs[0]-Vs[2],Vs[1],Vs[2],Vs[3],width-Vs[4],Vs[5],width-Vs[6],Vs[7],width-Vs[8],Vs[9],width-Vs[10],Vs[11],width-Vs[12],Vs[13]]
    R=f2s(R)
    return R

def noise(im, height, width):#adding noises to pics
    # white noises
    pts_x = np.random.randint(0, width-1 , 1000) #creating thousand random numbers between 0 and 'width-1'
    pts_y = np.random.randint(0, height-1 , 1000)#creating thousand random numbers between 0 and 'height-1'
    im[(pts_y,pts_x)] = (255,255,255) #note that the order is y,x (the color (255,255,255) represents white)

    # black noises
    pts_x = np.random.randint(0, width-1 , 1000)
    pts_y = np.random.randint(0, height-1 , 1000)
    im[(pts_y,pts_x)] = (0,0,0)
    return im

f2 = open('furuta.txt', 'r', encoding='UTF-8')
tx=f2.read()
#print(tx)
tx2=tx.split('# ')
tx2=tx2[1:]
print('==1==')
print(len(tx2))
#print((tx2[:3]))
print('==2==')
print(tx2[0].split()[0])
#########################
output_file='test_.txt'
folder_name='new_pics/'
io=' -1 -1 -1'
z=' '
#########################
for i in range(len(tx2)):#arranging each pic
    pic_name = tx2[i].split()[0].split('/')[1]#reading the names of pics
    im=cv2.imread(pic_name)
    height, width, channels = im.shape[:3]
    imr=cv2.flip(im, 1)#reversing pics, flipping right to left
    
    print('==3==')
    cv2.imwrite('R_' + pic_name, imr)#reversed pics
    cv2.imwrite('W5_' + pic_name, 0.5*im)#brightness-lowered pics
    cv2.imwrite('W15_' + pic_name, 1.5*im#brightness-increased pics

    imn=noise(im,height,width)
    imnr=noise(imr,height,width)
    imn05=noise(0.5*im)
    imn15=noise(1.5*im)
    cv2.imwrite('noises' + pic_name, imn)#pics with noises
    cv2.imwrite('Rnoises' + pic_name, imnr)#reversed pics with noises
    cv2.imwrite('05noises' + pic_name, imn05)#brightness-lowered pics with noises
    cv2.imwrite('15noises' + pic_name, imn15)#brightness-increased pics with noises

    print(pic_name)
    print(height, width, channels)
    s_tx2=tx2[i].split('\n')
    s_tx2=s_tx2[1:]
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
        
#print(23*io)
#print(54*io+' 1')