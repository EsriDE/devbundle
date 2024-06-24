# Generated documentation for module arcpy.stpm


class VisualizeSpaceTimeCube3D(object):
    """
    Visualizes the variables stored in a netCDF space-time cube created with the Space Time Pattern Mining tools. Output from this tool is a three-dimensional representation uniquely rendered based on the variable and theme specified.
    """

    @property
    def description(self) -> str:
        return """

        VisualizeSpaceTimeCube3D_stpm(in_cube, cube_variable, display_theme, output_features)

        Visualizes the variables stored in a netCDF space-time cube created
        with the Space Time Pattern Mining tools. Output from this tool is a
        three-dimensional representation uniquely rendered based on the
        variable and theme specified.

     INPUTS:
      in_cube (File):
          The space-time cube containing the variable to be analyzed. Space-time
          cubes have a .nc file extension and are created using various tools in
          the Space Time Pattern Mining toolbox.
      cube_variable (String):
          The numeric variable in the netCDF cube that will be explored. The
          space-time cube will always contain the COUNT variable if aggregation
          was used when creating the cube. Any summary fields or variables will
          also be available if they were included when the cube was created.
      display_theme (String):
          Specifies the characteristic of theparameter value to be
          displayed. Options will vary depending on how the cube was created and
          the analyses that were run. Cube Variable         VALUE-The
          numeric value of theparameter will be displayed.
          Cube VariableHOT_AND_COLD_SPOT_RESULTS-The statistical significance of
          each bin
          will be displayed based on the space-time hot spot analysis run in
          Emerging Hot Spot Analysis.ESTIMATED_BINS-Bins with estimated values
          will be displayed. LOCAL_OUTLIER_RESULTS-The cluster or
          outlier type () for each
          bin determined by Local Outlier Analysis will be displayed.
          COTypeTEMPORAL_AGGREGATION_COUNT-The count of records aggregated into
          each
          space-time bin will be displayed.FORECAST_RESULTS-The input time steps
          and the resulting forecasted
          values from the Time Series Forecasting tools will be displayed.
          TIME_SERIES_OUTLIER_RESULTS-The results of theparameter in
          the Time Series Forecasting tools will be displayed. Outlier
          OptionTIME_SERIES_CHANGE_POINTS-The results of the Change Point
          Detection
          tool will be displayed. The output will contain fields indicating
          whether each time step is a change point along with estimates of the
          mean or standard deviation for the current and previous time step.
          is the numeric value of theparameter and is always
          available.values are only available for the summary fields that were
          included when the cube was created.values will only be available for
          theparameter value for which Emerging Hot Spot Analysis has been
          run.values will only be available forvalues for which Local Outlier
          Analysis has been run.values will only be available for defined
          location cubes that have been aggregated temporally.values will only
          be available for theparameter value for which a Time Series
          Forecasting tool has been run.values will only be available when
          theparameter has been set for a tool in the the Time Series
          Forecasting toolset.values will only be available forvalues for which
          Change Point Detection has been run. ValueCube
          VariableEstimated binsHot and cold spot resultsCube VariableCluster
          and outlier resultsCube VariableTemporal aggregation countForecast
          resultsCube VariableTime series outlier resultsOutlier OptionTime
          series change pointsCube VariableFor in-depth information about each
          option, including descriptions of
          the output and created charts, see the Visualization display themes
          for the space-time cube topic.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class results. This feature class will be a three-
          dimensional map representation of the display variable that can be
          displayed in a 3D scene.

        """