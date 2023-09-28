



def bagage(N, K):
    elements = [0] * K
    number_of_items = 1
    while N > 0:
        parcel = (number_of_items - 1) % K  
        if number_of_items > N:
            elements[parcel] = N
        else:
            elements[parcel] = number_of_items
        N -= number_of_items
        number_of_items += 1
    print(elements)




def main() -> None:
    print(f'Hello main from : {__file__}')
    bagage(10, 5)

if __name__ == '__main__':
    main()