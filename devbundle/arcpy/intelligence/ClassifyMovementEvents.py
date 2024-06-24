# Generated documentation for module arcpy.intelligence


class ClassifyMovementEvents(object):
    """
    Identifies turn events, acceleration events, and speed from an input point track dataset.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyMovementEvents_intelligence(in_features, id_field, out_featureclass, {curvature}, {number_of_points}, {regions_of_interest}, {roi_id_field}, {include_turn_ids}, {exclude_non_turn_events}, {turn_events_representation})

        Identifies turn events, acceleration events, and speed from an input
        point track dataset.

     INPUTS:
      in_features (Feature Layer):
          A time-enabled point feature layer with a field annotating the track
          with which each point is associated. The geometry, object identifier,
          track name, and time will be transferred to the output feature class.
          The input must be in a projected coordinate system.
      id_field (Field):
          A field from the input features that will be used to obtain the unique
          identifiers per point track. The field will be copied to the output
          feature class.
      curvature {Double}:
          The minimum value that is necessary for an event to be
          classified as a turn event. After the curvature is calculated, any
          calculated curvature greater than this value will cause thefield to be
          populated with the relevant turn event, while values less than this
          will cause thefield to be classified as traveling.
          turn_eventturn_eventTurns are calculated using the curvature and
          number_of_points
          parameters. Each point is evaluated based on the bearing from the
          previous point in the track to the current point and from the current
          point to the next point in the track. If the value exceeds the value
          specified for the curvature parameter, it is considered a turn.
          Otherwise, it is considered to be traveling. For tracks representing
          large objects, it is recommended that you increase the
          number_of_points value to account for the longer amount of time to
          conduct a turn.
      number_of_points {Long}:
          The number of points that will be evaluated before and after a given
          point when calculating the bearing difference. When using data with a
          high sampling rate (subsecond), you may need to increase the
          number_of_points parameter value to account for the decreased movement
          that is possible in that brief time period. A value of 1 is suitable
          for automobiles and pedestrians assuming a one-second sampling on the
          input data. Larger values are necessary for aircraft and ships; use a
          value of 5 for these.
      regions_of_interest {Feature Layer}:
          The regions of interest. This input feature layer must be a
          polygon feature class. If a value is provided, afield will be added to
          the out_featureclass parameter. roi
      roi_id_field {Field}:
          A field from the regions_of_interest parameter that contains the
          unique identifiers for each region of interest.
      include_turn_ids {Boolean}:
          Specifies whether turn event identifiers will be created for the
          output feature class.INCLUDE_TURN_IDS-Unique turn event identifiers
          will be
          created.NO_TURN_IDS-Unique turn event identifiers will not be created.
          This is
          the default.
      exclude_non_turn_events {Boolean}:
          Specifies whether to filter features with afield value of
          Traveling. turn_event         ONLY_TURN_EVENTS-Features with
          afield value of Traveling will
          be excluded. turn_event         ALL_FEATURES-Features with
          afield value of Traveling will not
          be excluded; all features will be returned. This is the default.
          turn_event
      turn_events_representation {String}:
          Specifies how the output turn events will be represented.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class that will contain the calculated movement
          events.

        """