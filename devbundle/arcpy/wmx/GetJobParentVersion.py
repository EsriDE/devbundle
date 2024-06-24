# Generated documentation for module arcpy.wmx


class GetJobParentVersion(object):
    """
    Gets the parent version of a job as an enterprise geodatabase connection file to be used for posting edits in a geoprocessing model to the correct parent version.
    """

    @property
    def description(self) -> str:
        return """

        GetJobParentVersion_wmx(Input_JobID, {Input_DatabasePath})

        Gets the parent version of a job as an enterprise geodatabase
        connection file to be used for posting edits in a geoprocessing model
        to the correct parent version.

     INPUTS:
      Input_JobID (String):
          The ID for the job's parent version to be retrieved.
      Input_DatabasePath {File}:
          The Workflow Manager (Classic) database connection file that contains
          the job information. If no connection file is specified, the current
          default Workflow Manager (Classic) database in the project is used.

        """