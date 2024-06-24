# Generated documentation for module arcpy.td


class AddLevelVariables(object):
    """
    Adds a new field at the specified level.
    """

    @property
    def description(self) -> str:
        return """

        AddLevelVariables_td(in_territory_solution, level, base_level, variables;variables...)

        Adds a new field at the specified level.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The input territory solution.
      level (String):
          The level to which the calculated field will be added.
      base_level (String):
          The level below the territory level to which the attribute value will
          be added.
      variables (Value Table):
          The variables that will be added to the level.statistic_field-The
          field that will be used for statistical
          calculation. statistic-The type of statistical calculation.
          count-The number of values included in the calculation will be
          identified.sum-The values for the specified field will be added
          together.maximum-The largest value for the specified field will be
          identified.minimum-The smallest value for the specified field will be
          identified.average-The average of the values for the specified field
          will be
          calculated.median-The median of the values for the specified field
          will be
          calculated.standard_deviation-The standard deviation of values for the
          specified
          field will be calculated.percent_of_total-The percentage of each value
          for the specified field
          will be calculated from the total sum of the values for the
          field.field_name-The valid name of the field on the level where the
          calculated data will be stored.field_alias_name-The readable and
          understandable name of the
          calculated field.

        """