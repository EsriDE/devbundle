# Generated documentation for module arcpy.stpm


class TimeSeriesCrossCorrelation(object):
    """
    Calculates the cross correlation at various time lags between two time series stored in a space-time cube.
    """

    @property
    def description(self) -> str:
        return """

        TimeSeriesCrossCorrelation_stpm(in_cube, analysis_variable_1, analysis_variable_2, output_features, {enable_pop_ups}, {max_lag}, {lag_direction}, {neighborhood_type}, {num_nbrs}, {distance_band}, {spatial_weights}, {filter_option}, {out_corr_table}, {out_pair_table})

        Calculates the cross correlation at various time lags between two time
        series stored in a space-time cube.

     INPUTS:
      in_cube (File):
          The space-time cube containing the variable to be analyzed. Space-time
          cubes have a .nc file extension and are created using various tools in
          the Space Time Pattern Mining toolbox.
      analysis_variable_1 (String):
          The numeric variable of the space-time cube containing the time series
          values of the primary variable.
      analysis_variable_2 (String):
          The numeric variable of the space-time cube containing the secondary
          analysis variable. When using time lags, the secondary analysis
          variable is shifted relative to the primary analysis variable.
      enable_pop_ups {Boolean}:
          Specifies whether time series charts will be created in the pop-ups of
          each output feature showing the cross correlation results. Time series
          pop-ups are not supported for shapefile outputs.CREATE_POPUP-Time
          series charts will be created for the output
          features.NO_POPUP-Time series charts will not be created. This is the
          default.
      max_lag {Long}:
          The maximum number of time lags that will be used to shift the
          secondary analysis variable. Cross correlations will be calculated for
          every time lag value up to the maximum. Provide a positive value even
          for negative time lags; for example, if 10 is provided for this
          parameter and the time lag direction shifts the secondary variable
          both directions, cross correlations will be calculated for all time
          lags between -10 and 10. If no value is provided, a value will be
          determined based on the length of the time series. Provide a value of
          0 to calculate only the raw correlation between the time series
          without any time lags.
      lag_direction {String}:
          Specifies the direction of the time lag. The secondary variable can be
          shifted forward in time (relative to the primary variable), backward
          in time, or in both directions.BOTH-The secondary analysis variable
          will be shifted in both
          directions. For example, if the maximum time lag is 5, the
          correlations for all time lags between -5 and 5 will be calculated.
          This is the default.FORWARD-The secondary analysis variable will be
          shifted forward in
          time (right on the time axis). For example, if the maximum time lag is
          5, the correlations for all time lags between 0 and 5 will be
          calculated. This option is appropriate when changes in the secondary
          analysis variable occur before changes in the primary analysis
          variable.BACKWARD-The secondary analysis variable will be shifted
          backward in
          time (left on the time axis). For example, if the maximum time lag is
          5, the correlations for all time lags between -5 and 0 will be
          calculated. This option is appropriate when changes in the primary
          analysis variable occur before changes in the secondary analysis
          variable.
      neighborhood_type {String}:
          Specifies the neighbors around each location that will be used in
          calculations. If neighbors are used, the cross correlation of a
          location is the weighted average of the correlations between the
          primary variable of the focal location and the secondary variable of
          each of its neighbors (including itself).NO_NBRS-No spatial neighbors
          will be included in the
          calculations.FIXED_DISTANCE-Locations within a specified distance of
          each location
          will be included as neighbors in calculations.K_NEAREST_NEIGHBORS-A
          given number of nearest locations will be
          included as neighbors in calculations.CONTIGUITY_EDGES_ONLY-Polygons
          that share an edge will be included as
          neighbors (rook contiguity).CONTIGUITY_EDGES_CORNERS-Polygons that
          share an edge or a corner will
          be included as neighbors (queen contiguity).
      num_nbrs {Long}:
          The number of nearest locations that will be included as neighbors in
          the calculations.
      distance_band {Linear Unit}:
          All locations within this distance will be included as neighbors. If
          no value is provided, one will be estimated during processing and
          included as a geoprocessing message. If the specified distance results
          in more than 1,000 neighbors, only the closest 1,000 locations will be
          included as neighbors. For polygons, the distance between centroids is
          used to determine neighbors.
      spatial_weights {String}:
          Specifies the weighting scheme that will be applied to spatial
          neighbors when calculating the correlations. The weights are used when
          calculating the weighted average of the correlation between the focal
          feature and each neighbor.EQUAL-Each neighbor will receive equal
          weight (unweighted). This is
          the default.BISQUARE-Neighbors will be weighted using a bisquare
          kernel.GAUSSIAN-Neighbors will be weighted using a Gaussian kernel.
      filter_option {Boolean}:
          Specifies whether trends, seasonality, and autocorrelation will be
          removed from the primary analysis variable and used to filter the
          secondary analysis variable.FILTER-Trends, seasonality, and
          autocorrelation will be
          removed.NO_FILTER-The time series values will not be altered. This is
          the
          default.

     OUTPUTS:
      output_features (Feature Class):
          The output features containing the cross correlations of all locations
          for all time lags. The output will also have fields of the strongest
          correlations (positive, negative, and absolute) and fields of the
          correlations of all time lags. If you filter and remove trends, and
          you do not use neighbors, the output will contain fields of p-values
          and 95 percent confidence intervals of all cross correlations.
      out_corr_table {Table}:
          A table containing the correlations of every time lag of every
          location.
      out_pair_table {Table}:
          A table containing the pairwise correlations between each location and
          each neighbor at all time lags.

        """