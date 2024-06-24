# Generated documentation for module arcpy.stats


class BuildBalancedZones(object):
    """
    Creates spatially contiguous zones in a study area using a genetic growth algorithm based on specified criteria.
    """

    @property
    def description(self) -> str:
        return """

        BuildBalancedZones_stats(in_features, output_features, zone_creation_method, {number_of_zones}, {zone_building_criteria_target;zone_building_criteria_target...}, {zone_building_criteria;zone_building_criteria...}, {spatial_constraints}, {weights_matrix_file}, {zone_characteristics;zone_characteristics...}, {attribute_to_consider;attribute_to_consider...}, {distance_to_consider;distance_to_consider...}, {categorial_variable}, {proportion_method}, {population_size}, {number_generations}, {mutation_factor}, {output_convergence_table})

        Creates spatially contiguous zones in a study area using a genetic
        growth algorithm based on specified criteria.

     INPUTS:
      in_features (Feature Layer):
          The feature class or feature layer that will be aggregated into zones.
      zone_creation_method (String):
          Specifies the method that will be used to create each zone. Zones grow
          until all specified criteria are satisfied.
          ATTRIBUTE_TARGET-Zones will be created based on target values
          of one or multiple variables. The sum of each attribute must be
          specified in theparameter, and each zone will grow until the sum of
          the attributes exceeds these values. For example, you can use this
          option to create zones that each have at least 100,000 residents and
          20,000 family homes. Zone Building Criteria With Target
          NUMBER_ZONES_AND_ATTRIBUTE-A specified number of zones will
          be created while keeping the sum of an attribute approximately equal
          within each zone. The number of zones must be specified in
          theparameter. The attribute sum within each zone is equal to the sum
          of the total attribute divided by the number of zones. Target
          Number of Zones         NUMBER_OF_ZONES-A specified number of zones
          will be created
          that are each composed of approximately the same number of input
          features. The number of zones must be specified in theparameter.
          Target Number of Zones
      number_of_zones {Long}:
          The number of zones that will be created.
      zone_building_criteria_target {Value Table}:
          Specifies the variables that will be considered, as well as their
          target values and optional weights. The default weight is 1, and each
          variable contributes equally unless they are changed.
      zone_building_criteria {Value Table}:
          Specifies the variables that will be considered and, optionally, their
          weights. The default weight is 1, and each variable contributes
          equally unless changed.
      spatial_constraints {String}:
          Specifies how neighbors will be defined while the zones grow.
          Zones can only grow into new features that are neighbors of at least
          one of the features already in the zone. If the input features are
          polygons, the default spatial constraint is. If the input features are
          points, the default spatial constraint is. Contiguity edges
          cornersTrimmed Delaunay triangulationCONTIGUITY_EDGES_ONLY-For zones
          containing contiguous polygon
          features, only polygons that share an edge will be part of the same
          zone.CONTIGUITY_EDGES_CORNERS-For zones containing contiguous polygon
          features, only polygons that share an edge or a vertex will be part of
          the same zone.TRIMMED_DELAUNAY_TRIANGULATION-Features in the same
          zone will have at
          least one natural neighbor in common with another feature in the zone.
          Natural neighbor relationships are based on a trimmed Delaunay
          Triangulation. Conceptually, Delaunay Triangulation creates a
          nonoverlapping mesh of triangles from feature centroids. Each feature
          is a triangle node, and nodes that share edges are considered
          neighbors. These triangles are then clipped to a convex hull to ensure
          that features cannot be neighbors with any features outside of the
          convex hull. This is the default.
          GET_SPATIAL_WEIGHTS_FROM_FILE-Spatial, and, optionally,
          temporal relationships will be defined by a specified spatial weights
          file (.swm). Create the spatial weights matrix using the Generate
          Spatial Weights Matrix tool or the Generate Network Spatial Weights
          tool. The path to the spatial weights file is specified by
          theparameter. Spatial Weights Matrix File
      weights_matrix_file {File}:
          The path to a file containing spatial weights that define spatial and,
          optionally, temporal relationships among features.
      zone_characteristics {String}:
          Specifies the characteristics of the zones that will be
          created.EQUAL_AREA-Zones with total area as similar as possible will
          be
          created.COMPACTNESS-Zones with more closely-packed (compact) features
          will be
          created.EQUAL_NUMBER_OF_FEATURES-Zones with an equal number of
          features will
          be created.
      attribute_to_consider {Value Table}:
          Specifies attributes and statistics to consider in the selection of
          final zones. You can homogenize attributes based on their sum,
          average, median, or variance. For example, if you are creating zones
          based on home values and want to balance the average total income
          within each zone, the solution with the most equal average income
          across zones will be preferred.
      distance_to_consider {Feature Layer}:
          The feature class that will be used to homogenize the total distance
          per zone. The distance is calculated from each of the input features
          to the closest feature provided in this parameter. This distance is
          then used as an additional attribute constraint when selecting the
          final zone solution. For example, you can create police patrol
          districts that are each approximately the same distance from the
          closest police station.
      categorial_variable {Field}:
          The categorical variable to be considered for zone proportions.
      proportion_method {String}:
          Specifies the type of proportion that will be maintained based on the
          chosen categorical variable.MAINTAIN_WITHIN_PROPORTION-Each zone will
          maintain the same
          proportions as the overall study area for the given categorical
          variable. For example, given a categorical variable that is 60% Type A
          and 40% Type B, this method will prefer zones that are composed of
          approximately 60% Type A features and 40% Type B
          features.MAINTAIN_OVERALL_PROPORTION-Zones will be created so that the
          overall
          proportions of category predominance by zone matches the proportions
          of the given categorical variable for the entire dataset. For example,
          given a categorical variable that is 60% Type A and 40% Type B, this
          method will prefer solutions where 60% of the zones are predominantly
          Type A features and 40% of the zones are predominantly Type B
          features.
      population_size {Long}:
          The number of randomly generated initial seeds. For larger datasets,
          increasing this number will increase the search space and the
          probability of finding a better solution. The default is 100.
      number_generations {Long}:
          The number of times the zone search process will be repeated. For
          larger datasets, increasing the number is recommended to find an
          optimal solution. The default is 50 generations.
      mutation_factor {Double}:
          The probability that an individual's seed values will be mutated to a
          new set of seeds. Mutation increases the search space by introducing
          variability of the possible solutions in every generation and allows
          for faster convergence to an optimal solution. The default is 0.1.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class indicating which features are
          aggregated into each zone. The feature class will be symbolized by
          thefield and will contain fields displaying the values of each
          criteria that you specify. ZONE_ID
      output_convergence_table {Table}:
          The table containing the total fitness score for the best solution
          found in every generation as well as the fitness score for the
          individual zone constraints.

        """