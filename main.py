def main():
    path = "books/frankenstein.txt"
    #open file
    word_Count = 0
    with open(path) as f:
        file_contents = f.read()

    #split into individual words
    words = file_contents.split()
    
    #count the words
    for word in words:
        word_Count += 1

    print(word_Count)

main()