# Generated documentation for module arcpy.management


class AddCodedValueToDomain(object):
    """
    Adds a value to a domain's coded value list.
    """

    @property
    def description(self) -> str:
        return """

        AddCodedValueToDomain_management(in_workspace, domain_name, code, code_description)

        Adds a value to a domain's coded value list.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase containing the domain to be updated.
      domain_name (String):
          The name of the attribute domain that will have a value added to its
          coded value list.
      code (String):
          The value to be added to the specified domain's coded value list.
      code_description (String):
          A description of what the coded value represents.

        """