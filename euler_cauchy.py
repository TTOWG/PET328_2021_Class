def solve(eq, x, y):
    return eval(eq)

def get_val(req_string, type):
    if type == str:
        val = input(req_string)
        if len(val) == 0:
            get_val(req_string, type)
        else:
            return val
    val = 0
    while True:
        try:
            val = type(input(req_string))
        except:
            get_val(req_string, type)

        return val

def euler_cauchy():

    #Value examples
    # eq = 'y-x'
    # x0 = 0
    # y0 = 2
    # h = 0.1
    # xf = 0.5


    eq = get_val('equation in form of x and y: ', str)
    x0 = get_val('Enter x0: ', float)
    y0 = get_val('Enter y0: ', float)
    h = get_val('Enter h: ', float)
    xf = get_val('Enter final value of x: ', float)

    #generate x values
    xl = []
    n = int((xf-x0)/h)
    for i in range(n+1):
        xl.append(round(x0 + h*i, 3))

    yl = [y0] #list of y values
    y_prime = solve(eq, xl[0], yl[0]) #initial y_prime value

    y_prime_list = [y_prime]

    for i, x in enumerate(xl[:-1]):
        y = yl[i]
        y_p1 = y + h*y_prime
        y_c1 = y + 0.5*h*(y_prime + solve(eq, x, y_p1))
        yl.append(y_c1)
        y_prime = solve(eq, x, y)
        y_prime_list.append(y_prime)


    #Since euler-cauchy has 4dp accuracy, we only print in 4dp accuracy
    yl = [round(y, 4) for y in yl]
    y_prime_list = [round(y, 4) for y in y_prime_list]


    #print the table
    print("x     y      y_prime  ")

    for i in range(n):
        print(f"{xl[i]} | {yl[i]} | {y_prime_list[i]}")

    print(f"{xl[-1]} | {yl[-1]} | -   ")


    input("Press enter to exit.")
    return 0
euler_cauchy()
print('done.')