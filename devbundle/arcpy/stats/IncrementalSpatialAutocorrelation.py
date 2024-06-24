# Generated documentation for module arcpy.stats


class IncrementalSpatialAutocorrelation(object):
    """
    Measures spatial autocorrelation for a series of distances and optionally creates a line graph of those distances and their corresponding z-scores. Z-scores reflect the intensity of spatial clustering, and statistically significant peak z-scores indicate distances where spatial processes promoting clustering are most pronounced. These peak distances are often appropriate values to use for tools with a Distance Band or Distance Radius parameter.
    """

    @property
    def description(self) -> str:
        return """

        IncrementalSpatialAutocorrelation_stats(Input_Features, Input_Field, Number_of_Distance_Bands, {Beginning_Distance}, {Distance_Increment}, {Distance_Method}, {Row_Standardization}, {Output_Table}, {Output_Report_File})

        Measures spatial autocorrelation for a series of distances and
        optionally creates a line graph of those distances and their
        corresponding z-scores. Z-scores reflect the intensity of spatial
        clustering, and statistically significant peak z-scores indicate
        distances where spatial processes promoting clustering are most
        pronounced. These peak distances are often appropriate values to use
        for tools with a Distance Band or Distance Radius parameter.

     INPUTS:
      Input_Features (Feature Layer):
          The feature class for which spatial autocorrelation will be measured
          over a series of distances.
      Input_Field (Field):
          The numeric field used in assessing spatial autocorrelation.
      Number_of_Distance_Bands (Long):
          The number of times to increment the neighborhood size and analyze the
          dataset for spatial autocorrelation. The starting point and size of
          the increment are specified in the Beginning_Distance and
          Distance_Increment parameters, respectively.
      Beginning_Distance {Double}:
          The distance at which to start the analysis of spatial autocorrelation
          and the distance from which to increment. The value entered for this
          parameter should be in the units of the Output Coordinate System
          environment setting.
      Distance_Increment {Double}:
          The distance to increase after each iteration. The distance used in
          the analysis starts at the Beginning_Distance and increases by the
          amount specified in the Distance_Increment. The value entered for this
          parameter should be in the units of the Output Coordinate System
          environment setting.
      Distance_Method {String}:
          Specifies how distances are calculated from each feature to
          neighboring features.EUCLIDEAN-The straight-line distance between two
          points (as the crow
          flies)MANHATTAN-The distance between two points measured along axes at
          right
          angles (city block); calculated by summing the (absolute) difference
          between the x- and y-coordinates
      Row_Standardization {Boolean}:
          Row standardization is recommended whenever feature distribution is
          potentially biased due to sampling design or to an imposed aggregation
          scheme.ROW_STANDARDIZATION-Spatial weights are standardized by row.
          Each
          weight is divided by its row sum.NO_STANDARDIZATION-No standardization
          of spatial weights is applied.

     OUTPUTS:
      Output_Table {Table}:
          The table to be created with each distance band and associated z-score
          result.
      Output_Report_File {File}:
          The PDF file to be created containing a line graph summarizing
          results.

        """