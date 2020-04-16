import tenacity


class A:

    def __init__(self, var):
        self.var = var

    def pr(self):
        return self.var


def main():
    print('dziala')


def inny():
    print('dziala bardziej')


if __name__ == "__main__":
    print('nie dziala')
