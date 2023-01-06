def checkIfPangram(sentence):
    letters = set()

    for i in range(len(sentence)):
       letters.add(sentence[i])

    return len(letters) == 26

checkIfPangram("thequickbrownfoxjumpsoverthelazydog")