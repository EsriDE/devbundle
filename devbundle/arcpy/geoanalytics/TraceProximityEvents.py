# Generated documentation for module arcpy.geoanalytics


class TraceProximityEvents(object):
    """
    Traces events that are near each other in space (location) and time. The time-enabled point data must include features that represent an instant in time.
    """

    @property
    def description(self) -> str:
        return """

        TraceProximityEvents_geoanalytics(in_points, entity_id_field, output_name, distance_method, spatial_search_distance, temporal_search_distance, entities_of_interest_input_type, {entities_interest_ids;entities_interest_ids...}, {entities_interest_layer}, {include_tracks_layer}, {max_trace_depth}, {attribute_match_criteria;attribute_match_criteria...}, {data_store})

        Traces events that are near each other in space (location) and time.
        The time-enabled point data must include features that represent an
        instant in time.

     INPUTS:
      in_points (Feature Set):
          The time-enabled point feature class that will be used to trace
          proximity events.
      entity_id_field (Field):
          The text field representing unique IDs for each entity.
      output_name (String):
          The name of the output feature service.
      distance_method (String):
          Specifies the distance type that will be used with
          theparameter. Spatial Search DistancePLANAR-Planar distance
          will be used between features. This is the
          default.GEODESIC-Geodesic distance will be used between features. This
          line
          type takes into account the curvature of the spheroid and correctly
          deals with data near the dateline and poles.
      spatial_search_distance (Linear Unit):
          The maximum distance between two points to be considered in proximity.
          Features within the spatial search distance and temporal search
          distance criteria are considered to be in proximity of each other.
      temporal_search_distance (Time Unit):
          The maximum duration between two points to be considered in proximity.
          Features within the temporal search distance and that meet the spatial
          search distance criteria are considered to be in proximity of each
          other.
      entities_of_interest_input_type (String):
          Specifies the entities of interest.ID_START_TIME-Entity names and
          times will be used as the entities of
          interest. This is the default.SELECTED_FEATURE-The selected feature in
          a specified entity of
          interest layer will be used as the entities of interest.
      entities_interest_ids {Value Table}:
          The entity names and start times for the entities of interest. This
          parameter is supported only when ID_START_TIME is specified for the
          entities_of_interest_input_type parameter.Entity ID-A unique entity
          name. The names are case sensitive.Starting
          from-An optional starting time to trace an entity of
          interest. If a time is not specified, January 1, 1970, will be used.
      entities_interest_layer {Record Set}:
          The layer or table that contains the entities of interest. This
          parameter is supported only when SELECTED_FEATURE is specified for the
          entities_of_interest_input_type parameter.
      include_tracks_layer {Boolean}:
          Specifies whether an output layer containing the first trace event and
          all subsequent features for that specified entity will be
          generated.TRACKS-An output layer containing the first trace event and
          all
          subsequent features will be generated.NO_TRACKS-An output layer
          containing the first trace event and all
          subsequent features will not be generated.
      max_trace_depth {Long}:
          The maximum degrees of separation between an entity of interest and an
          entity farther down the trace (downstream).
      attribute_match_criteria {Field}:
          The fields used to constrain the proximity event.
      data_store {String}:
          Specifies the ArcGIS Data Store where the output will be saved. The
          default is SPATIOTEMPORAL_DATA_STORE. All results stored in a
          spatiotemporal big data store will be stored in WGS84. Results stored
          in a relational data store will maintain their coordinate
          system.SPATIOTEMPORAL_DATA_STORE-Output will be stored in a
          spatiotemporal
          big data store. This is the default.RELATIONAL_DATA_STORE-Output will
          be stored in a relational data
          store.

        """