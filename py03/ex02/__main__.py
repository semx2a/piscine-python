from DiamondTrap import King


def main():

    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)

    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
