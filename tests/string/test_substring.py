from algorist.string.substring import substring_z


def test_substring_z():
    assert substring_z("GEEKS FOR GEEKS", "GEEK") == [0, 10]
    assert substring_z("ABI", "ABI") == [0]
    assert substring_z("BABY", "ABY") == [1]
    assert substring_z("BBBB", "BB") == [0, 1, 2]
