# Generated documentation for module arcpy.gapro


class CalculateMotionStatistics(object):
    """
    Calculates motion statistics for points in a time-enabled feature class.
    """

    @property
    def description(self) -> str:
        return """

        CalculateMotionStatistics_gapro(input_layer, out_feature_class, track_fields;track_fields..., track_history_window, {motion_statistics;motion_statistics...}, {distance_method}, {idle_dist_tolerance}, {idle_time_tolerance}, {time_boundary_split}, {time_boundary_reference}, {distance_unit}, {duration_unit}, {speed_unit}, {acceleration_unit}, {elevation_unit})

        Calculates motion statistics for points in a time-enabled feature
        class.

     INPUTS:
      input_layer (Feature Layer):
          The time-enabled point features on which motion statistics will be
          calculated.
      track_fields (Field):
          One or more fields that will be used to identify distinct entities.
      track_history_window (Long):
          The number of observations (including the current observation) that
          will be used for summary statistics. The default value is 3, which
          means that the summary statistics will be calculated at each point in
          a track using the current observation and the previous two
          observations. This parameter does not affect instantaneous statistics
          or idle classification.
      motion_statistics {String}:
          Specifies the group containing the statistics that will be calculated
          and written to the result. If no value is specified, all statistics
          from all groups will be calculated.DISTANCE-The distance between the
          current and previous observation and
          the maximum, minimum, average, and total distance in the track history
          window will be calculated.DURATION-The duration between the current
          and previous observation and
          the maximum, minimum, average, and total duration in the track history
          window will be calculated.SPEED-The speed of travel between the
          current and previous observation
          and the maximum, minimum, and average speed in the track history
          window will be calculated.ACCELERATION-The acceleration between the
          current speed and the
          previous speed and the maximum, minimum, and average acceleration in
          the track history window will be calculated.ELEVATION-The current
          elevation, the elevation change between the
          current and previous observation, and the maximum, minimum, average,
          and total elevation change in the track history window will be
          calculated.SLOPE-The slope between the current and previous
          observation and the
          maximum, minimum, and average slope in the track history window will
          be calculated.IDLE-A determination as to whether an entity is
          currently idling will
          be made and the percentage of idle time and total idle time in the
          track history window will be calculated.BEARING-The angle of travel
          between the previous observation and the
          current observation will be calculated.
      distance_method {String}:
          Specifies the distance measurement method that will be used when
          calculating motion statistics.GEODESIC-Geodesic distance will be
          used.PLANAR-Planar distance will be
          used. This is the default.
      idle_dist_tolerance {Linear Unit}:
          The maximum distance that two sequential points in a track can be
          apart and still be considered idle. This parameter is used with the
          idle_time_tolerance parameter to determine whether an entity is
          idling. The idle_dist_tolerance parameter is required if the IDLE
          statistic group is specified for the motion_statistics parameter or if
          statistics in all the groups will be calculated.
      idle_time_tolerance {Time Unit}:
          The minimum duration that two sequential points in a track must be
          near each other to be considered idle. This parameter is used with the
          idle_dist_tolerance parameter to determine whether an entity is
          idling. The idle_time_tolerance parameter is required if the IDLE
          statistic group is specified for the motion_statistics parameter or if
          statistics in all the groups will be calculated.
      time_boundary_split {Time Unit}:
          A time span to split the input data into for analysis. A time boundary
          allows you to analyze values within a defined time span. For example,
          if you use a time boundary of 1 day, starting on January 1, 1980,
          tracks will be split at the beginning of every day. This parameter is
          only available with ArcGIS Enterprise 10.7 and later.
      time_boundary_reference {Date}:
          The reference time used to split the input data into for analysis.
          Time boundaries will be created for the entire span of the data, and
          the reference time does not need to occur at the start. If no
          reference time is specified, January 1, 1970, is used.
      distance_unit {String}:
          Specifies the unit of measure that will be used for distance values in
          the output feature class.METERS-The unit of measure will be meters.
          This is the
          default.KILOMETERS-The unit of measure will be kilometers.MILES-The
          unit of measure will be US survey miles.NAUTICAL_MILES-The unit of
          measure will be US survey nautical miles.YARDS-The unit of measure
          will be US survey yards.FEET-The unit of measure will be US survey
          feet.MILES_INT-The unit of measure will be statute
          miles.NAUTICAL_MILES_INT-The unit of measure will be international
          nautical
          miles.YARDS_INT-The unit of measure will be international
          yards.FEET_INT-The unit of measure will be international feet.
      duration_unit {String}:
          Specifies the unit of measure that will be used for duration values in
          the output feature class.YEARS-The unit of measure will be
          years.MONTHS-The unit of measure
          will be months.WEEKS-The unit of measure will be weeks.DAYS-The unit
          of measure will be days.HOURS-The unit of measure will be
          hours.MINUTES-The unit of measure will be minutes.SECONDS-The unit of
          measure will be seconds. This is the default.MILLISECONDS-The unit of
          measure will be milliseconds.
      speed_unit {String}:
          Specifies the unit of measure that will be used for speed values in
          the output feature class.METERS_PER_SECOND-The unit of measure will be
          meters per second. This
          is the default.MILES_PER_HOUR-The unit of measure will be miles per
          hour.KILOMETERS_PER_HOUR-The unit of measure will be kilometers per
          hour.FEET_PER_SECOND-The unit of measure will be feet per
          second.NAUTICAL_MILES_PER_HOUR-The unit of measure will be nautical
          miles per
          hour.
      acceleration_unit {String}:
          Specifies the unit of measure that will be used for acceleration
          values in the output feature class.METERS_PER_SECOND_SQUARED-The unit
          of measure will be meters per
          second squared. This is the default.FEET_PER_SECOND_SQUARED-The unit
          of measure will be feet per second
          squared.
      elevation_unit {String}:
          Specifies the unit of measure that will be used for elevation values
          in the output feature class.METERS-The unit of measure will be meters.
          This is the
          default.KILOMETERS-The unit of measure will be US survey
          kilometers.MILES-The unit of measure will be US survey miles.YARDS-The
          unit of measure will be US survey yards.FEET-The unit of measure will
          be US survey feet.MILES_INT-The unit of measure will be statute
          miles.YARDS_INT-The unit of measure will be international
          yards.FEET_INT-The unit of measure will be international feet.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class or layer containing the points with new
          fields for each motion statistic that was calculated.

        """