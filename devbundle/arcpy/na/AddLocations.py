# Generated documentation for module arcpy.na


class AddLocations(object):
    """
    Adds input features or records to a network analysis layer. The inputs are added to specific sublayers such as stops and barriers. When the network analysis layer references a network dataset as its network data source, the tool calculates the network locations of the inputs, unless precalculated network location fields are mapped from the inputs.
    """

    @property
    def description(self) -> str:
        return """

        AddLocations_na(in_network_analysis_layer, sub_layer, in_table, {field_mappings}, {search_tolerance}, {sort_field}, {search_criteria;search_criteria...}, {match_type}, {append}, {snap_to_position_along_network}, {snap_offset}, {exclude_restricted_elements}, {search_query;search_query...}, {allow_auto_relocate})

        Adds input features or records to a network analysis layer. The inputs
        are added to specific sublayers such as stops and barriers. When the
        network analysis layer references a network dataset as its network
        data source, the tool calculates the network locations of the inputs,
        unless precalculated network location fields are mapped from the
        inputs.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          The network analysis layer to which the network analysis objects will
          be added.
      sub_layer (String):
          The name of the sublayer of the network analysis layer to which the
          network analysis objects will be added.
      in_table (Table View):
          The feature class or table containing the locations to be added to the
          network analysis sublayer.
      field_mappings {Network Analyst Class FieldMap}:
          The mapping between the input fields of the network analysis sublayer
          to which locations will be added and the fields in the input data or
          specified constants.Input sublayers of network analysis layers have a
          set of input fields
          that can be populated to modify or control analysis behavior. When
          adding locations to the sublayer, you can use this parameter to map
          field values from the input table to these fields in the sublayer. You
          can also use field mappings to specify a constant default value for
          each property.If neither the Field value nor the Default value is
          specified for a
          property, the resulting network analysis objects will have null values
          for that property.A complete list of input fields for each sublayer
          for each network
          analysis layer type is available in the documentation for each layer.
          For example, examine the Route layer's Stops sublayer's input fields.
          An NAClassFieldMappings object obtained from the
          NAClassFieldMappings class is used to specify the parameter value. The
          NAClassFieldMappings object is a collection of NAClassFieldMap objects
          that allow you to specify the default values or map a field name from
          the input features for the properties of the network analysis object.
          If the data being loaded contains network locations or location ranges
          based on the network dataset used for the analysis, map the network
          location fields from the input features to the network location
          properties. Specifying the network location fields in the field
          mappings is similar to using theoption on the tool dialog box.
          Use Network Location FieldsArcGIS Online and some ArcGIS Enterprise
          portals do not support using
          network location fields. For network analysis layers that use one of
          these portals as the network data source, all inputs will be located
          at solve time, and any mapped location fields will be ignored.
      search_tolerance {Linear Unit}:
          The maximum search distance that will be used when locating the input
          features on the network. Features that are outside the search
          tolerance will be left unlocated. The parameter includes a value and
          units.The default value for this parameter is determined based on
          location
          properties stored in the input network analysis layer. If the network
          analysis layer has location settings overrides for the selected
          sublayer, those settings will be used. Otherwise, the network analysis
          layer's default location settings will be used. Setting a nondefault
          value for this parameter updates the network analysis layer's location
          settings overrides for the selected sublayer.The parameter is not used
          when adding locations to sublayers with line
          or polygon geometry, such as Line Barriers and Polygon Barriers.This
          parameter is not used when adding locations using existing
          network location fields.
      sort_field {Field}:
          The field on which the network analysis objects will be sorted
          as they are added to the network analysis layer. The default is
          thefield in the input feature class or table. ObjectID
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
          each.The default value for this parameter is determined based on
          location
          properties stored in the input network analysis layer. If the network
          analysis layer has location settings overrides for the selected
          sublayer, those settings will be used. Otherwise, the network analysis
          layer's default location settings will be used. Setting a nondefault
          value for this parameter updates the network analysis layer's location
          settings overrides for the selected sublayer.This parameter is not
          used when adding locations using existing
          network location fields.This parameter is not used when the network
          analysis layer's network
          data source is ArcGIS Online.
      match_type {Boolean}:
          Find Closest among All Classes
      append {Boolean}:
          Specifies whether new network analysis objects will be appended to
          existing objects.APPEND-The new network analysis objects will be
          appended to the
          existing set of objects in the selected sublayer. This is the
          default.CLEAR-The existing network analysis objects will be deleted
          and
          replaced with the new objects.
      snap_to_position_along_network {Boolean}:
          Specifies whether the inputs will be snapped to their calculated
          network locations or represented at their original geographic
          location.To use curb approach in the analysis to control which side of
          the road
          a vehicle must use to approach a location, do not snap the inputs to
          their network locations, or use a snap offset to ensure that the point
          remains clearly to one side of the road.The parameter is not used when
          adding locations to sublayers with line
          or polygon geometry, such as Line Barriers and Polygon Barriers.This
          parameter is not used when the input network analysis layer's
          network data source is a portal service.NO_SNAP-The geometries of the
          network locations will be based on the
          geometries of the input features. This is the default.SNAP-The
          geometries of the network locations will be snapped to their
          network locations.
      snap_offset {Linear Unit}:
          An offset distance that will be applied when snapping a point to the
          network. An offset distance of zero means the point will be coincident
          with the network feature (typically a line). To offset the point from
          the network feature, enter an offset distance. The offset is in
          relation to the original point location; that is, if the original
          point was on the left side, its new location will be offset to the
          left. If it was originally on the right side, its new location will be
          offset to the right.The default is 5 meters. However, this parameter
          is ignored if
          snap_to_position_along_network is set to NO_SNAP.The parameter is not
          used when adding locations to sublayers with line
          or polygon geometry, such as Line Barriers and Polygon Barriers.This
          parameter is not used when the input network analysis layer's
          network data source is a portal service.
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
          expressions used in ArcGIS.The default value for this parameter is
          determined based on location
          properties stored in the input network analysis layer. If the network
          analysis layer has location settings overrides for the selected
          sublayer, those settings will be used. Otherwise, the network analysis
          layer's default location settings will be used. Setting a nondefault
          value for this parameter updates the network analysis layer's location
          settings overrides for the selected sublayer.This parameter is not
          used when adding locations using existing
          network location fields.This parameter is not used when the network
          analysis layer's network
          data source is ArcGIS Online.
      allow_auto_relocate {Boolean}:
          Specifies whether inputs with existing network location fields can be
          automatically relocated at solve time to ensure valid, routable
          location fields for the analysis.ALLOW-Points located on restricted
          network elements and points
          affected by barriers will be relocated at solve time to the closest
          routable location. This is the default.NO_ALLOW-Network location
          fields will be used at solve time as is,
          even if the points are unreachable, and this may cause the solve to
          fail.The default value for this parameter is determined based on
          location
          properties stored in the input network analysis layer. If the network
          analysis layer has location settings overrides for the selected
          sublayer, those settings will be used. Otherwise, the network analysis
          layer's default location settings will be used. Setting a nondefault
          value for this parameter updates the network analysis layer's location
          settings overrides for the selected sublayer.Even if the automatic
          relocating at solve time is not allowed, inputs
          with no location fields or incomplete location fields will be located
          at solve time.This parameter is not used when the network analysis
          layer's network
          data source is ArcGIS Online.This parameter is not used when the
          network analysis layer's network
          data source is an ArcGIS Enterprise portal that does not support using
          network location fields.

        """