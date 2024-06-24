# Generated documentation for module arcpy.ba


class HuffModelCalibration(object):
    """
    Calculates exponent values for use in the Huff Model tool.
    """

    @property
    def description(self) -> str:
        return """

        HuffModelCalibration_ba(in_facility_features, facility_id_field, in_customer_features, link_field, in_sales_potential_features, sales_potential_id_field, out_calibration, attractiveness_variables;attractiveness_variables..., {customer_weight_field}, {distance_type}, {distance_units}, {travel_direction}, {time_of_day}, {time_zone})

        Calculates exponent values for use in the Huff Model tool.

     INPUTS:
      in_facility_features (Feature Layer):
          The input point feature class representing competitors or existing
          stores.
      facility_id_field (Field):
          A unique ID field representing a store or facility location.
      in_customer_features (Feature Layer):
          The input point feature class representing customer locations.
      link_field (Field):
          The field that will be used as an ID to assign individual customers to
          a facility or store.
      in_sales_potential_features (Feature Layer):
          The input polygon feature class used to determine the potential sales
          market.
      sales_potential_id_field (Field):
          A unique ID field representing the sales potential area.
      attractiveness_variables (Value Table):
          The fields that will be used to determine the attractiveness of each
          competitor. In many cases, the size of the store is used as a
          substitute for attractiveness.
      customer_weight_field {Field}:
          A calculated weighted value field assigned to each customer.
      distance_type {String}:
          The method of travel that will be used to calculate distance. The
          default value is Straight Line.
      distance_units {String}:
          The distance-measuring units that will be used when calculating
          distance.
      travel_direction {String}:
          Specifies the direction of travel that will be used between stores and
          sales potential features.TOWARD_STORES-The direction of travel will be
          from sales potential
          features to stores. This is the default.AWAY_FROM_STORES-The direction
          of travel will be from stores to sales
          potential features.
      time_of_day {Date}:
          The time and date that will be used when calculating distance.
      time_zone {String}:
          Specifies the time zone that will be used for the time_of_day
          parameter.TIME_ZONE_AT_LOCATION-The time zone in which the territories
          are
          located will be used. This is the default.UTC-Coordinated universal
          time (UTC) will be used.

     OUTPUTS:
      out_calibration (File):
          The output calibration file that will contain the calibrated Huff
          model results, which is the exponent values for the attractiveness
          variables and distance. The output file extension will be *.huffmodel.

        """