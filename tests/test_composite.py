"""Tests for Composite Element validation"""
import numpy as np
import properties
import pytest

import omf


def test_composite():
    """Test composite element validation"""
    elem = omf.CompositeElement()
    elem.elements = [
        omf.PointSetElement(vertices=np.random.rand(10, 3)),
        omf.PointSetElement(vertices=np.random.rand(10, 3)),
    ]
    assert elem.validate()
    assert elem.location_length('elements') == 2
    elem.attributes = [
        omf.NumericAttribute(array=[1., 2.], location='elements'),
    ]
    assert elem.validate()
    elem.attributes[0].array = [1., 2., 3.]
    with pytest.raises(properties.ValidationError):
        elem.validate()
