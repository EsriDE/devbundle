# Generated documentation for module arcpy.geocoding


class AssignStreetsToPoints(object):
    """
    Uses address information such as street names and distance to find the best street feature candidate for a point. Street name is prioritized over distance.
    """

    @property
    def description(self) -> str:
        return """

        AssignStreetsToPoints_geocoding(in_point_features, point_field_mapping;point_field_mapping..., in_street_features, street_field_mapping;street_field_mapping..., out_points, {street_fields;street_fields...}, {distance}, {output_geometry})

        Uses address information such as street names and distance to find the
        best street feature candidate for a point. Street name is prioritized
        over distance.

     INPUTS:
      in_point_features (Feature Layer):
          The input point feature class or layer.
      point_field_mapping (Value Table):
          The mapping of street address component fields from the point features
          that will be used to compare the full street name to the full street
          name in the in_street_features parameter value to calculate the street
          segment that the point is linked to. Provide the street address
          component field names and data
          field names from the in_point_features parameter value using the
          available address components as follows:        STREET_PREFIX_DIR-A
          direction that precedes the street name, such as
          the W in W. Redlands Blvd.STREET_PREFIX_TYPE-A street type that
          precedes the street name, such
          as Avenue in Avenue B.STREET_NAME-The name of the street, such as
          Cherry in Cherry Rd.STREET_SUFFIX_TYPE-A street type that follows the
          street name, such as
          St. in New York St.STREET_SUFFIX_DIR-A direction that follows the
          street name, such as NW
          in Bridge St. NW.STREET_FULL_NAME-The full street name of the address,
          such as S.
          Orange St.HOUSE_NUMBER-The house number associated with an address,
          such as 380
          in 380 New York St.
      in_street_features (Feature Layer):
          The input street feature class or layer from which attributes will be
          assigned to the in_point_features parameter value.
      street_field_mapping (Value Table):
          The mapping of street address component fields from the street
          features that will be used to compare the full street name to the full
          street name in the in_point_features parameter value to calculate the
          street segment that point is linked to.Provide the street address
          component field names and data field names
          from the in_street_features parameter value using the available
          address components as follows:STREET_PREFIX_DIR-A direction that
          precedes the street name, such as
          the W in W. Redlands Blvd.STREET_PREFIX_TYPE-A street type that
          precedes the street name, such
          as Avenue in Avenue B.STREET_NAME-The name of the street, such as
          Cherry in Cherry Rd.STREET_SUFFIX_TYPE-A street type that follows the
          street name, such as
          St. in New York St.STREET_SUFFIX_DIR-A direction that follows the
          street name, such as NW
          in Bridge St. NW.STREET_FULL_NAME-The full street name of the address,
          such as S.
          Orange St.HOUSE_NUMBER_FROM_LEFT-A value representing the beginning
          number of a
          house number range on the left side of the
          street.HOUSE_NUMBER_TO_LEFT-A value representing the ending number of
          a house
          number range on the left side of the street.HOUSE_NUMBER_FROM_RIGHT-A
          value representing the beginning number of a
          house number range on the right side of the
          street.HOUSE_NUMBER_TO_RIGHT-A value representing the ending number of
          a
          house number range on the right side of the street.
      street_fields {Field}:
          The fields from the in_street_features parameter value that will be
          assigned to the out_points parameter value. Specify fields from the
          input street features that contain attributes to assign to the linked
          point features, for example, a field that contains a street ID value.
          The fields will be added to the out_points parameter value.
      distance {Double}:
          The distance that will be used to find the nearest street feature to
          the point feature. The higher the distance limit, the more time it
          will take the tool to run, but the quality of the matches improves.
          The default value is 70 meters.
      output_geometry {String}:
          Specifies the geometry that will be included in the output point
          feature class.INPUT_POINT_GEOMETRY-Geometry for the original input
          point feature
          class will be included in the output point feature
          class.STREET_POINT_GEOMETRY-Geometry for the street location of the
          linked
          point will be included in the output point feature class.

     OUTPUTS:
      out_points (Feature Class):
          The output point feature class containing the street fields assigned
          to the point.

        """