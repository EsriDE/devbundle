# Generated documentation for module arcpy.td


class ValidateTerritories(object):
    """
    Validates a territory solution for invalid territories.
    """

    @property
    def description(self) -> str:
        return """

        ValidateTerritories_td(in_territory_solution, level)

        Validates a territory solution for invalid territories.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The territory solution that will be validated.
      level (String):
          The level that will be analyzed in the validation.

        """