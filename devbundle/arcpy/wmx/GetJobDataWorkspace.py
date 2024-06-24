# Generated documentation for module arcpy.wmx


class GetJobDataWorkspace(object):
    """
    Gets the job data workspace as an enterprise geodatabase connection file. This tool is typically used in ModelBuilder to retrieve the connection file for use as an input to other tools such as Reconcile Versions in the model.
    """

    @property
    def description(self) -> str:
        return """

        GetJobDataWorkspace_wmx(Input_JobID, {Input_DatabasePath}, {Input_SDEFileLocation})

        Gets the job data workspace as an enterprise geodatabase connection
        file. This tool is typically used in ModelBuilder to retrieve the
        connection file for use as an input to other tools such as Reconcile
        Versions in the model.

     INPUTS:
      Input_JobID (String):
          The ID for the job whose data workspace connection is to be retrieved.
      Input_DatabasePath {File}:
          The Workflow Manager (Classic) database connection file that contains
          the job information. If no connection file is specified, the current
          default Workflow Manager (Classic) database in the project is used.
      Input_SDEFileLocation {Folder}:
          The job's data workspace connection file will be written to the
          specified folder.

        """