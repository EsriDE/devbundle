# Generated documentation for module arcpy.intelligence


class FindFrequentedLocations(object):
    """
    Identifies areas where a movement track has dwelled for multiple time periods and aggregates those locations based on a track identifier.
    """

    @property
    def description(self) -> str:
        return """

        FindFrequentedLocations_intelligence(in_features, track_id_field, out_featureclass, {expression}, {search_distance}, {minimum_loiter_time}, {time_boundary}, {minimum_dwells}, {normalize_daily_distribution}, {summary_fields;summary_fields...})

        Identifies areas where a movement track has dwelled for multiple time
        periods and aggregates those locations based on a track identifier.

     INPUTS:
      in_features (Feature Layer):
          The input movement track points that will be analyzed for possible
          frequented locations. The layer must be time enabled.
      track_id_field (Field):
          The field containing the unique identifiers that will organize the
          source data into movement tracks.
      expression {SQL Expression}:
          An SQL expression used to select a subset of records. For more
          information about SQL syntax, see SQL reference for query expressions
          used in ArcGIS.
      search_distance {Linear Unit}:
          The maximum distance a movement track point can loiter before it is no
          longer considered part of a frequented location. The default is 100
          meters.
      minimum_loiter_time {Time Unit}:
          The minimum amount of time a movement track point can loiter in an
          area before it is considered to be dwelling.This value helps identify
          possible frequented locations where multiple
          unique movement tracks are dwelling in the same time and space. The
          default is 10 minutes.
      time_boundary {Time Unit}:
          The time span that will be used to split theparameter value.
          For example, if you use a time boundary of 1 day, tracks will be split
          at the beginning of every day. Input Features
      minimum_dwells {Long}:
          The minimum number of overlapping individual dwells that will need to
          occur to be defined as a frequented location. By default, all
          locations that meet the criteria for a dwell will be returned.
      normalize_daily_distribution {Boolean}:
          Specifies whether the daily distribution of dwell locations will be
          normalized. Normalized values represent a percentage of total time
          that a dwell location occurred on the particular day, while the real
          values represent the total number of dwells that occurred on the given
          day.NORMALIZED-The daily distribution of dwell locations values will
          be
          normalized.REAL-The daily distribution of dwell locations values will
          not be
          normalized and represent the actual value. This is the default.
      summary_fields {Value Table}:
          Specifies the statistics that will be calculated.Statistics can be
          calculated for the following variables:START_TIME-The time in hours
          that the individual dwell location was
          first detected. The time is rounded to the nearest hour.END_TIME-The
          time in hours that the individual dwell location was last
          detected. The time is rounded to the nearest hour.DWELL_DURATION-The
          time in seconds that the individual dwell location
          was active.The following statistics are supported:MEAN-The mean of
          numeric values.MIN-The minimum value of a numeric
          field.MAX-The maximum value of a numeric field.STDDEV-The standard
          deviation of a numeric field.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output polygon feature class containing the possible frequented
          locations.

        """