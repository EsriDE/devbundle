# Generated documentation for module arcpy.sa.Functions


class ExtractMultiValuesToPoints(object):
    """
    Extracts cell values at locations specified in a point feature class from one or more rasters and records the values to the attribute table of the point feature class.
    """

    @property
    def description(self) -> str:
        return """

        ExtractMultiValuesToPoints_sa(in_point_features, in_rasters, {bilinear_interpolate_values})

        Extracts cell values at locations specified in a point feature class
        from one or more rasters and records the values to the attribute table
        of the point feature class.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features to which raster values will be added.
      in_rasters (Extract Values):
          The input raster (or rasters) values that will be extracted based on
          the input point feature location.Optionally, you can supply the name
          for the field to store the raster
          value. By default, a unique field name will be created based on the
          input raster dataset name.
      bilinear_interpolate_values {Boolean}:
          Specifies whether interpolation will be used.NONE-No interpolation
          will be applied; the value of the cell center
          will be used. This is the default.BILINEAR-The value of the cell will
          be calculated from the adjacent
          cells with valid values using bilinear interpolation. NoData values
          will be ignored in the interpolation unless all adjacent cells are
          NoData.

        """