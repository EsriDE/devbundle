# Generated documentation for module arcpy.ba


class AddPointLayerBasedSuitabilityCriteria(object):
    """
    Adds criteria based on spatial relationships between the input layer and a given point layer.
    """

    @property
    def description(self) -> str:
        return """

        AddPointLayerBasedSuitabilityCriteria_ba(in_analysis_layer, site_layer_id_field, in_point_features, criteria_type, {distance_type}, {units}, {in_site_centers_features}, {site_centers_id_field}, weight_field, {statistics_type}, {cutoff_distance})

        Adds criteria based on spatial relationships between the input layer
        and a given point layer.

     INPUTS:
      in_analysis_layer (Feature Layer):
          The Suitability Analysis layer that will be used in the analysis.
      site_layer_id_field (Field):
          A field containing unique values for each record within the
          Suitability Analysis layer.
      in_point_features (Feature Layer):
          The layer containing point locations to be added as criteria based on
          spatial relationship to the Suitability Analysis layer.
      criteria_type (String):
          Defines the type of spatial relationship to be used as
          criteria.COUNT-A count of points that fall within each Suitability
          Analysis
          layer polygon. This is the default.WEIGHT-Calculates field-weighted
          criteria of points that fall within
          each Suitability Analysis polygon based on the user-selected
          statistical type.MINIMAL_DISTANCE-Adds distance from the closest point
          to each of the
          Suitability Analysis layer centroids as criteria.
      distance_type {String}:
          Defines how minimal distance is calculated based on method of travel.
      units {String}:
          Defines the type of distance measuring units to be used when
          calculating minimal distance.
      in_site_centers_features {Feature Layer}:
          The point layer that will be used as site centers. This point layer
          will replace default polygon centroids of the Suitability Analysis
          layer.
      site_centers_id_field {Field}:
          A field existing within the in_site_centers_features parameter that
          uniquely identifies each record.
      weight_field (Field):
          Numeric fields that exist within a point layer that can be selected
          for weighting.
      statistics_type {String}:
          The type of statistical operation to be applied to the weighted
          field.SUM-Calculates the total of the field values in each point
          feature.AVE-Determines the average field value in each point
          feature.STD_DEV-Calculates the standard deviation of the field values
          in each
          point feature.MIN-Determines the smallest field value in each point
          feature.MAX-Determines the largest field value in each point feature.
      cutoff_distance {Double}:
          The distance beyond which points will not be considered in the
          calculation.

        """