# from app import add, sub, mul, div
# def test_add():
#     result=add(2,3)
#     assert result==5
# def test_sub():
#     result=sub(5,2)
#     assert result==3    

# def test_mul():
#     result=mul(2,3)
#     assert result==6
# def test_div():
#     result=div(6,2)
#     assert result==3


# def test_calc():
#     assert add(1,2)==3
#     assert sub(5,2)==3
#     assert mul(2,3)==6
#     assert div(6,2)==3

# def test_calc_add():
#     assert add(1,2)==3
#     assert add(0,0)==0
#     assert add(-1,1)==0 


#pytest fixture
@pytest.fixture
def calc():
    return calcc()
def test_calc_add(calc):
    assert calc.add(1,2)==3