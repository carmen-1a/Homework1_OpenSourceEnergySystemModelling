import pytest
from el_price_calculator import current_grid_fee, NETZENTGELT


def test_standard_fee_outside_snap_month():
    assert current_grid_fee(1, 12) == pytest.approx(NETZENTGELT["Kärnten"])


def test_standard_fee_before_snap_hours():
    assert current_grid_fee(5, 9) == pytest.approx(NETZENTGELT["Kärnten"])


def test_standard_fee_after_snap_hours():
    assert current_grid_fee(5, 16) == pytest.approx(NETZENTGELT["Kärnten"])


def test_snap_fee_during_active_hours():
    expected = NETZENTGELT["Kärnten"] * 0.8
    assert current_grid_fee(5, 12) == pytest.approx(expected)


def test_snap_fee_april_boundary():
    expected = NETZENTGELT["Kärnten"] * 0.8
    assert current_grid_fee(4, 10) == pytest.approx(expected)


def test_snap_fee_september_boundary():
    expected = NETZENTGELT["Kärnten"] * 0.8
    assert current_grid_fee(9, 15) == pytest.approx(expected)


def test_october_no_snap():
    assert current_grid_fee(10, 12) == pytest.approx(NETZENTGELT["Kärnten"])


def test_discounted_fee_is_lower():
    normal = current_grid_fee(2, 12)
    discounted = current_grid_fee(6, 12)
    assert discounted < normal
    
