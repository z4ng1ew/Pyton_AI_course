def longest_unique_substr(text):
    curr = ""
    pos = 0
    while pos < len(text):
        if text[pos] in curr:
            break
        curr += text[pos]
        pos += 1
    if pos == len(text):
        return curr
    tail = longest_unique_substr(text[1:])
    return tail if len(tail) > len(curr) else curr

print(longest_unique_substr("abcdefab"))
print(longest_unique_substr("sssssss"))
print(longest_unique_substr("abcabcbb"))