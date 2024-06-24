# Generated documentation for module arcpy.ba


class CustomerDerivedTA(object):
    """
    Creates trade areas around stores based on the number of customers or volume attribute of each customer.
    """

    @property
    def description(self) -> str:
        return """

        CustomerDerivedTA_ba(in_stores_layer, store_id_field, in_customers_layer, link_field, out_feature_class, method, rings;rings..., customer_aggregation_type, {customer_weight_field}, {exclude_outlying_customers}, {cutoff_distance}, {dissolve_option}, {use_customer_centroids}, {distance_type}, {units}, {travel_direction}, {time_of_day}, {time_zone}, {search_tolerance}, {polygon_detail}, {iterations_limit}, {minimum_step}, {target_percent_diff})

        Creates trade areas around stores based on the number of customers or
        volume attribute of each customer.

     INPUTS:
      in_stores_layer (Feature Layer):
          A point layer representing store or facility locations.
      store_id_field (Field):
          The unique ID field representing a store or facility location.
      in_customers_layer (Feature Layer):
          An input point layer representing customers or patrons.
      link_field (Field):
          An ID field that will be used to assign individual customers to
          stores.
      method (String):
          Specifies the type of customer-derived trade area that will be
          generated.SIMPLE-A generalized trade area based on the percentages of
          customers
          corresponding to each store will be generated.AMOEBA-Points
          representing the boundary of the polygon trade area will
          be connected using natural curvature.DETAILED-Points representing the
          boundary of the polygon trade area
          will be connected using straight lines.DETAILED_WITH_SMOOTHING-Points
          representing the boundary of the
          polygon trade area will be connected with smoothed curves using cubic
          splines. This method takes into account the shape and pattern of the
          customer distributions. This is the default.THRESHOLD_RINGS-
          Concentric rings that expand from input stores until
          they contain the specified threshold of customers will be
          generated.THRESHOLD_DRIVETIMES-Polygons that expand from stores along
          network
          routes until they contain the specified threshold of customers will be
          generated.
      rings (Double):
          The values that will be used to represent the percentage of customers,
          for example, total count or a customer attribute and total sales
          assigned to each store. Each value represents one trade area polygon.
      customer_aggregation_type (String):
          Specifies the type of aggregation that will be used.COUNT-Percentage-
          based trade areas will be calculated using the
          geographic locations of customers. This is the
          default.WEIGHT-Percentage-based trade areas will be calculated using a
          customer attribute, for example, sales.
      customer_weight_field {Field}:
          The field that will be used to calculate the trade areas. This is
          based on either the number of customers (count) or the calculated
          weighted value assigned to each customer.
      exclude_outlying_customers {Boolean}:
          Specifies whether outlying customers will be excluded from the trade
          area generation.EXCLUDE_OUTLIERS-Outlying customers will be
          excluded.ALL_POINTS-Outlying customers will not be excluded; all
          customers will
          be considered. This is the default.
      cutoff_distance {Linear Unit}:
          The distance beyond which customers will be considered outliers and
          excluded from consideration during trade area generation.
      dissolve_option {String}:
          Specifies whether polygons of the entire area will be created or the
          polygons will be split into individual features. When the method
          parameter is set to THRESHOLD_DRIVETIMES, the only available option is
          OVERLAP.OVERLAP-Output polygons will be generated in which each
          feature
          begins at zero and grows to satisfy the specified percentage of
          customers. For example, if you specify a trade area of 50 percent and
          70 percent of customers, one polygon will be generated to include 0 to
          50 percent and a second polygon will include all 0 to 70 percent of
          customers. This is the default.SPLIT-Output polygons will be
          generated for individual features based
          on the specified percentage breaks. For example, if you specify a
          trade area of 50 percent and 70 percent of customers, one polygon will
          be generated to include 0 to 50 percent and a second polygon will
          include 50 to 70 percent of customers.
      use_customer_centroids {Boolean}:
          Specifies whether the centroid of your customer area will be used to
          calculate trade areas outward from this point.USE_CENTROIDS-The
          centroid of customer points will be used to
          calculate trade areas.USE_STORES-The centroid of customer points will
          not used; store
          location will be used as the starting point to calculate trade areas.
          This is the default.
      distance_type {String}:
          The method of travel that will be used to calculate the distance.
      units {String}:
          The units that will be used for the distance values.
      travel_direction {String}:
          Specifies the direction of travel that will be used between stores and
          customers.TOWARD_STORES-The direction of travel will be from customers
          to
          stores. This is the default.AWAY_FROM_STORES-The direction of travel
          will be from stores to
          customers.
      time_of_day {Date}:
          The time and date that will be used when calculating distance.
      time_zone {String}:
          Specifies the time zone that will be used for the time_of_day
          parameter.TIME_ZONE_AT_LOCATION-The time zone in which the territories
          are
          located will be used. This is the default.UTC-Coordinated universal
          time (UTC) will be used.
      search_tolerance {Linear Unit}:
          The maximum distance that input points can be from the network. Points
          located beyond the search tolerance will be excluded from
          processing.This parameter requires a distance value and units for the
          tolerance.
      polygon_detail {String}:
          Specifies the level of detail that will be used for the output drive
          time polygons.STANDARD-Polygons with a standard level of detail will
          be created.
          This is the default.GENERALIZED-Generalized polygons will be created
          using the hierarchy
          present in the network data source to produce results quickly.HIGH-
          Polygons with a high level of detail will be created for
          applications in which precise results are important.
      iterations_limit {Long}:
          Restricts the number of drive times that can be used to find the
          optimal threshold limit.
      minimum_step {Double}:
          The minimum increment distance or time-for example, 1 mile or 1
          minute-that will be used between iterations to expand until the
          threshold is reached.
      target_percent_diff {Double}:
          The maximum percentage difference between the target value and
          threshold value that will be used when determining the threshold drive
          time, for example, 5 percent. The default value is 5.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output trade area feature class.

        """