# Generated documentation for module arcpy.stats


class OptimizedOutlierAnalysis(object):
    """
    Given incident points or weighted features (points or polygons), creates a map of statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic. It evaluates the characteristics of the input feature class to produce optimal results.
    """

    @property
    def description(self) -> str:
        return """

        OptimizedOutlierAnalysis_stats(Input_Features, Output_Features, {Analysis_Field}, {Incident_Data_Aggregation_Method}, {Bounding_Polygons_Defining_Where_Incidents_Are_Possible}, {Polygons_For_Aggregating_Incidents_Into_Counts}, {Performance_Adjustment}, {Cell_Size}, {Distance_Band})

        Given incident points or weighted features (points or polygons),
        creates a map of statistically significant hot spots, cold spots, and
        spatial outliers using the Anselin Local Moran's I statistic. It
        evaluates the characteristics of the input feature class to produce
        optimal results.

     INPUTS:
      Input_Features (Feature Layer):
          The point or polygon feature class for which the cluster and outlier
          analysis will be performed.
      Analysis_Field {Field}:
          The numeric field (number of incidents, crime rates, test scores, and
          so on) to be evaluated.
      Incident_Data_Aggregation_Method {String}:
          The aggregation method to use to create weighted features for analysis
          from incident point data.COUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS-A
          fishnet polygon mesh will
          overlay the incident point data and the number of incidents within
          each polygon cell will be counted. If no bounding polygon is provided
          in the Bounding_Polygons_Defining_Where_Incidents_Are_Possible
          parameter, only cells with at least one incident will be used in the
          analysis; otherwise, all cells within the bounding polygons will be
          analyzed. This is the
          default.COUNT_INCIDENTS_WITHIN_HEXAGON_POLYGONS-A hexagon polygon mesh
          will
          overlay the incident point data and the number of incidents within
          each polygon cell will be counted. If no bounding polygon is provided
          in the Bounding_Polygons_Defining_Where_Incidents_Are_Possible
          parameter, only cells with at least one incident will be used in the
          analysis; otherwise, all cells within the bounding polygons will be
          analyzed.COUNT_INCIDENTS_WITHIN_AGGREGATION_POLYGONS-You provide
          aggregation
          polygons to overlay the incident point data in the
          Polygons_For_Aggregating_Incidents_Into_Counts parameter. The
          incidents within each polygon are
          counted.SNAP_NEARBY_INCIDENTS_TO_CREATE_WEIGHTED_POINTS-Nearby
          incidents will
          be aggregated together to create a single weighted point. The weight
          for each point is the number of aggregated incidents at that location.
      Bounding_Polygons_Defining_Where_Incidents_Are_Possible {Feature Layer}:
          A polygon feature class defining where the incident Input_Features
          could possibly occur.
      Polygons_For_Aggregating_Incidents_Into_Counts {Feature Layer}:
          The polygons to use to aggregate the incident Input_Features in order
          to get an incident count for each polygon feature.
      Performance_Adjustment {String}:
          This analysis utilizes permutations to create a reference
          distribution. Choosing the number of permutations is a balance between
          precision and increased processing time. Choose your preference for
          speed versus precision. More robust and precise results take longer to
          calculate.QUICK_199-With 199 permutations, the smallest possible
          pseudo p-value
          is 0.005 and all other pseudo p-values will be even multiples of this
          value.BALANCED_499-With 499 permutations, the smallest possible pseudo
          p-value is 0.002 and all other pseudo p-values will be even multiples
          of this value. This is the default.ROBUST_999-With 999 permutations,
          the smallest possible pseudo p-value
          is 0.001 and all other pseudo p-values will be even multiples of this
          value.
      Cell_Size {Linear Unit}:
          The size of the grid cells used to aggregate the Input_Features. When
          aggregating into a hexagon grid, this distance is used as the height
          to construct the hexagon polygons.
      Distance_Band {Linear Unit}:
          The spatial extent of the analysis neighborhood. This value determines
          which features are analyzed together in order to assess local
          clustering.

     OUTPUTS:
      Output_Features (Feature Class):
          The output feature class to receive the result fields.

        """