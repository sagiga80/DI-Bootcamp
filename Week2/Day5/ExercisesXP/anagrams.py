
from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()

    while True:
        print("\n==== Anagram Finder ====")
        print("1 to type your word\n2 to end the game")
        choice = input("Choose 1 or 2: ").strip()
        if choice == '2':
            print("\nThank you for playing\n")
            break
        if choice != '1':
            print("\nyour choice must be 1 or 2.\nTry again!")
            continue
        user_input = input("Enter a single word: ").strip()

        # Input validation
        if ' ' in user_input:
            print("\nSingle word only!\nTry again")
            continue
        if not user_input.isalpha():
            print("\nAlphabetic characters only.\nTry Again!")
            continue
        word = user_input
        print(f"\nYOUR WORD: \"{word.upper()}\"")
        if checker.is_valid_word(word):
            print("This is a valid English word.")
        else:
            print("This is NOT a valid English word.")

        anagrams = checker.get_anagrams(word)
        if anagrams:
            print("Anagrams for your word:", ', '.join(anagrams))
        else:
            print("No anagrams found.")

main()