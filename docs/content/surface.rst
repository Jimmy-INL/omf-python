.. _surfaces:

Surface
*******

Transfer geological domains from 3D modelling software to Resource Estimation software.

.. image:: /images/Surface.png

Elements
--------

.. image:: /images/SurfaceGeometry.png
    :align: center

.. autoclass:: omf.surface.SurfaceElement

.. image:: /images/SurfaceGridGeometry.png
    :align: center

.. autoclass:: omf.surface.SurfaceGridElement

Attributes
----------

Attributes is a list of :ref:`attributes <attributes>`. For Surfaces,
:code:`location='vertices'` and :code:`location='faces'` are valid.

Textures
--------

Textures are :ref:`ImageTexture <textures>` mapped to the Surface.
