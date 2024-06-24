# Generated documentation for module arcpy.management


class Mosaic(object):
    """
    Merges multiple existing raster datasets or mosaic datasets into an existing raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        Mosaic_management(inputs;inputs..., target, {mosaic_type}, {colormap}, {background_value}, {nodata_value}, {onebit_to_eightbit}, {mosaicking_tolerance}, {MatchingMethod})

        Merges multiple existing raster datasets or mosaic datasets into an
        existing raster dataset.

     INPUTS:
      inputs (Mosaic Dataset / Raster Dataset / Raster Layer):
          The raster datasets to be merged.
      target (Raster Dataset):
          The raster to which the input rasters will be added. This must be an
          existing raster dataset. By default, the target raster is considered
          the first raster in the list of input raster datasets. You can create
          an empty raster using the Create Raster Dataset tool.
      mosaic_type {String}:
          Specifies the method that will be used to mosaic overlapping
          areas.FIRST-The output cell value of the overlapping areas will be the
          value
          from the first raster dataset mosaicked into that location.LAST-The
          output cell value of the overlapping areas will be the value
          from the last raster dataset mosaicked into that location. This is the
          default.BLEND-The output cell value of the overlapping areas will be a
          horizontally weighted calculation of the values of the cells in the
          overlapping area.MEAN-The output cell value of the overlapping areas
          will be the
          average value of the overlapping cells.MINIMUM-The output cell value
          of the overlapping areas will be the
          minimum value of the overlapping cells.MAXIMUM-The output cell value
          of the overlapping areas will be the
          maximum value of the overlapping cells.SUM-The output cell value of
          the overlapping areas will be the total
          sum of the overlapping cells.
      colormap {String}:
          Specifies the method that will be used to choose which color map from
          the input rasters will be applied to the mosaic output.FIRST-The color
          map from the first raster dataset in the list will be
          applied to the output raster mosaic. This is the default.LAST-The
          color map from the last raster dataset in the list will be
          applied to the output raster mosaic.MATCH-All the color maps will be
          considered when mosaicking. If all
          possible values are already used (for the bit depth), the tool will
          match the value with the closest available color.REJECT-Only the
          raster datasets that do not have a color map
          associated with them will be mosaicked.
      background_value {Double}:
          Remove the unwanted values created around the raster data. The value
          specified will be distinguished from other valuable data in the raster
          dataset. For example, a value of zero along the raster dataset's
          borders will be distinguished from zero values in the raster
          dataset.The pixel value specified will be set to NoData in the output
          raster
          dataset. For file-based rasters and geodatabase rasters,must be
          set to
          the same value as NoData for the background value to be ignored.
          Enterprise geodatabase rasters will work without this extra step.
          Ignore Background Value
      nodata_value {Double}:
          All the pixels with the specified value will be set toin the
          output raster dataset. NoData
      onebit_to_eightbit {Boolean}:
          Specifies whether the input 1-bit raster dataset will be converted to
          an 8-bit raster dataset. In this conversion, the value 1 in the input
          raster dataset will be changed to 255 in the output raster dataset.
          This is useful when importing a 1-bit raster dataset to a geodatabase.
          One-bit raster datasets have 8-bit pyramid layers when stored in a
          file system, but in a geodatabase, 1-bit raster datasets can only have
          1-bit pyramid layers, which results in a lower-quality display. By
          converting the data to 8 bit in a geodatabase, the pyramid layers are
          built as 8 bit instead of 1 bit, resulting in a proper raster dataset
          in the display.NONE-No conversion will occur. This is the
          default.OneBitTo8Bit-The
          input raster will be converted.
      mosaicking_tolerance {Double}:
          When mosaicking occurs, the target and the source pixels do not always
          line up exactly. When there is a misalignment of pixels, you need to
          decide whether to resample or shift the data. The mosaicking tolerance
          controls whether resampling of the pixels will occur or the pixels
          will be shifted.If the difference in pixel alignment (of the incoming
          dataset and the
          target dataset) is greater than the tolerance, resampling will occur.
          If the difference in pixel alignment (of the incoming dataset and the
          target dataset) is less than the tolerance, resampling will not occur
          and a shift will be performed.The unit of tolerance is a pixel with a
          valid value range of 0 to 0.5.
          A tolerance of 0.5 will guarantee a shift occurs. A tolerance of zero
          guarantees resampling will occur if there is a misalignment in
          pixels.For example, the source and target pixels have a misalignment
          of 0.25.
          If the mosaicking tolerance is set to 0.2, resampling will occur since
          the pixel misalignment is greater than the tolerance. If the
          mosaicking tolerance is set to 0.3, the pixels will be shifted.
      MatchingMethod {String}:
          Specifies the color matching method that will be applied to the
          rasters.NONE-No color matching method will be applied when mosaicking
          the
          raster datasets.STATISTIC_MATCHING-Descriptive statistics from the
          overlapping areas
          will be matched; the transformation will then be applied to the entire
          target dataset.HISTOGRAM_MATCHING-The histogram from the reference
          overlap area will
          be matched to the source overlap area; the transformation will then be
          applied to the entire target
          dataset.LINEARCORRELATION_MATCHING-Overlapping pixels will be matched
          and the
          rest of the source dataset will be interpolated; pixels without a one-
          to-one relationship will use a weighted average.

        """