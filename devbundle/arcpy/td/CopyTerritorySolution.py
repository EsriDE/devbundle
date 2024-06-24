# Generated documentation for module arcpy.td


class CopyTerritorySolution(object):
    """
    Creates a copy of a territory solution.
    """

    @property
    def description(self) -> str:
        return """

        CopyTerritorySolution_td(in_territory_solution, target_gdb, territory_solution_name)

        Creates a copy of a territory solution.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The input territory solution.
      target_gdb (Workspace):
          The location of the output geodatabase.
      territory_solution_name (String):
          The name of the copied territory solution

        """