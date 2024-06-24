# Generated documentation for module arcpy.gapro


class FindDwellLocations(object):
    """
    Finds locations where moving objects have stopped, or dwelled, using given time and distance thresholds.
    """

    @property
    def description(self) -> str:
        return """

        FindDwellLocations_gapro(input_features, output, track_fields;track_fields..., distance_method, distance_tolerance, time_tolerance, output_type, {summary_statistics;summary_statistics...}, {time_boundary_split}, {time_boundary_reference})

        Finds locations where moving objects have stopped, or dwelled, using
        given time and distance thresholds.

     INPUTS:
      input_features (Feature Layer):
          The point tracks in which dwells will be found. The input must be a
          time-enabled layer with features that represent instants in time.
      track_fields (Field):
          One or more fields that will be used to identify unique tracks.
      distance_method (String):
          Specifies how the distances between dwell features will be
          calculated.GEODESIC-If the spatial reference can be panned, tracks
          will cross
          the international date line when appropriate. If the spatial reference
          cannot be panned, tracks will be limited to the coordinate system
          extent and may not wrap.PLANAR-Planar distances will be used.
      distance_tolerance (Linear Unit):
          The maximum distance between points to be considered a single dwell
          location.
      time_tolerance (Time Unit):
          The minimum time duration to be considered a single dwell location.
          Both time and distance are considered when finding dwells.
          Theparameter specifies distance. Distance Tolerance
      output_type (String):
          Specifies how the dwell features will be output.DWELL_FEATURES-All of
          the input point features that are part of a
          dwell will be returned.DWELL_MEAN_CENTERS-Points representing the
          mean centers of each dwell
          group will be returned. This is the default.DWELL_CONVEX_HULLS-
          Polygons representing the convex hull of each
          dwell group will be returned.ALL_FEATURES-All of the input point
          features will be returned.
      summary_statistics {Value Table}:
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
          type string.FIRST-The first value of a specified field in a
          track.LAST-The last value of a specified field in a track.
      time_boundary_split {Time Unit}:
          A time span to split the input data into for analysis. A time boundary
          allows you to analyze values within a defined time span. For example,
          if you use a time boundary of 1 day, and set the time boundary
          reference to January 1, 1980, tracks will be split at the beginning of
          every day.
      time_boundary_reference {Date}:
          The reference time used to split the input data into for analysis.
          Time boundaries will be created for the entire span of the data, and
          the reference time does not need to occur at the start. If no
          reference time is specified, January 1, 1970, is used.

     OUTPUTS:
      output (Feature Class):
          The output feature class with the resulting dwells.

        """