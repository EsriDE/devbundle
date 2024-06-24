# Generated documentation for module arcpy.na


class CalculateLocations(object):
    """
    Locates input features on a network and adds fields to the input features that describe the network locations. The tool is used to precalculate the network locations of inputs that will be used in a Network Analyst workflow, improving performance of the analysis at solve time. The tool stores the calculated network locations of the inputs in fields in the input data.
    """

    @property
    def description(self) -> str:
        return """

        CalculateLocations_na(in_point_features, {in_network_dataset}, {search_tolerance}, {search_criteria;search_criteria...}, {match_type}, {source_ID_field}, {source_OID_field}, {position_field}, {side_field}, {snap_X_field}, {snap_Y_field}, {distance_field}, {snap_Z_field}, {location_field}, {exclude_restricted_elements}, {search_query;search_query...}, {travel_mode})

        Locates input features on a network and adds fields to the input
        features that describe the network locations. The tool is used to
        precalculate the network locations of inputs that will be used in a
        Network Analyst workflow, improving performance of the analysis at
        solve time. The tool stores the calculated network locations of the
        inputs in fields in the input data.

     INPUTS:
      in_point_features (Table View):
          The input features for which the network locations will be
          calculated.For line and polygon features, since the network location
          information
          is stored in a BLOB field, only geodatabase feature classes are
          supported.
      in_network_dataset {Network Dataset Layer}:
          The network dataset that will be used to calculate the locations.This
          parameter is required unless a sublayer of a network analysis
          layer is used as input features. In that case, don't specify a value
          for this parameter or set it to the network dataset referenced by the
          network analysis layer.
      search_tolerance {Linear Unit}:
          The maximum search distance that will be used when locating the input
          features on the network. Features that are outside the search
          tolerance will be left unlocated. The parameter includes a value and
          units.The default is 5000 meters.If the input features are a sublayer
          of a network analysis layer, the
          default value for this parameter is determined based on location
          properties stored in the input network analysis layer. If the network
          analysis layer has location settings overrides for the selected
          sublayer, those settings will be used. Otherwise, the network analysis
          layer's default location settings will be used. Setting a nondefault
          value for this parameter updates the network analysis layer's location
          settings overrides for the selected sublayer.The parameter is not used
          when calculating locations for line or
          polygon features.
      search_criteria {Value Table}:
          The edge and junction sources in the network dataset that will be
          searched when locating inputs on the network. For example, if the
          network dataset references separate feature classes representing
          streets and sidewalks, you can locate inputs on streets but not on
          sidewalks.The parameter value is specified as a list with nested
          lists. The
          nested lists are composed of two values indicating the name and snap
          type of each network source. The following are the available
          snap type choices for each
          network source:        NONE-The point will not locate on elements in
          this network
          source.SHAPE-The point will locate on the closest point of an element
          in this
          network source.For example, a parameter value of
          [["Streets","SHAPE"],["Streets_ND_Junctions","NONE"]] specifies that
          the search can locate on the shape of the Streets source but not on
          the Streets_ND_Junctions source.Any network edge or junction source
          that is not included in this list
          will use its default snap type. It is recommended that you include all
          network sources in your list and explicitly set the snap type for
          each.The default value is to locate on all network sources except
          override
          junctions created by running the Dissolve Network tool and system
          junctions.If the input features are a sublayer of a network analysis
          layer, the
          default value for this parameter is determined based on location
          properties stored in the input network analysis layer. If the network
          analysis layer has location settings overrides for the selected
          sublayer, those settings will be used. Otherwise, the network analysis
          layer's default location settings will be used. Setting a nondefault
          value for this parameter updates the network analysis layer's location
          settings overrides for the selected sublayer.
      match_type {Boolean}:
          Find Closest among All Classes
      source_ID_field {Field}:
          The name of the field to be created or updated that will be
          populated with the ID of the network dataset source feature class for
          the input feature's computed network location. The default value is.
          SourceIDThe parameter is not used when calculating locations for line
          or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      source_OID_field {Field}:
          The name of the field to be created or updated that will be
          populated with thefield value of the network dataset source feature
          class for the input feature's computed network location. The default
          value is. ObjectIDSourceOIDThe parameter is not used when
          calculating locations for line or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      position_field {Field}:
          The name of the field to be created or updated describing the
          computed network location's percent along the network element where it
          was located. The default value is. PosAlongThe parameter is not
          used when calculating locations for line or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      side_field {Field}:
          The name of the field to be created or updated describing the
          side of the network edge on which the computed network location falls.
          The default value is. SideOfEdgeThe parameter is not used when
          calculating locations for line or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      snap_X_field {Field}:
          The name of the field to be created or updated with the
          x-coordinate of the computed network location. The default value is.
          SnapXThe parameter is not used when calculating locations for line or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      snap_Y_field {Field}:
          The name of the field to be created or updated with the
          y-coordinate of the computed network location. The default value is.
          SnapYThe parameter is not used when calculating locations for line or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      distance_field {Field}:
          The name of the field to be created or updated describing the
          distance in meters of the original point feature from its computed
          network location. The default value is.
          DistanceToNetworkInMetersThe parameter is not used when calculating
          locations for line or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      snap_Z_field {Field}:
          The name of the field to be created or updated with the
          z-coordinate of the computed network location. The default value is.
          SnapZThe parameter is used only when the input network dataset
          supports
          connectivity based on z-coordinate values of the network sources.The
          parameter is not used when calculating locations for line or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      location_field {Field}:
          The name of the field to be created or updated with the
          location ranges of the computed network locations for line or polygon
          features. The default value is. LocationsThe parameter is used
          only when calculating locations for line or
          polygon features.Do not use this parameter when the input features are
          a sublayer of a
          network analysis layer. Network locations in a sublayer must be stored
          in location fields with the default names or they will not be used
          when the layer is solved.
      exclude_restricted_elements {Boolean}:
          Exclude Restricted Portions of the Network
      search_query {Value Table}:
          A query that restricts the search to a subset of the features within a
          source feature class. This is useful if you don't want to find
          features that may be unsuited for a network location. For example, if
          you don't want to locate on highway ramps, you can define a query to
          exclude them. A separate SQL expression can be specified per edge or
          junction source feature class of the network dataset.The parameter
          value is specified as a list with nested lists, with one
          entry per network source. Each inner list is composed of two values
          indicating the name of the network source and the SQL expression used
          as the query for that source. An empty string, "", indicates no query
          for a particular source.For example, the value [["Streets",
          "ROAD_CLASS <> 3"],
          ["Streets_ND_Junctions", ""]] specifies an SQL expression for the
          Streets source feature class and no expression for the
          Streets_ND_Junctions source feature class. If a network source is not
          included in the list, it is interpreted to have no query. The value
          [["Streets", "ROAD_CLASS <> 3"]] is equivalent to [["Streets",
          "ROAD_CLASS <> 3"], ["Streets_ND_Junctions", ""]].For more information
          on SQL syntax, see SQL reference for query
          expressions used in ArcGIS.By default, no query is used for any
          source.If the input features are a sublayer of a network analysis
          layer, the
          default value for this parameter is determined based on location
          properties stored in the input network analysis layer. If the network
          analysis layer has location settings overrides for the selected
          sublayer, those settings will be used. Otherwise, the network analysis
          layer's default location settings will be used. Setting a nondefault
          value for this parameter updates the network analysis layer's location
          settings overrides for the selected sublayer.
      travel_mode {String}:
          The name of the travel mode that will be used.If you select a travel
          mode, the travel mode settings, such as
          restrictions and impedance attributes, will be considered when
          calculating network location. For example, if the closest network edge
          to one of the input points is restricted when the selected travel mode
          is applied, the tool will locate the point on the next-closest network
          edge that is not restricted.The available travel modes depend on the
          in_network_dataset parameter
          value.An arcpy.na.TravelMode object and a string containing the valid
          JSON
          representation of a travel mode can also be used as input to the
          parameter.If a sublayer of a network analysis layer is used as input
          features,
          do not set a value for this parameter. When network locations are
          calculated, the network analysis layer's current travel mode will
          automatically be used.

        """