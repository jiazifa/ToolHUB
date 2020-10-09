from task.one_word import get_caihongpi_info


def test_caihongpi():
    content = get_caihongpi_info()
    assert content
