# Generated documentation for module arcpy.management


class GenerateTessellation(object):
    """
    Generates a tessellated grid of regular polygon features to cover a given extent. The tessellation can be of triangles, squares, diamonds, hexagons, H3 hexagons, or transverse hexagons.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTessellation_management(Output_Feature_Class, Extent, {Shape_Type}, {Size}, {Spatial_Reference}, {H3_Resolution})

        Generates a tessellated grid of regular polygon features to cover a
        given extent. The tessellation can be of triangles, squares, diamonds,
        hexagons, H3 hexagons, or transverse hexagons.

     INPUTS:
      Extent (Extent):
          The extent that the tessellation will cover. This can be the currently
          visible area, the extent of a dataset, or manually entered
          values.MAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      Shape_Type {String}:
          Specifies the shape that will be generated.HEXAGON-Hexagon-shaped
          features will be generated. The top and bottom
          side of each hexagon will be parallel with the x-axis of the
          coordinate system (the top and bottom are
          flat).TRANSVERSE_HEXAGON-Transverse hexagon-shaped features will be
          generated. The right and left side of each hexagon will be parallel
          with the y-axis of the dataset's coordinate system (the top and bottom
          are pointed).SQUARE-Square-shaped features will be generated. The top
          and bottom
          side of each square will be parallel with the x-axis of the coordinate
          system, and the right and left sides will be parallel with the y-axis
          of the coordinate system.DIAMOND-Diamond-shaped features will be
          generated. The sides of each
          polygon will be rotated 45 degrees away from the x-axis and y-axis of
          the coordinate system.TRIANGLE-Triangular-shaped features will be
          generated. Each triangle
          will be a regular three-sided equilateral polygon.H3_HEXAGON-Hexagon-
          shaped features will be generated based on the H3
          Hexagonal hierarchical geospatial indexing system.
      Size {Areal Unit}:
          The area of each individual shape that comprises the tessellation.
      Spatial_Reference {Spatial Reference}:
          The spatial reference to which the output dataset will be projected.
          If a spatial reference is not provided, the output will be projected
          to the spatial reference of the input extent. If neither has a spatial
          reference, the output will be projected in GCS_WGS_1984.
      H3_Resolution {Long}:
          Specifies the H3 resolution of the hexagons.With each increasing
          resolution value, the area of the polygons will
          be one seventh the size.0-Hexagons will be created at the H3
          resolution of 0, with an average
          area of 4,357,449.416078381 square kilometers.1-Hexagons will be
          created at the H3 resolution of 1, with an average
          area of 609,788.441794133 square kilometers.2-Hexagons will be created
          at the H3 resolution of 2, with an average
          area of 86,801.780398997 square kilometers.3-Hexagons will be created
          at the H3 resolution of 3, with an average
          area of 12,393.434655088 square kilometers.4-Hexagons will be created
          at the H3 resolution of 4, with an average
          area of 1,770.347654491 square kilometers.5-Hexagons will be created
          at the H3 resolution of 5, with an average
          area of 252.903858182 square kilometers.6-Hexagons will be created at
          the H3 resolution of 6, with an average
          area of 36.129062164 square kilometers.7-Hexagons will be created at
          the H3 resolution of 7, with an average
          area of 5.161293360 square kilometers. This is the default.8-Hexagons
          will be created at the H3 resolution of 8, with an average
          area of 0.737327598 square kilometers.9-Hexagons will be created at
          the H3 resolution of 9, with an average
          area of 0.105332513 square kilometers.10-Hexagons will be created at
          the H3 resolution of 10, with an
          average area of 0.015047502 square kilometers.11-Hexagons will be
          created at the H3 resolution of 11, with an
          average area of 0.002149643 square kilometers.12-Hexagons will be
          created at the H3 resolution of 12, with an
          average area of 0.000307092 square kilometers.13-Hexagons will be
          created at the H3 resolution of 13, with an
          average area of 0.000043870 square kilometers.14-Hexagons will be
          created at the H3 resolution of 14, with an
          average area of 0.000006267 square kilometers.15-Hexagons will be
          created at the H3 resolution of 15, with an
          average area of 0.000000895 square kilometers.This parameter is
          enabled when the Shape_Type parameter is set to
          H3_HEXAGON.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The path and name of the output feature class containing the
          tessellated grid.

        """