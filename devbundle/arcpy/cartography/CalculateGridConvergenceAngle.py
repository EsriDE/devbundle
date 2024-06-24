# Generated documentation for module arcpy.cartography


class CalculateGridConvergenceAngle(object):
    """
    Calculates the rotation angle for true north based on the center point of each feature in a feature class and populates this value in a specified field. This field can be used in conjunction with a spatial map series to rotate each map to true north.
    """

    @property
    def description(self) -> str:
        return """

        CalculateGridConvergenceAngle_cartography(in_features, angle_field, {rotation_method}, {coordinate_sys_field})

        Calculates the rotation angle for true north based on the center point
        of each feature in a feature class and populates this value in a
        specified field. This field can be used in conjunction with a spatial
        map series to rotate each map to true north.

     INPUTS:
      in_features (Feature Layer):
          The input feature class (points, multipoints, lines, and polygons).
      angle_field (Field):
          The existing field that will be populated with the true north
          calculation value in decimal degrees.
      rotation_method {String}:
          Specifies the method used to calculate the rotation
          value.GEOGRAPHIC-The angle is calculated clockwise with 0 at the top.
          This
          is the default.ARITHMETIC-The angle is calculated counterclockwise
          with 0 at the
          right.GRAPHIC-The angle is calculated counterclockwise with 0 at the
          top.
      coordinate_sys_field {Field}:
          The field containing a projection engine string for a projected
          coordinate system to be used for angle calculation. The angle
          calculation for each feature will be based on the projected coordinate
          system projection engine string for the specific feature. In cases of
          an invalid value, the tool will use the cartographic coordinate system
          specified in the Cartography environment settings. The default is
          none, or no field specified. When no field is specified, the projected
          coordinate system used for calculation will be taken from the
          Cartography environment settings.

        """