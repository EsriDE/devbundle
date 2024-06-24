# Generated documentation for module arcpy.na


class MakeClosestFacilityAnalysisLayer(object):
    """
    Makes a closest facility network analysis layer and sets its analysis properties. A closest facility analysis layer is useful in determining the closest facility or facilities to an incident based on a specified travel mode. The layer can be created using a local network dataset or a service hosted online or in a portal.
    """

    @property
    def description(self) -> str:
        return """

        MakeClosestFacilityAnalysisLayer_na(network_data_source, {layer_name}, {travel_mode}, {travel_direction}, {cutoff}, {number_of_facilities_to_find}, {time_of_day}, {time_zone}, {time_of_day_usage}, {line_shape}, {accumulate_attributes;accumulate_attributes...}, {generate_directions_on_solve}, {ignore_invalid_locations})

        Makes a closest facility network analysis layer and sets its analysis
        properties. A closest facility analysis layer is useful in determining
        the closest facility or facilities to an incident based on a specified
        travel mode. The layer can be created using a local network dataset or
        a service hosted online or in a portal.

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
          Specifies the direction of travel between facilities and
          incidents.TO_FACILITIES-Direction of travel is from incidents to
          facilities.
          Retail stores commonly use this setting, since they are concerned with
          the time it takes the shoppers (incidents) to reach the store
          (facility). This is the default.FROM_FACILITIES-Direction of travel is
          from facilities to incidents.
          Fire departments commonly use this setting, since they are concerned
          with the time it takes to travel from the fire station (facility) to
          the location of the emergency (incident).The direction of travel may
          influence the facilities found if the
          network contains one-way streets or impedances based on the direction
          of travel. For instance, it may take 10 minutes to drive from a
          particular incident to a particular facility, but the journey may take
          15 minutes traveling in the other direction, from the facility to the
          incident, because of one-way streets or different traffic conditions.
      cutoff {Double}:
          The impedance value at which to stop searching for facilities for a
          given incident in the units of the impedance attribute used by the
          travel_mode value. This cutoff can be overridden on a per-incident
          basis by specifying individual cutoff values in the incidents sublayer
          when travel_direction = 'TO_FACILITIES' or on a per-facility basis by
          specifying individual cutoff values in the facilities sublayer when
          travel_direction = 'FROM_FACILITIES' By default, no cutoff is used for
          the analysis.
      number_of_facilities_to_find {Long}:
          The number of closest facilities to find per incident. This default
          can be overridden by specifying an individual value for the
          TargetFacilityCount property in the incidents sublayer. The default
          number of facilities to find is one.
      time_of_day {Date}:
          The time and date at which the routes will begin or end. The
          interpretation of this value depends on whether time_of_day_usage is
          set to be the start time or the end time of the route.If you chose a
          traffic-based impedance attribute, the solution will be
          generated given dynamic traffic conditions at the time of day
          specified here. A date and time can be specified as 5/14/2012 10:30
          AM. Configure your analysis to use one of the following special
          dates to model a day of the week or the current date instead of a
          specific, static date:
          Today-12/30/1899Sunday-12/31/1899Monday-1/1/1900Tuesday-1/2/1900Wednes
          day-1/3/1900Thursday-1/4/1900Friday-1/5/1900Saturday-1/6/1900
      time_zone {String}:
          Specifies the time zone for the time_of_day parameter.
          LOCAL_TIME_AT_LOCATIONS-                  The time_of_day
          parameter refers to the time zone in which
          the facilities or incidents are located. This is the default.
          If time_of_day_usage is set to START_TIME and travel_direction is set
          to FROM_FACILITIES, this is the time zone of the facilities.If
          time_of_day_usage is set to START_TIME and travel_direction is set
          to TO_FACILITIES, this is the time zone of the incidents.If
          time_of_day_usage is set to END_TIME and travel_direction is set to
          FROM_FACILITIES, this is the time zone of the incidents.If
          time_of_day_usage is set to END_TIME and travel_direction is set to
          TO_FACILITIES, this is the time zone of the facilities.UTC-The
          time_of_day parameter refers to coordinated universal time
          (UTC). Choose this option if you want to find what's nearest for a
          specific time, such as now, but aren't certain in which time zone the
          facilities or incidents will be located.
      time_of_day_usage {String}:
          Specifies whether the value of the time_of_day parameter represents
          the arrival or departure time for the route or routes.
          START_TIME-The time_of_day parameter value is interpreted as
          the departure time from the facility or incident. This is the default.
          When this setting is chosen, the time_of_day parameter indicates that
          the solver will find the best route given a departure time.
          END_TIME-The time_of_day parameter value is interpreted as
          the arrival time at the facility or incident. This option is
          useful if you want to know the time to depart from a
          location so you arrive at the destination at the time specified in the
          time_of_day parameter.
      line_shape {String}:
          Specifies the shape type that will be used for the route features that
          are output by the analysis.Regardless of the output shape type
          specified, the best route is
          always determined by the network impedance, never Euclidean distance.
          This means that only the route shapes are different, not the
          underlying traversal of the network.ALONG_NETWORK-The output routes
          will have the exact shape of the
          underlying network sources. The output includes route measurements for
          linear referencing. The measurements increase from the first stop and
          record the cumulative impedance to reach a given position.NO_LINES-No
          shape will be generated for the output routes.STRAIGHT_LINES-The
          output route shape will be a single straight line
          between the stops.
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
      generate_directions_on_solve {Boolean}:
          Specifies whether directions will be generated when running the
          analysis.DIRECTIONS-Turn-by-turn directions will be generated on
          solve.NO_DIRECTIONS-Turn-by-turn directions will not be generated on
          solve.
          This is the default.For an analysis in which generating turn-by-turn
          directions is not
          needed, use the default option NO_DIRECTIONS to reduce the time it
          takes to solve the analysis.
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