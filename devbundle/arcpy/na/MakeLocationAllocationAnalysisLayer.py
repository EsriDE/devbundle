# Generated documentation for module arcpy.na


class MakeLocationAllocationAnalysisLayer(object):
    """
    Makes a location-allocation network analysis layer and sets its analysis properties. A location-allocation analysis layer is useful for choosing a given number of facilities from a set of potential locations so that a demand will be allocated to facilities in an optimal and efficient manner. The layer can be created using a local network dataset or a service hosted online or in a portal.
    """

    @property
    def description(self) -> str:
        return """

        MakeLocationAllocationAnalysisLayer_na(network_data_source, {layer_name}, {travel_mode}, {travel_direction}, {problem_type}, {cutoff}, {number_of_facilities_to_find}, {decay_function_type}, {decay_function_parameter_value}, {target_market_share}, {capacity}, {time_of_day}, {time_zone}, {line_shape}, {accumulate_attributes;accumulate_attributes...}, {ignore_invalid_locations})

        Makes a location-allocation network analysis layer and sets its
        analysis properties. A location-allocation analysis layer is useful
        for choosing a given number of facilities from a set of potential
        locations so that a demand will be allocated to facilities in an
        optimal and efficient manner. The layer can be created using a local
        network dataset or a service hosted online or in a portal.

     INPUTS:
      network_data_source (Network Dataset Layer / String):
          The network dataset or service on which the network analysis will be
          performed. Use the portal URL for a service.
      layer_name {String}:
          The name of the network analysis layer to create.
      travel_mode {String}:
          The name of the travel mode to use in the analysis. The travel mode
          represents a collection of network settings, such as travel
          restrictions and U-turn policies, that determine how a pedestrian,
          car, truck, or other medium of transportation moves through the
          network. Travel modes are defined on your network data source.An
          arcpy.na.TravelMode object and a string containing the valid JSON
          representation of a travel mode can also be used as input to the
          parameter.
      travel_direction {String}:
          Specifies the direction of travel between facilities and demand points
          when calculating the network costs.FROM_FACILITIES-Direction of travel
          is from facilities to demand
          points. This is the default. Fire departments commonly use this
          setting, since they are concerned with the time it takes to travel
          from the fire station to the location of the
          emergency.TO_FACILITIES-Direction of travel is from demand points to
          facilities.
          Retail stores commonly use this setting, since they are concerned with
          the time it takes the shoppers to reach the store.The direction of
          travel may affect the allocation of the demand points
          to the facilities on a network with one-way restrictions and different
          impedances based on direction of travel. For instance, it may take 15
          minutes to drive from the demand point to the facility but only 10
          minutes when driving from the facility to the demand point.
      problem_type {String}:
          The problem type that will be solved. The choice of the problem type
          depends on the kind of facility being located. Different kinds of
          facilities have different priorities and
          constraints.MINIMIZE_IMPEDANCE-This option solves the warehouse
          location problem.
          It selects a set of facilities so that the total sum of weighted
          impedances (demand at a location times the impedance to the closest
          facility) is minimized. This problem type is often known as the
          P-Median problem. This is the default problem
          type.MAXIMIZE_COVERAGE-This option solves the fire station location
          problem. It selects facilities so that all or the greatest amount of
          demand is within a specified impedance
          cutoff.MAXIMIZE_CAPACITATED_COVERAGE-This option solves the location
          problem
          in which facilities have a finite capacity. It selects facilities so
          that all or the greatest amount of demand can be served without
          exceeding the capacity of any facility. In addition to honoring
          capacity, it selects facilities so that the total sum of weighted
          impedance (demand allocated to a facility multiplied by the impedance
          to or from the facility) is minimized.MINIMIZE_FACILITIES-This option
          solves the fire station location
          problem. It selects the minimum number of facilities needed to cover
          all or the greatest amount of demand within a specified impedance
          cutoff.MAXIMIZE_ATTENDANCE-This option solves the neighborhood store
          location
          problem in which the proportion of demand allocated to the nearest
          chosen facility falls with increasing distance. The set of facilities
          that maximize the total allocated demand is selected. Demand greater
          than the specified impedance cutoff does not affect the selected set
          of facilities.MAXIMIZE_MARKET_SHARE-This option solves the competitive
          facility
          location problem. It selects facilities to maximize market share in
          the presence of competitive facilities. Gravity model concepts are
          used to determine the proportion of demand allocated to each facility.
          The set of facilities that maximizes the total allocated demand is
          selected.TARGET_MARKET_SHARE-This option solves the competitive
          facility
          location problem. It selects facilities to reach a specified target
          market share in the presence of competitive facilities. Gravity model
          concepts are used to determine the proportion of demand allocated to
          each facility. The minimum number of facilities needed to reach the
          specified target market share is selected.
      cutoff {Double}:
          The maximum impedance at which a demand point can be allocated
          to a facility in the units of the impedance attribute used by the
          specifiedvalue. The maximum impedance is measured by the least-cost
          path along the network. If a demand point is outside the cutoff, it is
          left unallocated. This parameter can be used to model the maximum
          distance that people are willing to travel to visit stores or the
          maximum time that is permitted for a fire department to reach anyone
          in the community. Travel ModeThis cutoff value can be
          overridden on a per-demand-point basis by
          specifying individual cutoff values in the demand points sublayer in
          the Cutoff_[Impedance] property. For example, it may show that people
          in rural areas are willing to travel up to 10 miles to reach a
          facility, while people in the city are only willing to travel up to 2
          miles. You can model this behavior by setting the cutoff value of the
          analysis layer to 10 and setting the Cutoff_Miles value of each demand
          point in urban areas to 2.By default, no cutoff value is used for the
          analysis.
      number_of_facilities_to_find {Long}:
          The number of facilities that the solver will locate. The default
          value is 1. The facilities with a FacilityType value ofare
          always part of
          the solution when there are more facilities to find than required
          facilities; any excess facilities to choose are picked from candidate
          facilities. Required        Any facilities that have a
          FacilityType value ofbefore solving
          are treated as candidate facilities at solve time. ChosenThis
          parameter value is not considered for the MINIMIZE_FACILITIES
          problem type since the solver searches for the minimum number of
          facilities to locate to maximize coverage.This parameter value is
          overridden for the TARGET_MARKET_SHARE problem
          type because the solver searches for the minimum number of facilities
          required to capture the specified market share.
      decay_function_type {String}:
          The equation that will be used for transforming the network
          cost between facilities and demand points. This parameter, along with
          theparameter, specifies how severely the network impedance between
          facilities and demand points influences the solver's selection of
          facilities. Decay Function Parameter ValueLINEAR-The
          transformed network impedance between the facility and the
          demand point is the same as the shortest-path network impedance
          between them. With this option, the impedance parameter is always set
          to 1. This is the default.POWER-The transformed network impedance
          between the facility and the
          demand point is equal to the shortest-path network impedance raised to
          the power specified by the impedance parameter. Use this option with a
          positive impedance parameter to specify higher weight to nearby
          facilities. EXPONENTIAL-The transformed network impedance
          between the
          facility and the demand point is equal to the mathematical constant e
          raised to the power specified by the shortest-path network impedance
          multiplied with the impedance parameter. Use this option with a
          positive impedance parameter to specify a very high weight to nearby
          facilities. Exponential transformations are commonly used in
          conjunction with an
          impedance cutoff. Demand points have an ImpedanceTransformation
          property, which,
          if set, overrides theparameter of the analysis layer on a per-demand-
          point basis. You may determine that the decay function should be
          different for urban and rural residents. You can model this by setting
          the impedance transformation for the analysis layer to match that of
          rural residents and setting the impedance transformation for the
          individual demand points located in urban areas to match that of
          urbanites. Decay Function Parameter Value
      decay_function_parameter_value {Double}:
          A parameter value for the equations specified in the
          decay_function_type parameter. This parameter value is ignored when
          the decay_function_type parameter is set to LINEAR. For the POWER and
          EXPONENTIAL options, the value should not be zero.Demand points have
          an ImpedanceTransformation property, which, if set,
          overrides the decay_function_parameter_value parameter of the analysis
          layer on a per-demand-point basis. You may determine that the decay
          function should be different for urban and rural residents. You can
          model this by setting the impedance transformation for the analysis
          layer to match that of rural residents and setting the impedance
          transformation for the individual demand points located in urban areas
          to match that of urbanites.
      target_market_share {Double}:
          The target market share, as a percentage, to solve for when the
          problem_type parameter is set to TARGET_MARKET_SHARE. It is the
          percentage of the total demand weight that you want the solution
          facilities to capture. The solver selects the minimum number of
          facilities required to capture the target market share specified by
          this numeric value.
      capacity {Double}:
          The default capacity of facilities when the problem_type parameter is
          set to MAXIMIZE_CAPACITATED_COVERAGE. This parameter is ignored for
          all other problem types.Facilities have a Capacity property, which, if
          set to a nonnull value,
          overrides the capacity parameter value for that facility.
      time_of_day {Date}:
          The time and date of departure. The departure time can be from
          facilities or demand points, depending on whether travel_direction is
          set to TO_FACILITIES or FROM_FACILITIES.If you chose a traffic-based
          impedance attribute, the solution will be
          generated given dynamic traffic conditions at the time of day
          specified here. A date and time can be specified as 5/14/2012 10:30
          AM. Configure your analysis to use one of the following special
          dates to model a day of the week or the current date instead of a
          specific, static date:
          Today-12/30/1899Sunday-12/31/1899Monday-1/1/1900Tuesday-1/2/1900Wednes
          day-1/3/1900Thursday-1/4/1900Friday-1/5/1900Saturday-1/6/1900
      time_zone {String}:
          The time zone of theparameter. Time of
          DayLOCAL_TIME_AT_LOCATIONS-The time of day parameter refers to the
          time
          zone in which the facilities or demand points are located. If the
          travel direction is facilities to demand points, this is the time zone
          of the facilities. If the travel direction is demand points to
          facilities, this is the time zone of the demand points. This is the
          default.UTC-The time of day parameter refers to coordinated universal
          time
          (UTC). Choose this option if you want the best location for a specific
          time, such as now, but aren't certain in which time zone the
          facilities or demand points will be located.
      line_shape {String}:
          Specifies the output line shape.NO_LINES-No shape will be generated
          for the output of the analysis.
          This is useful if you are solving a very large problem and are
          interested only in a solution table and are not interested in
          visualizing the results on a map.STRAIGHT_LINES-The output line shapes
          will be straight lines
          connecting the solution facilities to their allocated demand points.
          This is the default.Regardless of the output shape type specified, the
          best route is
          always determined by the network impedance, never Euclidean distance.
          This means that only the route shapes are different, not the
          underlying traversal of the network.
      accumulate_attributes {String}:
          A list of cost attributes to be accumulated during analysis. These
          accumulated attributes are for reference only; the solver only uses
          the cost attribute used by the designated travel mode when solving the
          analysis.For each cost attribute that is accumulated, a
          Total_[Impedance]
          property is populated in the network analysis output features.This
          parameter is not available if the network data source is an
          ArcGIS Online service or the network data source is a service on a
          version of Portal for ArcGIS that does not support accumulation.
      ignore_invalid_locations {Boolean}:
          Specifies whether invalid input locations will be ignored. Typically,
          locations are invalid if they cannot be located on the network. When
          invalid locations are ignored, the solver will skip them and attempt
          to perform the analysis using the remaining locations.SKIP-Invalid
          input locations will be ignored and only valid locations
          will be used. This is the default.HALT-All input locations will be
          used. Invalid locations will cause
          the analysis to fail.

        """