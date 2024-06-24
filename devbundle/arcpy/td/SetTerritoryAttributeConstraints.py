# Generated documentation for module arcpy.td


class SetTerritoryAttributeConstraints(object):
    """
    Sets variables for adding constraints when solving the territory solution.
    """

    @property
    def description(self) -> str:
        return """

        SetTerritoryAttributeConstraints_td(in_territory_solution, level, {constraints;constraints...})

        Sets variables for adding constraints when solving the territory
        solution.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The Territory Design solution layer that will be used in the analysis
      level (String):
          The level to which the constraints will be applied.
      constraints {Value Table}:
          The variables that will be used for constraining the territory
          solution.variable-Numeric value to be used as the
          constraint.minimum-Numeric
          value that sets a hard limit for the territories'
          lower bound.maximum-Numeric value that sets a hard limit for the
          territories'
          upper bound.ideal_value-Numeric value that sets a soft limit for the
          ideal value
          for the territory solution.weight-The influence a constraint value has
          on the territory solution.
          The number must be greater than 0.

        """