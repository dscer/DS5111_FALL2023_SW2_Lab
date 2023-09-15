import sys
sys.path.append(".")

import bin.clockdeco_param as cp

def test_smoke():
    assert cp.snooze5111(0.5111) == '0.5111'
