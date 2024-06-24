# Generated documentation for module arcpy.conversion


class RasterToPolyline(object):
    """
    Converts a raster dataset to polyline features.
    """

    @property
    def description(self) -> str:
        return """

        RasterToPolyline_conversion(in_raster, out_polyline_features, {background_value}, {minimum_dangle_length}, {simplify}, {raster_field})

        Converts a raster dataset to polyline features.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster must be integer type.
      background_value {String}:
          Specifies the value that will identify the background cells. The
          raster dataset is viewed as a set of foreground cells and background
          cells. The linear features are formed from the foreground
          cells.ZERO-The background is composed of cells of zero or less or
          NoData.
          All cells with a value greater than zero are considered a foreground
          value.NODATA-The background is composed of NoData cells. All cells
          with
          valid values belong to the foreground.
      minimum_dangle_length {Double}:
          Minimum length of dangling polylines that will be retained. The
          default is zero.
      simplify {Boolean}:
          Simplifies a line by removing small fluctuations or extraneous bends
          from it while preserving its essential shape.SIMPLIFY-The polylines
          will be simplified into simpler shapes such
          that each contains a minimum number of segments. This is the
          default.NO_SIMPLIFY-The polylines will not be simplified.
      raster_field {Field}:
          The field used to assign values from the cells in the input raster to
          the polyline features in the output dataset.It can be an integer or a
          string field.

     OUTPUTS:
      out_polyline_features (Feature Class):
          The output feature class that will contain the converted polylines.

        """