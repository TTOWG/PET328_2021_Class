import math

#.Input Statements
rw = float(input('Enter the well radius?: '))
op = float(input('Enter the phasing angle?: '))
rp = float(input('Enter the peforation radius?: '))
lp = float(input('Enter the length of perforation?: '))
kv = float(input('Enter the formation vertical permeability?: '))
kh = float(input('Enter the formation horizontal permeability?: '))
kpd = float(input('Enter the perforation damage zone permeability?: '))
rpd = float(input('Enter the peforation radius of drilling damage zone?: '))
ldd = float(input('Enter the length of drilling damage zone permeabilty?: '))
kdd = float(input('Enter the formation drilling damaged zone permeability?: '))
hp = float(input('Enter the peforation height/spacing?, if not available, type 0: '))
if hp == 0:
    sd= float(input('Enter the shot density value?: '))
    hp= 1/sd

#.Initializing Output Variables

if op == 0:
    a_0= 0.250
    a_1=-2.091
    a_2=0.0453
    b_1=5.1313
    b_2=1.8672
    c_1=1.6*10**-1
    c_2=2.675
elif op == 45:
    a_0= 0.860
    a_1=-1.788
    a_2=0.2398
    b_1=1.1915
    b_2=1.6392
    c_1=4.6*10**-5
    c_2=8.791
elif op == 60:
    a_0= 0.813
    a_1=-1.898
    a_2=0.1023
    b_1=1.3654
    b_2=1.6490
    c_1=3*10**-4
    c_2=7.509
elif op == 90:
    a_0= 0.726
    a_1=-1.905
    a_2=0.1023
    b_1=1.5674
    b_2=1.6935
    c_1=1.9*10**-3
    c_2=6.155

#. Defining Functions 
def s_v(lp, rw):
    hd=(hp/lp)*(math.sqrt(kh/kv))
    rd= (rp/(2*hp))*(1+ math.sqrt(kv/kh))
    a= (a_1*(math.log10(rd)))+a_2
    b= (b_1*rd)+b_2
    sv= (10**a)*(hd**(b-1))*(rd**b)
    return sv

def s_h(lp, rw):
    if op == 0:
        r_w=lp/4
    elif op > 0:
        r_w=a_0*(rw + lp)
    sh = math.log(rw/r_w)
    return sh

def s_wb(lp,rw):
    rwd= (rw/(lp+rw))
    swb = c_1*math.exp(c_2*rwd)
    return swb

#. Conditional Statement

if lp>ldd:
    lp = lp - ((1-(kdd/kh))*ldd)
    rw = rw + ((1-(kdd/kh))*ldd)

    sh=s_h(lp,rw)
    sv=s_v(lp,rw)
    rwd= (rw/(lp+rw))
    swb=s_wb(lp,rw)
    spd = ((hp/lp)*((kh/kpd)-1))*(math.log(rpd/rp))
    Sp = sh+sv+swb+spd
    
#.Displaying The Results
    print('')
    print('The Plane-flow Effect(Sh) is {0:.3f}:'.format(sh))
    print('The Wellbore Effect(Swb) is {0:.3f}'.format(swb))
    print('The Vertical Coverging Effect(Sv) is {0:.3f}'.format(sv))
    print('The Drilling Damages Zone Effect(Spd) is {0:.3f}'.format(spd))
    print('The skin of the formation is {0:.3f}'.format(Sp))


else:
    sh=s_h(lp,rw)
    sv=s_v(lp,rw)
    swb=s_wb(lp,rw)
    s_p = sh+sv+swb

#.Displaying The Results
    print('')
    print('The Plane-flow Effect(Sh) is {0:.3f}:'.format(sh))
    print('The Wellbore Effect(Swb) is {0:.3f}:'.format(swb))
    print('The Vertical Coverging Effect(Sv) is {0:.3f}:'.format(sv))
    print('The skin of the formation is {0:.3f}:'.format(s_p))




    
   
