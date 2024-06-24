# Generated documentation for module arcpy.topographic


class SetDataWorkspace(object):
    """
    Sets the data workspace for the chosen job to the appropriate database based on the production type of the job.
    """

    @property
    def description(self) -> str:
        return """

        SetDataWorkspace_topographic(job_id, {database_path})

        Sets the data workspace for the chosen job to the appropriate database
        based on the production type of the job.

     INPUTS:
      job_id (Long):
          The job ID of the Workflow Manager (Classic) job that will be updated.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """