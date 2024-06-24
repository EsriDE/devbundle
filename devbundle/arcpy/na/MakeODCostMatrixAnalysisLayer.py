# Generated documentation for module arcpy.na


class MakeODCostMatrixAnalysisLayer(object):
    """
    Makes an origin destination (OD) cost matrix network analysis layer and sets its analysis properties. An OD cost matrix analysis layer is useful for representing a matrix of costs going from a set of origin locations to a set of destination locations. The layer can be created using a local network dataset or a service hosted online or in a portal.
    """

    @property
    def description(self) -> str:
        return """

        MakeODCostMatrixAnalysisLayer_na(network_data_source, {layer_name}, {travel_mode}, {cutoff}, {number_of_destinations_to_find}, {time_of_day}, {time_zone}, {line_shape}, {accumulate_attributes;accumulate_attributes...}, {ignore_invalid_locations})

        Makes an origin destination (OD) cost matrix network analysis layer
        and sets its analysis properties. An OD cost matrix analysis layer is
        useful for representing a matrix of costs going from a set of origin
        locations to a set of destination locations. The layer can be created
        using a local network dataset or a service hosted online or in a
        portal.

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
      cutoff {Double}:
          The impedance value at which to stop searching for destinations for a
          given origin. This value will be in the units of the impedance
          attribute used by the chosen travel mode. No destinations beyond this
          limit will be found. This cutoff value can be overridden on a per-
          origin basis by specifying individual cutoff values in the origins
          sublayer. By default, no cutoff is used for the analysis.
      number_of_destinations_to_find {Long}:
          The number of destinations to find per origin. The default can be
          overridden by specifying an individual value for the
          TargetDestinationCount property in the origins sublayer. By default,
          no limit is used, and all destinations are found.
      time_of_day {Date}:
          The departure time from origins.If you chose a traffic-based impedance
          attribute, the solution will be
          generated given dynamic traffic conditions at the time of day
          specified here. A date and time can be specified as 5/14/2012 10:30
          AM. Configure your analysis to use one of the following special
          dates to model a day of the week or the current date instead of a
          specific, static date:
          Today-12/30/1899Sunday-12/31/1899Monday-1/1/1900Tuesday-1/2/1900Wednes
          day-1/3/1900Thursday-1/4/1900Friday-1/5/1900Saturday-1/6/1900
      time_zone {String}:
          The time zone of theparameter. Time of Day
          LOCAL_TIME_AT_LOCATIONS-Theparameter refers to the time zone
          in which the origins are located. This is the default. Time of
          Day         UTC-Theparameter refers to coordinated universal time
          (UTC).
          Choose this option if you want to calculate the OD cost matrix for a
          specific time, such as now, but aren't certain in which time zone the
          origins will be located. Time of Day
      line_shape {String}:
          Specifies the output line shape.NO_LINES-No shape will be generated
          for the output origin-destination
          route pair. This is useful when you have a large number of origins and
          destinations and are interested only in the impedance costs in the OD
          cost matrix table, not in visualizing the OD cost matrix on a
          map.STRAIGHT_LINES-The output route shape will be a single straight
          line
          between each of the origin-destination pairs. This is the
          default.Regardless of the output shape type specified, the best route
          is
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