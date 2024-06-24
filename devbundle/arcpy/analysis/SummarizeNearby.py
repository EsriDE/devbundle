# Generated documentation for module arcpy.analysis


class SummarizeNearby(object):
    """
    Finds features that are within a specified distance of features in the input layer and calculates statistics for the nearby features. Distance can be measured as a straight-line distance, a drive-time distance (for example, within 10 minutes), or a drive distance (for example, within 5 kilometers). For drive-time and drive-distance measurements, you must be signed in to an ArcGIS Online organizational account with Network Analysis privileges. Both measurement options consume credits.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeNearby_analysis(in_features, in_sum_features, out_feature_class, distance_type, distances;distances..., distance_units, {time_of_day}, {time_zone}, {keep_all_polygons}, {sum_fields;sum_fields...}, {sum_shape}, {shape_unit}, {group_field}, {add_min_maj}, {add_group_percent}, {Output_Grouped_Table})

        Finds features that are within a specified distance of features in the
        input layer and calculates statistics for the nearby features.
        Distance can be measured as a straight-line distance, a drive-time
        distance (for example, within 10 minutes), or a drive distance (for
        example, within 5 kilometers). For drive-time and drive-distance
        measurements, you must be signed in to an ArcGIS Online organizational
        account with Network Analysis privileges. Both measurement options
        consume credits.

     INPUTS:
      in_features (Feature Layer):
          The point, line, or polygon features that will be buffered. Those
          buffers will be used to summarize the input summary features.
      in_sum_features (Feature Layer):
          The point, line, or polygon features that will be summarized.
      distance_type (String):
          Specifies the distance measurement type that will be used to generate
          buffer areas. Both driving distance and driving time will use the road
          network and honor restrictions such as one-way streets. Driving time
          honors the current posted speed limits.To use the drive-time and
          drive-distance measurement options, you must
          be signed in to an ArcGIS Online organizational account with Network
          Analysis privileges. Each time the tool runs successfully, credits are
          debited from your subscription based on the service used and the
          results returned from the service. The Credits page provides details
          about credits.All distance types except straight-line distance use
          ArcGIS Online
          routing and network services.DRIVING_DISTANCE-The distance will be
          covered in a car or other
          similar small automobiles, such as pickup trucks. Travel follows all
          rules that are specific to cars.DRIVING_TIME-The distance will be
          covered within a specified time in a
          car or other similar small automobiles, such as pickup trucks. Dynamic
          travel speeds based on traffic are used where it is available when you
          specify a time of day. Travel follows all rules that are specific to
          cars.STRAIGHT_LINE-A Euclidean or straight-line distance will be
          used.TRUCKING_DISTANCE-The distance will be covered along designated
          truck
          routes. Travel follows all rules for cars as well as rules specific to
          trucking.TRUCKING_TIME-The distance will be covered within a specified
          time
          when traveling along designated truck routes. Dynamic travel speeds
          based on traffic are used where it is available when you specify a
          time of day. Travel follows all rules for cars as well as rules
          specific to trucking.WALKING_DISTANCE-The distance will be covered
          along paths and roads
          that allow pedestrian traffic.WALKING_TIME-The distance will be
          covered within a specified time when
          walking along paths and roads that allow pedestrian traffic.
      distances (Double):
          Distance values that will define a search distance (for straight-line,
          driving, trucking, or walking distance) or travel time (for driving,
          trucking, or walking time). Features that are within (or equal to) the
          distances you provide will be summarized.Multiple values can be
          specified. One area around each input feature
          will be generated for each distance.
      distance_units (String):
          Specifies the unit that will be used for the distance values.MILES-The
          units will be miles.KILOMETERS-The units will be
          kilometers.FEET-The units will be feet.YARDS-The units will be
          yards.METERS-The units will be meters.HOURS-The units will be
          hours.MINUTES-The units will be minutes.SECONDS-The units will be
          seconds.
      time_of_day {Date}:
          The date or time when traffic conditions will be considered during
          travel time. Traffic conditions, especially in urbanized areas, can
          significantly impact the area covered within a specified travel time.
          If no date or time is specified, the distance covered during a
          specified travel time will not be impacted by traffic.Traffic
          conditions may be live or typical (historical) based on the
          date and time specified for this parameter. Esri saves live traffic
          data for 12 hours and references predictive data extending 12 hours
          into the future. If the time and date you specify is within the
          24-hour time window, live traffic is used. If it is outside the time
          window, typical or historic traffic is used.
      time_zone {String}:
          Specifies the time zone that will be used for the specified time of
          day. Time zones can be specified in local time or coordinated
          universal time (UTC). GEOLOCAL-The time of day refers to the
          local time zone or
          zones in which the input features are located. This option can cause
          the analysis to have rolling start times across time zones. This is
          the default. For example, setting a geolocal time of day to
          9:00 a.m. causes the
          drive times for points in the eastern time zone to start at 9:00 a.m.
          eastern time, and 9:00 a.m. central time for points in the central
          time zone. (The start times are offset by an hour in real or UTC
          time.)         UTC-The time of day refers to coordinated universal
          time
          (UTC). The start times for all points are simultaneous, regardless of
          time zones. For example, setting a UTC time of day to 9:00
          a.m. causes the drive
          times for points in the eastern time zone to start at 4:00 a.m.
          eastern time, and 3:00 a.m. central time for points in the central
          time zone. (The start times are simultaneous.)
      keep_all_polygons {Boolean}:
          Specifies whether all buffers of the input features or only those
          intersecting or containing at least one input summary feature will be
          copied to the output feature class.KEEP_ALL-All buffers will be copied
          to the output feature class. This
          is the default.ONLY_INTERSECTING-Only buffers that intersect or
          contain at least one
          input summary feature will be copied to the output feature class.
      sum_fields {Value Table}:
          A list of attribute field names from the input summary features and
          statistical summary types that will be calculated for those attribute
          fields for all points within each input feature buffer.Summary fields
          must be numeric. Text and other attribute field types
          are not supported. The following statistic types are supported:
          Sum-The
          total value of all the points in each buffer will be
          calculated.Mean-The average of all the points in each buffer will be
          calculated.Min-The smallest value of all the points in each buffer
          will be
          identified.Max-The largest value of all the points in each buffer will
          be
          identified.Stddev-The standard deviation of all the points in each
          buffer will be
          calculated.
      sum_shape {Boolean}:
          Specifies whether attributes for the number of points, length of
          lines, and area of polygon features summarized in each input feature
          buffer (shape summary attributes) will be added to the output feature
          class.ADD_SHAPE_SUM-Shape summary attributes will be added to the
          output
          feature class. This is the default.NO_SHAPE_SUM-Shape summary
          attributes will not be added to the output
          feature class.
      shape_unit {String}:
          Specifies the unit that will be used when calculating shape summary
          attributes. If the input summary features are points, no shape unit is
          necessary, since only the count of points within each input feature
          buffer is added.If the input summary features are lines, specify a
          linear unit. If the
          input summary features are polygons, specify an areal unit.METERS-The
          units will be meters.KILOMETERS-The units will be
          kilometers.FEET-The units will be feet.YARDS-The units will be
          yards.MILES-The units will be miles.ACRES-The units will be
          acres.HECTARES-The units will be hectares.SQUAREMETERS-The units will
          be square meters.SQUAREKILOMETERS-The units will be square
          kilometers.SQUAREFEET-The units will be square feet.SQUAREYARDS-The
          units will be square yards.SQUAREMILES-The units will be square miles.
      group_field {Field}:
          The attribute field from the input summary features that will be used
          for grouping. Features that have the same group field value will be
          combined and summarized with other features with the same group field
          value.When a group field is specified, an additional output grouped
          table
          will be created and its location must be specified in the
          out_grouped_table parameter.
      add_min_maj {Boolean}:
          Specifies whether minority (least dominant) and majority (most
          dominant) group field values within each input feature buffer will be
          added to the output. This parameter is enabled if you specified a
          group_field parameter value.NO_MIN_MAJ-Minority and majority fields
          will not be added to the
          output. This is the default.ADD_MIN_MAJ-Minority and majority fields
          will be added to the output.
      add_group_percent {Boolean}:
          Specifies whether a percentage of each attribute value in each group
          will be added to the output. This parameter allows you to determine
          the percentage of each attribute value in each group.This parameter is
          enabled if you specified a group_field parameter
          value.NO_PERCENT-A percentage attribute field will not be added to the
          output. This is the default.ADD_PERCENT-A percentage attribute field
          will be added to the output.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class containing the buffered input
          features, attributes of the input features, and new attributes about
          the number points, length of lines, and area of polygons inside each
          buffer and statistics about those features.
      Output_Grouped_Table {Table}:
          An output table that includes summary fields for each group of summary
          features for each input feature buffer. If a group field is specified,
          the output grouped table is required. The table will have the
          following attribute fields:
          -An ID corresponding to an ID field added to the output
          feature class          Join_IDThe group fieldA shape summary field
          such as count of points or length of linesOne field for each summary
          fieldPercentage field

        """