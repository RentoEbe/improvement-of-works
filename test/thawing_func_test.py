from utils.concession.thawing import Thawing
def test_thawing():
    x = Thawing(100, 100)
    y = Thawing(291, 187)
    z = Thawing(0, 0)
    x.thawing()
    y.thawing()
    assert (x.loaf_bags, x.sausage_bags) == (17, 10)
    assert (y.loaf_bags, y.sausage_bags) == (49, 19)
    assert (z.loaf_bags, z.sausage_bags) == (0, 0)

