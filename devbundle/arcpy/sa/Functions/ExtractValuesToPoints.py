# Generated documentation for module arcpy.sa.Functions


class ExtractValuesToPoints(object):
    """
    Extracts the cell values of a raster based on a set of point features and records the values in the attribute table of an output feature class.
    """

    @property
    def description(self) -> str:
        return """

        ExtractValuesToPoints_sa(in_point_features, in_raster, out_point_features, {interpolate_values}, {add_attributes})

        Extracts the cell values of a raster based on a set of point features
        and records the values in the attribute table of an output feature
        class.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features defining the locations from which you want to
          extract the raster cell values.
      in_raster (Composite Geodataset):
          The raster dataset whose values will be extracted.It can be an integer
          or floating-point type raster.
      interpolate_values {Boolean}:
          Specifies whether interpolation will be used.NONE-No interpolation
          will be applied; the value of the cell center
          will be used. This is the default.INTERPOLATE-The value of the cell
          will be calculated from the adjacent
          cells with valid values using bilinear interpolation. NoData values
          will be ignored in the interpolation unless all adjacent cells are
          NoData.
      add_attributes {Boolean}:
          Determines if the raster attributes are written to the output point
          feature dataset.VALUE_ONLY-Only the value of the input raster is added
          to the point
          attributes. This is the default. ALL-All the fields from the
          input raster (except) will be
          added to the point attributes. Count

     OUTPUTS:
      out_point_features (Feature Class):
          The output point feature dataset containing the extracted raster
          values.

        """