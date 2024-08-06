def centimeters_to_meter(cm):
    return cm / 100 
def meter_to_kilometers(meter):
    return meter / 1000
def grams_to_kilograms(grams):
    return grams / 1000
while True:
    print("unit converter")
    print("1. centemeters_to_meter")
    print("2. meter_to_kilometers")
    print("3. grams_to_kilograms")
    choice = int(input("select option(1/2/3):"))
    if choice == 1:
        cm = float(input("enter the cm:"))
        print(f"{cm} is centimeters {centimeters_to_meter(cm)} meter.")
    elif choice == 2:
        meter = float(input("enter the meters:"))
        print (f"{meter} is meters {meter_to_kilometers(meter)} kilometers.")
    elif choice == 3:
        grams = float(input("enter the grams:"))
        print(f"{grams} is gram {grams_to_kilograms(grams)} kilograms.")
    else:
        print("invalid selection")    
    print("1. yes")
    print("2. no")
    choice1 = (1/2)
    choice1 = int(input("enter your choice(1/2):"))
    if choice1 == 1:
            print("return on unit converter:")
    elif choice1 == 2:
        print("close:")
        break
