def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelsTypes = set(jewels)
    result = 0

    for i in range(len(stones)):
        if stones[i] in jewelsTypes:
            result += 1
            
    return result

numJewelsInStones("aA", "aAAbbbb")



# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
# Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".