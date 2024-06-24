# Generated documentation for module arcpy.nd


class AddSpatialQueryRule(object):
    """
    Adds a diagram rule that automatically appends new network features to the diagrams based on their location relative to the network features currently represented in the diagram.
    """

    @property
    def description(self) -> str:
        return """

        AddSpatialQueryRule_nd(in_utility_network, template_name, is_active, added_features, overlap_type, existing_features, {search_distance}, {added_where_clause}, {existing_where_clause}, {description})

        Adds a diagram rule that automatically appends new network features to
        the diagrams based on their location relative to the network features
        currently represented in the diagram.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network containing the diagram template
          that will be modified.
      template_name (String):
          The name of the diagram template that will be modified.
      is_active (Boolean):
          Specifies whether the rule will be enabled when generating and
          updating diagrams based on the specified template.ACTIVE-The added
          rule will become enabled during the generation and
          update of any diagrams based on the input template. This is the
          default.INACTIVE-The added rule will not become enabled during the
          generation
          or update of any diagrams based on the input template.
      added_features (Feature Class):
          The source feature class to which features will be added.
      overlap_type (String):
          Specifies the spatial relationship that will be evaluated.INTERSECT-
          The features in the added_features source feature class
          will be appended to the diagram if they intersect one of the
          existing_features. This is the default.WITHIN_A_DISTANCE-The features
          in the added_features source feature
          class will be appended to the diagram if they are within the specified
          distance (using Euclidean distance) of one of the existing_features.
          Use the search_distance parameter to specify the distance.CONTAINS-
          The features in the added_features source feature class will
          be appended to the diagram if they contain features from or are
          contained in the existing_features.WITHIN-The features in the
          added_features source feature class will
          be appended to the diagram if they are within the
          existing_features.BOUNDARY_TOUCHES-The features in the added_features
          source feature
          class will be appended to the diagram if they have a boundary that
          touches one of the existing_features. When the existing_features are
          lines or polygons, the boundary of the added_features can only touch
          the boundary of one of the existing_features, and no part of the input
          feature can cross the boundary of one of the
          existing_features.SHARE_A_LINE_SEGMENT_WITH-The features in the
          added_features source
          feature class will be appended to the diagram if they share a line
          segment with one of the existing_features. The added and existing
          features must be line or polygon.CROSSED_BY_THE_OUTLINE_OF-The
          features in the added_features source
          feature class will be appended to the diagram if they are crossed by
          the outline of one of the existing_features. The added and existing
          features must be lines or polygons. If polygons are used for the
          existing_features, the polygon's boundary (line) will be used. Lines
          that cross at a point will be appended; lines that share a line
          segment will not.
      existing_features (Feature Class):
          The source feature class on which the spatial query will run.
      search_distance {Linear Unit}:
          The distance between features in the existing_features parameter and
          features in the added_features parameter. This parameter is only valid
          if the overlap_type parameter is set to INTERSECT, WITHIN_A_DISTANCE,
          CONTAINS, or WITHIN.
      added_where_clause {SQL Expression}:
          The SQL query that will be used to filter the features that will be
          added to the diagram. Without an SQL query, the features based on the
          specified source class that are spatially related to the specified
          existing features will be appended to the diagram.
      existing_where_clause {SQL Expression}:
          The SQL query that will be used to filter the features existing in the
          diagram. Without an SQL query, the features based on the specified
          source class that exist in the diagram will be considered.
      description {String}:
          The description of the rule.

        """