def main():
    words = load_words_from_file("words.txt") # Load words from file into a list.
    # define dictionary
    word_dict = {}

    # go through the list
    for word in words:
        # Count towards using a dictionary (key: word, value: count)

        # if the word isn't in the dictionary, said count to one
        if word not in word_dict:
            word_dict[word] = 1

        # if the word is in the dictionary, increment count
        else:
            word_dict[word] += 1


    # print histogram for each word
    for word, count in word_dict.items():
        print_histogram_bar(word, count)

def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words


if __name__ == '__main__':
    main()
