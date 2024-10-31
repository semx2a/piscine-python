from new_student import Student


def main():

    try:
        student = Student(name="Edward", surname="agle")
        print(student)

        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
