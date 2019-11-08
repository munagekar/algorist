from algorist.string.substring import substring_z, substring_kmp, hash_cal, substring_rabin_karp


def test_substring():
    for f in [substring_z, substring_kmp]:
        assert f("GEEKS FOR GEEKS", "GEEK") == [0, 10]
        assert f("ABI", "ABI") == [0]
        assert f("BABY", "ABY") == [1]
        assert f("BBBB", "BB") == [0, 1, 2]
        assert f("BBBBB", "B") == [0, 1, 2, 3, 4]


def test_substring_rabin_karp():
    ans = substring_rabin_karp("abc", ["a", "b", "c"])
    exp = {"b": [1], "c": [2], "a": [0]}
    assert ans == exp

    ans = substring_rabin_karp("bbbb", ["b"])
    exp = {"b": [0, 1, 2, 3]}
    assert ans == exp

    ans = substring_rabin_karp("defdef", ["de", "ef"])
    exp = {"de": [0, 3], "ef": [1, 4]}
    assert ans == exp


def test_hash_cal():
    assert hash_cal("a") == 1
    assert hash_cal("aa") == 102
