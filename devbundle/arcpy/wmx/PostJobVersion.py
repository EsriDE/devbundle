# Generated documentation for module arcpy.wmx


class PostJobVersion(object):
    """
    Post the current version edits to the parent version of the job.
    """

    @property
    def description(self) -> str:
        return """

        PostJobVersion_wmx(Input_JobID, {Input_DatabasePath})

        Post the current version edits to the parent version of the job.

     INPUTS:
      Input_JobID (String):
          The ID for the job whose edits from the job's version are going to be
          posted to it's parent version.
      Input_DatabasePath {File}:
          The Workflow Manager (Classic) database connection file that contains
          the job information. If no connection file is specified, the current
          default Workflow Manager (Classic) database will be used.

        """