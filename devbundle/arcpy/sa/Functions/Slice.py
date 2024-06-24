# Generated documentation for module arcpy.sa.Functions


class Slice(object):
    """
    Slices or reclassifies the range of values of the input cells into zones (classes). The available data classification methods are equal interval, equal area (quantile), natural breaks, standard deviation (mean-centered), standard deviation (mean as a break), defined interval, and geometric interval.
    """

    @property
    def description(self) -> str:
        return """

        Slice_sa(in_raster, {number_zones}, {slice_type}, {base_output_zone}, {nodata_to_value}, {class_interval_size})

        Slices or reclassifies the range of values of the input cells into
        zones (classes). The available data classification methods are equal
        interval, equal area (quantile), natural breaks, standard deviation
        (mean-centered), standard deviation (mean as a break), defined
        interval, and geometric interval.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be reclassified.
      number_zones {Long}:
          The number of zones that the input raster will be reclassified
          into.This parameter is required when the slice_type parameter value is
          EQUAL_AREA, EQUAL_INTERVAL, NATURAL_BREAKS, or GEOMETRIC_INTERVAL.When
          the slice_type parameter value is
          STANDARD_DEVIATION_MEAN_CENTERED, STANDARD_DEVIATION_MEAN_BREAK, or
          DEFINED_INTERVAL, the number_zones parameter is not supported. The
          number of output zones will be determined by the class_interval_size
          parameter value.
      slice_type {String}:
          Specifies the manner in which the input raster will be reclassified
          into zones.EQUAL_INTERVAL-The range of input values will be equally
          divided into
          the specified number of output zones to determine the class breaks.
          This is the default.EQUAL_AREA-The number of input cells will be
          equally divided into the
          specified number of output zones to determine the class breaks. Each
          zone will have a similar number of cells, indicating a similar amount
          of area.NATURAL_BREAKS-The class breaks will be determined in a way
          that
          minimizes the variance within classes and maximizes the variance
          between classes. The breaks are usually set at relatively big changes
          in the data values.STANDARD_DEVIATION_MEAN_CENTERED-The class breaks
          will be placed above
          and below the mean value at a specified interval size, such as 2, 1,
          or 0.5, in the unit of standard deviation, until reaching the minimum
          and maximum values of the input raster. Mean is not used as a break
          but centered by two class breaks. One break is at half of the
          specified interval size above the mean and the other is at half of the
          specified interval size below the mean. Standard deviation is
          calculated with the n-1 denominator, where n is the number of pixels
          with value.STANDARD_DEVIATION_MEAN_BREAK-The mean value will be used
          as a class
          break. Other class breaks will be placed above and below the mean
          value at a specified interval size, such as 2, 1, or 0.5, in the unit
          of standard deviation, until reaching the minimum and maximum values
          of the input raster. Standard deviation is calculated with the n-1
          denominator, where n is the number of pixels with
          value.DEFINED_INTERVAL-The class breaks will be set to zero and a
          multiple
          of the specified interval size relative to zero. They will then be
          clipped to the minimum and maximum values of the input data for the
          first and last classes. For a value range that contains zero, zero
          will always be included as a break point.GEOMETRIC_INTERVAL-The class
          breaks will be created based on class
          intervals that have a geometric series. This is a pattern in which the
          current value equals the previous value divided by a geometric
          coefficient. The geometric coefficient in this classifier can change
          once (to its inverse) to optimize the class ranges. The algorithm
          creates these geometrical intervals by minimizing the sum of squares
          of the number of elements in each class. This ensures that each class
          has approximately the same number of values and that the change
          between intervals is consistent.
      base_output_zone {Long}:
          The starting value that will be used for zones (classes) on the output
          raster dataset.Classes will be assigned integer values, increasing by
          1 from the
          starting value.The default starting value is 1.
      nodata_to_value {Long}:
          Replace NoData with a value in the output.If this parameter is not
          set, NoData cells will remain as NoData in
          the output raster.
      class_interval_size {Double}:
          The size of the interval between classes.This parameter is required
          when the slice_type parameter is set to
          DEFINED_INTERVAL, STANDARD_DEVIATION_MEAN_CENTERED, or
          STANDARD_DEVIATION_MEAN_BREAK.If DEFINED_INTERVAL is used, the
          interval size indicates the actual
          value range of a class used to calculate class breaks.If
          STANDARD_DEVIATION_MEAN_CENTERED or STANDARD_DEVIATION_MEAN_BREAK
          is used, the interval size indicates the number of standard deviations
          used to calculate class breaks.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output reclassified raster.The output will always be of integer
          type. The attribute table of the output raster will have two
          new
          fields in addition to the standard,, andfields. Thefield indicates the
          class value. Theandfields record the minimum and maximum values,
          respectively, used for generating a class.
          ObjectIDValueCountValueZoneMinZoneMax

        """