def string_has_repeating_chars(s: str) -> bool:
    for i in range(0, len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return True
    return False


def substring_without_repeating_chars(s: str) -> int:
    max_len = 0
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            k = s[i:j]
            if not string_has_repeating_chars(k) and len(k) > max_len:
                max_len = len(k)

    return max_len


if __name__ == "__main__":
    for s in ["abcabcbb", "a", "aab", "aab", "abcba", "abcdabcf"]:
        print(f"{s}: {substring_without_repeating_chars(s)}")
