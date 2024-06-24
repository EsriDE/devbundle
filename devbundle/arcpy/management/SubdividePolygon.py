# Generated documentation for module arcpy.management


class SubdividePolygon(object):
    """
    Divides polygon features into a number of equal areas or parts.
    """

    @property
    def description(self) -> str:
        return """

        SubdividePolygon_management(in_polygons, out_feature_class, method, {num_areas}, {target_area}, {target_width}, {split_angle}, {subdivision_type})

        Divides polygon features into a number of equal areas or parts.

     INPUTS:
      in_polygons (Feature Layer):
          The polygon features to be subdivided.
      method (String):
          Specifies the method that will be used to divide the
          polygons.NUMBER_OF_EQUAL_PARTS-Polygons will be divided evenly into a
          number
          of parts. This is the default.EQUAL_AREAS-Polygons will be divided
          into a specified number of parts
          of a certain area, and a remainder part.
      num_areas {Long}:
          The number of areas into which the polygon will be divided if the
          NUMBER_OF_EQUAL_PARTS subdivision method is specified.
      target_area {Areal Unit}:
          The area of the equal parts if the EQUAL_AREAS subdivision method is
          specified. If the target_area is larger than the area of the input
          polygon, the polygon will not be subdivided.
      target_width {Linear Unit}:
          This parameter is not yet supported.
      split_angle {Double}:
          The angle that will be used to draw the lines that divide the polygon.
          The default is 0.
      subdivision_type {String}:
          Specifies how the polygons will be divided.STRIPS-Polygons will be
          divided into strips. This is the
          default.STACKED_BLOCKS-Polygons will be divided into stacked blocks.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class of subdivided polygons.

        """