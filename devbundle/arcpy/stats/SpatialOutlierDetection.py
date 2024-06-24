# Generated documentation for module arcpy.stats


class SpatialOutlierDetection(object):
    """
    Identifies global or local spatial outliers in point features.
    """

    @property
    def description(self) -> str:
        return """

        SpatialOutlierDetection_stats(in_features, output_features, {n_neighbors}, {percent_outlier}, {output_raster}, {outlier_type}, {sensitivity}, {keep_type})

        Identifies global or local spatial outliers in point features.

     INPUTS:
      in_features (Feature Layer):
          The point features that will be used to build the spatial outlier
          detection model. Each point will be classified as an outlier or inlier
          based on its local outlier factor.
      n_neighbors {Long}:
          The number of neighbors that will be used to detect spatial outliers
          for each input point.For local outlier detection, the value must be at
          least 2, and all
          features within the neighborhood will be used as neighbors. If no
          value is specified, a value is estimated at run time and is displayed
          as a geoprocessing message.For global outlier detection, only the
          farthest neighbor in the
          neighborhood will be used, and the default is 1 (the closest
          neighbor). For example, a value of 3 indicates that global outliers
          are detected using distances to the third nearest neighbor of each
          point.
      percent_outlier {Double}:
          The percent of locations that will be identified as spatial outliers
          by defining the threshold of the local outlier factor. If no value is
          specified, a value is estimated at run time and is displayed as a
          geoprocessing message. A maximum of 50 percent of the features can be
          identified as spatial outliers.
      outlier_type {String}:
          Specifies the type of outlier that will be detected. A global outlier
          is a point that is far away from all other points in the feature
          class. A local outlier is a point that is farther away from its
          neighbors than would be expected by the density of points in the
          surrounding area.GLOBAL-Global outliers of input points will be
          detected. This is the
          default.LOCAL-Local outliers of input points will be detected.
      sensitivity {String}:
          Specifies the sensitivity level that will be used to detect global
          outliers. The higher the sensitivity, the more points that will be
          detected as outliers.The sensitivity value will determine the
          threshold, and any point with
          a neighbor distance larger than this threshold will be identified as a
          global outlier. The thresholds are determined using the box plot rule,
          in which the threshold for high sensitivity is one interquartile range
          above the third quartile. For medium sensitivity, the threshold is 1.5
          interquartile ranges above the third quartile. For low sensitivity,
          the threshold is two interquartile ranges above the third
          quartile.LOW-Outliers will be detected using low sensitivity. This
          option will
          detect the fewest outliers.MEDIUM-Outliers will be detected using
          moderate sensitivity. This is
          the default.HIGH-Outliers will be detected using high sensitivity.
          This option
          will detect the most outliers.
      keep_type {Boolean}:
          Specifies whether the output features will contain all input features
          or only features identified as spatial outliers.KEEP_OUTLIER-The
          output features will only contain features identified
          as spatial outliers.KEEP_ALL-The output features will contain all
          input features. This is
          the default.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class containing the local outlier factor for each
          input feature as well as an indicator of whether the point is a
          spatial outlier.
      output_raster {Raster Dataset}:
          The output raster containing the local outlier factors at each cell,
          which is calculated based on the spatial distribution of the input
          features.This parameter is only available with a Desktop Advanced
          license.

        """