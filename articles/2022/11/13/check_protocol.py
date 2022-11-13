

from typing import Protocol


class Device(Protocol):
    def connect(self, to: str):
        ...

    def run(self):
        ...


class Robot:
    def connect(self, to: str):
        print(f"Robot is connectiong to {to}")

    def run(self):
        print("Running Robot")

class Heafphones:
    def connect(self, to: str):
        print(f"Headphones are connectiong to {to}")


def do_device_stuff(device: Device):
    device.connect("PC")
    device.run()



def main() -> None:
    print(f'Hello main from : {__file__}')
    robot = Robot()
    do_device_stuff(robot)
    headphones = Heafphones()
    do_device_stuff(headphones)

if __name__ == '__main__':
    main()