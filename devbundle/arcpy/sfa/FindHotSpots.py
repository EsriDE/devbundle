# Generated documentation for module arcpy.sfa


class FindHotSpots(object):
    """
    Identifies statistically significant spatial clustering of high values (hot spots) or low values (cold spots), or data counts, in your data. Use this tool to uncover hot and cold spots of high and low home values, crime densities, traffic accident fatalities, unemployment or biodiversity, for example.
    """

    @property
    def description(self) -> str:
        return """

        FindHotSpots_sfa(analysisLayer, outputName, {analysisField}, {divideByField}, {boundingPolygonLayer}, {aggregatePolygonLayer})

        Identifies statistically significant spatial clustering of high values
        (hot spots) or low values (cold spots), or data counts, in your data.
        Use this tool to uncover hot and cold spots of high and low home
        values, crime densities, traffic accident fatalities, unemployment or
        biodiversity, for example.

     INPUTS:
      analysisLayer (Feature Set):
          The point or polygon feature layer for which hot spots will be
          calculated.
      outputName (String):
          The name of the output layer to create on your portal.
      analysisField {Field}:
          A numeric field (number of incidents, crime rates, test
          scores, and so on) to be evaluated. The field you select might
          represent the following:        Counts (such as the number of traffic
          accidents)Rates (such as the
          number of crimes per square mile)Averages (such as the mean math test
          score)Indices (such as a customer satisfaction score)
      divideByField {Field}:
          The numeric field in the input layer that will be used to normalize
          your data. For example, if your points represent crimes, dividing by
          total population would result in an analysis of crimes per capita
          rather than raw crime counts.
      boundingPolygonLayer {Feature Set}:
          When the analysis layer is points and no analysis field is specified,
          you can provide polygon features that define where incidents could
          have occurred. For example, if you are analyzing boating accidents in
          a harbor, the outline of the harbor might provide a good boundary for
          where accidents could occur. When no bounding areas are provided, only
          locations with at least one point will be included in the analysis.
      aggregatePolygonLayer {Feature Set}:
          When the input layer contains points and no analysis field is
          specified, you can provide polygon features into which the points will
          be aggregated and analyzed, such as administrative units. The number
          of points that fall within each polygon is counted and the point count
          in each polygon is analyzed.

        """