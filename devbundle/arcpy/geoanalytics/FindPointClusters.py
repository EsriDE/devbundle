# Generated documentation for module arcpy.geoanalytics


class FindPointClusters(object):
    """
    Finds clusters of point features in surrounding noise based on their spatial or spatiotemporal distribution.
    """

    @property
    def description(self) -> str:
        return """

        FindPointClusters_geoanalytics(input_points, output_name, minimum_points, {search_distance}, {data_store}, {clustering_method}, {use_time}, {search_duration})

        Finds clusters of point features in surrounding noise based on their
        spatial or spatiotemporal distribution.

     INPUTS:
      input_points (Feature Set):
          The point feature class containing the point clusters.
      output_name (String):
          The name of the output feature service.
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
          The maximum distance to be considered. Thespecified must be
          found within this distance for cluster
          membership. Individual clusters will be separated by at least this
          distance. If a feature is located farther than this distance from the
          next closest feature in the cluster, it will not be included in the
          cluster. Minimum Features per Cluster
      data_store {String}:
          Specifies the ArcGIS Data Store where the output will be saved. The
          default is SPATIOTEMPORAL_DATA_STORE. All results stored in a
          spatiotemporal big data store will be stored in WGS84. Results stored
          in a relational data store will maintain their coordinate
          system.SPATIOTEMPORAL_DATA_STORE-Output will be stored in a
          spatiotemporal
          big data store. This is the default.RELATIONAL_DATA_STORE-Output will
          be stored in a relational data
          store.
      clustering_method {String}:
          Specifies the method that will be used to define clusters.DBSCAN-Uses
          a specified distance to separate dense clusters from
          sparser noise. DBSCAN is the fastest of the clustering methods but is
          only appropriate if there is a clear distance that works well to
          define all clusters that may be present. This results in clusters that
          have similar densities. This is the default.HDBSCAN-Uses varying
          distances to separate clusters of varying
          densities from sparser noise. HDBSCAN is the most data driven of the
          clustering methods and requires the least user input.
      use_time {Boolean}:
          Specifies whether or not time will be used to discover clusters with
          DBSCAN.TIME-Spatiotemporal clusters will be found using both a search
          distance and a search duration.NO_TIME-Spatial clusters will be found
          using a search distance and
          time will be ignored. This is the default.
      search_duration {Time Unit}:
          When searching for cluster members, the specified minimum number of
          points must be found within this time duration to form a cluster.

        """