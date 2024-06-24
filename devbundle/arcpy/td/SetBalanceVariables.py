# Generated documentation for module arcpy.td


class SetBalanceVariables(object):
    """
    Configures variables to be used in the balancing process.
    """

    @property
    def description(self) -> str:
        return """

        SetBalanceVariables_td(in_territory_solution, level, {variables;variables...})

        Configures variables to be used in the balancing process.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The name of the input territory solution.
      level (String):
          The name of the level to which the calculated field will be added.
      variables {Value Table}:
          The variables that will be used in the balance process.
          variable-The defined input.weight-The amount of influence a given
          variable has in the analysis.

        """