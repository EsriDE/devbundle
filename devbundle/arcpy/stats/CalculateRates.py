# Generated documentation for module arcpy.stats


class CalculateRates(object):
    """
    Calculates crude or smoothed rates. The global empirical Bayes rate method smooths the rates toward a global reference rate. The local empirical Bayes, locally weighted average, and locally weighted median rate methods use local neighbors to spatially smooth rates.
    """

    @property
    def description(self) -> str:
        return """

        CalculateRates_stats(in_table, rate_fields;rate_fields..., {append_to_input}, {out_table}, {rate_method}, {probability_distribution}, {neighborhood_type}, {distance_band}, {number_of_neighbors}, {weights_matrix_file}, {local_weighting_scheme}, {kernel_bandwidth}, {rate_multiplier})

        Calculates crude or smoothed rates. The global empirical Bayes rate
        method smooths the rates toward a global reference rate. The local
        empirical Bayes, locally weighted average, and locally weighted median
        rate methods use local neighbors to spatially smooth rates.

     INPUTS:
      in_table (Table View):
          The table or features containing count fields and population fields to
          calculate rates.
      rate_fields (Value Table):
          The count and population fields that will be used to calculate rates.
      append_to_input {Boolean}:
          Specifies whether fields will be appended to the input dataset or
          saved to an output table or feature class.APPEND-Fields will be
          appended to the input features. This modifies
          the input data.NO_APPEND-An output table or feature class containing
          the fields will
          be created. This is the default.
      rate_method {String}:
          Specifies the method that will be used to calculate
          rates.CRUDE_RATE-The rates will be calculated by dividing the count
          field
          values by the population field values. This is the
          default.GLOBAL_EMPIRICAL_BAYES-The rates will be the weighted average
          of the
          crude rate and the global average rate. The weight will depend on the
          feature's population size.LOCAL_EMPIRICAL_BAYES-The rates will be the
          weighted average of the
          focal feature's crude rate and the weighted average rate of its
          neighborhood.LOCALLY_WEIGHTED_AVERAGE-The rates will be the spatially
          weighted
          average rate of each feature and its
          neighborhood.LOCALLY_WEIGHTED_MEDIAN-The rates will be the spatially
          weighted
          median rate of each feature and its neighborhood.
      probability_distribution {String}:
          Specifies the probability distribution of the count field.POISSON-The
          count field is assumed to follow a Poisson distribution.
          This is the default.BINOMIAL-The count field is assumed to follow a
          binomial distribution.
      neighborhood_type {String}:
          Specifies the method that will be used to identify the neighbors of
          each feature.DISTANCE_BAND-A threshold distance is applied to identify
          neighbors.
          Every feature that is within the threshold distance of a focal feature
          is considered a neighbor. If the input contains point or line
          features, this is the default.CONTIGUITY_EDGES_ONLY-Polygon features
          that share an edge or overlap
          a feature become neighbors of that feature.CONTIGUITY_EDGES_CORNERS-
          Features that overlap, share an edge, or
          share a vertex with a feature are neighbors of that feature. If the
          input contains polygon features, this is the
          default.K_NEAREST_NEIGHBORS-The same number of neighbors, k, is
          assigned to
          every feature. The k nearest features to a feature become its
          neighbors.DELAUNAY_TRIANGULATION-A nonoverlapping mesh of triangles is
          created
          from feature centroids. Each feature is a triangle node and nodes that
          share edges are considered neighbors.GET_SPATIAL_WEIGHTS_FROM_FILE-The
          spatial relationships between
          features is defined in a spatial weights matrix (.swm) file.
      distance_band {Linear Unit}:
          The distance from each feature that will be used to search for
          neighbors. All features within this distance will be included as
          neighbors.
      number_of_neighbors {Long}:
          The number of neighbors that will be included in a feature's
          neighborhood.
      weights_matrix_file {File}:
          The path and file name of the spatial weights matrix file that defines
          the spatial relationships among features.
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
      rate_multiplier {Long}:
          A constant value that will be multiplied by the rates. This parameter
          can be used to scale the rates or to report the rates per specific
          unit of population. For example, when the value is set to 10,000, the
          rates will be reported as a number per 10,000 people.

     OUTPUTS:
      out_table {Feature Class / Table}:
          The output table or feature class containing the rates and additional
          fields to help evaluate the rates.

        """