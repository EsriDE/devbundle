# Generated documentation for module arcpy.stats


class MultivariateClustering(object):
    """
    Finds natural clusters of features based solely on feature attribute values.
    """

    @property
    def description(self) -> str:
        return """

        MultivariateClustering_stats(in_features, output_features, analysis_fields;analysis_fields..., {clustering_method}, {initialization_method}, {initialization_field}, {number_of_clusters}, {output_table})

        Finds natural clusters of features based solely on feature attribute
        values.

     INPUTS:
      in_features (Feature Layer):
          The feature class or feature layer for which clusters will be created.
      analysis_fields (Field):
          A list of fields that will be used to distinguish one cluster from
          another.
      clustering_method {String}:
          Specifies the clustering algorithm that will be used.The K_MEANS and
          K_MEDOIDS options generally produce similar results.
          However, K_MEDOIDS is more robust to noise and outliers in the
          in_features parameter value. K_MEANS is generally faster than
          K_MEDOIDS and is recommended for large data sets.K_MEANS-The
          in_features parameter value will be clustered using the K
          means algorithm. This is the default.K_MEDOIDS-The in_features
          parameter value will be clustered using the
          K medoids algorithm.
      initialization_method {String}:
          Specifies how initial seeds to grow clusters are obtained. If you
          indicate you want three clusters, for example, the analysis will begin
          with three seeds.OPTIMIZED_SEED_LOCATIONS-Seed features will be
          selected to optimize
          analysis results and performance. This is the
          default.USER_DEFINED_SEED_LOCATIONS-Nonzero entries in the
          initialization_field parameter value will be used as starting points
          to grow clusters.RANDOM_SEED_LOCATIONS-Initial seed features will be
          randomly selected.
      initialization_field {Field}:
          The numeric field identifying seed features. Features with a value of
          1 for this field will be used to grow clusters. Each seed results in a
          cluster, so at least two seed features must be provided.
      number_of_clusters {Long}:
          The number of clusters that will be created. If you leave this
          parameter empty, the tool will evaluate the optimal number of clusters
          by computing a pseudo F-statistic for clustering solutions with 2
          through 30 clusters.This parameter is disabled if the seed locations
          were provided in an
          initialization field.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class that will be created containing all features,
          the analysis fields specified, and a field indicating to which cluster
          each feature belongs.
      output_table {Table}:
          The table containing the pseudo F-statistic for clustering
          solutions 2 through 30, calculated to evaluate the optimal number of
          clusters. The chart created from this table can be accessed in the
          stand-alone tables section of thepane. Contents

        """