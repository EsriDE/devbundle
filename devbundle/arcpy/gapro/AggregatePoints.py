# Generated documentation for module arcpy.gapro


class AggregatePoints(object):
    """
    Aggregates points into polygon features or bins. A polygon is returned with a count of points as well as optional statistics at all locations where points exist.
    """

    @property
    def description(self) -> str:
        return """

        AggregatePoints_gapro(point_layer, out_feature_class, polygon_or_bin, {polygon_layer}, {bin_type}, {bin_size}, {time_step_interval}, {time_step_repeat}, {time_step_reference}, {summary_fields;summary_fields...}, {bin_resolution})

        Aggregates points into polygon features or bins. A polygon is returned
        with a count of points as well as optional statistics at all locations
        where points exist.

     INPUTS:
      point_layer (Feature Layer):
          The point features that will be aggregated into polygons or bins.
      polygon_or_bin (String):
          Specifies how the point_layer parameter value will be
          aggregated.POLYGON-The point layer will be aggregated into a polygon
          dataset.BIN-The point layer will be aggregated into square or
          hexagonal bins
          that are generated when the tool is run.
      polygon_layer {Feature Layer}:
          The polygon features into which the input points will be aggregated.
      bin_type {String}:
          Specifies the bin shape that will be generated to hold the aggregated
          points.SQUARE-Square bins will be generated in which the bin_size
          value
          represents the height of a square. This is the
          default.HEXAGON-Hexagonal bins will be generated in which the bin_size
          value
          represents the height between two parallel sides.H3-H3 bins will be
          generated. The bin size will be determined by the
          bin_resolution parameter value.
      bin_size {Linear Unit}:
          The distance interval that represents the bin size and units into
          which the point_layer value will be aggregated. The distance interval
          must be a linear unit.
      time_step_interval {Time Unit}:
          A value that specifies the duration of the time step. This parameter
          is only available if the input points are time enabled and represent
          an instant in time.Time stepping can only be applied if time is
          enabled on the input.
      time_step_repeat {Time Unit}:
          A value that specifies how often the time-step interval occurs. This
          parameter is only available if the input points are time enabled and
          represent an instant in time.
      time_step_reference {Date}:
          A date that specifies the reference time with which to align the time
          steps. The default is January 1, 1970, at 12:00 a.m. This parameter is
          only available if the input points are time enabled and represent an
          instant in time.
      summary_fields {Value Table}:
          The statistics that will be calculated on specified fields.COUNT-The
          number of nonnull values. It can be used on numeric fields
          or strings. The count of [null, 0, 2] is 2.SUM-The sum of numeric
          values in a field. The sum of [null, null, 3]
          is 3.MEAN-The mean of numeric values. The mean of [0,2, null] is
          1.MIN-The minimum value of a numeric field. The minimum of [0, 2,
          null]
          is 0.MAX-The maximum value of a numeric field. The maximum value of
          [0, 2,
          null] is 2.STDDEV-The standard deviation of a numeric field. The
          standard
          deviation of [1] is null. The standard deviation of [null, 1,1,1] is
          null.VAR-The variance of a numeric field in a track. The variance of
          [1] is
          null. The variance of [null, 1,1,1] is null.RANGE-The range of a
          numeric field. This is calculated as the minimum
          value subtracted from the maximum value. The range of [0, null, 1] is
          1. The range of [null, 4] is 0.ANY-A sample string from a field of
          type string.
      bin_resolution {Long}:
          The resolution of the H3 bins. This is a value between 0 and 15 in
          which 0 will produce the largest H3 bins and 15 will produce the
          smallest H3 bins.

     OUTPUTS:
      out_feature_class (Feature Class):
          A new feature class with the aggregated polygon results.

        """