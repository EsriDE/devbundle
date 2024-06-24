# Generated documentation for module arcpy.td


class SetTerritoryLevelOptions(object):
    """
    Sets options for how territory levels are created.
    """

    @property
    def description(self) -> str:
        return """

        SetTerritoryLevelOptions_td(in_territory_solution, level, {compactness}, {fill_extent}, {random_seed}, {spatial_relationship}, {buffer_tolerance})

        Sets options for how territory levels are created.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The Territory Design solution layer that will be used in the analysis.
      level (String):
          The level to which the options will be applied.
      compactness {Long}:
          A numeric value between 0 and 100 that defines the shape of
          territories.
      fill_extent {Boolean}:
          Specifies whether features are automatically assigned to the nearest
          territory.AUTO_FILL_EXTENT-Features are automatically assigned to the
          nearest
          territory.DO_NOT_AUTO_FILL_EXTENT-Features are not automatically
          assigned to the
          nearest territory. This is the default.
      random_seed {Long}:
          An integer used for the seed value. The default is no value and uses a
          random generator.
      spatial_relationship {String}:
          Specifies the spatial relationship of how features are related to
          determine adjacency.CONTIGUITY_EDGES_ONLY-Polygon features that share
          a boundary or share
          a node with neighboring features.
      buffer_tolerance {Linear Unit}:
          The distance between features to determine adjacency. Features that
          are within the buffer tolerance are considered adjacent features.

        """