# Generated documentation for module arcpy.na


class MakeServiceAreaAnalysisLayer(object):
    """
    Makes a service area network analysis layer and sets its analysis properties. A service area analysis layer is useful in determining the area of accessibility within a given cutoff cost from a facility location. The layer can be created using a local network dataset or a routing service hosted online or in a portal.
    """

    @property
    def description(self) -> str:
        return """

        MakeServiceAreaAnalysisLayer_na(network_data_source, {layer_name}, {travel_mode}, {travel_direction}, {cutoffs;cutoffs...}, {time_of_day}, {time_zone}, {output_type}, {polygon_detail}, {geometry_at_overlaps}, {geometry_at_cutoffs}, {polygon_trim_distance}, {exclude_sources_from_polygon_generation;exclude_sources_from_polygon_generation...}, {accumulate_attributes;accumulate_attributes...}, {ignore_invalid_locations})

        Makes a service area network analysis layer and sets its analysis
        properties. A service area analysis layer is useful in determining the
        area of accessibility within a given cutoff cost from a facility
        location. The layer can be created using a local network dataset or a
        routing service hosted online or in a portal.

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
          Specifies the direction of travel to or from the
          facilities.FROM_FACILITIES-The direction of travel is away from the
          facilities.
          This is the default.TO_FACILITIES-The direction of travel is toward
          the facilities.Using this parameter can result in different service
          areas on a
          network with one-way restrictions and different impedances based on
          direction of travel. The service area for a pizza delivery store, for
          example, should be created away from the facility, whereas the service
          area of a hospital should be created toward the facility.
      cutoffs {Double}:
          The extent of the service area to be calculated in the units of the
          impedance attribute used by the selected travel mode. For example,
          when analyzing driving time, a cutoff value of 10 means that the
          resulting service area will represent the area reachable within a
          10-minute drive time.Multiple cutoffs can be set to create concentric
          service areas. For
          example, to find 2-, 3-, and 5-minute service areas for the same
          facility, specify 2, 3, and 5 as the values for this parameter.This
          default cutoff value can be overridden on a per-facility basis by
          specifying individual break values in the facilities sublayer.
      time_of_day {Date}:
          The time to depart from or arrive at the facilities of the
          service area layer. The interpretation of this value as a departure or
          arrival time depends on whether travel is away from or toward the
          facilities. It represents the departure time if
          travel_direction='FROM_FACILITIES'.It represents the arrival time if
          travel_direction='TO_FACILITIES'.The time_of_day parameter is most
          useful for finding the roads that
          can be reached based on a travel mode that uses an impedance attribute
          that varies with the time of the day, such as one based on dynamic
          traffic conditions. Solving the same analysis using different
          time_of_day values allows you to see how a facility's reach changes
          over time. For example, the five-minute service area around a fire
          station may start out large in the early morning, diminish during the
          morning rush hour, grow in the late morning, and so on throughout the
          day.A date and time can be specified as 10/21/2015 10:30 AM.
          Configure your analysis to use one of the following special
          dates to model a day of the week or the current date instead of a
          specific, static date:
          Today-12/30/1899Sunday-12/31/1899Monday-1/1/1900Tuesday-1/2/1900Wednes
          day-1/3/1900Thursday-1/4/1900Friday-1/5/1900Saturday-1/6/1900
      time_zone {String}:
          Specifies the time zone for the time of day parameter.
          LOCAL_TIME_AT_LOCATIONS-The time of day parameter will use
          the time zone or zones in which the facilities are located. The start
          or end times of the service areas are staggered by time zone. This is
          the default. For example, setting time of day to 9:00 a.m.
          causes service areas to
          be generated for 9:00 a.m. eastern time for facilities in the eastern
          time zone, 9:00 a.m. central time for facilities in the central time
          zone, 9:00 a.m. mountain time for facilities in the mountain time
          zone, and so on. If stores in a chain that span the U.S. open at 9:00
          a.m. local time, choose this parameter value to find market
          territories at opening time for all stores in one solve. First, the
          stores in the eastern time zone open and a polygon is generated. An
          hour later, stores open in the central time zone, and so on. Nine
          o'clock is always in local time but staggered in real time.
          UTC-The time of day parameter will use coordinated universal
          time (UTC). All facilities are reached or departed from
          simultaneously, regardless of the time zone or zones in which they are
          located. Setting time of day to 2:00 p.m. causes service areas
          to be generated
          for 9:00 a.m. eastern standard time for facilities in the eastern time
          zone, 8:00 a.m. central standard time for facilities in the central
          time zone, 7:00 a.m. mountain standard time for facilities in the
          mountain time zone, and so on.The scenario above assumes standard
          time. During daylight saving time,
          the eastern, central, and mountain times will each be one hour ahead
          (that is, 10:00, 9:00, and 8:00 a.m., respectively).One of the cases
          in which the UTC option is useful is to visualize
          emergency response coverage for a jurisdiction that is split into two
          time zones. The emergency vehicles are loaded as facilities. Time of
          day is set to now in UTC. (You need to determine what the current time
          and date are in terms of UTC to correctly use this option.) Other
          properties are set and the analysis is solved. Even though a time-zone
          boundary divides the vehicles, the results show areas that can be
          reached given current traffic conditions. This same process can be
          used for other times as well, not just for now.
      output_type {String}:
          Specifies the type of output to be generated. Service area output can
          be line features representing the roads reachable before the cutoffs
          are exceeded or the polygon features encompassing these lines
          (representing the reachable area).POLYGONS-The service area output
          will contain polygons only. This is
          the default.LINES-The service area output will contain lines
          only.POLYGONS_AND_LINES-The service area output will contain both
          polygons
          and lines. Theandoutput types are not available if the network
          data
          source is a service on a version of Portal for ArcGIS that does not
          support line generation. LinesPolygons and lines
      polygon_detail {String}:
          Specifies the level of detail of the output polygons.STANDARD-Polygons
          with a standard level of detail will be created.
          This is the default.GENERALIZED-Generalized polygons will be created
          using the network's
          hierarchy attribute to produce results quickly. This option is not
          available if the network does not have a hierarchy
          attribute.HIGH-Polygons with a higher level of detail will be created
          for
          applications in which precise results are important.If the analysis
          includes an urban area with a grid-like street
          network, the difference between generalized and standard polygons will
          be minimal. However, for mountain and rural roads, the standard and
          detailed polygons may present more accurate results than generalized
          polygons.
      geometry_at_overlaps {String}:
          Specifies the behavior of service-area output from multiple facilities
          in relation to one another.OVERLAP-Individual polygons or sets of
          lines for each facility will be
          created. The polygons or lines can overlap each other. This is the
          default.DISSOLVE-The polygons of multiple facilities that have the
          same cutoff
          value will be joined into a single polygon. This option does not apply
          to line output.SPLIT-An area will be assigned to the closest facility
          so polygons or
          lines do not overlap each other.
      geometry_at_cutoffs {String}:
          Specifies the behavior of service area output for a single facility
          when multiple cutoff values are specified. This parameter does not
          apply to line output.RINGS-Each polygon will include only the area
          between consecutive
          cutoff values. It will not include the area between the facility and
          any smaller cutoffs. For example, if you create 5- and 10-minute
          service areas, the 5-minute service area polygon will include the area
          reachable in 0 to 5 minutes, and the 10-minute service area polygon
          will include the area reachable in 5 to 10 minutes. This is the
          default.DISKS-Each polygon will include the area reachable from the
          facility
          up to the cutoff value, including the area reachable within smaller
          cutoff values. For example, if you create 5- and 10-minute service
          areas, the 10-minute service area polygon will include the area under
          the 5-minute service area polygon.
      polygon_trim_distance {Linear Unit}:
          The service area polygon trim distance. The polygon trim distance is
          the distance the service area polygon will extend from the road when
          no other reachable roads are nearby, similar to a line buffer size.
          This is useful when the network is sparse and you don't want the
          service area to cover large areas where there are no features.This
          parameter includes a value and units for the distance. The
          default value is 100 meters.
      exclude_sources_from_polygon_generation {String}:
          The network dataset edge sources that will be excluded when generating
          service area polygons. Polygons will not be generated around the
          excluded sources, even though they are traversed in the
          analysis.Excluding a network source from service area polygons does
          not prevent
          those sources from being traversed. Excluding sources from service
          area polygons only influences the polygon shape of the service areas.
          To prevent traversal of a given network source, you must create an
          appropriate restriction when defining the network dataset.This is
          useful if you have some network sources that you don't want to
          be included in the polygon generation because they create less-
          accurate polygons or are inconsequential for the service area
          analysis. For example, while creating a walk-time service area in a
          multimodal network that includes streets and metro lines, you should
          exclude the metro lines from polygon generation. Although the traveler
          can use the metro lines, they cannot stop partway along a metro line
          and enter a nearby building. Instead, they must travel the full length
          of the metro line, exit the metro system at a station, then use the
          streets to walk to the building. It would be inaccurate to generate a
          polygon feature around a metro line.This parameter is not available
          when the output geometry types do not
          include polygons, there are fewer than two edge sources in the
          network, the network data source is an ArcGIS Online service, or the
          network data source is a service on a version of Portal for ArcGIS
          that does not support excluding sources.
      accumulate_attributes {String}:
          A list of cost attributes to be accumulated during analysis. These
          accumulated attributes are for reference only; the solver only uses
          the cost attribute used by the designated travel mode when solving the
          analysis.For each cost attribute that is accumulated, a
          Total_[Impedance]
          property is populated in the network analysis output features.This
          parameter is not available if the analysis layer is not
          configured to output lines, the network data source is an ArcGIS
          Online service, or the network data source is a service on a version
          of Portal for ArcGIS that does not support accumulation.
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