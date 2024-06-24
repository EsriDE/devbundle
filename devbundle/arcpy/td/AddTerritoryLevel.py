# Generated documentation for module arcpy.td


class AddTerritoryLevel(object):
    """
    Creates a new empty feature class to represent a level.
    """

    @property
    def description(self) -> str:
        return """

        AddTerritoryLevel_td(in_territory_solution, level_name, {default_territory_name}, {primary_feature_class})

        Creates a new empty feature class to represent a level.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The input territory solution.
      level_name (String):
          The name of the new territory level.
      default_territory_name {String}:
          The name to be used as a prefix for new territories that will be
          created.
      primary_feature_class {String}:
          Specifies the class level that will be used for storing level
          attributes.TERRITORY_BOUNDARIES-Polygon features that represent the
          territory
          boundaries.TERRITORY_CENTERS-Point features that represent the
          territory
          centers.BASE_BOUNDARIES-Polygon features that represent the base-level
          feature
          boundaries.BASE_CENTERS-Point features that represent the base-level
          feature
          centers.

        """