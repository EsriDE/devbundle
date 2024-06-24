# Generated documentation for module arcpy.management


class SetValueForRangeDomain(object):
    """
    Sets the minimum and maximum values for an existing Range domain.
    """

    @property
    def description(self) -> str:
        return """

        SetValueForRangeDomain_management(in_workspace, domain_name, min_value, max_value)

        Sets the minimum and maximum values for an existing Range domain.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase containing the domain to be updated.
      domain_name (String):
          The name of the range domain to be updated.
      min_value (String):
          The minimum value of the range domain.
      max_value (String):
          The maximum value of the range domain.

        """