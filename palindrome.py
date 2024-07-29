def palimdrome(word):
    l = len(word)
    last = l-1
    for i in range(l):
        if i>l/2:
            print("Word is palindrome")
            break
        if word[i] == word[last]:
            last = last - 1
            continue
        else:
            print("Word is not a palindrome")
            break
check = input("enter the word: ")
palimdrome(check)