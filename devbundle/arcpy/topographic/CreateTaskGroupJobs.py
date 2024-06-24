# Generated documentation for module arcpy.topographic


class CreateTaskGroupJobs(object):
    """
    Creates task group jobs based on the properties of an existing job.
    """

    @property
    def description(self) -> str:
        return """

        CreateTaskGroupJobs_topographic(job_id, {database_path})

        Creates task group jobs based on the properties of an existing job.

     INPUTS:
      job_id (Long):
          The job ID of the ArcGIS Workflow Manager (Classic) job that will have
          dependencies set.
      database_path {File}:
          The Workflow Manager (Classic) database connection file that contains
          the job information. If no connection file is specified, the default
          Workflow Manager (Classic) database will be used.

        """