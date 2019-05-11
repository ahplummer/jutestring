import string, random

def getRandomLetter():
    return random.choice(string.ascii_letters)

def getRandomString(length):
    result = ''
    for i in range(0, length):
        result += getRandomLetter()
    return result

if __name__ == "__main__":
    print(getRandomString(13))