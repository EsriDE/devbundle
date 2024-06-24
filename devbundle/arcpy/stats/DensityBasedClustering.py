# Generated documentation for module arcpy.stats


class DensityBasedClustering(object):
    """
    Finds clusters of point features within surrounding noise based on their spatial distribution. Time can also be incorporated to find space-time clusters.
    """

    @property
    def description(self) -> str:
        return """

        DensityBasedClustering_stats(in_features, output_features, cluster_method, min_features_cluster, {search_distance}, {cluster_sensitivity}, {time_field}, {search_time_interval})

        Finds clusters of point features within surrounding noise based on
        their spatial distribution. Time can also be incorporated to find
        space-time clusters.

     INPUTS:
      in_features (Feature Layer):
          The point features for which density-based clustering will be
          performed.
      cluster_method (String):
          Specifies the method that will be used to define clusters.DBSCAN-A
          specified distance will be used to separate dense clusters
          from sparser noise. DBSCAN is the fastest of the clustering methods
          but is only appropriate if there is a clear distance to use that works
          well to define all clusters that may be present. This results in
          clusters that have similar densities.HDBSCAN-Varying distances will
          be used to separate clusters of
          varying densities from sparser noise. HDBSCAN is the most data-driven
          of the clustering methods and requires the least user input.OPTICS-The
          distance between neighbors and a reachability plot will be
          used to separate clusters of varying densities from noise. OPTICS
          offers the most flexibility in fine-tuning the clusters that are
          detected, though it is computationally intensive, particularly with a
          large search distance.
      min_features_cluster (Long):
          The minimum number of points that will be considered a cluster. Any
          cluster with fewer points than the number provided will be considered
          noise.
      search_distance {Linear Unit}:
          The maximum distance that will be considered.For the cluster_method
          parameter's DBSCAN option, the
          min_features_cluster parameter value must be found within this
          distance for cluster membership. Individual clusters will be separated
          by at least this distance. If a point is located farther than this
          distance from the next closest point in the cluster, it will not be
          included in the cluster.For the cluster_method parameter's OPTICS
          option, this parameter is
          optional and is used as the maximum search distance when creating the
          reachability plot. For OPTICS, the reachability plot, combined with
          the cluster_sensitivity parameter value, determines cluster
          membership. If no distance is specified, the tool will search all
          distances, which will increase processing time.If left blank, the
          default distance used will be the highest core
          distance found in the dataset, excluding those core distances in the
          top 1 percent (he most extreme core distances). If the time_field
          parameter value is provided, a search distance must be provided and
          does not include a default value.
      cluster_sensitivity {Long}:
          An integer between 0 and 100 that determines the compactness of
          clusters. A number close to 100 will result in a higher number of
          dense clusters. A number close to 0 will result in fewer, less compact
          clusters. If left blank, the tool will find a sensitivity value using
          the Kullback-Leibler divergence that finds the value in which adding
          more clusters does not add additional information.
      time_field {Field}:
          The field containing the time stamp for each record in the dataset.
          This field must be of type Date. If provided, the tool will find
          clusters of points that are close to each other in space and time. The
          search_time_interval parameter value must be provided to determine
          whether a point is close enough in time to a cluster to be included in
          the cluster.
      search_time_interval {Time Unit}:
          The time interval that will be used to determine whether points form a
          space-time cluster. The search time interval spans before and after
          the time of each point; for example, an interval of 3 days around a
          point will include all points starting 3 days before and ending 3 days
          after the time of the point.For the cluster_method parameter's DBSCAN
          option, the
          min_features_cluster value specified must be found within the search
          distance and the search time interval to be included in a cluster.For
          the cluster_method parameter's OPTICS option, all points outside
          of the search time interval will be excluded when calculating core
          distances, neighbor-distances, and reachability distances.The search
          time interval does not control the overall time span of the
          resulting space-time clusters. The time span of points within a
          cluster can be larger than the search time interval as long as each
          point has neighbors within the cluster that are within the search time
          interval.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class that will receive the cluster results.

        """