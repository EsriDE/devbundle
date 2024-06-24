# Generated documentation for module arcpy.ga


class GenerateSubsetPolygons(object):
    """
    Generates nonoverlapping subset polygon features from a set of input points. The goal is to divide the points into compact, nonoverlapping subsets, and create polygon regions around each subset of points. The minimum and maximum number of points in each subset can be controlled.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSubsetPolygons_ga(in_point_features, out_feature_class, {min_points_per_subset}, {max_points_per_subset}, {coincident_points})

        Generates nonoverlapping subset polygon features from a set of input
        points. The goal is to divide the points into compact, nonoverlapping
        subsets, and create polygon regions around each subset of points. The
        minimum and maximum number of points in each subset can be controlled.

     INPUTS:
      in_point_features (Feature Layer):
          The points that will be grouped into subsets.
      min_points_per_subset {Long}:
          The minimum number of points that can be grouped into a subset. All
          subset polygons will contain at least this many points.
      max_points_per_subset {Long}:
          The maximum number of points that can be grouped into a subset.Each
          subset will always contain fewer than two times the
          min_points_per_subset regardless of the maximum number provided. This
          is because if a subset contains at least twice the minimum number of
          points, it will always be subdivided into two or more new subsets.
      coincident_points {Boolean}:
          Specifies whether coincident points (points that are at the same
          location) are treated like a single point or as multiple individual
          points. If you intend to use the subset polygons asin EBK
          Regression
          Prediction, you should maintain consistency between this parameter and
          your choice for the Coincident points environment in EBK Regression
          Prediction. Subset polygon featuresIf COINCIDENT_ALL is chosen,
          your Out_feature_class polygons may
          overlap.COINCIDENT_SINGLE-Coincident points will be treated as a
          single point
          in the subsetting. This is the default.COINCIDENT_ALL-Coincident
          points will be treated as multiple
          individual points in the subsetting.

     OUTPUTS:
      out_feature_class (Feature Class):
          The polygons defining the region of each subset. All points
          within a single polygon feature are considered part of the same
          subset. The polygon feature class will contain a field namedthat will
          store the number of points contained in each polygon subset.
          PointCount

        """