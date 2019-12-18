import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

anagram_list = []

userin = input("Welcome to Anagram Finder!\nInput word/name to find anagrams:")
print("Input word = {}".format(userin))
userin = userin.lower()
print("Using word = {}".format(userin))

userin_sorted = sorted(userin)
for word in word_list:
    word = word.lower()
    if word != userin:
        if sorted(word) == userin_sorted:
            anagram_list.append(word)

print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =", *anagram_list, sep='\n')
