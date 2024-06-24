# Generated documentation for module arcpy.management


class EnableAttributeRules(object):
    """
    Enables one or more attribute rules in a dataset
    """

    @property
    def description(self) -> str:
        return """

        EnableAttributeRules_management(in_table, names;names..., {type})

        Enables one or more attribute rules in a dataset

     INPUTS:
      in_table (Table View):
          The table or feature class that contains the attribute rule to be
          enabled.
      names (String):
          The names of the rules to enable for the dataset.
      type {String}:
          Specifies the type of attribute rules to enable. The tool will verify
          that the type of rule specified in this parameter matches the rule
          type specified. If they do not match, the rule will not be
          enabled.CALCULATION-Enable a calculation rule.CONSTRAINT-Enable a
          constraint
          rule.VALIDATION-Enable a validation rule.

        """