# Generated documentation for module arcpy.stats


class SpatialAutocorrelation(object):
    """
    Measures spatial autocorrelation based on feature locations and attribute values using the Global Moran's I statistic.
    """

    @property
    def description(self) -> str:
        return """

        SpatialAutocorrelation_stats(Input_Feature_Class, Input_Field, {Generate_Report}, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, {Distance_Band_or_Threshold_Distance}, {Weights_Matrix_File}, {number_of_neighbors})

        Measures spatial autocorrelation based on feature locations and
        attribute values using the Global Moran's I statistic.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which spatial autocorrelation will be
          calculated.
      Input_Field (Field):
          The numeric field used in assessing spatial autocorrelation.
      Generate_Report {Boolean}:
          Specifies whether a graphical summary of result will be created as an
          .html file.NO_REPORT-No graphical summary will be created. This is the
          default.GENERATE_REPORT-A graphical summary will be created.
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features are
          defined.INVERSE_DISTANCE-Nearby neighboring features have a larger
          influence
          on the computations for a target feature than features that are far
          away.INVERSE_DISTANCE_SQUARED-This is the same as INVERSE_DISTANCE
          except
          that the slope is sharper, so influence drops off more quickly, and
          only a target feature's closest neighbors will exert substantial
          influence on computations for that feature.FIXED_DISTANCE_BAND-Each
          feature is analyzed within the context of
          neighboring features. Neighboring features inside the specified
          critical distance (Distance_Band_or_Threshold) receive a weight of one
          and exert influence on computations for the target feature.
          Neighboring features outside the critical distance receive a weight of
          zero and have no influence on a target feature's
          computations.ZONE_OF_INDIFFERENCE-Features within the specified
          critical distance
          (Distance_Band_or_Threshold) of a target feature receive a weight of
          one and influence computations for that feature. Once the critical
          distance is exceeded, weights (and the influence a neighboring feature
          has on target feature computations) diminish with
          distance.K_NEAREST_NEIGHBORS-The closest k features are included in
          the
          analysis. The number of neighbors (k) to include in the analysis is
          specified by the number_of_neighbors
          parameter.CONTIGUITY_EDGES_ONLY-Only neighboring polygon features that
          share a
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
          the crow flies) will be used.MANHATTAN_DISTANCE-The distance between
          two points measured along axes
          at right angles (city block) will be used. This is calculated by
          summing the (absolute) difference between the x- and y-coordinates
      Standardization (String):
          Specifies whether standardization of spatial weights will be applied.
          Row standardization is recommended whenever the distribution of your
          features is potentially biased due to sampling design or an imposed
          aggregation scheme.NONE-No standardization of spatial weights is
          applied.ROW-Spatial
          weights are standardized; each weight is divided by its
          row sum (the sum of the weights of all neighboring features). This is
          the default.
      Distance_Band_or_Threshold_Distance {Double}:
          The cutoff distance for the various inverse distance and fixed
          distance options. Features outside the specified cutoff for a target
          feature are ignored in analyses for that feature. However, for
          ZONE_OF_INDIFFERENCE, the influence of features outside the given
          distance is reduced with distance, while those inside the distance
          threshold are equally considered. The distance value entered should
          match that of the output coordinate system.For the inverse distance
          conceptualizations of spatial relationships,
          a value of 0 indicates that no threshold distance is applied; when
          this parameter is left blank, a default threshold value is computed
          and applied. This default value is the Euclidean distance, which
          ensures that every feature has at least one neighbor.This parameter
          has no effect when polygon contiguity
          (CONTIGUITY_EDGES_ONLY or CONTIGUITY_EDGES_CORNERS) or
          GET_SPATIAL_WEIGHTS_FROM_FILE spatial conceptualization is selected.
      Weights_Matrix_File {File}:
          The path to a file containing weights that define spatial, and
          potentially temporal, relationships among features.
      number_of_neighbors {Long}:
          An integer specifying the number of neighbors to include in the
          analysis.

        """