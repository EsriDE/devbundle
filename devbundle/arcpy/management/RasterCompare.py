# Generated documentation for module arcpy.management


class RasterCompare(object):
    """
    Compares the properties of two raster datasets or two mosaic datasets.
    """

    @property
    def description(self) -> str:
        return """

        RasterCompare_management(in_base_raster, in_test_raster, {compare_type}, {ignore_option;ignore_option...}, {continue_compare}, {out_compare_file}, {parameter_tolerances;parameter_tolerances...}, {attribute_tolerances;attribute_tolerances...}, {omit_field;omit_field...})

        Compares the properties of two raster datasets or two mosaic datasets.

     INPUTS:
      in_base_raster (Raster Layer / Mosaic Layer):
          The first raster or mosaic dataset to compare.
      in_test_raster (Raster Layer / Mosaic Layer):
          The second raster or mosaic dataset to compare with the first.
      compare_type {String}:
          Specifies the type of rasters that will be compared.RASTER_DATASET-Two
          raster datasets will be
          compared.GDB_RASTER_DATASET-Two raster datasets in a geodatabase will
          be
          compared.MOSAIC_DATASET-Two mosaic datasets will be compared.
      ignore_option {String}:
          Specifies the properties that will be ignored in the
          comparison.BandCount-The number of bands will be ignored.Extent-The
          extent will
          be ignored.Columns And Rows-The number of columns and rows will be
          ignored.Pixel Type-The pixel type will be ignored.NoData-The NoData
          value will be ignored.Spatial Reference-The spatial reference system
          will be ignored.Pixel Value-The pixel values will be
          ignored.Colormap-Existing color maps will be ignored.Raster Attribute
          Table-Existing attribute tables will be ignored.Statistics-Statistics
          will be ignored.Metadata-Metadata will be ignored.Pyramids
          Exist-Existing pyramids will be ignored.Compression Type-The
          compression type will be ignored.Data Source Type-The data source type
          will be ignored.
      continue_compare {Boolean}:
          Specifies whether the comparison will stop if a mismatch is
          encountered.NO_CONTINUE_COMPARE-The comparison will stop if a mismatch
          is
          encountered. This is the default.CONTINUE_COMPARE-The comparison will
          continue if a mismatch is
          encountered.
      parameter_tolerances {Value Table}:
          The tolerances that determine the range in which values are considered
          equal. The same tolerance can be applied to all parameters, or
          different tolerances can be applied to individual parameters.The
          tolerance type can be either a value or a fraction. If the
          tolerance type is a fraction, the tolerance for each
          pixel will be different since each pixel has a different value. For
          example, if a tolerance fraction is set to 0.5, the tolerance will be
          calculated as follows:        If a pixel has a value of 0.2, the
          tolerance will be 0.1, since 0.5 *
          0.2 = 0.1.If a pixel has a value of 3, the tolerance will be 1.5,
          since 0.5 * 3
          = 1.5.
      attribute_tolerances {Value Table}:
          The fields that will be compared to determine if they are within a
          tolerance. The tolerance value is a value in the units of the
          attribute.
      omit_field {String}:
          The field or fields that will be omitted during comparison.

     OUTPUTS:
      out_compare_file {File}:
          A text file containing the comparison results.

        """