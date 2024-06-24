# Generated documentation for module arcpy.management


class XYToLine(object):
    """
    Creates a feature class containing geodetic or planar line features from the values in a start x-coordinate field, start y-coordinate field, end x-coordinate field, and end y-coordinate field of a table.
    """

    @property
    def description(self) -> str:
        return """

        XYToLine_management(in_table, out_featureclass, startx_field, starty_field, endx_field, endy_field, {line_type}, {id_field}, {spatial_reference}, {attributes})

        Creates a feature class containing geodetic or planar line features
        from the values in a start x-coordinate field, start y-coordinate
        field, end x-coordinate field, and end y-coordinate field of a table.

     INPUTS:
      in_table (Table View):
          The input table. It can be a text file, CSV file, Excel file, dBASE
          table, or geodatabase table.
      startx_field (Field):
          A numerical field in the input table containing the x-coordinates (or
          longitudes) of the starting points of lines to be positioned in the
          output coordinate system specified by the spatial_reference parameter.
      starty_field (Field):
          A numerical field in the input table containing the y-coordinates (or
          latitudes) of the starting points of lines to be positioned in the
          output coordinate system specified by the spatial_reference parameter.
      endx_field (Field):
          A numerical field in the input table containing the x-coordinates (or
          longitudes) of the ending points of lines to be positioned in the
          output coordinate system specified by the spatial_reference parameter.
      endy_field (Field):
          A numerical field in the input table containing the y-coordinates (or
          latitudes) of the ending points of lines to be positioned in the
          output coordinate system specified by the spatial_reference parameter.
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