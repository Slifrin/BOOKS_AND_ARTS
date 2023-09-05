
def main() -> None:
    print(f'Hello main from : {__file__}')
    try:
        raise ValueError(345)
    except ValueError as err:
        err.add_note("Enriching Exceptions with Notes")
        raise
    

if __name__ == '__main__':
    main()