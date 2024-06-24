# Generated documentation for module arcpy.geoanalytics


class SummarizeWithin(object):
    """
    Overlays a polygon layer with another layer to summarize the number of points, length of the lines, or area of the polygons within each polygon and calculates attribute field statistics for those features within the polygons.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeWithin_geoanalytics(summarized_layer, output_name, {polygon_or_bin}, {bin_type}, {bin_size}, {summary_polygons}, {sum_shape}, {shape_units}, {standard_summary_fields;standard_summary_fields...}, {weighted_summary_fields;weighted_summary_fields...}, {data_store}, {group_by_field}, {add_minority_majority}, {add_percentages})

        Overlays a polygon layer with another layer to summarize the number of
        points, length of the lines, or area of the polygons within each
        polygon and calculates attribute field statistics for those features
        within the polygons.

     INPUTS:
      summarized_layer (Feature Set):
          The point, line, or polygon features that will be summarized by either
          polygons or bins.
      output_name (String):
          The name of the output polygon feature service containing the
          intersecting geometries and attributes.
      polygon_or_bin {String}:
          Specifies whether the summarized_layer value will be summarized by
          polygons or bins.POLYGON-The summarized layer will be aggregated into
          a polygon
          dataset.BIN-The summarized layer will be aggregated into square or
          hexagonal
          bins.
      bin_type {String}:
          Specifies the bin shape that will be generated to summarize
          features.SQUARE-The bin_size value represents the height of a square.
          This is
          the default.HEXAGON-The bin_size value represents the height between
          two parallel
          sides.
      bin_size {Linear Unit}:
          The distance interval that represents the bin size and units by which
          the input features will be summarized.
      summary_polygons {Feature Set}:
          The polygons that will be used to summarize the features in the input
          summarized layer.
      sum_shape {Boolean}:
          Specifies whether the length of lines or area of polygons within the
          summary layer (polygon or bin) will be calculated. The count of
          points, lines, and polygons intersecting the summary shape will always
          be included.ADD_SUMMARY-Summary shape values will be calculated. This
          is the
          default.NO_SUMMARY-Summary shape values will not be calculated.
      shape_units {String}:
          Specifies the unit of measurement that will be used to calculate shape
          summary attributes. If the input summarized_layer value is points, no
          shape unit is necessary, since only the count of points within each
          input polygon is added. If the input summary features are lines,
          specify a linear unit. If the input summary features are polygons,
          specify an areal unit.METERS-The shape units will be
          meters.KILOMETERS-The shape units will
          be kilometers.FEET-The shape units will be US survey feet.YARDS-The
          shape units will be US survey yards.MILES-The shape units will be US
          survey miles.NAUTICAL_MILES-The shape units will be US survey nautical
          miles.FEET_INT-The shape units will be international
          feet.YARDS_INT-The shape units will be international
          yards.MILES_INT-The shape units will be statute
          miles.NAUTICAL_MILES_INT-The shape units will be international
          nautical
          miles.ACRES-The shape units will be international acres.HECTARES-The
          shape units will be hectares.SQUARE_METERS-The shape units will be
          square meters.SQUARE_KILOMETERS-The shape units will be square
          kilometers.SQUARE_FEET-The shape units will be square international
          feet.SQUARE_YARDS-The shape units will be square international
          yards.SQUARE_MILES-The shape units will be square statute
          miles.SQUARE_FEET_US-The shape units will be square US survey
          feet.SQUARE_YARDS_US-The shape units will be square US survey
          yards.SQUARE_MILES_US-The shape units will be square US survey
          miles.ACRES_US-The shape units will be US survey acres.
      standard_summary_fields {Value Table}:
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
          type string.Specifies whether a field represents a count or a
          rate.COUNT-For line and polygon layers, the summarized field values
          will be
          proportioned by the percentage of the summarized features that
          intersect the summary polygons prior to calculating statistics. Values
          will not be proportioned for point layers.RATE-The summarized field
          values will not be proportioned. The raw
          field values will be used to calculate statistics.
      weighted_summary_fields {Value Table}:
          Specifies the weighted statistics that will be calculated on specified
          fields.MEAN-The weighted mean of each field will be calculated in
          which the
          weight applied is the proportion of the summarized layer within the
          polygons.STDDEV-The weighted standard deviation of each field will be
          calculated in which the weight applied is the proportion of the
          summarized layer within the polygons.VAR-The weighted variance of each
          field will be calculated in which
          the weight applied is the proportion of the summarized layer within
          the polygons.Specifies whether a field represents a count or a
          rate.Count-The summarized field values will be proportioned by the
          percentage of the summarized features that intersect the summary
          polygons prior to calculating statistics.Rate-The summarized field
          values will not be proportioned. The raw
          field values will be used to calculate statistics.
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
      group_by_field {Field}:
          A field from the input summary features that will be used to
          calculate statistics for each unique attribute value. For example, the
          input summary features contain point locations of businesses that
          store hazardous materials, and one of the fields is, which contains
          codes that describe the type of hazardous material stored. To
          calculate summaries by each unique value of, use it as the group-by
          field. HazardClassHazardClass
      add_minority_majority {Boolean}:
          Specifies whether minority (least dominant) and majority (most
          dominant) attribute values for each group field within each boundary
          will be added. When this parameter value is ADD_MIN_MAJ, two new
          fields will be added to the output layer prefixed with Minority_ and
          Majority_. This parameter only applies when a value is provided for
          the group_by_field parameter.NO_MIN_MAJ-Minority and majority fields
          will not be added. This is the
          default.ADD_MIN_MAJ-Minority and majority fields will be added.
      add_percentages {Boolean}:
          Specifies whether percentage fields will be added. When this parameter
          value is ADD_PERCENT, the percentage of each unique group value will
          be calculated for each input polygon. This parameter only applies when
          a value is provided for the group_by_field parameter and a value is
          specified for the add_minority_majority
          parameter.NO_PERCENT-Percentage fields will not be added. This is the
          default.ADD_PERCENT-Percentage fields will be added.

        """