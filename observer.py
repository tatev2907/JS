from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, message: str) -> None:

        pass

class Observable(metaclass=ABCMeta):


    def __init__(self) -> None:

        self.observers = []

    def register(self, observer: Observer) -> None:

        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:

        for observer in self.observers:
            observer.update(message)

class Blog(Observable):

    def add_psot(self, post: str) -> None:

        self.notify_observers(post)

class Person(Observer):
    def __init__(self, name: str) -> None:
      self.name = name

    def update(self, message: str) -> None:

        print(f'{self.name} read a new post: {message}')

if __name__ == '__main__':
    newspaper = Blog()
    newspaper.register(Person('John'))
    newspaper.register(Person('Maya'))
    newspaper.add_news('New sensation post')

