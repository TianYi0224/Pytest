import pytest
import logging
from src.calculator import Calculator

logger = logging.getLogger(__name__)


@pytest.fixture
def calc():
    """提供一个计算器实例作为测试夹具"""
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(10, 10) == 0
    assert calc.subtract(-5, -3) == -3

def test_multiply(calc):
    a = 10
    logger.info("111测试一下%d", a)
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 100) == 0
    assert calc.multiply(-2, 5) == -10
    logger.info("222测试一下%d", a)

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(0, 1) == 0

def test_divide_by_zero(calc):
    with pytest.raises(ValueError) as excinfo:
        calc.divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)


def test_N69R(calc):
    # calc.N69R_ProgramOrd_2_PhyPage(2201)
    # calc.N69R_RealPage2OrderPage(2160)

    # for WL in range(0,1112):
    #     for CellType in range(1,5):
    #         calc.N69R_WordLineNum_2_PageNum(WL,CellType)

    # calc.PAA_2_FAA(3, 0, 1)
    # calc.BS_2_Blk(0xd4, 6, 1)
    calc.Blk_2_BS(1236, 6, 1, 1)