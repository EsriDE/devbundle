# Generated documentation for module arcpy.management


class ReorderAttributeRule(object):
    """
    Reorders the evaluation order of an attribute rule.
    """

    @property
    def description(self) -> str:
        return """

        ReorderAttributeRule_management(in_table, name, evaluation_order)

        Reorders the evaluation order of an attribute rule.

     INPUTS:
      in_table (Table View):
          The table that contains the attribute rule with the evaluation order
          that will be updated.
      name (String):
          The name of the calculation rule that will have its evaluation order
          updated.
      evaluation_order (Long):
          The new evaluation order for the rule. For example, if there are five
          rules and a particular rule is in position 5 (the fifth order
          position, to be evaluated last) but you want it to be evaluated in
          position 2 (to be evaluated second), enter 2 for the value. The
          evaluation order for the rules after position 2 will be reassigned
          (that is, position 2 becomes position 3, position 3 becomes position
          4, and position 4 becomes position 5).

        """