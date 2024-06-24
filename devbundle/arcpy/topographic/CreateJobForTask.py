# Generated documentation for module arcpy.topographic


class CreateJobForTask(object):
    """
    Automatically creates a Workflow Manager (Classic) job for a task.
    """

    @property
    def description(self) -> str:
        return """

        CreateJobForTask_topographic(job_id, {database_path})

        Automatically creates a Workflow Manager (Classic) job for a task.

     INPUTS:
      job_id (Long):
          The job ID of the Workflow Manager (Classic) job that will be the
          parent to the newly created child job. The Current Task extended
          property value for this job will be used to determine the type of task
          job that will be created.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """