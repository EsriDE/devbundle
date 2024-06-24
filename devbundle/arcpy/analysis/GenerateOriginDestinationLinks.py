# Generated documentation for module arcpy.analysis


class GenerateOriginDestinationLinks(object):
    """
    Generates connecting lines from origin features to destination features. This is often referred to as a spider diagram.
    """

    @property
    def description(self) -> str:
        return """

        GenerateOriginDestinationLinks_analysis(origin_features, destination_features, out_feature_class, {origin_group_field}, {destination_group_field}, {line_type}, {num_nearest}, {search_distance}, {distance_unit}, {aggregate_links}, {sum_fields;sum_fields...})

        Generates connecting lines from origin features to destination
        features. This is often referred to as a spider diagram.

     INPUTS:
      origin_features (Feature Layer):
          The input features from which links will be generated.
      destination_features (Feature Layer):
          The destination features to which links will be generated.
      origin_group_field {Field}:
          The attribute field from the input origin features that will be used
          for grouping. Features that have the same group field value between
          origins and destinations will be connected with a link.
      destination_group_field {Field}:
          The attribute field from the input destination features that will be
          used for grouping. Features that have the same group field value
          between origins and destinations will be connected with a link.
      line_type {String}:
          Specifies whether a shortest path on a spheroid (geodesic) or a
          Cartesian projected earth (planar) will be used when generating the
          output links. Geodesic lines will have a slight curve when their
          length exceeds approximately 50 kilometers, as the curvature of the
          Earth makes the shortest distance between two points appear curved
          when viewed on a 2D map.It is recommended that you use the GEODESIC
          line type with data stored
          in a coordinate system that is not appropriate for distance
          measurements (for example, Web Mercator and any geographic coordinate
          system) or any dataset that spans a large geographic
          area.PLANAR-Planar distance will be used between features. This is the
          default.GEODESIC-Geodesic distances will be used between features.
          This line
          type takes into account the curvature of the spheroid and correctly
          deals with data near the dateline and poles.
      num_nearest {Double}:
          The maximum number of links that will be generated per origin feature
          to the nearest destination features. If no number is specified, the
          tool will generate links between all origin and destination
          features.For example, using a value of 1 will generate links between
          each
          origin feature and its closest destination feature.
      search_distance {Double}:
          The maximum distance between an origin and destination feature that
          will produce a link feature in the output. The unit of the search
          distance is specified in the distance unit parameter. If no search
          distance is specified, the tool will generate links between all origin
          and destination features regardless of their distance apart.
      distance_unit {String}:
          Specifies the units used to measure the length of the links.
          Distances for each link will appear in thefield. If a distance unit is
          not specified, the distance unit of the origin features' coordinate
          system will be used. LINK_DISTKILOMETERS-The distance between
          origin and destination will be
          calculated in kilometers.METERS-The distance between origin and
          destination will be calculated
          in meters.MILES-The distance between origin and destination will be
          calculated
          in miles.NAUTICALMILES-The distance between origin and destination
          will be
          calculated in nautical miles.YARDS-The distance between origin and
          destination will be calculated
          in yards.FEET-The distance between origin and destination will be
          calculated in
          feet.
      aggregate_links {Boolean}:
          Specifies whether overlapping links will be
          aggregated.AGGREGATE_OVERLAPPING-Overlapping links will be aggregated
          if the
          starting point coordinates are the same.NO_AGGREGATE-Overlapping links
          will not be aggregated. This is the
          default.
      sum_fields {Value Table}:
          Specifies the field or fields containing the attribute values that
          will be used to calculate the specified statistic. Multiple statistic
          and field combinations can be specified. Null values are excluded from
          all calculations.By default, the tool will not calculate any
          statistics.Text attribute fields can be summarized using first and
          last
          statistics. Numeric attribute fields can be summarized using any
          statistic.Available statistics types are as follows:SUM-The values for
          the specified field will be added together.MEAN-The
          average for the specified field will be calculated.MIN-The smallest
          value for all records of the specified field will be
          found.MAX-The largest value for all records of the specified field
          will be
          found.RANGE-The range of values (maximum minus minimum) for the
          specified
          field will be calculated.STD-The standard deviation of values in the
          specified field will be
          calculated.COUNT-The number of values included in the statistical
          calculations
          will be found. Each value will be counted except null values. To
          determine the number of null values in a field, create a count on the
          field in question, create a count on a different field that does not
          contain null values (for example, the OID if present), and subtract
          the two values.FIRST-The specified field value of the first record in
          the input will
          be used.LAST-The specified field value of thee last record in the
          input will
          be used.MEDIAN-The median for all records of the specified field will
          be
          calculated.VARIANCE-The variance for all records of the specified
          field will be
          calculated.UNIQUE-The number of unique values of the specified field
          will be
          counted.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polyline feature class that will contain the output links.

        """