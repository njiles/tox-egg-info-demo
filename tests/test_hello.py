from tox_egg_info_demo import read_hello

def test_read_hello():
    assert read_hello() == "Hello world\n"
