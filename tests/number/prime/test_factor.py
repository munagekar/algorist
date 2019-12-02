from algorist.number.prime.factor import pollard_rho_brent


def test_pollard_rho_brent():
    for num in [10967535067, 215, 35, 195, 707]:
        assert num % pollard_rho_brent(num) == 0
