n=int(input("Enter the number of samples?:"))

tsoh=0
tswoh=0
toh=0

def soh(h,poro,so):
    soh= h*poro*so
    return soh
def swoh(h,poro,so):
    soh= h*poro*so
    return soh

list_soh=[]
list_swoh=[]

for x in range(1,n+1):
    sample_position= (x)
    h=float(input("Enter the thickness of sample {0}?:".format(sample_position)))
    poro=float(input("Enter the porosity of sample {0}?:".format(sample_position)))
    so=float(input("Enter the oil saturation of sample {0}?:".format(sample_position)))
    swo=float(input("Enter the water saturation of sample {0}?:".format(sample_position)))
    s_oh=soh(h,poro, so)
    s_woh= swoh(h,poro,so)
    oh= h*poro
    toh= toh+oh
    tsoh= tsoh+s_oh
    tswoh= tswoh+s_woh
    list_soh.append(s_oh)
    list_swoh.append(s_woh)
print('SOH=', list_soh)
print('SWOH=', list_swoh)
print("The average oil saturation: {0:.3f}".format(tsoh/toh))
print("The average water saturation: {0:.3f}".format(tswoh/toh))


    



