def lengthOfLongestSubstring(ary):
    longest = 0
    for st in range(0, len(ary), 1):
        for ed in range(st+1, len(ary), 1):
            if ary[st] != ary[ed]:
                temp_str = ary[st:ed]
                if longest < len(temp_str):
                    longest = len(temp_str)
                    print(longest)
            else:
                break
    return longest


str1 = 'asodpadsop'

print(lengthOfLongestSubstring(str1))
