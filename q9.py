def reverse(string):
    invertida = str()
    i = len(string) - 1
    while i>=0:
        invertida += string[i]
        i = i-1
    print(invertida)
    return invertida


def is_palindrome(string):
    aux = reverse(string)
    if aux == string:
        return True
    else:
        return False


def test(passou):
    if passou:
        print("Teste ok")
    else:
        print("Teste FAILED")

def test_suite():
    test(is_palindrome("abba"))
    test(is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(is_palindrome(""))
    
test_suite()