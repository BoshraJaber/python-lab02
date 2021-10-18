from lab02.series import fibonacci,lucas 

# to run test we use : pytest
# pytest tests/test_series.py

def test_fibonacci():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected


def test_lucas():
    actual = lucas(9)
    print(actual)
    expected = 76
    assert actual == expected