# Generated documentation for module arcpy.ba


class GenerateGridsAndHexagons(object):
    """
    Creates features with vector-based square grid cells, hexagons, or H3 hexagons for a given area.
    """

    @property
    def description(self) -> str:
        return """

        GenerateGridsAndHexagons_ba(area_of_interest, out_feature_class, {cell_type}, {enrich_type}, {cell_size}, {h3_resolution}, {variables;variables...}, {distance_type}, {distance}, {units}, {out_enriched_buffers}, {travel_direction}, {time_of_day}, {time_zone}, {search_tolerance}, {polygon_detail}, {out_centroids})

        Creates features with vector-based square grid cells, hexagons, or H3
        hexagons for a given area.

     INPUTS:
      area_of_interest (Feature Layer):
          The input feature class used to define the extent of the grid or
          hexagon layer.
      cell_type {String}:
          Specifies the cell type that will be created in the
          output.SQUARE-Regular four-sided polygons with equal side lengths will
          be
          created. This is the default.HEXAGON-Regular six-sided polygons with
          equal side lengths will be
          created.H3_HEXAGON-Regular six-sided polygons with equal side lengths
          based on
          Uber's hexagonal hierarchical spatial index will be created.
      enrich_type {String}:
          Specifies the method that will be used for variable
          enrichment.ENRICH_CELL-Enrichment will be performed on the cell_type
          parameter
          value.ENRICH_BUFFER-Enrichment will be performed on a buffer around
          the
          centroid of the grid or hexagon. The default distance_type parameter
          value is straight_line.
      cell_size {Areal Unit}:
          The size of the cell to generate squares or hexagons. The default
          value is 1 square mile.
      h3_resolution {Long}:
          The resolution that will be used to generate the H3 hexagons. A value
          of 15 represents the finest resolution. The default value is 7.
      variables {String}:
          A list of variables that will be appended to the output.
      distance_type {String}:
          The method of travel that will be used for the buffer calculation.
      distance {Double}:
          The distance that will be used for the buffer calculations.
      units {String}:
          The units that will be used for the distance parameter.
      travel_direction {String}:
          Specifies the direction of travel that will be used between the center
          of the cell and the buffer boundary.TOWARD_STORES-The direction of
          travel will be from location points to
          input features. This is the default.AWAY_FROM_STORES-The direction of
          travel will be from input features
          to location points.
      time_of_day {Date}:
          The time at which the travel will begin.
      time_zone {String}:
          Specifies the time zone that will be used for the time_of_day
          parameter.UTC-Coordinated universal time (UTC) will be used. Choose
          this option
          if you want the best location for a specific time, such as now, but
          aren't certain of the time zone.TIME_ZONE_AT_LOCATION-The time zone in
          which the area_of_interest
          value is located will be used. This is the default.
      search_tolerance {Linear Unit}:
          The maximum distance that input points can be from the network. Points
          located beyond the search tolerance will be excluded from processing.
      polygon_detail {String}:
          Specifies the level of detail that will be used for the output drive
          time polygons.STANDARD-The optimal setting that combines processing
          speed with
          overall accuracy will be used. This is the default.GENERALIZED-The
          fastest method will be used.HIGH-The highest level of detail will be
          used.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will contain the grid or hexagon features.
      out_enriched_buffers {Feature Class}:
          The feature class that will contain the enriched buffers.
      out_centroids {Feature Class}:
          The feature class that will contain the cell centroids.

        """