# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('story.txt', 'r') as f:
        contents = f.read()
        print(contents)
        f.close()
    #return "Hello World"

read_file_content("story.txt")


def count_words(text):
    text = open("story.txt")
    di = dict()
    for lin in text:
        lin = lin.rstrip()
        # print(lin)
        words = lin.split()
        # print(words)
        for w in words:
            di[w] = di.get(w,0) + 1

    print(di)

count_words("story.txt")
