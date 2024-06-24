# Generated documentation for module arcpy.sfa


class CalculateDensity(object):
    """
    Creates a density map from point or line features by spreading known quantities of some phenomenon (represented as attributes of the points or lines) across the map. The result is a layer of areas classified from least dense to most dense.
    """

    @property
    def description(self) -> str:
        return """

        CalculateDensity_sfa(inputLayer, outputName, {field}, {cellSize}, {cellSizeUnits}, {radius}, {radiusUnits}, {boundingPolygonLayer}, {areaUnits}, {classificationType}, {numClasses})

        Creates a density map from point or line features by spreading known
        quantities of some phenomenon (represented as attributes of the points
        or lines) across the map. The result is a layer of areas classified
        from least dense to most dense.

     INPUTS:
      inputLayer (Feature Set):
          The point or line features from which to calculate density.
      outputName (String):
          The name of the output layer to create on your portal.
      field {Field}:
          A field specifying the number of incidents at each location. For
          example, if you have points that represent cities, you can use a field
          representing the population of the city as the count field, and the
          resulting population density layer will calculate larger population
          densities near cities with larger populations.If not specified, each
          location will be assumed to represent a single
          count.
      cellSize {Double}:
          This value is used to create a mesh of points where density
          values are calculated. The default is approximately 1/1000of the
          smaller of the width and height of the analysis extent as defined in
          the context parameter. The smaller the value, the smoother the polygon
          boundaries will be. Conversely, with larger values, the polygon
          boundaries will be more coarse and jagged. th
      cellSizeUnits {String}:
          The units of the cell size value. You must provide a value if cell
          size has been
          set.MILES-MilesFEET-FeetKILOMETERS-KilometersMETERS-Meters
      radius {Double}:
          A distance specifying how far to search to find point or line features
          when calculating density values. For example, if you provide a search
          distance of 1,800 meters, the density of any location in the output
          layer is calculated based on features that are within 1,800 meters of
          the location. Any location that does not have any incidents within
          1,800 meters will receive a density value of zero.If no distance is
          provided, a default will be calculated based on the
          locations of the input features and the values in the count field (if
          a count field is provided).
      radiusUnits {String}:
          The units of the radius value. You must provide a value if a radius
          has been set.MILES-MilesFEET-FeetKILOMETERS-KilometersMETERS-Meters
      boundingPolygonLayer {Feature Set}:
          A layer specifying the polygons where you want densities to be
          calculated. For example, if you are interpolating densities of fish
          within a lake, you can use the boundary of the lake in this parameter
          and the output will only draw within the boundary of the lake.
      areaUnits {String}:
          The units of the calculated density values.SQUAREMILES-Square
          milesSQUAREKILOMETERS-Square kilometers
      classificationType {String}:
          Determines how density values will be classified into
          polygons.EQUALINTERVAL-Polygons are created such that the range of
          density
          values is equal for each area.GEOMETRICINTERVAL-Polygons are based on
          class intervals that have a
          geometric series. This method ensures that each class range has
          approximately the same number of values within each class and that the
          change between intervals is consistent.NATURALBREAKS-Class intervals
          for polygons are based on natural
          groupings of the data. Class break values are identified that best
          group similar values and that maximize the differences between
          classes.EQUALAREA-Polygons are created such that the size of each
          area is
          equal. For example, if the result has more high-density values than
          low-density values, more polygons will be created for high
          densities.STANDARDDEVIATION-Polygons are created based upon the
          standard
          deviation of the predicted density values.
      numClasses {Long}:
          This value is used to divide the range of predicted values into
          distinct classes. The range of values in each class is determined by
          the classification type. Each class defines the boundaries of the
          result polygons.The default is 10 and the maximum is 32.

        """