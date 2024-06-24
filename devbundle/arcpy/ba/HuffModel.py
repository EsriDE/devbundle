# Generated documentation for module arcpy.ba


class HuffModel(object):
    """
    Creates a probability surface to predict the sales potential of an area based on distance and an attractiveness factor.
    """

    @property
    def description(self) -> str:
        return """

        HuffModel_ba(in_facility_features, facility_id_field, in_candidate_features, candidate_id_field, in_sales_potential_features, sales_potential_id_field, sales_potential_field, out_feature_class, attractiveness_variables;attractiveness_variables..., distance_exponent, {distance_type}, {distance_units}, {out_distance_matrix}, {travel_direction}, {time_of_day}, {time_zone})

        Creates a probability surface to predict the sales potential of an
        area based on distance and an attractiveness factor.

     INPUTS:
      in_facility_features (Feature Layer):
          An input point feature layer representing existing facility locations.
          It is the first feature from the layer or the feature selected when a
          selection is available.
      facility_id_field (Field):
          A unique ID field for existing facilities.
      in_candidate_features (Feature Layer):
          An input point feature layer representing new candidate facility
          locations. It is the first feature from the layer or the feature
          selected when a selection is available.
      candidate_id_field (Field):
          A unique ID field for candidate facilities.
      in_sales_potential_features (Feature Layer):
          An input point or polygon feature layer used to calculate the sales
          potential. It is either all features from a layer or only selected
          features when a selection is available.
      sales_potential_id_field (Field):
          A unique ID field for sales potential features.
      sales_potential_field (Field):
          The field containing the values that will be used to calculate the
          sales potential.
      attractiveness_variables (Value Table):
          The attribute fields that indicate the attractiveness of each
          competitor. In many cases, the size of the facility is used as a
          substitute for attractiveness and will be a multivalue table.An
          additional attractiveness variable is needed. The attractiveness
          field must be present in the existing facilities (competitors) and the
          candidate facilities layer.existing_facilities_value-Numeric field in
          the in_facility_features
          parameter layer that represents
          attractiveness.candidates_location_value-Numeric field in the
          in_candidate_features
          parameter layer that matches the attractiveness value from the
          in_facility_features parameter layer. Distance does not require a
          matching field.exponent-The value that determines how much of a factor
          the variable
          is to the attractiveness value. The default value is 1.
      distance_exponent (Double):
          The distance exponent is generally a negative number because
          attractiveness decreases when distance increases. The default value is
          -1.5.
      distance_type {String}:
          The type of distance, based on method of travel, that will be used.
          The default value is Straight Line.
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
      out_feature_class (Feature Class):
          The output feature class that will contain the tool results
          representing the probability of sales.
      out_distance_matrix {Table}:
          The name and location of the matrix table of distance calculations.
          The IDs for the in_facility_features and in_candidate_features
          parameters must be unique.

        """