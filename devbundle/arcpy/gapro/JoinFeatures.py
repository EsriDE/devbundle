# Generated documentation for module arcpy.gapro


class JoinFeatures(object):
    """
    Joins attributes from one layer to another based on spatial, temporal, or attribute relationships, or a combination of those relationships.
    """

    @property
    def description(self) -> str:
        return """

        JoinFeatures_gapro(target_layer, join_layer, output, join_operation, {spatial_relationship}, {spatial_near_distance}, {temporal_relationship}, {temporal_near_distance}, {attribute_relationship;attribute_relationship...}, {summary_fields;summary_fields...}, {join_condition}, {keep_all_target_features}, {include_distance}, {distance_unit})

        Joins attributes from one layer to another based on spatial, temporal,
        or attribute relationships, or a combination of those relationships.

     INPUTS:
      target_layer (Table View):
          Contains the target features. The attributes from the target features
          and the attributes from the joined features will be transferred to the
          output.
      join_layer (Table View):
          Contains the join features. The attributes from the join
          features will be joined to the attributes of the target features. See
          the explanation for theparameter for details about how the aggregation
          of joined attributes are affected by the type of join operation.
          Join Operation
      join_operation (String):
          Specifies how joins between the target_layer values and join_layer
          values will be handled in the output feature if multiple join features
          have the same spatial relationship with a single target
          feature.JOIN_ONE_TO_ONE-The attributes from the multiple join
          features will
          be aggregated. For example, if a point target feature is in two
          separate polygon join features, the attributes from the two polygons
          will be aggregated before being transferred to the output point
          feature class. If one polygon has an attribute value of 3 and the
          other has a value of 7, and the summary statistic sum is specified for
          that field, the aggregated value in the output feature class will be
          10. This is the default, and only the count statistic is
          returned.JOIN_ONE_TO_MANY-The output feature class will contain
          multiple copies
          (records) of the target feature. For example, if a single-point target
          feature is in two separate polygon join features, the output feature
          class will contain two copies of the target feature: one record with
          the attributes of one polygon and another record with the attributes
          of the other polygon. There are no summary statistics available with
          this option.
      spatial_relationship {String}:
          Specifies the criteria that will be used to spatially join
          features.INTERSECTS-The features in the join features will be matched
          if they
          intersect a target feature. This is the default.EQUALS-The features
          in the join features will be matched if they are
          the same geometry as a target feature.NEAR-The features in the join
          features will be matched if they are
          within a specified distance of a target feature. The distance is
          measured using planar distance. Specify a distance in the
          spatial_near_distance parameter.NEAR_GEODESIC-The features in the join
          features will be matched if
          they are within a specified distance of a target feature. The distance
          is measured geodesically. Specify a distance in the
          spatial_near_distance parameter.CONTAINS-The features in the join
          features will be matched if a target
          feature contains them. The target features must be polygons or
          polylines. The join features can only be polygons when the target
          features are also polygons. A polygon can contain any feature type. A
          polyline can contain only polylines and points. A point cannot contain
          any feature, not even a point. If the join feature is entirely on the
          boundary of the target feature (no part is properly inside or
          outside), the feature will not be matched.WITHIN-The features in the
          join features will be matched if a target
          feature is within them. This is the opposite of the contains
          relationship. The target features can only be polygons when the join
          features are also polygons. A point can be a join feature only if a
          point is also a target feature. If the entirety of the feature in the
          join features is on the boundary of the target feature, the feature
          will not be matched.TOUCHES-The features in the join features will be
          matched if they have
          a boundary that touches a target feature. When the target and join
          features are lines or polygons, the boundary of the join feature can
          only touch the boundary of the target feature, and no part of the join
          feature can cross the boundary of the target feature.CROSSES-The
          features in the join features will be matched if a target
          feature is crossed by their outline. The join and target features must
          be lines or polygons. If polygons are used for the join or target
          features, the polygon's boundary (line) will be used. Lines that cross
          at a point will be matched, but lines that share a line segment will
          not.OVERLAPS-The features in the join features will be matched if they
          overlap a target feature.
      spatial_near_distance {Linear Unit}:
          The distance from a target feature within which join features will be
          considered for the spatial join. A search radius is only valid when
          the spatial_relationship parameter value is NEAR or NEAR_GEODESIC.
      temporal_relationship {String}:
          Specifies the time criteria that will be used to match
          features.MEETS-When a target time interval end is equal to the join
          time
          interval start, the target time meets the join time.MET_BY-When a
          target time interval start is equal to the join time
          interval end, the target time is met by the join time.OVERLAPS-When a
          target time interval starts and ends before the start
          and end of the join time interval, the target time overlaps the join
          time.OVERLAPPED_BY-When a target time interval starts and ends after
          the
          start and end time of the join time interval, the target time is
          overlapped by the join time.DURING-When a target time occurs between
          the start and end of the join
          time interval, the target time is during the join time.CONTAINS-When a
          join feature time occurs between the start and end of
          the target time interval, the target time contains the join
          time.EQUALS-Two times are considered equal if their instants or
          intervals
          are identical.FINISHES-When a target time ends at the same time as a
          join time, and
          the target time started after the join time, the target time finishes
          the join time.FINISHED_BY-When a join feature time ends at the same
          time as a target
          time, and the join time started after the target time, the target time
          is finished by the join time.STARTS-When a target time starts at the
          same time as the join time
          interval and ends before the join time interval ends, the target time
          starts the join time.STARTED_BY-When a target interval time starts at
          the same time as the
          join time and ends after the join time, the target time is started by
          the join time.INTERSECTS-When any part of a target time occurs at the
          same time as
          the join time, the target time intersects the join time.NEAR-When a
          target time is within a specified range of time from the
          join time, the target time is near the join time.NEAR_BEFORE-When a
          target time is before the join time but within a
          specified range of time from the join time, the target time is near
          before the join time.NEAR_AFTER-When a target time is after the join
          time but within a
          specified range of time from the join time, the target time is near
          after the join time.
      temporal_near_distance {Time Unit}:
          The distance in time from a target feature within which join features
          will be considered for the spatial join. A time is only valid when the
          temporal_relationship parameter value is NEAR, NEAR_BEFORE, or
          NEAR_AFTER and both feature are time enabled.
      attribute_relationship {Value Table}:
          Joins features based on values in an attribute field. Specify
          the attribute field from the target layer that matches an attribute
          field from the join layer. Target Field-An attribute field from
          the target layer containing
          values to match.Join Field-An attribute field from the join layer
          containing values to
          match.
      summary_fields {Value Table}:
          The statistics that will be calculated on specified fields.COUNT-The
          number of nonnull values. It can be used on numeric fields
          or strings. The count of [null, 0, 2] is 2.SUM-The sum of numeric
          values in a field. The sum of [null, null, 3]
          is 3.MEAN-The mean of numeric values. The mean of [0,2, null] is
          1.MIN-The minimum value of a numeric field. The minimum of [0, 2,
          null]
          is 0.MAX-The maximum value of a numeric field. The maximum value of
          [0, 2,
          null] is 2.STDDEV-The standard deviation of a numeric field. The
          standard
          deviation of [1] is null. The standard deviation of [null, 1,1,1] is
          null.VAR-The variance of a numeric field in a track. The variance of
          [1] is
          null. The variance of [null, 1,1,1] is null.RANGE-The range of a
          numeric field. This is calculated as the minimum
          value subtracted from the maximum value. The range of [0, null, 1] is
          1. The range of [null, 4] is 0.ANY-A sample string from a field of
          type string.
      join_condition {String}:
          Applies a condition to specified fields. Only features with fields
          that meet these conditions will be joined.For example, you can apply a
          join condition to features in which the
          HealthSpending attribute in the join layer is more than 20 percent of
          the Income attribute in the target layer. Use an Arcade expression
          such as $join["HealthSpending"] > $target["Income"] * .2.
      keep_all_target_features {Boolean}:
          Specifies whether all target features will be maintained in the output
          feature class (a left outer join) or only those that have the
          specified relationships with the join features (an inner
          join).KEEP_ALL-All target features will be maintained in the
          output.KEEP_COMMON-Only those target features that have the specified
          relationships will be maintained in the output feature class. This is
          the default.
      include_distance {Boolean}:
          Specifies whether the spatial distance or the temporal difference will
          be included in the result. This parameter is active when the
          join_operation parameter
          value is JOIN_ONE_TO_MANY and either of the following is true:
          The spatial_relationship parameter value is NEAR or NEAR_GEODESIC.The
          temporal_relationship parameter value is NEAR, NEAR_BEFORE, or
          NEAR_AFTER.INCLUDE_DISTANCE-The spatial distance or the temporal
          difference will
          be included in the result.NO_INCLUDE_DISTANCE-Neither the spatial
          distance nor the temporal
          difference will be included in the result. This is the default.
      distance_unit {String}:
          Specifies the unit of measure that will be used for distance values in
          the output feature class.METERS-The unit of measure will be meters.
          This is the
          default.KILOMETERS-The unit of measure will be kilometers.MILES-The
          unit of measure will be US survey miles.NAUTICAL_MILES-The unit of
          measure will be US survey nautical miles.YARDS-The unit of measure
          will be US survey yards.FEET-The unit of measure will be US survey
          feet.MILES_INT-The unit of measure will be statute
          miles.NAUTICAL_MILES_INT-The unit of measure will be international
          nautical
          miles.YARDS_INT-The unit of measure will be international
          yards.FEET_INT-The unit of measure will be international feet.

     OUTPUTS:
      output (Feature Class / Table):
          The new feature class containing the target layer features with joined
          features.

        """