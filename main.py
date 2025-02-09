def main():
    character_Count = {}         
    path = "books/frankenstein.txt"
    #open file
    word_Count = 0
    with open(path) as f:
        file_contents = f.read()
    #remove capital letters
    lower_string = file_contents.lower()
    #split into individual words
    words = file_contents.split()

    #count the words
    for word in words:
        word_Count += 1

    #count individual characters
    characters =list(lower_string)
    for character in characters:
        if character not in character_Count:
            character_Count[character] = 1
        else:    
            character_Count[character] += 1 

    #sort into list of dictionaries, convert to list of dict
    char_list = [] 
    for char, count in character_Count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)
    print(f"there are {word_Count} words in the book")
    print(f"heres a list of individual character counts in the book: \n {char_list}")

#sorting hat
def sort_on(dict):
    return dict["num"]
main()