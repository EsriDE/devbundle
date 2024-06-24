# Generated documentation for module arcpy.sa.Functions


class ExtractByPoints(object):
    """
    Extracts the cells of a raster based on a set of coordinate points.
    """

    @property
    def description(self) -> str:
        return """

        ExtractByPoints_sa(in_raster, points;points..., {extraction_area})

        Extracts the cells of a raster based on a set of coordinate points.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster from which cells will be extracted.
      points (Point):
          A Python list of Point class objects denote the locations where values
          will be extracted from the raster.The point objects are specified in a
          list of x,y coordinate pairs in
          the same map units as the input raster.The form of the object is:
          [point(x,y), point(x,y),...]         1122
      extraction_area {String}:
          Identifies whether to extract cells based on the specified point
          locations (inside) or outside the point locations (outside)
          .INSIDE-The cell in which the selected point falls will be written to
          the output raster. All cells outside the box will receive NoData on
          the output raster.OUTSIDE-The cells outside the input points should be
          selected and
          written to the output raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster containing the cell values extracted from the input
          raster.

        """