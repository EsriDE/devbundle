# Generated documentation for module arcpy.management


class TableToEllipse(object):
    """
    Creates a feature class containing geodetic or planar ellipses from the values in an x-coordinate field, y-coordinate field, major axis and minor axis fields, and azimuth field of a table.
    """

    @property
    def description(self) -> str:
        return """

        TableToEllipse_management(in_table, out_featureclass, x_field, y_field, major_field, minor_field, distance_units, {azimuth_field}, {azimuth_units}, {id_field}, {spatial_reference}, {attributes}, {geometry_type}, {method})

        Creates a feature class containing geodetic or planar ellipses from
        the values in an x-coordinate field, y-coordinate field, major axis
        and minor axis fields, and azimuth field of a table.

     INPUTS:
      in_table (Table View):
          The input table. It can be a text file, CSV file, Excel file, dBASE
          table, or geodatabase table.
      x_field (Field):
          A numerical field in the input table containing the x-coordinates (or
          longitudes) of the center points of ellipses to be positioned in the
          output coordinate system specified by the spatial_reference parameter.
      y_field (Field):
          A numerical field in the input table containing the y-coordinates (or
          latitudes) of the center points of ellipses to be positioned in the
          output coordinate system specified by the spatial_reference parameter.
      major_field (Field):
          A numerical field in the input table containing major axis lengths of
          the ellipses.
      minor_field (Field):
          A numerical field in the input table containing minor axis lengths of
          the ellipses.
      distance_units (String):
          Specifies the units that will be used for the major_field and
          minor_field parameters.METERS-The units will be meters.KILOMETERS-The
          units will be
          kilometers.MILES-The units will be miles.NAUTICAL_MILES-The units will
          be nautical miles.FEET-The units will be feet.US_SURVEY_FEET-The units
          will be U.S. survey feet.
      azimuth_field {Field}:
          A numerical field in the input table containing azimuth angle values
          for the major axis rotations of the output ellipses. The values are
          measured clockwise from north.
      azimuth_units {String}:
          Specifies the units that will be used for the azimuth_field
          parameter.DEGREES-The units will be decimal degrees. This is the
          default.MILS-The units will be mils.RADS-The units will be
          radians.GRADS-The units will be gradians.
      id_field {Field}:
          A field in the input table. This field and the values are included in
          the output and can be used to join the output features with the
          records in the input table.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature class. A spatial
          reference can be specified as any of the following:        The path to
          a .prj file, such as C:/workspace/watershed.prjThe path to
          a feature class or feature dataset whose spatial reference
          you want to apply, such as
          C:/workspace/myproject.gdb/landuse/grasslandA SpatialReference object,
          such as
          arcpy.SpatialReference("C:/data/Africa/Carthage.prj")
      attributes {Boolean}:
          Specifies whether the remaining input fields will be added to the
          output feature class.NO_ATTRIBUTES-The remaining input fields will not
          be added to the
          output feature class. This is the default. ATTRIBUTES-The
          remaining input fields will be added to the
          output feature class. A new field,, will also be added to the output
          feature class to store the input feature ID values. ORIG_FID
      geometry_type {String}:
          Specifies the geometry type for the output feature class.LINE-An
          output polyline feature class will be created. This is the
          default.POLYGON-An output polygon feature class will be created.
      method {String}:
          Specifies whether the ellipse will be generated based on geodesic or
          planar measurements.GEODESIC-A geodesic ellipse will be generated. The
          ellipse will
          accurately represent the shape on the surface of the earth. This is
          the default.PLANAR-A planar ellipse will be generated on the projected
          plane. It
          usually does not accurately represent the shape on the surface of the
          earth as a geodesic ellipse does. This option is not available for
          geographic coordinate systems.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class that will contain geodetic or planar
          ellipses.

        """