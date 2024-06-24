# Generated documentation for module arcpy.management


class DisableAttributeRules(object):
    """
    Disables one or more attribute rules for a dataset.
    """

    @property
    def description(self) -> str:
        return """

        DisableAttributeRules_management(in_table, names;names..., {type})

        Disables one or more attribute rules for a dataset.

     INPUTS:
      in_table (Table View):
          The table or feature class that contains the attribute rule to be
          disabled.
      names (String):
          The names of the rules to disable for the dataset.
      type {String}:
          Specifies the type of attribute rules to disable. The tool will verify
          that the type of rule specified in this parameter matches the rule
          type specified. If they do not match, the rule will not be
          disabled.CALCULATION-Disable a calculation rule.CONSTRAINT-Disable a
          constraint
          rule.VALIDATION-Disable a validation rule.

        """