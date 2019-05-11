import pytest, sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')
from pocowork import generateShortURL, saveShortURL, readShortURL, readLongURL

strlen = 10
#host = 'http://poco-fy.com/'
longUrl = 'https://sonicdrivein.splunkcloud.com/en-US/account/login?return_to=%2Fen-US%2Fapp%2Fsonic_design%2Fsearch%3Fq%3Dsearch%2520index%253Dprod%2520cf_app_name%253D%2522payment-api%252A%2522%2520%250A%257C%2520rex%2520field%253Dmsg%2520%255C%2522paymentType%255C%2522%253A%255C%2522%2528%253F%253CpaymentType%253E%255Cw%252B%2529%2520%250A%257C%2520rex%2520field%253Dmsg%2520%255C%2522orderId%255C%2522%253A%255C%2522%2528%253F%253CorderId%253E%255Cw%252B%2529%250A%257C%2520rex%2520field%253Dmsg%2520%255C%2522paymentStatus%255C%2522%253A%255C%2522%2528%253F%253CpaymentStatus%253E%255Cw%252B%2529%250A%257C%2520dedup%2520orderId%250A%257C%2520eval%2520status%253Dcase%2528like%2528paymentStatus%252C%2522APPROVED_%2525%2522%2529%252C%2520%2522APPROVED%2522%252C%2520paymentStatus%2520in%2520%2528%2522BLOCKED%2522%252C%2520%2522DECLINED%2522%2529%252C%2520%2522USER_FAILURES%2522%252C%2520paymentStatus%2520in%2520%2528%2522RESOLUTION_TIMEOUT%2522%252C%2520%2522REQUEST_TIMEOUT%2522%252C%2520%2522ERROR%2522%2529%252C%2520%2522SYSTEM_FAILURES%2522%252C%2520true%2528%2529%252C%2520paymentStatus%2529%250A%257C%2520where%2520NOT%2520status%2520in%2520%2528%2522PROCESSING%2522%252C%2520%2522REQUESTED%2522%2529%250A%257C%2520table%2520orderId%2520paymentType%2520status%250A%257C%2520stats%2520count%2520by%2520paymentType%252C%2520status%26display.page.search.mode%3Dverbose%26dispatch.sample_ratio%3D1%26earliest%3D%2540d%26latest%3Dnow%26display.page.search.tab%3Dstatistics%26display.general.type%3Dstatistics%26sid%3D1557432373.37728590'
dbname = 'test.db'
shortUrl = None

def test_generateShortURL():
    result = generateShortURL(strlen, longUrl)
    print('\nShort URL: ' + result)
    assert len(result) == strlen

def test_saveShortURL():
    shortUrl = generateShortURL(strlen, longUrl)
    print('\nPersisting shortURL: ' + shortUrl)
    result, error = saveShortURL(dbname, shortUrl, longUrl)
    assert True == result
    assert error == None

def test_readShortURL():
    result, error = readShortURL(dbname, longUrl)
    print('\nRetrieved shortURL: ' + str(result))
    assert error == None
    assert len(result) == strlen

def test_readLongURL():
    shortUrl = generateShortURL(strlen, longUrl)
    result, error = saveShortURL(dbname, shortUrl, longUrl)
    assert error == None
    assert True == result
    result, error = readLongURL(dbname, shortUrl)
    print('\nRetrieved longURL: ' + str(result))
    assert error == None
    assert result == longUrl
