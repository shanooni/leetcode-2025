def longestSubstring(s: str, k: int) -> int:
    map_ = {}
    for i in range(len(s)):
        map_[s[i]] = map_.get(s[i], 0) + 1
        print(map_)
        if map_.get(s[i]) >= k:
            map_.get(s[i - k]) - 1


longestSubstring("ababbc", 2)

# not correct solution
