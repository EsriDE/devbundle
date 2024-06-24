# Generated documentation for module arcpy.management


class MakeXYEventLayer(object):
    """
    Creates a point feature layer based on x- and y-coordinates defined in a table. If the source table contains z-coordinates (elevation values), that field can also be specified in the creation of the event layer. The layer created by this tool is temporary.
    """

    @property
    def description(self) -> str:
        return """

        MakeXYEventLayer_management(table, in_x_field, in_y_field, out_layer, {spatial_reference}, {in_z_field})

        Creates a point feature layer based on x- and y-coordinates defined in
        a table. If the source table contains z-coordinates (elevation
        values), that field can also be specified in the creation of the event
        layer. The layer created by this tool is temporary.

     INPUTS:
      table (Table View):
          The table containing the x- and y-coordinates that define the
          locations of the point features that will be created.
      in_x_field (Field):
          The field in the input table that contains the x-coordinates (or
          longitude).
      in_y_field (Field):
          The field in the input table that contains the y-coordinates (or
          latitude).
      spatial_reference {Spatial Reference}:
          The spatial reference of the coordinates specified in the in_x_field
          and in_y_field parameters. This will be the output event layer's
          spatial reference.
      in_z_field {Field}:
          The field in the input table that contains the z-coordinates.

     OUTPUTS:
      out_layer (Feature Layer):
          The name of the output point event layer.

        """