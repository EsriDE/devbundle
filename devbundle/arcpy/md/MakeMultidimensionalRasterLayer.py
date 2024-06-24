# Generated documentation for module arcpy.md


class MakeMultidimensionalRasterLayer(object):
    """
    Creates a raster layer from a multidimensional raster dataset or a multidimensional raster layer by slicing data along defined variables and dimensions.
    """

    @property
    def description(self) -> str:
        return """

        MakeMultidimensionalRasterLayer_md(in_multidimensional_raster, out_multidimensional_raster_layer, {variables;variables...}, {dimension_def}, {dimension_ranges;dimension_ranges...}, {dimension_values;dimension_values...}, {dimension}, {start_of_first_iteration}, {end_of_first_iteration}, {iteration_step}, {iteration_unit}, {template}, {dimensionless}, {spatial_reference})

        Creates a raster layer from a multidimensional raster dataset or a
        multidimensional raster layer by slicing data along defined variables
        and dimensions.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional raster dataset. Supported inputs are
          netCDF, GRIB, HDF, CRF, and Zarr files, a
          multidimensional mosaic dataset, a multidimensional image service, an
          OPeNDAP URL, or a multidimensional raster layer. A Zarr file
          must have an extension of .zarr and a .zgroup file in the
          folder.
      variables {String}:
          The variables that will be included in the output multidimensional
          raster layer. If no variable is specified, the first variable will be
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
      template {Extent}:
          The extent (bounding box) of the layer. Choose the
          appropriateoption for the layer. ExtentMAXOF-The maximum extent
          of all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      dimensionless {Boolean}:
          Specifies whether the layer will have dimension values. This parameter
          is only enabled if a single slice is selected to create a
          layer.NO_DIMENSIONS-The layer will not have dimension
          values.DIMENSIONS-The
          layer will have dimension values. This is the default.
      spatial_reference {Coordinate System}:
          The coordinate system for the out_multidimensional_raster_layer
          parameter value. This parameter only applies when the
          in_multidimensional_raster parameter value is in Zarr format. Use this
          parameter to define the spatial reference if it is missing in the
          data.

     OUTPUTS:
      out_multidimensional_raster_layer (Raster Layer):
          The output multidimensional raster layer.

        """