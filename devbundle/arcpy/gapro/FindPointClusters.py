# Generated documentation for module arcpy.gapro


class FindPointClusters(object):
    """
    Finds clusters of point features in surrounding noise based on their spatial or spatiotemporal distribution.
    """

    @property
    def description(self) -> str:
        return """

        FindPointClusters_gapro(input_points, out_feature_class, clustering_method, minimum_points, {search_distance}, {use_time}, {search_duration})

        Finds clusters of point features in surrounding noise based on their
        spatial or spatiotemporal distribution.

     INPUTS:
      input_points (Feature Layer):
          The point feature class containing the point clusters.
      clustering_method (String):
          Specifies the method that will be used to define clusters.DBSCAN-A
          defined distance will be used to separate dense clusters from
          sparser noise. DBSCAN is the fastest of the clustering methods but is
          only appropriate when there is a clear distance that works well to
          define all clusters that may be present. This results in clusters that
          have similar densities. This is the default.HDBSCAN-Varying distances
          will be used to separate clusters of
          varying densities from sparser noise. HDBSCAN is the most data-driven
          of the clustering methods and requires the least user input.
      minimum_points (Long):
          This parameter is used differently depending on the clustering method
          chosen as follows:          Defined distance (DBSCAN)-Specifies the
          number of features
          that must be found within a certain distance of a point for that point
          to start to form a cluster. The distance is defined using
          theparameter. Search DistanceSelf-adjusting
          (HDBSCAN)-Specifies the number of features neighboring
          each point (including the point) that will be considered when
          estimating density. This number is also the minimum cluster size
          allowed when extracting clusters.
      search_distance {Linear Unit}:
          The maximum distance that will be considered. Thevalue
          specified must be found within this distance for
          cluster membership. Individual clusters will be separated by at least
          this distance. If a feature is located farther than this distance from
          the next closest feature in the cluster, it will not be included in
          the cluster. Minimum Features per Cluster
      use_time {Boolean}:
          Specifies whether or not time will be used to discover clusters with
          DBSCAN.TIME-Spatiotemporal clusters will be found using both a search
          distance and a search duration.NO_TIME-Spatial clusters will be found
          using a search distance and
          time will be ignored. This is the default.
      search_duration {Time Unit}:
          When searching for cluster members, the specified minimum number of
          points must be found within this time duration to form a cluster.

     OUTPUTS:
      out_feature_class (Feature Class):
          A new feature class with the resulting point clusters.

        """