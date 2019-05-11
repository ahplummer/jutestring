from sqlitedriver import sqliteclass
from randomizer import getRandomString


def generateShortURL(strlen, longurl):
    shorturl = getRandomString(strlen)
    return shorturl

def saveShortURL(dbname, shorturl, longurl):
    sqlite = sqliteclass(dbname)
    result, error = sqlite.insertData(shorturl, longurl)
    return result, error

def readShortURL(dbname, longurl):
    sqlite = sqliteclass(dbname)
    result, error = sqlite.readShortUrl(longurl)
    return result, error

def readLongURL(dbname, shorturl):
    sqlite = sqliteclass(dbname)
    result, error = sqlite.readLongUrl(shorturl)
    return result, error