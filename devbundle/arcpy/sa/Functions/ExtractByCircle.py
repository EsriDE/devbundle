# Generated documentation for module arcpy.sa.Functions


class ExtractByCircle(object):
    """
    Extracts the cells of a raster based on a circle by specifying the circle's center and radius.
    """

    @property
    def description(self) -> str:
        return """

        ExtractByCircle_sa(in_raster, center_point, radius, {extraction_area})

        Extracts the cells of a raster based on a circle by specifying the
        circle's center and radius.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster from which cells will be extracted.
      center_point (Point):
          The Point class determines the center coordinate (x,y) of the circle
          defining the area to be extracted. The form of the class is the
          following:        Point (x, y)The coordinates are specified in the
          same map units as the input
          raster.
      radius (Double):
          The radius of the circle defining the area to be extracted.The radius
          is specified in map units and is in the same units as the
          input raster.
      extraction_area {String}:
          Specifies whether cells inside or outside the input circle will be
          selected and written to the output raster.INSIDE-Cells inside the
          input circle will be selected and written to
          the output raster. All cells outside the circle will receive NoData
          values on the output raster.OUTSIDE-Cells outside the input circle
          will be selected and written to
          the output raster. All cells inside the circle will receive NoData
          values on the output raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster containing the cell values extracted from the input
          raster.

        """