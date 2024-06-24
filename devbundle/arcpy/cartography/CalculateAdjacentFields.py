# Generated documentation for module arcpy.cartography


class CalculateAdjacentFields(object):
    """
    Creates fields and calculates values for the neighboring pages (polygon) of a grid polygon feature class.
    """

    @property
    def description(self) -> str:
        return """

        CalculateAdjacentFields_cartography(in_features, in_field)

        Creates fields and calculates values for the neighboring pages
        (polygon) of a grid polygon feature class.

     INPUTS:
      in_features (Feature Layer):
          The polygon grid index features that will be appended with adjacent
          field data.
      in_field (Field):
          The field whose values will be used to populate adjacent field data.

        """