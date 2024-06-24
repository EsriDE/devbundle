# Generated documentation for module arcpy.topographic


class SetTaskGroupDependencies(object):
    """
    Creates dependencies between a job and other existing Task Group jobs based on the criteria defined in the extended properties.
    """

    @property
    def description(self) -> str:
        return """

        SetTaskGroupDependencies_topographic(job_id, {database_path})

        Creates dependencies between a job and other existing Task Group jobs
        based on the criteria defined in the extended properties.

     INPUTS:
      job_id (Long):
          The job ID of the Workflow Manager (Classic) job that will have
          dependencies set.
      database_path {File}:
          The Workflow Manager (Classic) database connection file that contains
          the job information. If no connection file is specified, the current
          default Workflow Manager (Classic) database will be used.

        """