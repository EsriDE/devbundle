# Generated documentation for module arcpy.sa.Functions


class LineStatistics(object):
    """
    Calculates a statistic on the attributes of lines in a circular neighborhood around each output cell.
    """

    @property
    def description(self) -> str:
        return """

        LineStatistics_sa(in_polyline_features, field, {cell_size}, {search_radius}, {statistics_type})

        Calculates a statistic on the attributes of lines in a circular
        neighborhood around each output cell.

     INPUTS:
      in_polyline_features (Composite Geodataset):
          The input lines to use in the neighborhood operation.For each output
          cell, a statistic will be calculated for all of the
          portions of the input polyline features that fall within a circular
          neighborhood around that cell.The size the circular neighbourhood is
          defined by the search radius.
      field (Field):
          The field for which the specified statistic will be calculated. It can
          be any numeric field of the input line features.When statistics_type
          is set to Length, the field parameter can be set
          to NONE. It can be thefield if the input features contain
          z-values.
          Shape
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      search_radius {Double}:
          The search radius that will be used to calculate the statistic within,
          in map units.The default radius is five times the output cell size.
      statistics_type {String}:
          Specifies the statistic type to be calculated.Statistics are
          calculated on the value of the specified field for all
          lines within the neighborhood. MEAN-The average field value in
          each neighborhood, weighted
          by the length, will be calculated. The form of the calculation
          is: Mean = (sum of (length * field_value))
          / (sum_of_length).Only the part of the line that falls within the
          neighborhood is used.MAJORITY-The value having the greatest length of
          line in the
          neighborhood will be identified.MAXIMUM-The largest value in the
          neighborhood will be identified. MEDIAN-The median value,
          weighted by the length, will be
          calculated. Conceptually, all line segments in the
          neighborhood are sorted by
          value and placed end to end in a straight line. The value of the
          segment at the midpoint of the straight line is the median.MINIMUM-The
          smallest value in each neighborhood will be identified.MINORITY-The
          value having the least length of line in the neighborhood
          will be identified.RANGE-The range of values (maximum-minimum) will be
          calculated.VARIETY-The number of unique values will be
          calculated.LENGTH-The total line length in the neighborhood will be
          calculated.
          If the value of the field is not 1, the lengths are multiplied by the
          item value before adding them together. This option can be used when
          the field parameter is set to None.The default statistic type is
          MEAN.The available choices for the statistic type are determined by
          the
          numeric type of the specified field. If the field is integer, the
          available statistic choices will be majority, maximum, mean, median,
          minimum, minority, range, variety, and length. If the field is
          floating point, only the mean, maximum, minimum, range, and length
          statistics will be available.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output line statistics raster.

        """