from gendiff import generate_diff


def main():
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    print(diff)


if __name__ == "__main__":
    main()
