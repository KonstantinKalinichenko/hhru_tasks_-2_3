from task2_easy import classify_triangle

def test_classify_triangle():
    assert classify_triangle('23 11 13') == '39.27'

    assert classify_triangle('10 24 26') == 120

    assert classify_triangle('1 1 2') == 'Не существует'
