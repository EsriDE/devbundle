# Generated documentation for module arcpy.td


class ExportTerritorySolution(object):
    """
    Exports a territory solution to a feature class. The export includes records from all levels (hierarchy) of the solution.
    """

    @property
    def description(self) -> str:
        return """

        ExportTerritorySolution_td(in_territory_solution, out_feature_class, {output_geometry_type})

        Exports a territory solution to a feature class. The export includes
        records from all levels (hierarchy) of the solution.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The Territory Design solution layer that will be exported.
      output_geometry_type {String}:
          Specifies the feature geometry type to
          export.TERRITORY_BOUNDARIES-Polygon features that represent the
          territory
          boundaries will be exported.TERRITORY_CENTERS-Point features that
          represent the territory centers
          will be exported.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will contain the exported territory solution.

        """