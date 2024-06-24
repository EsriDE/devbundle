# Generated documentation for module arcpy.md


class SubsetMultidimensionalRaster(object):
    """
    Creates a subset of a multidimensional raster by slicing data along defined variables and dimensions.
    """

    @property
    def description(self) -> str:
        return """

        SubsetMultidimensionalRaster_md(in_multidimensional_raster, out_multidimensional_raster, {variables;variables...}, {dimension_def}, {dimension_ranges;dimension_ranges...}, {dimension_values;dimension_values...}, {dimension}, {start_of_first_iteration}, {end_of_first_iteration}, {iteration_step}, {iteration_unit})

        Creates a subset of a multidimensional raster by slicing data along
        defined variables and dimensions.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional raster dataset.Supported inputs include
          netCDF, GRIB, HDF or CRF files, a
          multidimensional mosaic dataset, or a multidimensional raster layer.
      variables {String}:
          The variables that will be included in the output multidimensional
          raster. If no variable is specified, all of the variables will be
          used.
      dimension_def {String}:
          Specifies the method that will be used to slice the dimension.ALL-The
          full range for each dimension will be used. This is the
          default.BY_RANGES-The dimension will be sliced using a range or a list
          of
          ranges.BY_ITERATION-The dimension will be sliced over a specified
          interval
          size.BY_VALUE-The dimension will be sliced using a list of dimension
          values.
      dimension_ranges {Value Table}:
          The range or list of ranges for the specified dimension.The data will
          be sliced based on the dimension name and the minimum
          and maximum values for the range. This parameter is required when the
          dimension_def parameter is set to BY_RANGES.
      dimension_values {Value Table}:
          A list of values for the specified dimension. This parameter is
          required when the dimension_def parameter is set to BY_VALUE.
      dimension {String}:
          The dimension along which the variables will be sliced. This parameter
          is required when the dimension_def parameter is set to BY_ITERATION.
      start_of_first_iteration {String}:
          The beginning of the first interval. This interval will be used to
          iterate through the dataset. This parameter is required when the
          dimension_def parameter is set to BY_ITERATION.
      end_of_first_iteration {String}:
          The end of the first interval. This interval will be used to iterate
          through the dataset. This parameter is required when the dimension_def
          parameter is set to BY_ITERATION.
      iteration_step {Double}:
          The frequency with which the data will be sliced. This parameter is
          required when the dimension_def parameter is set to BY_ITERATION.
      iteration_unit {String}:
          Specifies the iteration unit that will be used. This parameter is
          required when the dimension_def parameter is set to BY_ITERATION and
          the dimension parameter is set to StdTime.HOURS-The specified unit of
          time will be hours.DAYS-The specified unit
          of time will be days.WEEKS-The specified unit of time will be
          weeks.MONTHS-The specified unit of time will be months.YEARS-The
          specified unit of time will be years.

     OUTPUTS:
      out_multidimensional_raster (Raster Dataset):
          The output multidimensional raster dataset.

        """