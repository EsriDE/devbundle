# Generated documentation for module arcpy.management


class BuildRasterAttributeTable(object):
    """
    Adds a raster attribute table to a raster dataset or updates an existing one. This is used primarily with discrete data.
    """

    @property
    def description(self) -> str:
        return """

        BuildRasterAttributeTable_management(in_raster, {overwrite}, {convert_colormap})

        Adds a raster attribute table to a raster dataset or updates an
        existing one. This is used primarily with discrete data.

     INPUTS:
      in_raster (Raster Layer):
          The input raster dataset to which a table will be added. This tool
          will not run if the pixel type is floating point or double precision.
      overwrite {Boolean}:
          Specifies whether the existing table will be overwritten.NONE-The
          existing raster attribute table will not be overwritten and
          any edits will be appended to it. This is the default.Overwrite-The
          existing raster attribute table will be overwritten and
          a new raster attribute table will be created.
      convert_colormap {Boolean}:
          Specifies whether the color map will be converted to a raster
          attribute table. The output raster attribute table will include,,
          andfields containing color values from the color map. These fields
          define the display colors for the corresponding class values.
          RedGreenBlue        This parameter only applies when theparameter
          value includes
          an associated color map. Input RasterChecked-The color map will
          be converted to a new raster attribute
          table.Unchecked-The color map will not be converted to a raster
          attribute
          table. This is the default.ConvertColormap-The color map will be
          converted to a new raster
          attribute table.NONE-The color map will not be converted to a raster
          attribute table.
          This is the default.

        """