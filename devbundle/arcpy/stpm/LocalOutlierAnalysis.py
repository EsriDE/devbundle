# Generated documentation for module arcpy.stpm


class LocalOutlierAnalysis(object):
    """
    Identifies statistically significant clusters and outliers in the context of both space and time. This tool is a space-time implementation of the Anselin Local Moran's I statistic.
    """

    @property
    def description(self) -> str:
        return """

        LocalOutlierAnalysis_stpm(in_cube, analysis_variable, output_features, {neighborhood_distance}, {neighborhood_time_step}, {number_of_permutations}, {polygon_mask}, {conceptualization_of_spatial_relationships}, {number_of_neighbors}, {define_global_window})

        Identifies statistically significant clusters and outliers in the
        context of both space and time. This tool is a space-time
        implementation of the Anselin Local Moran's I statistic.

     INPUTS:
      in_cube (File):
          The space-time cube containing the variable to be analyzed. Space-time
          cubes have a .nc file extension and are created using various tools in
          the Space Time Pattern Mining toolbox.
      analysis_variable (String):
          The numeric variable in the netCDF file you want to analyze.
      neighborhood_distance {Linear Unit}:
          The spatial extent of the analysis neighborhood. This value determines
          which features are analyzed together in order to assess local space-
          time clustering.
      neighborhood_time_step {Long}:
          The number of time-step intervals to include in the analysis
          neighborhood. This value determines which features are analyzed
          together in order to assess local space-time clustering.
      number_of_permutations {Long}:
          The number of random permutations for the calculation of pseudo
          p-values. The default number of permutations is 499. If you choose 0
          permutations, the standard p-value is calculated.0-Permutations are
          not used and a standard p-value is
          calculated.99-With 99 permutations, the smallest possible pseudo
          p-value is 0.01
          and all other pseudo p-values will be even multiples of this
          value.199-With 199 permutations, the smallest possible pseudo p-value
          is
          0.005 and all other pseudo p-values will be even multiples of this
          value.499-With 499 permutations, the smallest possible pseudo p-value
          is
          0.002 and all other pseudo p-values will be even multiples of this
          value.999-With 999 permutations, the smallest possible pseudo p-value
          is
          0.001 and all other pseudo p-values will be even multiples of this
          value.9999-With 9999 permutations, the smallest possible pseudo
          p-value is
          0.0001 and all other pseudo p-values will be even multiples of this
          value.
      polygon_mask {Feature Layer}:
          A polygon feature layer with one or more polygons defining the
          analysis study area. You would use a polygon analysis mask to exclude
          a large lake from the analysis, for example. Bins defined in the
          in_cube that fall outside of the mask will not be included in the
          analysis.This parameter is only available for grid cubes.
      conceptualization_of_spatial_relationships {String}:
          Specifies how spatial relationships among bins are
          defined.FIXED_DISTANCE-Each bin is analyzed within the context of
          neighboring
          bins. Neighboring bins inside the specified critical distance
          (neighborhood_distance) receive a weight of one and exert influence on
          computations for the target bin. Neighboring bins outside the critical
          distance receive a weight of zero and have no influence on a target
          bin's computations.K_NEAREST_NEIGHBORS-The closest k bins are included
          in the analysis
          for the target bin; k is a specified numeric
          parameter.CONTIGUITY_EDGES_ONLY-Only neighboring bins that share an
          edge will
          influence computations for the target polygon
          bin.CONTIGUITY_EDGES_CORNERS-Bins that share an edge or share a node
          will
          influence computations for the target polygon bin.
      number_of_neighbors {Long}:
          An integer specifying either the minimum or the exact number of
          neighbors to include in calculations for the target bin. For
          K_NEAREST_NEIGHBORS, each bin will have exactly this specified number
          of neighbors. For FIXED_DISTANCE, each bin will have at least this
          many neighbors (the neighborhood_distance will be temporarily extended
          to ensure this many neighbors if necessary). When one of the
          contiguity conceptualizations are selected, each bin will be assigned
          this minimum number of neighbors. For bins with fewer than this number
          of contiguous neighbors, additional neighbors will be based on feature
          centroid proximity.
      define_global_window {String}:
          The Anselin Local Moran's I statistic works by comparing a local
          statistic calculated from the neighbors for each bin to a global
          value. This parameter can be used to control which bins are used to
          calculate the global value.ENTIRE_CUBE-Each neighborhood is analyzed
          in comparison to the entire
          cube. This is the default. NEIGHBORHOOD_TIME_STEP-Each
          neighborhood is analyzed in
          comparison to the bins contained within the specified.
          Neighborhood Time StepINDIVIDUAL_TIME_STEP-Each neighborhood is
          analyzed in comparison to
          the bins in the same time step.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class containing locations that were considered
          statistically significant clusters or outliers.

        """