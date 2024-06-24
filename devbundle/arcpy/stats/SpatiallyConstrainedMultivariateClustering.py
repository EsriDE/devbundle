# Generated documentation for module arcpy.stats


class SpatiallyConstrainedMultivariateClustering(object):
    """
    Finds spatially contiguous clusters of features based on a set of feature attribute values and optional cluster size limits.
    """

    @property
    def description(self) -> str:
        return """

        SpatiallyConstrainedMultivariateClustering_stats(in_features, output_features, analysis_fields;analysis_fields..., {size_constraints}, {constraint_field}, {min_constraint}, {max_constraint}, {number_of_clusters}, {spatial_constraints}, {weights_matrix_file}, {number_of_permutations}, {output_table})

        Finds spatially contiguous clusters of features based on a set of
        feature attribute values and optional cluster size limits.

     INPUTS:
      in_features (Feature Layer):
          The feature class or feature layer for which you want to create
          clusters.
      analysis_fields (Field):
          A list of fields that will be used to distinguish one cluster from
          another.
      size_constraints {String}:
          Specifies cluster size based on number of features per group or a
          target attribute value per group.NONE-No cluster size constraints will
          be used. This is the
          default.NUM_FEATURES-A minimum and maximum number of features per
          group will
          be used.ATTRIBUTE_VALUE-A minimum and maximum attribute value per
          group will
          be used.
      constraint_field {Field}:
          The attribute value to be summed per cluster.
      min_constraint {Double}:
          The minimum number of features per cluster or the minimum attribute
          value per cluster. This must be a positive value.
      max_constraint {Double}:
          The maximum number of features per cluster or the maximum attribute
          value per cluster. If a maximum constraint is set, the
          number_of_clusters parameter is disabled. This must be a positive
          value.
      number_of_clusters {Long}:
          The number of clusters to create. If this parameter is empty, the tool
          will evaluate the optimal number of clusters by computing a pseudo
          F-statistic value for clustering solutions with 2 through 30
          clusters.This parameter will be disabled if a maximum number of
          features or
          maximum attribute value has been set.
      spatial_constraints {String}:
          Specifies how spatial relationships among features will be
          defined.CONTIGUITY_EDGES_ONLY-Clusters will contain contiguous polygon
          features. Only polygons that share an edge can be part of the same
          cluster.CONTIGUITY_EDGES_CORNERS-Clusters will contain contiguous
          polygon
          features. Only polygons that share an edge or a vertex can be part of
          the same cluster. This is the default for polygon
          features.TRIMMED_DELAUNAY_TRIANGULATION-Features in the same cluster
          will have
          at least one natural neighbor in common with another feature in the
          cluster. Natural neighbor relationships are based on a trimmed
          Delaunay triangulation. Conceptually, Delaunay triangulation creates a
          nonoverlapping mesh of triangles from feature centroids. Each feature
          is a triangle node, and nodes that share edges are considered
          neighbors. These triangles are then clipped to a convex hull to ensure
          that features cannot be neighbors with any features outside the convex
          hull. This is the default for point
          features.GET_SPATIAL_WEIGHTS_FROM_FILE-Spatial, and optionally
          temporal,
          relationships are defined by a specified spatial weights file (.swm).
          Create the spatial weights matrix using the Generate Spatial Weights
          Matrix or Generate Network Spatial Weights tool. The path to the
          spatial weights file is specified by the Weights_Matrix_File
          parameter.
      weights_matrix_file {File}:
          The path to a file containing spatial weights that define spatial, and
          potentially temporal, relationships among features.
      number_of_permutations {Long}:
          The number of random permutations for the calculation of membership
          stability scores. If 0 (zero) is chosen, probabilities will not be
          calculated. Calculating these probabilities uses permutations of
          random spanning trees and evidence accumulation. This
          calculation can take a significant time to run for larger
          datasets. It is recommended that you iterate and find the optimal
          number of clusters for your analysis first; then calculate
          probabilities for your analysis in a subsequent run. Setting
          theEnvironment setting to 50 may improve the run time of the tool.
          Parallel Processing Factor

     OUTPUTS:
      output_features (Feature Class):
          The new output feature class created containing all features, the
          analysis fields specified, and a field indicating to which cluster
          each feature belongs.
      output_table {Table}:
          The table created containing the results of the F-statistic
          values calculated to evaluate the optimal number of clusters. The
          chart created from this table can be accessed in thepane under the
          output feature layer. Contents

        """