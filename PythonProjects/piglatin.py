def Prompt():
    print("""
    Welcome to Pig Latin translator!
    """)


def translate():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = input("Enter word to translate into Pig Latin:")
    first = word[0]
    print("Translating " + word + " into pig latin...")
    if first.lower() in vowels:
        print(word + "way")
        input("Translation complete!")
    else:
        print(word[1:] + word[0] + "ay")
        input("Translation complete!")


Prompt()
translate()
