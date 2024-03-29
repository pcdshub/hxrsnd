#!/usr/bin/env python
import logging
from collections import OrderedDict

import pytest
from ophyd.device import Device

from hxrsnd import rtd

from .conftest import fake_device, get_classes_in_module

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("dev", get_classes_in_module(rtd, Device))
def test_rtd_devices_instantiate_and_run_ophyd_functions(dev):
    device = fake_device(dev)
    assert isinstance(device.read(), OrderedDict)
    assert isinstance(device.read_configuration(), OrderedDict)
