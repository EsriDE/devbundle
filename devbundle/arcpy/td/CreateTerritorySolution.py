# Generated documentation for module arcpy.td


class CreateTerritorySolution(object):
    """
    Creates a new territory solution with two levels and loads input features into the base level.
    """

    @property
    def description(self) -> str:
        return """

        CreateTerritorySolution_td(in_features, solution_name, {id_field}, {name_field}, {territory_level_name}, {default_territory_name}, {in_boundary_mask})

        Creates a new territory solution with two levels and loads input
        features into the base level.

     INPUTS:
      in_features (Feature Layer):
          The geometry or data features that will be used as the base level of
          the created solution. The level will have the same name as the input
          features.
      solution_name (String):
          The name of the territory solution to be created.
      id_field {Field}:
          The field that contains ID values for objects in the level.
      name_field {Field}:
          The field that contains name values for objects in the level.
      territory_level_name {String}:
          The name of the territory level-for example, level 2.
      default_territory_name {String}:
          The prefix for the names of the new territories that will be
          created-for example, Territory 1, Territory 2, and Territory 3 or
          District 1, District 2, and District 3.
      in_boundary_mask {Feature Layer}:
          The layer that is used as a mask to limit the growth of point-based
          layers.

        """