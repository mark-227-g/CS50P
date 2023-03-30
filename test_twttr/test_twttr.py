from twttr import shorten

def test_shorten():
    assert shorten("fox")=="fx"
    assert shorten("Arrive")=="rrv"
    assert shorten("Sunset70")=="Snst70"
    assert shorten("Home.")=="Hm."
    assert shorten("POSITIVE")=="PSTV"