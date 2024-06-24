# Generated documentation for module arcpy.conversion


class FeatureToRaster(object):
    """
    Converts features to a raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        FeatureToRaster_conversion(in_features, field, out_raster, {cell_size})

        Converts features to a raster dataset.

     INPUTS:
      in_features (Composite Geodataset):
          The input feature dataset to be converted to a raster dataset.
      field (Field):
          The field used to assign values to the output raster.It can be any
          field of the input feature dataset's attribute table. If
          thefield of a point or multipoint dataset contains z- or
          m-values, either of these can be used. Shape
      cell_size {Analysis Cell Size}:
          The cell size of the output raster being created.This parameter can be
          defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value is
          used, if specified; otherwise, additional rules are used to calculate
          it from the other inputs. See Usages for more detail.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset to be created.If the output raster will not
          be saved to a geodatabase, specify .tif
          for TIFF file format, .CRF for CRF file format, .img for ERDAS IMAGINE
          file format, or no extension for Esri Grid raster format.

        """