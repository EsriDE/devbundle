# Generated documentation for module arcpy.stats


class TimeSeriesSmoothing(object):
    """
    Smooths a numeric variable of one or more time series using centered, forward, and backward moving averages, as well as an adaptive method based on local linear regression. After smoothing short-term fluctuations, longer-term trends or cycles often become apparent.
    """

    @property
    def description(self) -> str:
        return """

        TimeSeriesSmoothing_stats(in_features, time_field, analysis_field, {group_method}, {method}, {time_window}, {append_to_input}, {output_features}, {id_field}, {apply_shorter_window}, {enable_time_series_popups})

        Smooths a numeric variable of one or more time series using centered,
        forward, and backward moving averages, as well as an adaptive method
        based on local linear regression. After smoothing short-term
        fluctuations, longer-term trends or cycles often become apparent.

     INPUTS:
      in_features (Table View):
          The features or table containing the time series data and the field to
          smooth.
      time_field (Field):
          The field containing the time of each record.
      analysis_field (Field):
          The field containing the values that will be smoothed.
      group_method {String}:
          Specifies the method that will be used to group records into different
          time series. Smoothing is performed independently for each time
          series.LOCATION-Features at the same location will be grouped in the
          same
          time series. This is the default.ID_FIELD-Records with the same value
          of the ID field will be grouped
          in the same time series.NONE-All records will be in the same time
          series.
      method {String}:
          Specifies the smoothing method that will be used.BACKWARD-The smoothed
          value is the average of the record and the
          values within the time window before it. This is the
          default.CENTERED-The smoothed value is the average of the record and
          the
          values before and after it. Half of the time window is used before the
          time of the record, and half is used after.FORWARD-The smoothed value
          is the average of the record and the values
          within the time window after it.ADAPTIVE-The smoothed value is the
          result of a local linear regression
          centered at the record. The size of the time window is optimized for
          each record.
      time_window {Time Unit}:
          The length of the time window. The value can be provided in seconds,
          minutes, hours, days, weeks, months, or years. For backward, forward,
          and centered moving averages, the value and unit must be provided. For
          adaptive bandwidth local linear regression, the value can be left
          empty and a time window will be estimated independently for each
          value. Values that fall on the border of the time window will be
          included within the window. For example, if you have daily data and
          you use a backward moving average with a time window of four days,
          five values will be included in the window when smoothing a record:
          the value of the record and the values of the four previous days.
      append_to_input {Boolean}:
          Specifies whether the output fields will be appended to the input
          dataset or saved as a new output table or feature class. If you append
          the fields to the input, the output coordinate system environment will
          be ignored.APPEND_TO_INPUT-The output fields will be appended to the
          input
          features. This option modifies the input data.NEW_OUTPUT-The output
          fields will not be appended to the input. An
          output table or a feature class will be created containing the output
          fields. This is the default.
      id_field {Field}:
          The integer or text field containing a unique ID for each time series.
          All records with the same value of this field are part of the same
          time series.
      apply_shorter_window {Boolean}:
          Specifies whether the time window will be shortened at the beginning
          and end of each time series.APPLY_SHORTER_WINDOW-The time window will
          be shortened at the start
          and end of the time series so that the time window does not extend
          before the start or after the end of the time
          series.NOT_APPLY_SHORTER_WINDOW-The time window will not be shortened.
          If the
          time window extends before the start or after the end of the time
          series, the smoothed value will be null. This is the default.
      enable_time_series_popups {Boolean}:
          Specifies whether the output features or table will include pop-up
          charts showing the original and smoothed values of the time
          series.CREATE_POPUP-The output will include pop-up charts. This is the
          default.NO_POPUP-The output will not include pop-up charts.

     OUTPUTS:
      output_features {Table}:
          The output features containing the smoothed values as well as fields
          for the time window and number of neighbors.

        """