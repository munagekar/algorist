from algorist.string.substring import substring_z, substring_kmp


def test_substring():
    for f in [substring_z, substring_kmp]:
        assert f("GEEKS FOR GEEKS", "GEEK") == [0, 10]
        assert f("ABI", "ABI") == [0]
        assert f("BABY", "ABY") == [1]
        assert f("BBBB", "BB") == [0, 1, 2]
        assert f("BBBBB", "B") == [0, 1, 2, 3, 4]
