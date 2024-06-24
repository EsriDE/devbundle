# Generated documentation for module arcpy.conversion


class PolygonToRaster(object):
    """
    Converts polygon features to a raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        PolygonToRaster_conversion(in_features, value_field, out_rasterdataset, {cell_assignment}, {priority_field}, {cellsize}, {build_rat})

        Converts polygon features to a raster dataset.

     INPUTS:
      in_features (Feature Layer):
          The polygon input feature dataset to be converted to a raster.
      value_field (Field):
          The field used to assign values to the output raster.It can be any
          field of the input feature dataset's attribute table.
      cell_assignment {String}:
          The method to determine how the cell will be assigned a value when
          more than one feature falls within a cell.CELL_CENTER-The polygon that
          overlaps the center of the cell yields
          the attribute to assign to the cell.MAXIMUM_AREA-The single feature
          with the largest area within the cell
          yields the attribute to assign to the cell.MAXIMUM_COMBINED_AREA-If
          there is more than one feature in a cell with
          the same value, the areas of these features will be combined. The
          combined feature with the largest area within the cell will determine
          the value to assign to the cell.
      priority_field {Field}:
          This field is used to determine which feature should take
          preference over another feature that falls over a cell. When it is
          used, the feature with the largest positive priority is always
          selected for conversion irrespective of thechosen. Cell
          assignment type
      cellsize {Analysis Cell Size}:
          The cell size of the output raster being created.This parameter can be
          defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value is
          used, if specified; otherwise, additional rules are used to calculate
          it from the other inputs. See Usages for more detail.
      build_rat {Boolean}:
          Specifies whether the output raster will have a raster attribute
          table.This parameter only applies to integer rasters.BUILD-The output
          raster will have a raster attribute table. This is
          the default.DO_NOT_BUILD-The output raster will not have a raster
          attribute table.

     OUTPUTS:
      out_rasterdataset (Raster Dataset):
          The output raster dataset to be created.If the output raster will not
          be saved to a geodatabase, specify .tif
          for TIFF file format, .CRF for CRF file format, .img for ERDAS IMAGINE
          file format, or no extension for Esri Grid raster format.

        """