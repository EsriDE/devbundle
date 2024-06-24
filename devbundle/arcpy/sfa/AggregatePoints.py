# Generated documentation for module arcpy.sfa


class AggregatePoints(object):
    """
    Uses a layer of point features and a layer of polygon features to determine which points fall within each polygon's area. After determining this point-in-polygon spatial relationship, statistics about all points in the polygon are calculated and assigned to the area.
    """

    @property
    def description(self) -> str:
        return """

        AggregatePoints_sfa(pointLayer, polygonLayer, outputName, keepBoundariesWithNoPoints, {summaryFields;summaryFields...}, {groupByField}, {minorityMajority}, {percentPoints})

        Uses a layer of point features and a layer of polygon features to
        determine which points fall within each polygon's area. After
        determining this point-in-polygon spatial relationship, statistics
        about all points in the polygon are calculated and assigned to the
        area.

     INPUTS:
      pointLayer (Feature Set):
          The point features that will be aggregated into the polygons in the
          polygon layer.
      polygonLayer (Feature Set):
          The polygon features (areas) into which the input points will be
          aggregated.
      outputName (String):
          The name of the output layer to create on your portal.
      keepBoundariesWithNoPoints (Boolean):
          Specifies whether the polygons that have no points within them should
          be returned in the output.KEEP_EMPTY-Keep polygons that have no
          points. This is the
          default.REMOVE_EMPTY-Do not return polygons with no points in the
          output.
      summaryFields {Value Table}:
          A list of field names and statistical summary type that you
          wish to calculate for all points within each polygon. The count of
          points within each polygon is always returned. The following statistic
          types are supported:        SUM-The total value.MIN-The smallest
          value.MAX-The largest
          value.MEAN-The average or mean value.STD-The standard deviation.
      groupByField {Field}:
          A field name in the pointLayer. Points that have the same value for
          the group by field will have their own counts and summary field
          statistics.You can create statistical groups using an attribute in the
          analysis
          layer. For example, if you are aggregating crimes to neighborhood
          boundaries, you may have a Crime_type attribute with five different
          crime types. Each unique crime type forms a group, and the statistics
          you choose will be calculated for each unique value of Crime_type.
          When you choose a grouping attribute, two results are created: the
          result layer and a related table containing the statistics.
      minorityMajority {Boolean}:
          This Boolean parameter is applicable only when a groupByField is
          specified. If true, the minority (least dominant) or the majority
          (most dominant) attribute values for each group field within each
          boundary are calculated. Two new fields are added to the output layer
          prefixed with Majority_ and Minority_.NO_MIN_MAJ-Do not add minority
          and majority fields. This is the
          default.ADD_MIN_MAJ-Add minority and majority fields.
      percentPoints {Boolean}:
          This Boolean parameter is applicable only when a groupByField is
          specified. If set to ADD_PERCENT, the percentage count of points for
          each unique groupByField value is calculated. A new field is added to
          the output group summary table containing the percentages of each
          attribute value within each group. If minorityMajority is true, two
          additional fields are added to the output containing the percentages
          of the minority and majority attribute values within each
          group.NO_PERCENT-Do not add percentage fields. This is the
          default.ADD_PERCENT-Add percentage fields.

        """