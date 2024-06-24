# Generated documentation for module arcpy.intelligence


class SelectMovementTracks(object):
    """
    Selects movement tracks based on an area of interest.
    """

    @property
    def description(self) -> str:
        return """

        SelectMovementTracks_intelligence(in_features, track_id_field, area_of_interest, {time_relationship}, {selection_time})

        Selects movement tracks based on an area of interest.

     INPUTS:
      in_features (Feature Layer):
          The features that will be compared with the area_of_interest parameter
          value to identify unique tracks and select the relevant tracks.
      track_id_field (Field):
          The field containing the unique identifiers for the movement track
          points. The field can be either a number or a string.
      area_of_interest (Feature Set):
          The feature or features that will be compared with the in_features
          value to determine the tracks to select.
      time_relationship {String}:
          Specifies the time relationship between the in_features and
          area_of_interest parameter values. If the BEFORE, AFTER, or
          BEFORE_AFTER option is specified, only features that are present in
          the area_of_interest value within the specified time window will be
          included in the output selection. BEFORE_AFTER-When a
          feature's time is before the first time
          identified and after the last time identified for thevalue but within
          the specified range of time from the first identified time and the
          last identified time, the time relationship will be before and after
          the selection time. Area Of Interest         BEFORE-When a
          feature's time is before the first time
          identified for thevalue but within the specified range of time from
          the first identified time, the time relationship will be before the
          selection time. Area Of Interest         AFTER-When a
          feature's time is after the last time identified
          for thevalue but within the specified range of time from the last
          identified time, the time relationship will be after the selection
          time. Area Of Interest         NONE-All tracks associated with
          the unique identifier
          specified inthat are present in thevalue will be returned.
          Track ID FieldArea Of Interest
      selection_time {Time Unit}:
          The time frame that will be used to select features if BEFORE, AFTER,
          or BEFORE_AFTER is specified for the time_relationship parameter.If
          BEFORE or BEFORE_AFTER is specified, the earliest time selected
          will be the first identified time of the features selected from the
          initial selection generated from the in_features and area_of_interest
          parameters, subtracting the time value specified. If AFTER or
          BEFORE_AFTER is specified, the selection time will be added to the
          latest time from the initial selection to determine the selected
          features.

        """