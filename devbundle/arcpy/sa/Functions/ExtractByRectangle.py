# Generated documentation for module arcpy.sa.Functions


class ExtractByRectangle(object):
    """
    Extracts the cells of a raster based on a rectangle by specifying the rectangle's extent.
    """

    @property
    def description(self) -> str:
        return """

        ExtractByRectangle_sa(in_raster, extent, {extraction_area})

        Extracts the cells of a raster based on a rectangle by specifying the
        rectangle's extent.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster from which cells will be extracted.
      extent (Extent):
          A rectangle that defines the area to be extracted.MAXOF-The maximum
          extent of all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.The coordinates are specified in the same map
          units as the input
          raster.
      extraction_area {String}:
          Specifies whether cells inside or outside the input rectangle will be
          selected and written to the output raster.INSIDE-Cells inside the
          input rectangle will be selected and written
          to the output raster. All cells outside the rectangle will receive
          NoData values on the output raster.OUTSIDE-Cells outside the input
          rectangle will be selected and written
          to the output raster. All cells inside the rectangle will receive
          NoData values on the output raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster containing the cell values extracted from the input
          raster.

        """