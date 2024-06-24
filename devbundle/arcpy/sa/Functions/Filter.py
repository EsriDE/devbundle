# Generated documentation for module arcpy.sa.Functions


class Filter(object):
    """
    Performs either a smoothing (Low pass) or edge-enhancing (High pass) filter on a raster.
    """

    @property
    def description(self) -> str:
        return """

        Filter_sa(in_raster, {filter_type}, {ignore_nodata})

        Performs either a smoothing (Low pass) or edge-enhancing (High pass)
        filter on a raster.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster on which to perform the filter operation.
      filter_type {String}:
          The type of filter operation to perform.LOW-Traverses a low pass
          3-by-3 filter over the raster. This option
          smooths the entire input raster and reduces the significance of
          anomalous cells. This is the default.HIGH-Traverses a high pass 3-by-3
          filter over the raster. This option
          enhances the edges of subdued features in a raster.
      ignore_nodata {Boolean}:
          Denotes whether NoData values are ignored by the filter
          calculation.DATA-If a NoData value exists within the filter, the
          NoData value will
          be ignored. Only cells within the filter that have data values will be
          used in determining the output. This is the default.NODATA-If a NoData
          value exists within the filter, the output for the
          processing cell will be NoData. With this option, the presence of a
          NoData value implies that there is insufficient information to
          determine the statistic value for the neighborhood.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output filtered raster.The output is always floating point.

        """