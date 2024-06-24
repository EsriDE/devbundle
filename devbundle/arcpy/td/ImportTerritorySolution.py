# Generated documentation for module arcpy.td


class ImportTerritorySolution(object):
    """
    Creates a new territory solution and imports the territories hierarchy from a table or a layer.
    """

    @property
    def description(self) -> str:
        return """

        ImportTerritorySolution_td(in_data, solution_name, level_settings;level_settings...)

        Creates a new territory solution and imports the territories hierarchy
        from a table or a layer.

     INPUTS:
      in_data (Table View):
          The layer or records to be imported.
      solution_name (String):
          The name of the territory solution to be created.
      level_settings (Value Table):
          The level settings for importing the territories
          hierarchy.level_name-The name of the level
          (required).default_territory_name-The
          prefix for the new territories that will,
          subsequently, be created at the level (optional).id_field-The field
          that contains IDs (unique IDs) for territories
          (required).name_field-The field that contains names for territories
          (optional).parent_id_field-The field that contains IDs of parent
          territories
          (optional). primary_feature_class-Specifies the class level
          that will be
          used for storing level attributes (optional).
          TERRITORY_BOUNDARIES-Level attributes will be stored using the
          boundaries of the territory solution.TERRITORY_CENTERS-Level
          attributes will be stored using the boundary
          centers of the territory solution.BASE_BOUNDARIES-Level attributes
          will be stored using the boundaries
          of the base layer.BASE_CENTERS-Level attributes will be stored using
          the boundary
          centers of the base layer.

        """