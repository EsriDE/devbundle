# Generated documentation for module arcpy.sa.Functions


class ExtractByMask(object):
    """
    Extracts the cells of a raster that correspond to the areas defined by a mask.
    """

    @property
    def description(self) -> str:
        return """

        ExtractByMask_sa(in_raster, in_mask_data, {extraction_area}, {analysis_extent})

        Extracts the cells of a raster that correspond to the areas defined by
        a mask.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster from which cells will be extracted.
      in_mask_data (Composite Geodataset):
          The input mask data defining the cell locations to extract.It can be a
          raster or a feature dataset.When the input mask data is a raster,
          NoData cells on the mask will be
          assigned NoData values on the output raster.When the input mask is
          feature data, cells in the input raster whose
          center falls within the specified shape of the feature will be
          included in the output, while cells whose center falls outside will
          receive NoData.
      extraction_area {String}:
          Specifies whether cells inside or outside the locations defined by the
          input mask will be selected and written to the output
          raster.INSIDE-Cells within the input mask will be selected and written
          to the
          output raster. All cells outside the mask will receive NoData on the
          output raster. This is default.OUTSIDE-Cells outside the input mask
          will be selected and written to
          the output raster. All cells covered by the mask will receive NoData.
      analysis_extent {Extent}:
          The extent that defines the area to be extracted.If not specified, the
          default extent is the intersection of the
          in_raster value and the in_mask_data value.The coordinates are
          specified in the same map units as the input
          raster if not explicitly set by the analysis environment.MAXOF-The
          maximum extent of all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster containing the cell values extracted from the input
          raster.

        """