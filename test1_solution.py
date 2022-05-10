#...TTOWG!
 # Way to go:
     # Simply replace all the input statements requesting values of
     # parameters with arguments for the function to be created
     # With that, those parameters need not be requested one after
     # the other, but can be passed as arguments when the function
     # get called.
def stoiip_discretized(Lx, Ly, h, nx, ny, boi, poro_list, swi_list): # 2 marks!
                            # poro_list and swi_list would be passed as lists.
    # discretizing the reservoir
    delta_x = Lx/nx
    delta_y = Ly/ny
    # calculating the area per block
    area = delta_x*delta_y
    # initializing output variables
    total_stoiip = 0
    stoiip_list =[] # 1 mark!
            # Neccessary to initialized a list to hold stoiip_list
            # A list is appropriate here since it can be updated with
            # stoiip_list.append, in the loop.
    # the 'for' loop
    for j in range(1,ny+1):
        for i in range(1,nx+1):
            block_n_order = (nx*(j-1))+i
            poro = poro_list[(block_n_order - 1)] # 1 mark! Take note of the -1; because index starts at 0
            sw = swi_list[(block_n_order - 1)]  # 1 mark! Take note of the -1; because index starts at 0
            block_stoiip = (7758*area*h*poro*(1-sw))/boi
            stoiip_list.append(block_stoiip) # 1 mark! That's how the stoiip_list is updated 
            total_stoiip = total_stoiip + block_stoiip
    return total_stoiip, stoiip_list # 1 mark! A tuple containing total_stoiip and stoiip_list is returned

# Sample calls
# Sample call 1
volumetrics = stoiip_discretized(100, 100, 40, 2, 1, 1.2, [0.2, 0.2], [0.3, 0.3]) 
print(volumetrics)

# Sample call 2: with the output tuple unpacked into two separate variables
(my_STOIIP, my_STOIIP_list) = stoiip_discretized(100, 100, 40, 2, 1, 1.2, [0.2, 0.2], [0.3, 0.3]) 

print(my_STOIIP)
print(my_STOIIP_list)

    
  
