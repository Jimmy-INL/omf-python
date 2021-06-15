"""volume.py: Volume element and geometry"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
import properties

from .base import ProjectElement


class VolumeGridElement(ProjectElement):
    """Contains 3D grid volume spatial information and attributes"""
    tensor_u = properties.List(
        'Tensor cell widths, u-direction',
        properties.Float('', min=0.),
        coerce=True,
    )
    tensor_v = properties.List(
        'Tensor cell widths, v-direction',
        properties.Float('', min=0.),
        coerce=True,
    )
    tensor_w = properties.List(
        'Tensor cell widths, w-direction',
        properties.Float('', min=0.),
        coerce=True,
    )
    axis_u = properties.Vector3(
        'Vector orientation of u-direction',
        default='X',
        length=1,
    )
    axis_v = properties.Vector3(
        'Vector orientation of v-direction',
        default='Y',
        length=1,
    )
    axis_w = properties.Vector3(
        'Vector orientation of w-direction',
        default='Z',
        length=1,
    )
    origin = properties.Vector3(
        'Origin of the Mesh relative to Project coordinate reference system',
        default=[0., 0., 0.],
    )
    subtype = properties.StringChoice(
        'Category of Volume',
        choices=('volume',),
        default='volume',
    )

    _valid_locations = ('vertices', 'cells')

    def location_length(self, location):
        """Return correct data length based on location"""
        if location == 'cells':
            return self.num_cells
        return self.num_nodes

    @property
    def num_nodes(self):
        """Number of nodes (vertices)"""
        return ((len(self.tensor_u)+1) * (len(self.tensor_v)+1) *
                (len(self.tensor_w)+1))

    @property
    def num_cells(self):
        """Number of cells"""
        return len(self.tensor_u) * len(self.tensor_v) * len(self.tensor_w)

    @properties.validator
    def _validate_mesh(self):
        """Check if mesh content is built correctly"""
        if not (np.abs(self.axis_u.dot(self.axis_v) < 1e-6) and                #pylint: disable=no-member
                np.abs(self.axis_v.dot(self.axis_w) < 1e-6) and                #pylint: disable=no-member
                np.abs(self.axis_w.dot(self.axis_u) < 1e-6)):                  #pylint: disable=no-member
            raise ValueError('axis_u, axis_v, and axis_w must be orthogonal')
        return True
