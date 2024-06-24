# Generated documentation for module arcpy.analysis


class SpatialJoin(object):
    """
    Joins attributes from one feature to another based on the spatial relationship. The target features and the joined attributes from the join features are written to the output feature class.
    """

    @property
    def description(self) -> str:
        return """

        SpatialJoin_analysis(target_features, join_features, out_feature_class, {join_operation}, {join_type}, {field_mapping}, {match_option}, {search_radius}, {distance_field_name}, {match_fields;match_fields...})

        Joins attributes from one feature to another based on the spatial
        relationship. The target features and the joined attributes from the
        join features are written to the output feature class.

     INPUTS:
      target_features (Feature Layer):
          The attributes from the target features and the attributes from the
          joined features will be transferred to the output feature class.
          However, a subset of attributes can be defined by the field map
          parameter.
      join_features (Feature Layer):
          The attributes from the join features will be joined to the attributes
          of the target features. See the explanation of the join_operation
          parameter for details on how the aggregation of joined attributes are
          affected by the type of join operation.
      join_operation {String}:
          The operation that will join the target features and join features in
          the output feature class if multiple join features are found that have
          the same spatial relationship with a single target
          feature.JOIN_ONE_TO_ONE-If multiple join features are found that have
          the same
          spatial relationship with a single target feature, the attributes from
          the multiple join features will be aggregated using a field map merge
          rule. For example, if a point target feature is found within two
          separate polygon join features, the attributes from the two polygons
          will be aggregated before being transferred to the output point
          feature class. If one polygon has an attribute value of 3 and the
          other has a value of 7, and a Sum merge rule is specified, the
          aggregated value in the output feature class will be 10. This is the
          default.JOIN_ONE_TO_MANY-If multiple join features are found that have
          the
          same spatial relationship with a single target feature, the output
          feature class will contain multiple copies (records) of the target
          feature. For example, if a single point target feature is found within
          two separate polygon join features, the output feature class will
          contain two copies of the target feature: one record with the
          attributes of one polygon and another record with the attributes of
          the other polygon.
      join_type {Boolean}:
          Specifies whether all target features will be maintained in the output
          feature class (an outer join) or only those that have the specified
          spatial relationship with the join features (an inner
          join).KEEP_ALL-All target features will be maintained in the output
          (outer
          join). This is the default.KEEP_COMMON-Only those target features
          that have the specified
          spatial relationship with the join features will be maintained in the
          output feature class (inner join). For example, if a point feature
          class is specified for the target features, and a polygon feature
          class is specified for the join features with a match_option value of
          WITHIN, the output feature class will only contain those target
          features that are within a polygon join feature. Any target features
          not within a join feature will be excluded from the output.
      field_mapping {Field Mappings}:
          The fields that will be included in the output feature class with
          their respective properties and source fields. The output includes all
          fields from the join and target features by default.Use the field map
          to add, delete, rename, and reorder fields, as well
          as change other field properties.The field map can be used to combine
          values from two or more input
          fields into a single output field.In Python, use the FieldMappings
          class to define this parameter.
      match_option {String}:
          Specifies the criteria that will be used to match rows.INTERSECT-The
          features in the join features will be matched if they
          intersect a target feature. This is the default. Specify the distance
          in the search_radius parameter.INTERSECT_3D-The features in the join
          features will be matched if
          they intersect a target feature in three-dimensional space (x, y, and
          z). Specify the distance in the search_radius
          parameter.WITHIN_A_DISTANCE-The features in the join features will be
          matched if
          they are within a specified distance of a target feature. Specify the
          distance in the search_radius
          parameter.WITHIN_A_DISTANCE_GEODESIC-This is the same as
          WITHIN_A_DISTANCE
          except that geodesic distance is used rather than planar distance.
          Distance between features will be calculated using a geodesic formula
          that takes into account the curvature of the spheroid and correctly
          handles data near and across the dateline and poles. Use this option
          if the data covers a large geographic extent or the coordinate system
          of the inputs is unsuitable for distance
          calculations.WITHIN_A_DISTANCE_3D-The features in the join features
          will be matched
          if they are within a specified distance of a target feature in three-
          dimensional space. Specify the distance in the search_radius
          parameter.CONTAINS-The features in the join features will be matched
          if a target
          feature contains them. The target features must be polygons or
          polylines. For this option, the target features cannot be points, and
          the join features can only be polygons when the target features are
          also polygons.COMPLETELY_CONTAINS-The features in the join features
          will be matched
          if a target feature completely contains them. A polygon can completely
          contain any feature. A point cannot completely contain any feature,
          not even a point. A polyline can completely contain only polyline and
          point features.CONTAINS_CLEMENTINI-This spatial relationship produces
          the same
          results as COMPLETELY_CONTAINS except that if the join feature is
          entirely on the boundary of the target feature (no part is properly
          inside or outside) the feature will not be matched. Clementini defines
          the boundary polygon as the line separating inside and outside, the
          boundary of a line is defined as its end points, and the boundary of a
          point is always empty.WITHIN-The features in the join features will be
          matched if a target
          feature is within them. This is the opposite of CONTAINS. For this
          option, the target features can only be polygons when the join
          features are also polygons. A point can be a join feature only if a
          point is the target.COMPLETELY_WITHIN-The features in the join
          features will be matched if
          a target feature is completely within them. This is the opposite of
          COMPLETELY_CONTAINS.WITHIN_CLEMENTINI-The result will be identical to
          WITHIN except if the
          entirety of the feature in the join features is on the boundary of the
          target feature, the feature will not be matched. Clementini defines
          the boundary polygon as the line separating inside and outside, the
          boundary of a line is defined as its end points, and the boundary of a
          point is always empty.ARE_IDENTICAL_TO-The features in the join
          features will be matched if
          they are identical to a target feature. Both join and target feature
          must be of the same shape type-point to point, line to line, or
          polygon to polygon.BOUNDARY_TOUCHES-The features in the join features
          will be matched if
          they have a boundary that touches a target feature. When the target
          and join features are lines or polygons, the boundary of the join
          feature can only touch the boundary of the target feature and no part
          of the join feature can cross the boundary of the target
          feature.SHARE_A_LINE_SEGMENT_WITH-The features in the join features
          will be
          matched if they share a line segment with a target feature. The join
          and target features must be lines or
          polygons.CROSSED_BY_THE_OUTLINE_OF-The features in the join features
          will be
          matched if a target feature is crossed by their outline. The join and
          target features must be lines or polygons. If polygons are used for
          the join or target features, the polygon's boundary (line) will be
          used. Lines that cross at a point will be matched; lines that share a
          line segment will not be matched.HAVE_THEIR_CENTER_IN-The features in
          the join features will be matched
          if a target feature's center falls within them. The center of the
          feature is calculated as follows: For polygon and multipoint, the
          geometry's centroid is used, and for line input, the geometry's
          midpoint is used. Specify the distance in the search_radius
          parameter.CLOSEST-The feature in the join features that is closest to
          a target
          feature will be matched. See the usage tip for more information.
          Specify the distance in the search_radius
          parameter.CLOSEST_GEODESIC-This is the same as CLOSEST except that
          geodesic
          distance is used rather than planar distance. Use this option if the
          data covers a large geographic extent or the coordinate system of the
          inputs is unsuitable for distance calculationsLARGEST_OVERLAP-The
          feature in the join features will be matched with
          the target feature with the largest overlap.
      search_radius {Linear Unit}:
          Join features within this distance of a target feature will be
          considered for the spatial join. A search radius is only valid when
          the spatial relationship is specified (the match_option parameter is
          set to INTERSECT, WITHIN_A_DISTANCE, WITHIN_A_DISTANCE_GEODESIC,
          HAVE_THEIR_CENTER_IN, CLOSEST, or CLOSEST_GEODESIC). For example,
          using a search radius of 100 meters with the WITHIN_A_DISTANCE spatial
          relationship will join feature within 100 meters of a target feature.
          For the three within-a-distance relationships, if no value is
          specified for the search_radius, a distance of 0 is used.
      distance_field_name {String}:
          The name of the field that contains the distance between the target
          feature and the closest join feature. This field will be added to the
          output feature class. This parameter is only valid when the spatial
          relationship is specified (match_option is set to CLOSEST or
          CLOSEST_GEODESIC. The value of this field is -1 if no feature is
          matched within a search radius. If no field name is provided, the
          field will not be added to the output feature class.
      match_fields {Value Table}:
          Pairs of fields from the join features and target features that will
          be used for attribute matching. Only the records from the join
          features that share match field values with the target features will
          participate in the spatial join.

     OUTPUTS:
      out_feature_class (Feature Class):
          A new feature class containing the attributes of the target and join
          features. By default, all attributes of the target features and the
          attributes of the joined features will be written to the output.
          However, the set of attributes to be transferred can be defined by the
          field map parameter.

        """