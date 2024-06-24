# Generated documentation for module arcpy.td


class RebuildTerritorySolution(object):
    """
    Updates the territory solution to reflect changes made to the base level.
    """

    @property
    def description(self) -> str:
        return """

        RebuildTerritorySolution_td(in_territory_solution, {in_boundary_mask})

        Updates the territory solution to reflect changes made to the base
        level.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The input territory solution.
      in_boundary_mask {Feature Layer}:
          The layer that is used as a mask to limit the growth of point-based
          layers.

        """