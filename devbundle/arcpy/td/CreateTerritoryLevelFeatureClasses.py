# Generated documentation for module arcpy.td


class CreateTerritoryLevelFeatureClasses(object):
    """
    Creates feature classes for a specified territory level.
    """

    @property
    def description(self) -> str:
        return """

        CreateTerritoryLevelFeatureClasses_td(in_territory_solution, level, feature_classes;feature_classes...)

        Creates feature classes for a specified territory level.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The Territory Design solution layer that will be used in the analysis.
      level (String):
          The level to which the feature classes will be added.
      feature_classes (String):
          Specifies the feature classes that will be created at the specified
          level parameter value.TERRITORY_BOUNDARIES-Polygon features that
          represent the territory
          boundaries will be created.TERRITORY_CENTERS-Point features that
          represent the territory centers
          will be created.BASE_BOUNDARIES-Polygon features that represent the
          base boundaries
          will be created.BASE_CENTERS-Point features that represent the base
          centers will be
          created.LINE_BARRIERS-Line features that restrict traversal across a
          line will
          be created.SEED_POINTS-Point features from which territories are
          derived will be
          created.RESTRICTED_AREAS-Polygon features that prevent the creation of
          territories will be created.POLYGON_BARRIERS-Polygon features that
          restrict traversal across a
          polygon will be created.

        """