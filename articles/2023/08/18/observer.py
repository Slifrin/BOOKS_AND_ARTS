from abc import ABC, abstractmethod


class Channel:
    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = list()

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def send_notifications(self, event):
        for sub in self.subscribers:
            sub.notify(self.name, event)


class Subscriber(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def notify(self, channel, event):
        ...


class LoudSubscriber(Subscriber):
    def notify(self, channel, event):
        print(f"{self.name} with di: {id(self)} received {event=} from {channel=}")


def show_observer():
    from os.path import basename
    print()
    print(f"{basename(__file__):_^80}")
    channel = Channel("Informations")

    channel.subscribe(LoudSubscriber("John"))
    channel.subscribe(LoudSubscriber("Bob"))
    channel.subscribe(LoudSubscriber("Tom"))

    channel.send_notifications("There is new event")