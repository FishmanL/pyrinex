#!/usr/bin/env python
import pytest
import xarray
from pathlib import Path
import pyrinex as pr
#
rdir = Path(__file__).parent


def test_obs3_onesat():
    """
    ./ReadRinex.py tests/demo3.10o  -u G -o tests/test3G.nc
    """

    truth = xarray.open_dataset(rdir/'test3G.nc', group='OBS')

    for u in ('G', ['G']):
        obs = pr.rinexobs(rdir/'demo3.10o', use=u)
        assert obs.equals(truth)


def test_obs3_multisat():
    """
    ./ReadRinex.py tests/demo3.10o  -u G R -o tests/test3GR.nc
    """
    use = ('G', 'R')

    obs = pr.rinexobs(rdir/'demo3.10o', use=use)
    truth = xarray.open_dataset(rdir/'test3GR.nc', group='OBS')

    assert obs.equals(truth)


def test_obs3_allsat():
    """
    ./ReadRinex.py tests/demo3.10o -o tests/test3all.nc
    """

    obs = pr.rinexobs(rdir/'demo3.10o')
    truth = pr.rinexobs(rdir/'test3all.nc', group='OBS')

    assert obs.equals(truth)


if __name__ == '__main__':
    pytest.main()
