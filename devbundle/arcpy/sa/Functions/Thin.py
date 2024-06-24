# Generated documentation for module arcpy.sa.Functions


class Thin(object):
    """
    Thins rasterized linear features by reducing the number of cells representing the width of the features.
    """

    @property
    def description(self) -> str:
        return """

        Thin_sa(in_raster, {background_value}, {filter}, {corners}, {maximum_thickness})

        Thins rasterized linear features by reducing the number of cells
        representing the width of the features.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be thinned.It must be of integer type.
      background_value {String}:
          Specifies the cell value that will identify the background cells. The
          linear features are formed from the foreground cells.ZERO-The
          background is composed of cells of 0 or less, or NoData. All
          cells whose value is greater than 0 are the foreground.NODATA-The
          background is composed of NoData cells. All cells with
          valid values belong to the foreground.
      filter {Boolean}:
          Specifies whether a filter will be applied as the first phase of
          thinning. NO_FILTER-No filter will be applied. This is
          the
          default.FILTER-The raster will be filtered to smooth the boundaries
          between
          foreground and background cells. This option will eliminate minor
          irregularities from the output raster.
      corners {String}:
          Specifies whether round or sharp turns will be made at turns or
          junctions.It is also used during the vector conversion process to
          spline curves
          or create sharp intersections and corners.ROUND-Attempts to smooth
          corners and junctions. This is best for
          vectorizing natural features, such as contours or
          streams.SHARP-Attempts to preserve rectangular corners and junctions.
          This is
          best for vectorizing man-made features such as streets.
      maximum_thickness {Double}:
          The maximum thickness, in map units, of linear features in the input
          raster.The default thickness is ten times the cell size.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output thinned raster.The output is always of integer type.

        """