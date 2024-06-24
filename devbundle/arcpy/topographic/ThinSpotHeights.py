# Generated documentation for module arcpy.topographic


class ThinSpotHeights(object):
    """
    Generalizes spot heights for a given area of interest (AOI) in accordance with product specifications.
    """

    @property
    def description(self) -> str:
        return """

        ThinSpotHeights_topographic(in_features, area_of_interest, elevation_field, invisibility_field, {high_low_spots}, {search_distance}, {max_spots}, {input_contours}, {contour_code_field}, {depression_code_value;depression_code_value...})

        Generalizes spot heights for a given area of interest (AOI) in
        accordance with product specifications.

     INPUTS:
      in_features (Feature Layer):
          A point feature layer or feature class representing the spot heights
          for a given AOI.
      area_of_interest (Feature Layer):
          The feature in the AOI that will be used to identify input features to
          process. Provide only one feature from the AOI.
      elevation_field (Field):
          The elevation field in the in_features parameter value that will be
          used for the spot height.
      invisibility_field (Field):
          The field where the visibility attribute will be written.
      high_low_spots {Field}:
          The field that will be used to identify the highest and lowest spots.
      search_distance {Linear Unit}:
          The minimum distance between spot heights. For example, if the search
          distance is 3,000 meters, there will be at least 3,000 meters between
          a chosen spot height and the next chosen spot height. The default
          value is 1,300 meters, as this is the optimal value for 50K sheets.
      max_spots {Long}:
          The maximum number of spot heights that will be processed.
      input_contours {Feature Layer}:
          The input contours that will be used to identify whether point
          features are in depressions or tops.
      contour_code_field {Field}:
          The field in the database that contains the domain value for
          index contour, intermediate contour, depression contour, and
          depression intermediate contour. It is a string value of the field,
          such as. HQC
      depression_code_value {Long}:
          The depression code values. A depression refers to an elevation
          completely surrounded by higher-elevation contour lines.

        """