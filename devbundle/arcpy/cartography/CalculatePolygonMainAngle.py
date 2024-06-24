# Generated documentation for module arcpy.cartography


class CalculatePolygonMainAngle(object):
    """
    Calculates the dominant angles of input polygon features and assigns the values to a field to use to orient symbology such as markers or hatch lines within the polygons.
    """

    @property
    def description(self) -> str:
        return """

        CalculatePolygonMainAngle_cartography(in_features, angle_field, {rotation_method})

        Calculates the dominant angles of input polygon features and assigns
        the values to a field to use to orient symbology such as markers or
        hatch lines within the polygons.

     INPUTS:
      in_features (Feature Layer):
          The input polygon features.
      angle_field (Field):
          The field that will be updated with the polygon main angle values.
      rotation_method {String}:
          Specifies the method and origin point of rotation that will be
          used..GEOGRAPHIC-The angle will be calculated clockwise with 0 at the
          top
          (north).ARITHMETIC-The angle will be calculated counterclockwise with
          0 at the
          right (east).GRAPHIC-The angle will be calculated counterclockwise
          with 0 at the
          top (north). This is the default.

        """