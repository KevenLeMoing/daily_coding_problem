from challenges.instructions.easy._1024_facebook import compute

def test_compute():
    bit_example = int('1111 0000 1111 0000 1111 0000 1111 0000')
    assert compute(bit_example) == int('0000 1111 0000 1111 0000 1111 0000 1111')