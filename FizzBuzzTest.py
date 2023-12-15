import  pytest
def fizzBuzz(value):
    return str(value)

# Now instead of repeating the code we can write a utility function
def checkFizzBuzz( value, expectedRetVal ):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal


def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2PassedIn():
    checkFizzBuzz(1, "1")