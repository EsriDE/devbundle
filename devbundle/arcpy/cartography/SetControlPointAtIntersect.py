# Generated documentation for module arcpy.cartography


class SetControlPointAtIntersect(object):
    """
    Creates a control point at vertices that are shared by one or more line or polygon features. This tool is commonly used to synchronize boundary symbology on adjacent polygons.
    """

    @property
    def description(self) -> str:
        return """

        SetControlPointAtIntersect_cartography(in_line_or_polygon_features, {in_features})

        Creates a control point at vertices that are shared by one or more
        line or polygon features. This tool is commonly used to synchronize
        boundary symbology on adjacent polygons.

     INPUTS:
      in_line_or_polygon_features (Feature Layer):
          The line or polygon feature layer.
      in_features {Feature Layer}:
          The line or polygon feature layer with features coincident to the
          input features.

        """