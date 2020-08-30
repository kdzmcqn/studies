from abc import abstractmethod, ABC


class TouchScreenLaptop(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        print('*click*')


class HP(TouchScreenLaptop):
    def __init__(self, model):
        super().__init__(model)

    def scroll(self):
        print('scrolling HP')

    def click(self):
        super().click()


class DELL(TouchScreenLaptop):
    def __init__(self, model):
        super().__init__(model)

    def scroll(self):
        print('scrolling Dell')

    def click(self):
        super().click()


HPNotebook = HP('HPNote-1')
print(HPNotebook.model)
HPNotebook.click()
HPNotebook.scroll()

DellNotebook = DELL('Dell N1')
print(DellNotebook.model)
DellNotebook.click()
DellNotebook.scroll()
