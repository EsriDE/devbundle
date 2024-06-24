# Generated documentation for module arcpy.stats


class NeighborhoodSummaryStatistics(object):
    """
    Calculates summary statistics of one or more numeric fields using local neighborhoods around each feature. The local statistics include mean (average), median, standard deviation, interquartile range, skewness, and quantile imbalance. All statistics can be geographically weighted using kernels to give more influence to neighbors closer to the focal feature. Various neighborhood types can be used, including distance band, number of neighbors, polygon contiguity, Delaunay triangulation, and spatial weights matrix files (.swm). Summary statistics are also calculated for the distances to the neighbors of each feature.
    """

    @property
    def description(self) -> str:
        return """

        NeighborhoodSummaryStatistics_stats(in_features, output_features, {analysis_fields;analysis_fields...}, {local_summary_statistic}, {include_focal_feature}, {ignore_nulls}, {neighborhood_type}, {distance_band}, {number_of_neighbors}, {weights_matrix_file}, {local_weighting_scheme}, {kernel_bandwidth})

        Calculates summary statistics of one or more numeric fields using
        local neighborhoods around each feature. The local statistics include
        mean (average), median, standard deviation, interquartile range,
        skewness, and quantile imbalance. All statistics can be geographically
        weighted using kernels to give more influence to neighbors closer to
        the focal feature. Various neighborhood types can be used, including
        distance band, number of neighbors, polygon contiguity, Delaunay
        triangulation, and spatial weights matrix files (.swm). Summary
        statistics are also calculated for the distances to the neighbors of
        each feature.

     INPUTS:
      in_features (Feature Layer):
          The point or polygon features that will be used to calculate the local
          statistics.
      analysis_fields {Field}:
          One or more fields for which local statistics will be calculated. If
          no analysis fields are provided, only local statistics based on
          distances to neighbors will be calculated.
      local_summary_statistic {String}:
          Specifies the local summary statistic that will be calculated for each
          analysis field.ALL-All local statistics will be calculated. This is
          the
          default.MEAN-The local mean (average) will be calculated.MEDIAN-The
          local median will be calculated.STD_DEV-The local standard deviation
          will be calculated.IQR-The local interquartile range will be
          calculated.SKEWNESS-The local skewness will be
          calculated.QUANTILE_IMBALANCE-The local quantile imbalance will be
          calculated.
      include_focal_feature {Boolean}:
          Specifies whether the focal feature will be included when calculating
          local statistics for each feature.INCLUDE_FOCAL-The focal feature and
          all of its neighbors will be
          included when calculating local statistics. This is the
          default.EXCLUDE_FOCAL-The focal feature will not be included when
          calculating
          local statistics. Only neighbors of the feature will be included.
      ignore_nulls {Boolean}:
          Specifies whether null values in the analysis fields will be included
          or ignored in the calculations.IGNORE_NULLS-Null values will be
          ignored in the local
          calculations.INCLUDE_NULLS-Null values will be included in the local
          calculations.
      neighborhood_type {String}:
          Specifies how neighbors will be chosen for each input feature.
          To calculate local statistics, neighboring features must be identified
          for each input feature, and these neighbors are used to calculate the
          local statistics for each feature. For point features, the default is.
          For polygon features, the default is. Delaunay
          triangulationContiguity edges corners        Theoption is only
          available with a Desktop Advanced license.
          Delaunay triangulationDISTANCE_BAND-Features within a specified
          critical distance of each
          feature will be included as neighbors.NUMBER_OF_NEIGHBORS-The closest
          features will be included as
          neighbors.CONTIGUITY_EDGES_ONLY-Polygon features that share an edge
          will be
          included as neighbors.CONTIGUITY_EDGES_CORNERS-Polygon features that
          share an edge or a
          corner will be included as neighbors. This is the default for polygon
          features.DELAUNAY_TRIANGULATION-Features whose Delaunay triangulation
          share an
          edge will be included as neighbors. This is the default for point
          features.GET_SPATIAL_WEIGHTS_FROM_FILE-Neighbors and weights will be
          defined
          by a specified spatial weights file.
      distance_band {Linear Unit}:
          All features within this distance will be included as neighbors. If no
          value is provided, one will be estimated during processing and
          included as a geoprocessing message. If the specified distance results
          in more than 1,000 neighbors, only the closest 1,000 features will be
          included as neighbors.
      number_of_neighbors {Long}:
          The number of neighbors that will be included for each local
          calculation. The number does not include the focal feature. If the
          focal feature is included in calculations, one additional neighbor
          will be used. The default is 8.
      weights_matrix_file {File}:
          The path and file name of the spatial weights matrix file that defines
          spatial, and potentially temporal, relationships among features.
      local_weighting_scheme {String}:
          Specifies the weighting scheme that will be applied to neighbors when
          calculating local statistics.UNWEIGHTED-Neighbors will not be
          weighted. This is the
          default.BISQUARE-Neighbors will be weighted using a bisquare kernel
          scheme.GAUSSIAN-Neighbors will be weighted using a Gaussian kernel
          scheme.
      kernel_bandwidth {Linear Unit}:
          The bandwidth of the bisquare or Gaussian local weighting schemes. If
          no value is provided, one will be estimated during processing and
          included as a geoprocessing message.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class containing the local statistics as fields.
          Each statistic of each analysis field will be stored as an individual
          field.

        """