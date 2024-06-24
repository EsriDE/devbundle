# Generated documentation for module arcpy.management


class GenerateExcludeArea(object):
    """
    Masks pixels based on their color or by clipping a range of values. The output of this tool is used as an input to the Color Balance Mosaic Dataset tool to eliminate areas such as clouds and water that can skew the statistics used to color balance multiple images.
    """

    @property
    def description(self) -> str:
        return """

        GenerateExcludeArea_management(in_raster, out_raster, pixel_type, generate_method, {max_red}, {max_green}, {max_blue}, {max_white}, {max_black}, {max_magenta}, {max_cyan}, {max_yellow}, {percentage_low}, {percentage_high})

        Masks pixels based on their color or by clipping a range of values.
        The output of this tool is used as an input to the Color Balance
        Mosaic Dataset tool to eliminate areas such as clouds and water that
        can skew the statistics used to color balance multiple images.

     INPUTS:
      in_raster (Mosaic Dataset / Raster Dataset / Raster Layer):
          The raster or mosaic dataset layer that you want to mask.
      pixel_type (String):
          Choose the pixel depth of your input raster dataset. 8-bit is the
          default value; however, raster datasets with a greater bit-depth will
          need to have the color mask and histogram values scaled
          accordingly.8_BIT-The input raster dataset has values from 0 to 255.
          This is the
          default.11_BIT-The input raster dataset has values from 0 to
          2047.12_BIT-The input raster dataset has values from 0 to
          4095.16_BIT-The input raster dataset has values from 0 to 65535.
      generate_method (String):
          Create your mask based on the color of the pixels or by clipping high
          and low values.COLOR_MASK-Set the maximum color values to include in
          the output. This
          is the default.HISTOGRAM_PERCENTAGE-Remove a percentage of high and
          low pixel values.
      max_red {Double}:
          The maximum red value to exclude. The default is 255.
      max_green {Double}:
          The maximum green value to exclude. The default is 255.
      max_blue {Double}:
          The maximum blue value to exclude. The default is 255.
      max_white {Double}:
          The maximum white value to exclude. The default is 255.
      max_black {Double}:
          The maximum black value to exclude. The default is 0.
      max_magenta {Double}:
          The maximum magenta value to exclude. The default is 255.
      max_cyan {Double}:
          The maximum cyan value to exclude. The default is 255.
      max_yellow {Double}:
          The maximum yellow value to exclude. The default is 255.
      percentage_low {Double}:
          Exclude this percentage of the lowest pixel values. The default is 0.
      percentage_high {Double}:
          Exclude this percentage of the highest pixel values. The default is
          100.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location and format for the dataset you are
          creating. When storing a raster dataset in a geodatabase, do not add a
          file extension to the name of the raster dataset. When storing your
          raster dataset to a JPEG file, a JPEG 2000 file, or a geodatabase, you
          can specify atype andwithin the Environment Settings.
          CompressionCompression Quality

        """