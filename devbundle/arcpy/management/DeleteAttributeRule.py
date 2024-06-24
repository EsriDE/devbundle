# Generated documentation for module arcpy.management


class DeleteAttributeRule(object):
    """
    Deletes one or more attribute rules from a dataset.
    """

    @property
    def description(self) -> str:
        return """

        DeleteAttributeRule_management(in_table, names;names..., {type})

        Deletes one or more attribute rules from a dataset.

     INPUTS:
      in_table (Table View):
          The table or feature class containing the attribute rules that will be
          deleted.
      names (String):
          The names of the rules that will be deleted from the dataset.
      type {String}:
          Specifies the type of attribute rules that will be
          deleted.CALCULATION-Calculation rules will be
          deleted.CONSTRAINT-Constraint
          rules will be deleted.VALIDATION-Validation rules will be deleted.

        """