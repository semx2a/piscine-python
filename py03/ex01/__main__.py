from S1E9 import Stark
from S1E7 import Baratheon, Lannister
from S1E9 import Character


def main():

    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print(Ned.__str__)

        print("---")

        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)

        Hodor = Character("Hodor")
        print(Hodor.__dict__)
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"Exception: {e}")

    finally:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)

        print("---")

        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)

        print("---")

        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {Jaine.first_name, type(Jaine).__name__}, \
Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
