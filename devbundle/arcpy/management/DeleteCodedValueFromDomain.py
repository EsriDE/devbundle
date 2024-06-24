# Generated documentation for module arcpy.management


class DeleteCodedValueFromDomain(object):
    """
    Removes a value from a coded value domain.
    """

    @property
    def description(self) -> str:
        return """

        DeleteCodedValueFromDomain_management(in_workspace, domain_name, code;code...)

        Removes a value from a coded value domain.

     INPUTS:
      in_workspace (Workspace):
          The workspace containing the domain to be updated.
      domain_name (String):
          The name of the coded value domain to be updated.
      code (String):
          The value(s) to be deleted from the specified domain.

        """