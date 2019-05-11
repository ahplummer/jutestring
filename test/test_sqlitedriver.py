import pytest, sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

from sqlitedriver import sqliteclass

dbname = 'test.db'
shorturl = "shortdata"
longurl = "longdata"

@pytest.fixture(scope='module')
def resource_setup(request):
    print('Setting up resources for testing')
    if os.path.exists(dbname):
        os.remove(dbname)
    def resource_teardown():
        print('Tearing down resources from testing')
        if os.path.exists(dbname):
            os.remove(dbname)
    request.addfinalizer(resource_teardown)

def test_createTable(resource_setup):
    sqlitedriver = sqliteclass(dbname)
    result, error = sqlitedriver.createTable()
    assert None == error
    assert True == result

def test_insertData(resource_setup):
    sqlitedriver = sqliteclass(dbname)
    result, error = sqlitedriver.insertData(shorturl, longurl)
    assert None == error
    assert True == result

def test_readShortUrl(resource_setup):
    sqlitedriver = sqliteclass(dbname)
    result, error = sqlitedriver.readShortUrl(longurl)
    assert None == error
    assert shorturl == result
    result, error = sqlitedriver.readShortUrl("blah")
    assert None == error
    assert None == result

def test_deleteShortUrl(resource_setup):
    sqlitedriver = sqliteclass(dbname)
    result, error = sqlitedriver.readShortUrl(longurl)
    assert None == error
    assert shorturl == result
    result, error = sqlitedriver.deleteShortUrl(longurl)
    assert None == error
    assert 1 == result
