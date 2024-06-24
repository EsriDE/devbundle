# Generated documentation for module arcpy.stpm


class TimeSeriesClustering(object):
    """
    Partitions a collection of time series, stored in a space-time cube, based on the similarity of time series characteristics. Time series can be clustered based on three criteria: having similar values across time, tending to increase and decrease at the same time, and having similar repeating patterns. The output of this tool is a 2D map displaying each location in the cube symbolized by cluster membership and messages. The output also includes charts containing information about the representative time series signature for each cluster.
    """

    @property
    def description(self) -> str:
        return """

        TimeSeriesClustering_stpm(in_cube, analysis_variable, output_features, characteristic_of_interest, {cluster_count}, {output_table_for_charts}, {shape_characteristic_to_ignore;shape_characteristic_to_ignore...}, {enable_time_series_popups})

        Partitions a collection of time series, stored in a space-time cube,
        based on the similarity of time series characteristics. Time series
        can be clustered based on three criteria: having similar values across
        time, tending to increase and decrease at the same time, and having
        similar repeating patterns. The output of this tool is a 2D map
        displaying each location in the cube symbolized by cluster membership
        and messages. The output also includes charts containing information
        about the representative time series signature for each cluster.

     INPUTS:
      in_cube (File):
          The space-time cube containing the variable to be analyzed. Space-time
          cubes have a .nc file extension and are created using various tools in
          the Space Time Pattern Mining toolbox.
      analysis_variable (String):
          The numeric variable in the netCDF file, changing over time, that will
          be used to distinguish one cluster from another.
      characteristic_of_interest (String):
          Specifies the characteristic of the time series that will be used to
          determine which locations should be clustered together.VALUE-
          Locations with similar values across time will be clustered
          together.PROFILE-Locations with values that tend to increase and
          decrease
          proportionally at the same times will be clustered
          together.PROFILE_FOURIER-Locations with values that have similar
          smooth,
          periodic patterns will be clustered together.
      cluster_count {Long}:
          The number of clusters to create. When left empty, the tool will
          evaluate the optimal number of clusters using a pseudo-F statistic.
          The optimal number of clusters will be reported in the messages
          window.
      shape_characteristic_to_ignore {String}:
          Specifies characteristics that will be ignored when determining the
          similarity between two time series.TIME_LAG-The starting time of each
          period, including time lags, will
          be ignored. For example, if two time series have similar periodic
          patterns, but the values of one are three days behind the other, the
          time series will be considered similar.RANGE-The magnitude of the
          values in each period will be ignored. For
          example, if two time series begin and end their periods at the same
          times, they will be considered similar, even if the actual values are
          very different.If both characteristics are ignored, two time series
          will be
          considered similar if the durations of the periods are similar, even
          if they start at different times and have different values within the
          periods.
      enable_time_series_popups {Boolean}:
          Specifies whether time series charts will be created in the pop-ups of
          each output feature showing the time series of the feature and the
          average time series of all features in the same cluster as the
          feature. Time series pop-ups are not supported for shapefile
          outputs.CREATE_POPUP-Time series charts will be created for the output
          features.NO_POPUP-Time series charts will not be created. This is the
          default.

     OUTPUTS:
      output_features (Feature Class):
          The new output feature class containing all locations in the space-
          time cube and a field indicating cluster membership. This feature
          class will be a two-dimensional representation of the clusters in your
          data.
      output_table_for_charts {Table}:
          If specified, this table contains the representative time
          series for each cluster based on both the average for each time series
          cluster and the medoid time series. Charts created from this table can
          be accessed in thesection. Standalone Tables

        """