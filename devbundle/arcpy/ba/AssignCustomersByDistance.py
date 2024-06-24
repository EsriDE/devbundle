# Generated documentation for module arcpy.ba


class AssignCustomersByDistance(object):
    """
    Assigns customers to the closest store based on a selected distance type.
    """

    @property
    def description(self) -> str:
        return """

        AssignCustomersByDistance_ba(in_features, in_store_features, store_id_field, out_feature_class, {link_field}, {distance_type}, {distance_units}, {travel_direction}, {time_of_day}, {time_zone}, {search_tolerance})

        Assigns customers to the closest store based on a selected distance
        type.

     INPUTS:
      in_features (Feature Layer):
          The input point feature layer representing customers.
      in_store_features (Feature Layer):
          The input point feature layer representing store or facilities.
      store_id_field (Field):
          A unique ID field for in_store_features.
      link_field {String}:
          A new field that contains the assigned store or facility ID.
      distance_type {String}:
          The method of travel used to calculate the distance between customers
          and stores.
      distance_units {String}:
          The units that will be used to measure the selected distance type.
      travel_direction {String}:
          Specifies the direction of travel that will be used between stores or
          facilities and customers.TOWARD_STORES-The direction of travel will be
          from customers to
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
          processing.The parameter requires a distance value and units for the
          tolerance.
          The default value is 5000 meters.

     OUTPUTS:
      out_feature_class (Feature Class):
          A point layer containing customers with assigned store or facility and
          distance.

        """