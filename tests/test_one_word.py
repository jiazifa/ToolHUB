from utils import save_csv
import os


def test_caihongpi():
    from hub.one_word import get_caihongpi_info
    one_word = get_caihongpi_info
    content = one_word()
    assert content
    path: str = './.data/test_caihongpi.csv'
    save_csv(path, content.keys(), [[k for k in content.values()]])
    assert os.path.exists(path)


def test_aiciba():
    from hub.one_word import get_acib_info
    one_word = get_acib_info
    content = one_word()
    assert content
    path: str = './.data/test_aciba.csv'

    save_csv(path, content.keys(), [[k for k in content.values()]])
    assert os.path.exists(path)


def test_hitokoto():
    from hub.one_word import get_hitokoto_info as one_word

    content = one_word()
    assert content
    path: str = './.data/test_hitokoto.csv'

    save_csv(path, content.keys(), [[k for k in content.values()]])
    assert os.path.exists(path)


def test_lovelive():
    from hub.one_word import get_lovelive_info as one_word

    content = one_word()
    assert content
    path: str = './.data/test_lovelive.csv'

    save_csv(path, content.keys(), [[k for k in content.values()]])
    assert os.path.exists(path)


def test_wufazhuce():
    from hub.one_word import get_wufazhuce_info as one_word

    content = one_word()
    assert content
    path: str = './.data/test_wufazhuce.csv'
    
    save_csv(path, content.keys(), [[k for k in content.values()]])
    assert os.path.exists(path)
