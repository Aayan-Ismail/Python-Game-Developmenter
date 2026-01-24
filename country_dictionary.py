countries = {

}

while True:
    print(":------Country Dictionary Menu------:")
    print("1. insert")
    print("2. display all countries")
    print("3. display all capitals")
    print("4. get capital")
    print("5. delete country")
    choice = int(input("enter choice between 1-5: "))

    if choice == 1:
        country = input("enter country: ")
        capital = input("enter capital: ")
        countries[country] = capital
    
    elif choice == 2:
        print(list(countries.keys()))
    
    elif choice == 3:
        print(list(countries.values()))
    
    elif choice == 4:
        country = input("enter country name: ")
        print(countries.get(country))
    
    elif choice == 5:
        country = input("enter country: ")
        del countries[country]
    
    else: break
