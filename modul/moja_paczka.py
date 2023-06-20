import pydantic


class Model(pydantic.BaseModel):
    param: int


def main():
    print("dziala")


def inny():
    print("dziala bardziej")


if __name__ == "__main__":
    print("nie dziala")
