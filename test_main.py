import pytest
import main as m

def test_fibo():
    sf = m.fibo(3)
    assert "1, 1, 2, " == sf
    
def test_fibo_neg():
    with pytest.raises(ValueError) as ex:
        sf = m.fibo(-2)
    assert str(ex.value) == "No se admiten valores negativos"