# Generated documentation for module arcpy.stats


class ClustersOutliers(object):
    """
    Given a set of weighted features, identifies statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic.
    """

    @property
    def description(self) -> str:
        return """

        ClustersOutliers_stats(Input_Feature_Class, Input_Field, Output_Feature_Class, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, {Distance_Band_or_Threshold_Distance}, {Weights_Matrix_File}, {Apply_False_Discovery_Rate__FDR__Correction}, {Number_of_Permutations}, {number_of_neighbors})

        Given a set of weighted features, identifies statistically significant
        hot spots, cold spots, and spatial outliers using the Anselin Local
        Moran's I statistic.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which cluster and outlier analysis will be
          performed.
      Input_Field (Field):
          The numeric field to be evaluated.
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features are
          defined.INVERSE_DISTANCE-Nearby neighboring features have a larger
          influence
          on the computations for a target feature than features that are far
          away.INVERSE_DISTANCE_SQUARED-Same as INVERSE_DISTANCE except that the
          slope is sharper, so influence drops off more quickly, and only a
          target feature's closest neighbors will exert substantial influence on
          computations for that feature.FIXED_DISTANCE_BAND-Each feature is
          analyzed within the context of
          neighboring features. Neighboring features inside the specified
          critical distance (Distance_Band_or_Threshold_Distance) receive a
          weight of one and exert influence on computations for the target
          feature. Neighboring features outside the critical distance receive a
          weight of zero and have no influence on a target feature's
          computations.ZONE_OF_INDIFFERENCE-Features within the specified
          critical distance
          (Distance_Band_or_Threshold_Distance) of a target feature receive a
          weight of one and influence computations for that feature. Once the
          critical distance is exceeded, weights (and the influence a
          neighboring feature has on target feature computations) diminish with
          distance.K_NEAREST_NEIGHBORS-The closest k features are included in
          the
          analysis. The number of neighbors (k) is specified by the
          number_of_neighbors parameter.CONTIGUITY_EDGES_ONLY-Only neighboring
          polygon features that share a
          boundary or overlap will influence computations for the target polygon
          feature.CONTIGUITY_EDGES_CORNERS-Polygon features that share a
          boundary, share
          a node, or overlap will influence computations for the target polygon
          feature.GET_SPATIAL_WEIGHTS_FROM_FILE-Spatial relationships are
          defined by a
          specified spatial weights file. The path to the spatial weights file
          is specified by the Weights_Matrix_File parameter.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to
          neighboring features.EUCLIDEAN_DISTANCE-The straight-line distance
          between two points (as
          the crow flies)MANHATTAN_DISTANCE-The distance between two points
          measured along axes
          at right angles (city block); calculated by summing the (absolute)
          difference between the x- and y-coordinates
      Standardization (String):
          Row standardization is recommended whenever the distribution of your
          features is potentially biased due to sampling design or an imposed
          aggregation scheme.NONE-No standardization of spatial weights is
          applied.ROW-Spatial
          weights are standardized; each weight is divided by its
          row sum (the sum of the weights of all neighboring features).
      Distance_Band_or_Threshold_Distance {Double}:
          Specifies a cutoff distance for Inverse Distance and Fixed Distance
          options. Features outside the specified cutoff for a target feature
          are ignored in analyses for that feature. However, for Zone of
          Indifference, the influence of features outside the given distance is
          reduced with distance, while those inside the distance threshold are
          equally considered. The distance value entered should match that of
          the output coordinate system.For the Inverse Distance
          conceptualizations of spatial relationships,
          a value of 0 indicates that no threshold distance is applied; when
          this parameter is left blank, a default threshold value is computed
          and applied. This default value is the Euclidean distance that ensures
          every feature has at least one neighbor.This parameter has no effect
          when Polygon Contiguity or Get Spatial
          Weights From File spatial conceptualizations are selected.
      Weights_Matrix_File {File}:
          The path to a file containing weights that define spatial, and
          potentially temporal, relationships among features.
      Apply_False_Discovery_Rate__FDR__Correction {Boolean}:
          APPLY_FDR-Statistical significance will be based on the False
          Discovery Rate correction for a 95 percent confidence level.
          NO_FDR-Features with p-values less than 0.05 will appear in
          thefield reflecting statistically significant clusters or outliers at
          a 95 percent confidence level (default). COType
      Number_of_Permutations {Long}:
          The number of random permutations for the calculation of pseudo
          p-values. The default number of permutations is 499. If you choose 0
          permutations, the standard p-value is calculated.0-Permutations are
          not used and a standard p-value is
          calculated.99-With 99 permutations, the smallest possible pseudo
          p-value is 0.01
          and all other pseudo p-values will be multiples of this value.199-With
          199 permutations, the smallest possible pseudo p-value is
          0.005 and all other possible pseudo p-values will be multiples of this
          value.499-With 499 permutations, the smallest possible pseudo p-value
          is
          0.002 and all other pseudo p-values will be multiples of this
          value.999-With 999 permutations, the smallest possible pseudo p-value
          is
          0.001 and all other pseudo p-values will be multiples of this
          value.9999-With 9999 permutations, the smallest possible pseudo
          p-value is
          0.0001 and all other pseudo p-values will be multiples of this value.
      number_of_neighbors {Long}:
          The number of neighbors to include in the analysis.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output feature class to receive the results fields.

        """