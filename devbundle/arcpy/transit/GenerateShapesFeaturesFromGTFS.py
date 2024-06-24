# Generated documentation for module arcpy.transit


class GenerateShapesFeaturesFromGTFS(object):
    """
    Generates an estimate of the paths traveled by the vehicles in a public transit system. The output from this tool can be used to generate a new shapes.txt file for a GTFS public transit dataset.
    """

    @property
    def description(self) -> str:
        return """

        GenerateShapesFeaturesFromGTFS_transit(in_gtfs_folder, out_shape_lines, out_shape_stops, out_gtfs_trips, {network_modes;network_modes...}, {network_data_source}, {travel_mode}, {drive_side}, {bearing_tolerance}, {max_bearing_angle})

        Generates an estimate of the paths traveled by the vehicles in a
        public transit system. The output from this tool can be used to
        generate a new shapes.txt file for a GTFS public transit dataset.

     INPUTS:
      in_gtfs_folder (Folder):
          A folder containing a valid GTFS dataset for which you want to create
          a new shapes.txt file. The folder must contain the GTFS stops.txt,
          trips.txt, routes.txt, and stop_times.txt files.
      network_modes {String}:
          Specifies the modes of transit for which line shapes will be generated
          along the road network rather than with straight lines. Shapes for all
          modes not selected will be generated using straight lines.You should
          typically select modes that run on streets, such as buses,
          since those modes are most accurately represented by the road network.
          Do not select modes that are not modeled by your road network. For
          example, unless your network explicitly models ferry lanes, don't use
          the network to represent the paths traveled by ferries. The
          modes are specified using the codes in the table below.
          These correspond to the valid GTFS routes.txt file'sfield values from
          the GTFS documentation. route_typeModes 3, 5, and 11 are used
          by default. 0-Tram, streetcar, light rail. This mode
          corresponds to
          GTFS0. route_type         1-Subway or metro. This mode
          corresponds to GTFS1.
          route_type         2-Rail. This mode corresponds to GTFS2.
          route_type         3-Bus. This mode corresponds to GTFS3.
          route_type         4-Ferry. This mode corresponds to GTFS4.
          route_type         5-Cable tram. This mode corresponds to GTFS5.
          route_type         6-Aerial lift, suspended cable car, gondola lift,
          aerial
          tramway. This mode corresponds to GTFS6. route_type         7-
          Funicular. This mode corresponds to GTFS7.
          route_type         11-Trolleybus. This mode corresponds to GTFS11.
          route_type         12-Monorail. This mode corresponds to GTFS12.
          route_typeOTHER-This option corresponds to any mode of public transit
          not
          encompassed by the other options.
      network_data_source {Network Data Source}:
          The network dataset or service that will be used for calculating route
          shapes along a road network. You can use a catalog path to a network
          dataset, a network dataset layer object, the string name of the
          network dataset layer, or a portal URL for a network analysis service.
          The network must have at least one travel mode.To use a portal URL,
          you must be signed in to the portal with an
          account that has routing privileges.Running the tool will consume
          credits if you use ArcGIS Online as the
          network data source.This parameter is required when any network modes
          are selected.The network dataset you choose should be appropriate for
          modeling
          transit vehicles, such as buses, driving on streets. Don't use a
          network dataset configured to use public transit data with the Public
          Transit evaluator because this type of network models passengers
          riding on public transit, not public transit vehicles driving on
          streets.
      travel_mode {Network Travel Mode}:
          The travel mode on the network data source that will be used when
          calculating route shapes along a road network. You can specify the
          travel mode as a string name of the travel mode or as an
          arcpy.nax.TravelMode object.Use the travel mode most appropriate for
          modeling vehicles in your
          transit system driving along the road network.This parameter is
          required when any network modes are selected.Do not use a travel mode
          with an impedance attribute that uses the
          Public Transit evaluator because that travel mode models passengers
          riding on public transit, not transit vehicles driving on streets.
      drive_side {String}:
          Specifies the side of the road on which vehicles drive in your transit
          system. This is used to ensure that stops are visited on the correct
          side of the road.LEFT-Vehicles drive on the left side of the
          road.RIGHT-Vehicles drive
          on the right side of the road. This is the
          default.
      bearing_tolerance {Double}:
          The maximum allowed angle between a transit vehicle's estimated
          direction of travel at a stop and the angle of the network edge where
          the stop could locate. If the angles differ by more than this value,
          it is assumed that this is not the correct network edge on which to
          locate the stop, and Network Analyst will continue searching other
          nearby network edges for a more appropriate edge.When calculating
          route shapes along a road network, bearing and
          bearing tolerance are used to more accurately locate transit stops
          along the road network. The transit vehicle's bearing is estimated at
          each stop based on the angles between the current stop and the
          previous and next stops along the transit route.Specify the value in
          units of degrees between 0 and 180. The default
          is 30.
      max_bearing_angle {Double}:
          The maximum allowable difference in bearing angle between the previous
          stop and the current stop and the current stop to the next stop.The
          transit vehicle's bearing is estimated at each stop based on the
          angles between the current stop and the previous and next stops along
          the transit route. When the transit route follows a relatively
          straight road, this angle is a good representation of the bearing.
          However, if the route goes around a corner, makes a U-turn, follows a
          twisty road, or diverts into a parking lot or side road, the average
          angle is not a good estimate of bearing and using this estimate can
          cause the stop to locate on the network far away from where it should
          and worsen the quality of the tool output.The tool will ignore the
          bearing estimate if the difference in angle
          from the previous stop to the current stop and the current stop to the
          next stop is greater than the value specified in this parameter. In
          this situation, the stop will revert to the normal network locating
          behavior and will snap to the closest nonrestricted network
          edge.Specify the value in units of degrees between 0 and 180. The
          default
          is 65.

     OUTPUTS:
      out_shape_lines (Feature Class):
          A line feature class representing the estimated route shapes
          calculated by this tool. Each line in the output represents a unique
          shape required for this GTFS dataset. You can edit the line geometry
          and use this feature class as input to the Features To GTFS Shapes
          tool.
      out_shape_stops (Feature Class):
          A point feature class of GTFS transit stops with an ID associating
          them with each shape line to be created by the tool. In cases where
          the same GTFS stop is visited by multiple shapes, this feature class
          will contain multiple copies of that stop, one for each shape with
          which it is associated. This feature class is useful with definition
          queries when editing one shape line at a time. Use this feature class
          as input to the Features To GTFS Shapes tool.This output feature class
          is not equivalent to the output of the GTFS
          Stops To Features tool. That tool produces a feature class of the GTFS
          stops exactly as they are in the original dataset; this tool may
          produce multiple copies of each stop to associate them with different
          shapes. Use this output feature class in conjunction with the other
          outputs of the Generate Shapes Features From GTFS tool to create a
          shapes.txt file.
      out_gtfs_trips (File):
          The output GTFS trips.txt file. This file will be equivalent
          to the trips.txt file in the input GTFS folder but will include
          thefield added and populated with values corresponding to thefield in
          thefeature class. shape_idshape_idOutput Transit Shape Lines

        """