import uuid


def create_som_uuid():
    some_uuid = uuid.uuid1()
    print(some_uuid)
    some_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
    print(some_uuid)
    some_uuid = uuid.uuid4()
    print(some_uuid)
    some_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    print(some_uuid)

    print(str(some_uuid))
    print(some_uuid.hex)
    print(some_uuid.bytes)
    print(uuid.UUID(bytes=some_uuid.bytes))

    print(some_uuid.version)
    print(f"{some_uuid.is_safe=}")
    


def main() -> None:
    print(f'Hello main from : {__file__}')
    create_som_uuid()

if __name__ == '__main__':
    main()