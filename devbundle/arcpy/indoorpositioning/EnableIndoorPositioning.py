# Generated documentation for module arcpy.indoorpositioning


class EnableIndoorPositioning(object):
    """
    Creates the feature classes and table necessary for storing ArcGIS IPS data in an existing geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        EnableIndoorPositioning_indoorpositioning(in_workspace)

        Creates the feature classes and table necessary for storing ArcGIS IPS
        data in an existing geodatabase.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase where the ArcGIS IPS table and feature classes will be
          created. It can be a file or enterprise geodatabase.

        """