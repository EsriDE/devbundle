# Generated documentation for module arcpy.intelligence


class CompareAreas(object):
    """
    Compares movement point tracks across multiple known areas of interest.
    """

    @property
    def description(self) -> str:
        return """

        CompareAreas_intelligence(in_point_features, in_area_features, out_featureclass, point_id_field, area_id_field, relationship, {time_difference}, {time_relationship}, {include_time_statistics})

        Compares movement point tracks across multiple known areas of
        interest.

     INPUTS:
      in_point_features (Feature Layer):
          The point features representing the movement track points. The layer
          can be time enabled.
      in_area_features (Feature Layer):
          The area features representing the areas of interest that will be used
          to identify unique movement track point identifiers. The layer can be
          time enabled.
      point_id_field (Field):
          The field containing the unique identifiers for the movement track
          points. The field can be either a number or a string.
      area_id_field (Field):
          The field containing the unique identifiers for the areas of interest.
          The field can be either a number or a string.
      relationship (String):
          Specifies the relationship between the inputs.LOCATION_ONLY-Points
          and area features will be evaluated based on
          spatial co-occurrence.LOCATION_TIME-Points and area features will be
          evaluated based on
          spatial and temporal co-occurrence.
      time_difference {Time Unit}:
          The time allowed between the in_point_features and in_area_features
          parameter values before a spatial relationship is considered invalid.
          This parameter is enabled when the relationship parameter is set to
          LOCATION_TIME and both inputs are time enabled.
      time_relationship {String}:
          Specifies the time relationship between the in_point_features and
          in_area_features parameter values.This parameter is only enabled when
          the relationship parameter is set
          to LOCATION_TIME and both inputs are time enabled. If the NEAR_BEFORE
          or NEAR_AFTER option is specified, only features in the
          in_point_features parameter value that are within the specified time
          window will be evaluated for inclusion in the out_featureclass
          parameter value.NEAR-When a point feature time is within a specified
          range of time
          from the area feature time, the point feature time is near the area
          feature time.NEAR_BEFORE-When a point feature time is before the area
          feature time
          but within a specified range of time from the join time, the point
          feature time is near before the area feature time.NEAR_AFTER-When a
          point feature time is after the area feature time
          but within a specified range of time from the join time, the point
          feature time is near after the area feature time.
      include_time_statistics {Boolean}:
          Specifies whether time statistics fields will be
          added.TIME_STATISTICS-Time statistics fields will be added to the
          output.NO_TIME_STATISTICS-Time statistics fields will not be added to
          the
          output.

     OUTPUTS:
      out_featureclass (Feature Layer):
          The output area feature class. The output will contain a copy of the
          in_area_features geometry and the unique identifiers from the
          area_id_field and point_id_field parameters.If both the
          in_point_features and in_area_features parameter values
          are time enabled and relationship is set to LOCATION_TIME, only the
          features matching the geometry and the time span will be returned.

        """