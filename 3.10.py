r=int(input('nhap r:'))
import math
def Tinh(R):
    if R>0:
        p=2*r*math.pi
        s=math.pi*r*2
        print('chu vi hinh tron: ',p)
        print('dien tich hinh tron:',s)
    else:
        print('ban kinh khong hop le')
Tinh(R)
        
