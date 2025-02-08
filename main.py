def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    print(file_contents)

main()