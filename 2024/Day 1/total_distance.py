def main() -> None:
    reading_txt_data()

def reading_txt_data() -> None:
    filename = "sample_data.txt"

    file = open(filename, "r")
    print(file)

if __name__ == "__main__":
    main()