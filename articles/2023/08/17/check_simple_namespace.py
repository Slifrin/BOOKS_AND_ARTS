import types




def main() -> None:
    print(f'Hello main from : {__file__}')
    
    sn_example = types.SimpleNamespace(a=10, b=11, c=12)
    print(sn_example)



if __name__ == '__main__':
    main()