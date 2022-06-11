word = "abcd"

def palindrome(l):

    is_palindrome = True
    for i in range (len(word) // 2):
        if word[i] != word[len(word)-i-1]:
            is_palindrome = False

    return is_palindrome

palindrome(word)


