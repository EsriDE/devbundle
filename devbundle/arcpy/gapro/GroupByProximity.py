# Generated documentation for module arcpy.gapro


class GroupByProximity(object):
    """
    Groups features that are within spatial or spatiotemporal proximity to each other.
    """

    @property
    def description(self) -> str:
        return """

        GroupByProximity_gapro(input_layer, output, spatial_relationship, {spatial_near_distance}, {temporal_relationship}, {temporal_near_distance}, {attribute_relationship})

        Groups features that are within spatial or spatiotemporal proximity to
        each other.

     INPUTS:
      input_layer (Feature Layer):
          The point, line, or polygon features that will be grouped.
      spatial_relationship (String):
          Specifies the type of relationship that features will be grouped
          by.INTERSECTS-Features will be grouped when features or portions of
          features overlap. This is the default.TOUCHES-Features will be grouped
          with another feature if they have an
          intersecting vertex, but the features do not
          overlap.NEAR_PLANAR-Features will be grouped when a vertex or edge is
          within a
          given planar distance of another feature.NEAR_GEODESIC-Features will
          be grouped when a vertex or edge is within
          a given geodesic distance of another feature.
      spatial_near_distance {Linear Unit}:
          The distance that will be used to group near features. This parameter
          is only used when the spatial_relationship parameter value is
          NEAR_PLANAR or NEAR_GEODESIC.
      temporal_relationship {String}:
          Specifies the time criteria that will be used to match features. When
          the parameter is set to INTERSECTS or NEAR, features are grouped when
          both the spatial and time criteria are met. Time must be enabled on
          the input to support this option.INTERSECTS-Features will be grouped
          when any part of a feature's time
          overlaps another feature. This is the default.NEAR-Features will be
          grouped when the feature's time is within a
          range of time of another feature.NONE-Time will not be used to group
          features.
      temporal_near_distance {Time Unit}:
          The temporal distance that will be used to group near features. This
          parameter is only used when the temporal_relationship parameter value
          is Near.
      attribute_relationship {String}:
          An ArcGIS Arcade expression that will be used to group
          features by. For example, $a["Amount"] == $b["Amount"] groups features
          when thefield has the same value. Amount

     OUTPUTS:
      output (Feature Class):
          The output feature class with grouped features represented by
          a new field named. group_id

        """