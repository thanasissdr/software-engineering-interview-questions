def is_palindrome(s: str) -> bool:
    return s == s[::-1]


if __name__ == "__main__":
    strings = ["abba", "abc"]
    for s in strings:
        if is_palindrome(s):
            print(f"{s} is palindrome")
        else:
            print(f"{s} is not palindrome")
