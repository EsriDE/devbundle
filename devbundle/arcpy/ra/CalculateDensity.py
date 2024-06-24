# Generated documentation for module arcpy.ra


class CalculateDensity(object):
    """
    Creates a density map from point or line features by spreading known quantities of some phenomenon (represented as attributes of the points or lines) across the map. The result is a layer of areas classified from least dense to most dense.
    """

    @property
    def description(self) -> str:
        return """

        CalculateDensity_ra(inputPointOrLineFeatures, outputName, {countField}, {searchDistance}, {outputAreaUnits}, {outputCellSize}, {inBarriers})

        Creates a density map from point or line features by spreading known
        quantities of some phenomenon (represented as attributes of the points
        or lines) across the map. The result is a layer of areas classified
        from least dense to most dense.

     INPUTS:
      inputPointOrLineFeatures (Feature Set):
          The input point or line features that will be used to calculate the
          density raster.
      outputName (String):
          The name of the output raster service.The default name is based on the
          tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      countField {Field}:
          A field indicating the number of incidents at each location. For
          example, if you are making a population density raster, and the input
          points are cities, it is appropriate to use the population of the city
          for the count field so cities with larger populations have more impact
          on the density calculations.
      searchDistance {Linear Unit}:
          The search distance and units for the distance. When calculating the
          density of a cell, all features within this distance will be used in
          the density calculation for that cell.The unit values are Kilometers,
          Meters, MilesInt, FeetInt, Miles, and
          Feet.The default units are meters.
      outputAreaUnits {String}:
          Specifies the units that will be used for calculating area. Density is
          count divided by area, and this parameter sets the units of the area
          in the density calculation.Square Meters-Calculate the density per
          square meter. This is the
          default.Square Kilometers-Calculate the density per square
          kilometer.Square Feet-Calculate the density per square foot.Square
          Miles-Calculate the density per square mile.
      outputCellSize {Linear Unit}:
          The cell size and units for the output raster.The unit values are
          Kilometers, Meters, MilesInt, FeetInt, Miles, and
          Feet.
      inBarriers {Feature Set}:
          The dataset that defines the barriers.The barriers can be a feature
          layer of polyline or polygon features.

        """