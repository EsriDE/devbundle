# Generated documentation for module arcpy.management


class DeleteDomain(object):
    """
    Deletes a domain from a workspace.
    """

    @property
    def description(self) -> str:
        return """

        DeleteDomain_management(in_workspace, domain_name)

        Deletes a domain from a workspace.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase that contains the domain to be deleted.
      domain_name (String):
          The name of the domain to be deleted.

        """