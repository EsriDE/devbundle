# Generated documentation for module arcpy.stpm


class ChangePointDetection(object):
    """
    Detects time steps when a statistical property of the time series changes for each location of a space-time cube.
    """

    @property
    def description(self) -> str:
        return """

        ChangePointDetection_stpm(in_cube, analysis_variable, output_features, {change_type}, {method}, {num_change_points}, {sensitivity}, {min_seg_len})

        Detects time steps when a statistical property of the time series
        changes for each location of a space-time cube.

     INPUTS:
      in_cube (File):
          The space-time cube containing the variable to be analyzed. Space-time
          cubes have a .nc file extension and are created using various tools in
          the Space Time Pattern Mining toolbox.
      analysis_variable (String):
          The numeric variable of the space-time cube containing the time series
          values of each location.
      change_type {String}:
          Specifies the type of change that will be detected. Each option
          specifies a statistical property of the time series that is assumed to
          be constant in each segment. The value changes to a new constant value
          at each change point in the time series.MEAN-Shifts in mean value will
          be detected. This is the
          default.STANDARD_DEVIATION-Changes in standard deviation will be
          detected.SLOPE-Changes in slope (linear trend) will be
          detected.COUNT-Changes in the mean of count data will be detected.
      method {String}:
          Specifies whether the number of change points will be detected
          automatically or specified by a defined number of change points used
          for all locations.AUTO_DETECT-The number of change points will be
          detected
          automatically. The sensitivity of the detection will be defined by the
          sensitivity parameter. This is the default.DEFINED_NUMBER-The number
          of change points will be defined by the
          num_change_points parameter.
      num_change_points {Long}:
          The number of change points that will be detected at each location.
          The default is 1.
      sensitivity {Double}:
          A number between 0 and 1 that defines the sensitivity of the
          detection. Larger values will result in more detected change points at
          each location. The default is 0.5.
      min_seg_len {Long}:
          The minimum number of time steps within each segment. The change
          points will divide each time series into segments in which each
          segment has at least this number of time steps. For change in mean,
          standard deviation, and count, the default is 1, meaning that every
          time step can be a change point. For change in slope (linear trend),
          the default is 2 because at least two values are required to fit a
          line. The value must be less than half the number of time steps in the
          time series.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class that will contain the change point detection
          results. The layer displays the number of change points detected at
          each location and contains pop-up line charts showing the time series
          values, change points, and estimates of mean or standard deviation of
          each segment.

        """