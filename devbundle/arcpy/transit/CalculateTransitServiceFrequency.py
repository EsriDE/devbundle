# Generated documentation for module arcpy.transit


class CalculateTransitServiceFrequency(object):
    """
    Calculates the frequency of scheduled public transit service available within one or more specified time windows at public transit stops, along public transit lines, at points of interest, or in areas.
    """

    @property
    def description(self) -> str:
        return """

        CalculateTransitServiceFrequency_transit(in_transit_feature_dataset, analysis_type, out_feature_class, time_windows;time_windows..., {separate_counts_by_line}, {in_points_of_interest}, {network_data_source}, {travel_mode}, {travel_limit}, {travel_limit_units}, {cell_size}, {barriers;barriers...}, {wheelchair}, {bicycle}, {exclude_modes;exclude_modes...})

        Calculates the frequency of scheduled public transit service available
        within one or more specified time windows at public transit stops,
        along public transit lines, at points of interest, or in areas.

     INPUTS:
      in_transit_feature_dataset (Feature Dataset):
          A feature dataset containing the Stops and LineVariantElements feature
          classes from the Network Analyst public transit data model. The
          feature dataset's parent geodatabase must contain the public transit
          data model's Lines, LineVariants, Schedules, ScheduleElements, and
          Runs tables and the Calendars table, the CalendarExceptions table, or
          both.A valid feature dataset with its associated feature classes and
          tables
          can be created from General Transit Feed Specification (GTFS) public
          transit data using the GTFS To Public Transit Data Model tool.
      analysis_type (String):
          Specifies the location type for which the tool will calculate the
          frequency of public transit service.STOPS-The frequency of public
          transit service at public transit stops
          will be calculated. The output will be a feature class containing a
          copy of the public transit stops from the input public transit data
          model Stops feature class.LINES-The frequency of public transit
          service along public transit
          lines will be calculated. The output will be a feature class
          containing a copy of the public transit lines from the input public
          transit data model's LineVariantElements feature
          class.POINTS_OF_INTEREST-The frequency of public transit service at
          specified points of interest will be calculated. The output will be a
          copy of the input points of interest.AREAS-The frequency of public
          transit service for all areas within
          range of all public transit stops will be calculated. The output will
          be a polygon feature class representing the area served by the public
          transit system.
      time_windows (Value Table):
          The periods of time for which public transit service frequency will be
          calculated. Multiple time windows can be specified. The output
          feature
          class will include a set of fields representing the transit frequency
          statistics for each time window. These fields will be prefixed by the
          value specified in thecolumn. Output Field Prefix        Time
          windows can be interpreted either as specific dates or as
          generic weekdays. Thecolumn determines whether the date component of
          thecolumn will be interpreted as an exact date or as a generic
          weekday. For example, if the date component of thevalue is December
          25, 2021, andis True, the exact date will be used, and the public
          transit service frequency calculated will include any special service
          added or removed for the Christmas holiday. Ifis False, this date will
          be interpreted as Saturday, and the public transit service frequency
          calculated will include regular service for any typical Saturday.
          Use Specific DateStart DatetimeStart DatetimeUse Specific DateUse
          Specific DateFor specific dates, all exceptions to the regular public
          transit
          service included in the CalendarExceptions table and the date range
          defined in the Calendars table will be considered. For a generic
          weekday, only regular service defined in the weekday fields in the
          Calendars table will be considered.Use Specific Date-A Boolean value
          indicating whether the time window's
          date will be interpreted as the exact date specified (True) or the
          generic weekday represented by the date (False).Start Datetime-The
          date and time the time window begins.Duration (minutes)-The duration
          of the time window in minutes. Count Arrivals or
          Departures-Count arrivals or departures at
          public transit stops when calculating transit frequency statistics.
          ARRIVALS-Arrivals at public transit stops will be counted. The arrival
          times will be considered in the calculations.DEPARTURES-Departures
          from public transit stops will be counted. The
          departure times will be considered in the calculations.Output Field
          Prefix-A string prefix that will be included in the names
          of all output fields associated with this time window. String prefixes
          must be unique and must contain only characters valid for field names
          in the output feature class.
      separate_counts_by_line {Boolean}:
          Specifies whether service from multiple transit lines using the same
          stop or corridor will be separated by transit line or combined when
          calculating transit frequency statistics.When separated by transit
          line, the output will contain a copy of each
          stop or transit line segment for each unique transit line using the
          stop or corridor, and these duplicated features will have overlapping
          geometry. If the LineVariants table in the input data has the
          optionalfield, the output will additionally separate counts by
          thefield value. For example, if a stop serves both directions of
          travel along the same line, the output will contain a copy of the stop
          for each direction of travel as defined by thefield.
          GDirectionIDGDirectionIDGDirectionIDSEPARATE-Multiple transit lines
          serving the same stop or corridor will
          be counted separately when calculating transit frequency
          statistics.NO_SEPARATE-Multiple transit lines serving the same stop or
          corridor
          will not be counted separately when calculating transit frequency
          statistics; they will be combined. This is the default.This parameter
          only applies when the analysis_type parameter is set to
          STOPS or LINES.
      in_points_of_interest {Feature Layer}:
          The points of interest for which the frequency of available public
          transit service will be calculated.If a polygon layer is specified,
          the public transit service available
          at the polygon centroids will be used.This parameter is required when
          the analysis_type parameter is set to
          POINTS_OF_INTEREST; otherwise, it is ignored.
      network_data_source {Network Data Source}:
          The network dataset or service that will be used to determine the
          public transit stops within range of the designated points of interest
          or to calculate the polygon areas within range of public transit
          stops. You can use a catalog path to a network dataset, a network
          dataset layer object, the string name of the network dataset layer, or
          a portal URL for a network analysis service. The network must have at
          least one travel mode.To use a portal URL, you must be signed in to
          the portal with an
          account that has routing privileges.Running the tool will consume
          credits if you use ArcGIS Online as the
          network data source.Use a network dataset appropriate for modeling
          passengers traveling to
          and from public transit stops. Don't use a network dataset configured
          to use public transit data with the Public Transit evaluator because
          this type of network models passengers riding public transit, not
          people traveling to and from the public transit stops.This parameter
          is required when the analysis_type parameter is set to
          POINTS_OF_INTEREST or AREAS; otherwise, it is ignored.
      travel_mode {Network Travel Mode}:
          The travel mode on the network data source that will be used to
          determine the public transit stops within range of the designated
          points of interest or to calculate the polygon areas within range of
          public transit stops. You can specify the travel mode as a string name
          of the travel mode or as an arcpy.nax.TravelMode object.Use the travel
          mode most appropriate for modeling passengers traveling
          to and from public transit stops. Typically, a travel mode that models
          walking time or distance should be used.Do not use a travel mode with
          an impedance attribute that uses the
          Public Transit evaluator because that travel mode models passengers
          riding public transit, not passengers traveling to and from the public
          transit stops.This parameter is required when the analysis_type
          parameter is set to
          POINTS_OF_INTEREST or AREAS; otherwise, it is ignored.
      travel_limit {Double}:
          The impedance limit that will be used when finding the public transit
          stops within range of points of interest or when calculating the area
          reachable from public transit stops.Provide this parameter value in
          the units designated in the
          travel_limit_units parameter.This parameter is required when the
          analysis_type parameter is set to
          POINTS_OF_INTEREST or AREAS; otherwise, it is ignored.
      travel_limit_units {String}:
          Specifies the units that will be used for the impedance limit provided
          in the travel_limit parameter.The available units depend on the value
          specified in the travel_mode
          parameter. If the travel mode's impedance has units of time, only
          time-based units will be available. If the travel mode's impedance has
          units of distance, only distance-based units will be available. If the
          travel mode's impedance units are neither time based nor distance
          based, the only option available will be unknown units, and the
          travel_limit parameter value will be in the units of the travel mode's
          impedance.KILOMETERS-The impedance limit will be in
          kilometers.METERS-The
          impedance limit will be in meters.MILES-The impedance limit will be in
          miles.YARDS-The impedance limit will be in yards.FEET-The impedance
          limit will be in feet.NAUTICALMILES-The impedance limit will be in
          nautical miles.DAYS-The impedance limit will be in days.HOURS-The
          impedance limit will be in hours.MINUTES-The impedance limit will be
          in minutes.SECONDS-The impedance limit will be in seconds.UNKNOWN-The
          impedance limit will be in the impedance unit of the
          travel mode provided.This parameter is required when the analysis_type
          parameter is set to
          POINTS_OF_INTEREST or AREAS; otherwise, it is ignored.It is
          recommended that you use a distance-based travel limit when
          calculating public transit service frequency for points of interest.
          With a distance-based limit, the tool can reduce the OD cost matrix
          size in advance using a simple straight-line distance selection. This
          may eliminate some origins and destinations from the OD cost matrix
          analysis and improve performance. If the network data source is a
          service that charges credits, this optimization also reduces the
          number of credits needed.
      cell_size {Linear Unit}:
          The size (edge length) of cells that will be used to represent the
          area reachable from transit stops in the tool output. The numerical
          value and the units are set using this parameter.When calculating the
          area reachable from public transit stops, a
          service area is calculated. The resulting service area polygons, which
          often overlap, are simplified into a raster-like polygon feature class
          composed of square cells of the size specified in this parameter. The
          public transit service frequency statistics are calculated for each of
          these cells based on the public transit stops whose service area
          polygons overlap the cell centroid.Use a cell size relevant to how
          pedestrians travel in the real world.
          For example, you can base the cell size on the size of city blocks or
          parcels or the distance a pedestrian can walk in less than a minute.
          Smaller cells are more accurate but take longer to process.The default
          is 80 meters.This parameter is required when the analysis_type
          parameter is set to
          AREAS; otherwise, it is ignored.
      barriers {Feature Layer}:
          The point, line, or polygon features that will be used as barriers in
          the network analysis when calculating the public transit stops within
          range of the designated points of interest or when calculating the
          polygon areas within range of public transit stops.This parameter is
          relevant only when the analysis_type parameter is
          set to POINTS_OF_INTEREST or AREAS; otherwise, it is ignored.
      wheelchair {Boolean}:
          Specifies whether travel with a wheelchair will be modeled, excluding
          transit service that is not wheelchair accessible, when calculating
          transit frequency statistics. When modeling travel with a
          wheelchair, transit service with a
          value of 2 in thefield in the Runs table will be excluded. If the Runs
          table does not have this field, no transit runs will be excluded.
          GWheelchairAccessible        When modeling travel with a wheelchair,
          when the analysis_type
          parameter is set to POINTS_OF_INTEREST, transit stops with a value of
          2 in thefield in the Stops feature class will be excluded. When the
          analysis_type parameter is set to STOPS or AREAS, transit stops with a
          value of 2 in thefield in the Stops feature class will be included in
          the analysis but will be considered to have no service because they
          are not accessible. If the Stops table does not have this field, no
          transit stops will be considered inaccessible.
          GWheelchairAccessibleGWheelchairAccessibleWHEELCHAIR-Traveling with a
          wheelchair will be modeled. Transit
          service that is not wheelchair accessible will be excluded when
          calculating transit frequency statistics.NO_WHEELCHAIR-Traveling with
          a wheelchair will not be modeled. Transit
          service that is not wheelchair accessible will not be excluded when
          calculating transit frequency statistics. This is the default.
      bicycle {Boolean}:
          Specifies whether travel with a bicycle will be modeled, excluding
          transit service on which bicycles are not allowed, when calculating
          transit frequency statistics. When modeling travel with a
          bicycle, transit service with a
          value of 2 in thefield in the Runs table will be excluded. If the Runs
          table does not have this field, no transit service will be excluded.
          GBikesAllowedBICYCLE-Traveling with a bicycle will be modeled. Transit
          service that
          does not allow bicycles will be excluded when calculating transit
          frequency statistics.NO_BICYCLE-Traveling with a bicycle will not be
          modeled. Transit
          service that does not allow bicycles will not be excluded when
          calculating transit frequency statistics. This is the default.
      exclude_modes {Long}:
          Modes of public transit that will be excluded when calculating
          transit frequency statistics. Provide excluded modes as integers
          corresponding to thefield in the Lines table. GRouteType

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class.A shapefile is not a valid value.

        """