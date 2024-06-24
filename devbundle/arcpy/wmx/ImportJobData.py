# Generated documentation for module arcpy.wmx


class ImportJobData(object):
    """
    Imports configuration and job information from a Workflow Manager (Classic) repository to a destination repository. This tool is most useful for setting up a repository similar to an existing repository, disconnected repository replica creation, and changing synchronization.
    """

    @property
    def description(self) -> str:
        return """

        ImportJobData_wmx(Input_File, Input_Merge, {Input_DatabasePath}, {Input_Repository_Name})

        Imports configuration and job information from a Workflow Manager
        (Classic) repository to a destination repository. This tool is most
        useful for setting up a repository similar to an existing repository,
        disconnected repository replica creation, and changing
        synchronization.

     INPUTS:
      Input_File (File):
          The JXL file that contains the jobs and configuration elements
          generated using the Export Job Data tool.
      Input_Merge (Boolean):
          Specifies whether contents of the destination Workflow Manager
          (Classic) repository should be combined rather than overwritten with
          the contents of the input configuration file.COMBINE-Combines the
          contents of the destination Workflow Manager
          (Classic) database with the contents of the input configuration
          file.REPLACE-Replaces the entire contents of the destination Workflow
          Manager (Classic) database with the contents of the input
          configuration file.
      Input_DatabasePath {File}:
          The Workflow Manager (Classic) connection file that contains the
          connection information to the destination repository. If no connection
          file is specified, the current default Workflow Manager (Classic)
          database in the project will be used.
      Input_Repository_Name {String}:
          The name of the repository as specified in the Workflow Manager
          (Classic) system settings. This name should be unique within all the
          repositories in your cluster. If the repository name is not specified,
          the current default Workflow Manager (Classic) repository name will be
          used.

        """