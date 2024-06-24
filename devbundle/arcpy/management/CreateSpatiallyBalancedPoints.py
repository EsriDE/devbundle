# Generated documentation for module arcpy.management


class CreateSpatiallyBalancedPoints(object):
    """
    Creates a set of sample points based on inclusion probabilities, resulting in a spatially balanced sample design. This tool is typically used for designing a monitoring network by suggesting locations to take samples, and a preference for particular locations can be defined using an inclusion probability raster.
    """

    @property
    def description(self) -> str:
        return """

        CreateSpatiallyBalancedPoints_management(in_probability_raster, number_output_points, out_feature_class)

        Creates a set of sample points based on inclusion probabilities,
        resulting in a spatially balanced sample design. This tool is
        typically used for designing a monitoring network by suggesting
        locations to take samples, and a preference for particular locations
        can be defined using an inclusion probability raster.

     INPUTS:
      in_probability_raster (Raster Layer / Mosaic Layer):
          Defines the inclusion probabilities for each location in the area of
          interest. The location values must range from 0 (low inclusion
          probability) to 1 (high inclusion probability).
      number_output_points (Long):
          The number of sample locations that will be created.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the selected sample locations and
          their inclusion probabilities.

        """