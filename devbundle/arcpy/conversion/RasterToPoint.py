# Generated documentation for module arcpy.conversion


class RasterToPoint(object):
    """
    Converts a raster dataset to point features.
    """

    @property
    def description(self) -> str:
        return """

        RasterToPoint_conversion(in_raster, out_point_features, {raster_field})

        Converts a raster dataset to point features.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster can be integer or floating-point
          type.
      raster_field {Field}:
          The field to assign values from the cells in the input raster to the
          points in the output dataset.It can be an integer, floating point, or
          string field.

     OUTPUTS:
      out_point_features (Feature Class):
          The output feature class that will contain the converted points.

        """