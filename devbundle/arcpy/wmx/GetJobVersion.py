# Generated documentation for module arcpy.wmx


class GetJobVersion(object):
    """
    Gets the job version as an enterprise geodatabase connection file to process data in a version.
    """

    @property
    def description(self) -> str:
        return """

        GetJobVersion_wmx(Input_JobID, {Input_DatabasePath})

        Gets the job version as an enterprise geodatabase connection file to
        process data in a version.

     INPUTS:
      Input_JobID (String):
          The ID for the job whose version is to be retrieved.
      Input_DatabasePath {File}:
          The Workflow Manager (Classic) database connection file that contains
          the job information. If no connection file is specified, the current
          default Workflow Manager (Classic) database in the project is used.

        """