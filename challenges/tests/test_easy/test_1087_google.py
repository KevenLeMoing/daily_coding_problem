from challenges.instructions.easy._1087_google import compute

def test_compute():
    assert compute(a='abcde', b='cdeab') == True
    assert compute(a='x', b='cdeab') == False
    assert compute(a='abcde', b='abcdet') == False
    assert compute(a='', b='') == True
    assert compute(a='abcde', b='abcde') == True
    assert compute(a='abcde', b='aecdb') == True
