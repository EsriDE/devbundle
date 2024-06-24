# Generated documentation for module arcpy.conversion


class MultipatchToRaster(object):
    """
    Converts multipatch features to a raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        MultipatchToRaster_conversion(in_multipatch_features, out_raster, {cell_size}, {cell_assignment_method})

        Converts multipatch features to a raster dataset.

     INPUTS:
      in_multipatch_features (Composite Geodataset):
          The input multipatch features to be converted to a raster.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster being created.This parameter can be
          defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value is
          used, if specified; otherwise, additional rules are used to calculate
          it from the other inputs. See Usages for more detail.
      cell_assignment_method {String}:
          Specifies whether the maximum or minimum z-value will be used for a
          cell when more than one z-value is detected at the cell center
          location when a vertical line is extended from the cell center
          location to intersect the input multipatch feature.MAXIMUM_HEIGHT-The
          maximum z-value will be assigned to the cell. This
          is the default.MINIMUM_HEIGHT-The minimum z-value will be assigned to
          the cell.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset to be created.It will be of floating point
          type.If the output raster will not be saved to a geodatabase, specify
          .tif
          for TIFF file format, .CRF for CRF file format, .img for ERDAS IMAGINE
          file format, or no extension for Esri Grid raster format.

        """