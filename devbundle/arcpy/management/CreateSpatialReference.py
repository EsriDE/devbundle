# Generated documentation for module arcpy.management


class CreateSpatialReference(object):
    """
    Creates a spatial reference for use in ModelBuilder.
    """

    @property
    def description(self) -> str:
        return """

        CreateSpatialReference_management({spatial_reference}, {spatial_reference_template}, {xy_domain}, {z_domain}, {m_domain}, {template;template...}, {expand_ratio})

        Creates a spatial reference for use in ModelBuilder.

     INPUTS:
      spatial_reference {Spatial Reference}:
          The name of the spatial reference to be created.
      spatial_reference_template {Feature Layer / Raster Dataset}:
          The feature class or layer to be used as a template to set the value
          for the spatial reference.
      xy_domain {Envelope}:
          The allowable coordinate range for x,y coordinates.
      z_domain {String}:
          The allowable coordinate range for z-values.
      m_domain {String}:
          The allowable coordinate range for m-values.
      template {Feature Layer}:
          The feature classes or layers that can be used to define the XY
          Domain.
      expand_ratio {Double}:
          The percentage by which the XY Domain will be expanded.

        """