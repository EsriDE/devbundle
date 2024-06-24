# Generated documentation for module arcpy.management


class BearingDistanceToLine(object):
    """
    Creates a feature class containing geodetic or planar line features from the values in an x-coordinate field, y-coordinate field, bearing field, and distance field of a table.
    """

    @property
    def description(self) -> str:
        return """

        BearingDistanceToLine_management(in_table, out_featureclass, x_field, y_field, distance_field, distance_units, bearing_field, bearing_units, {line_type}, {id_field}, {spatial_reference}, {attributes})

        Creates a feature class containing geodetic or planar line features
        from the values in an x-coordinate field, y-coordinate field, bearing
        field, and distance field of a table.

     INPUTS:
      in_table (Table View):
          The input table. It can be a text file, CSV file, Excel file, dBASE
          table, or geodatabase table.
      x_field (Field):
          A numerical field in the input table containing the x-coordinates (or
          longitudes) of the starting points of lines to be positioned in the
          output coordinate system specified by the spatial_reference parameter.
      y_field (Field):
          A numerical field in the input table containing the y-coordinates (or
          latitudes) of the starting points of lines to be positioned in the
          output coordinate system specified by the spatial_reference parameter.
      distance_field (Field):
          A numerical field in the input table containing the distances from the
          starting points for creating the output lines.
      distance_units (String):
          Specifies the units that will be used for the distance_field
          parameter.METERS-The units will be meters.KILOMETERS-The units will be
          kilometers.MILES-The units will be miles.NAUTICAL_MILES-The units will
          be nautical miles.FEET-The units will be feet.US_SURVEY_FEET-The units
          will be U.S. survey feet.
      bearing_field (Field):
          A numerical field in the input table containing bearing angle values
          for the output line rotation. The angles are measured clockwise from
          north.
      bearing_units (String):
          Specifies the units of the bearing_field parameter values.DEGREES-The
          units will be decimal degrees. This is the
          default.MILS-The units will be mils.RADS-The units will be
          radians.GRADS-The units will be gradians.
      line_type {String}:
          Specifies the type of line that will be constructed.GEODESIC-A type
          of geodetic line that most accurately represents the
          shortest distance between any two points on the surface of the earth
          will be constructed. This is the default. GREAT_CIRCLE-A type
          of geodetic line that represents the path
          between any two points along the intersection of the surface of the
          earth and a plane that passes through the center of the earth will be
          constructed. If theparameter value is a spheroid-based coordinate
          system, the line is a great elliptic. If theparameter value is a
          sphere-based coordinate system, the line is uniquely called a great
          circle-a circle of the largest radius on the spherical surface.
          Spatial ReferenceSpatial ReferenceRHUMB_LINE-A type of geodetic line,
          also known as a loxodrome line,
          that represents a path between any two points on the surface of a
          spheroid defined by a constant azimuth from a pole will be
          constructed. A rhumb line is shown as a straight line in the Mercator
          projection.NORMAL_SECTION-A type of geodetic line that represents a
          path between
          any two points on the surface of a spheroid defined by the
          intersection of the spheroid surface and a plane that passes through
          the two points and is normal (perpendicular) to the spheroid surface
          at the starting point of the two points will be constructed. The
          normal section line from point A to point B is different from the line
          from point B to point A.PLANAR-A straight line in the projected plane
          will be used. A planar
          line usually does not accurately represent the shortest distance on
          the surface of the earth as a geodesic line does. This option is not
          available for geographic coordinate systems.
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

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class containing geodetic or planar lines.

        """