
side = 5

def half_area():
    area = side * side
    def divide():
        # area /= 2 # will raise exception
        print(area)
    
    def divide2():
        nonlocal area
        area /= 2

    divide()
    divide2()
    return area



def main():
    print('Hello main')
    print(half_area())

if __name__ == '__main__':
    main()