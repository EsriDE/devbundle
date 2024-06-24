# Generated documentation for module arcpy.stats


class HotSpots(object):
    """
    Given a set of weighted features, identifies statistically significant hot spots and cold spots using the Getis-Ord Gi* statistic.
    """

    @property
    def description(self) -> str:
        return """

        HotSpots_stats(Input_Feature_Class, Input_Field, Output_Feature_Class, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, {Distance_Band_or_Threshold_Distance}, {Self_Potential_Field}, {Weights_Matrix_File}, {Apply_False_Discovery_Rate__FDR__Correction}, {number_of_neighbors})

        Given a set of weighted features, identifies statistically significant
        hot spots and cold spots using the Getis-Ord Gi* statistic.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which hot spot analysis will be performed.
      Input_Field (Field):
          The numeric field (number of victims, crime rate, test scores, and so
          on) to be evaluated.
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features will be
          defined.INVERSE_DISTANCE-Nearby neighboring features will have a
          larger
          influence on the computations for a target feature than features that
          are far away.INVERSE_DISTANCE_SQUARED-Same as INVERSE_DISTANCE except
          that the
          slope is sharper, so influence will drop off more quickly, and only a
          target feature's closest neighbors will exert substantial influence on
          computations for that feature.FIXED_DISTANCE_BAND-Each feature will be
          analyzed within the context
          of neighboring features. Neighboring features inside the specified
          critical distance (Distance_Band_or_Threshold) will receive a weight
          of one and exert influence on computations for the target feature.
          Neighboring features outside the critical distance will receive a
          weight of zero and have no influence on a target feature's
          computations.ZONE_OF_INDIFFERENCE-Features within the specified
          critical distance
          (Distance_Band_or_Threshold) of a target feature will receive a weight
          of one and influence computations for that feature. Once the critical
          distance is exceeded, weights (and the influence a neighboring feature
          has on target feature computations) will diminish with
          distance.K_NEAREST_NEIGHBORS-The closest k features will be included
          in the
          analysis; k is a specified numeric
          parameter.CONTIGUITY_EDGES_ONLY-Only neighboring polygon features that
          share a
          boundary or overlap will influence computations for the target polygon
          feature.CONTIGUITY_EDGES_CORNERS-Polygon features that share a
          boundary, share
          a node, or overlap will influence computations for the target polygon
          feature.GET_SPATIAL_WEIGHTS_FROM_FILE-Spatial relationships will be
          defined by
          a specified spatial weights file. The path to the spatial weights file
          is specified by the Weights_Matrix_File parameter.
      Distance_Method (String):
          Specifies how distances will be calculated from each feature to
          neighboring features.EUCLIDEAN_DISTANCE-The straight-line distance
          between two points (as
          the crow flies)MANHATTAN_DISTANCE-The distance between two points
          measured along axes
          at right angles (city block), calculated by summing the (absolute)
          difference between the x- and y-coordinates
      Standardization (String):
          Row standardization has no impact on this tool: results from Hot Spot
          Analysis (the Getis-Ord Gi* statistic) would be identical with or
          without row standardization. The parameter is disabled; it remains as
          a tool parameter only to support backward compatibility.NONE-No
          standardization of spatial weights is applied.ROW-No
          standardization of spatial weights is applied.
      Distance_Band_or_Threshold_Distance {Double}:
          Specifies a cutoff distance for the inverse distance and fixed
          distance options. Features outside the specified cutoff for a target
          feature will be ignored in analyses for that feature. However, for
          ZONE_OF_INDIFFERENCE, the influence of features outside the given
          distance will be reduced with distance, while those inside the
          distance threshold will be equally considered. The distance value
          entered should match that of the output coordinate system.For the
          inverse distance conceptualizations of spatial relationships,
          a value of 0 indicates that no threshold distance will be applied;
          when this parameter is left blank, a default threshold value will be
          computed and applied. The default value is the Euclidean distance,
          which ensures that every feature has at least one neighbor.This
          parameter has no effect when polygon contiguity
          (CONTIGUITY_EDGES_ONLY or CONTIGUITY_EDGES_CORNERS) or
          GET_SPATIAL_WEIGHTS_FROM_FILE spatial conceptualization is selected.
      Self_Potential_Field {Field}:
          The field representing self potential: the distance or weight between
          a feature and itself.
      Weights_Matrix_File {File}:
          The path to a file containing weights that define spatial, and
          potentially temporal, relationships among features.
      Apply_False_Discovery_Rate__FDR__Correction {Boolean}:
          APPLY_FDR-Statistical significance will be based on the FDR
          correction.NO_FDR-Statistical significance will not be based on the
          FDR
          correction; it will be based on the p-value and z-score fields. This
          is the default.
      number_of_neighbors {Long}:
          An integer specifying the number of neighbors to include in the
          analysis.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output feature class to receive the z-score and p-value results.

        """