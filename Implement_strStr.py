def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

strStr("sadbutsad", "sad")

# must find the first index of needle in haystack string