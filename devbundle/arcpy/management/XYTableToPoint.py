# Generated documentation for module arcpy.management


class XYTableToPoint(object):
    """
    Creates a point feature class based on x-, y-, and z-coordinates from a table.
    """

    @property
    def description(self) -> str:
        return """

        XYTableToPoint_management(in_table, out_feature_class, x_field, y_field, {z_field}, {coordinate_system})

        Creates a point feature class based on x-, y-, and z-coordinates from
        a table.

     INPUTS:
      in_table (Table View):
          The table containing the x- and y-coordinates that define the
          locations of the point features that will be created.
      x_field (Field):
          The field in the input table that contains the x-coordinates (or
          longitude).
      y_field (Field):
          The field in the input table that contains the y-coordinates (or
          latitude).
      z_field {Field}:
          The field in the input table that contains the z-coordinates.
      coordinate_system {Spatial Reference}:
          The coordinate system of the x- and y-coordinates. This will be the
          coordinate system of the output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output point features.

        """