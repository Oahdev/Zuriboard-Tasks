# Reading Text Files

def read_file_content(filename):
    file = open(filename)
    file = file.read()
    return file

def count_words():
    counts = dict()
    text = read_file_content("./story.txt").split()
    for word in text:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words())