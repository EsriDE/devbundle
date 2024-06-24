# Generated documentation for module arcpy.topographic


class CancelRemainingTasks(object):
    """
    Prevents the remaining tasks in a job from starting or being created. The active task and its task group job will still complete.
    """

    @property
    def description(self) -> str:
        return """

        CancelRemainingTasks_topographic(job_id, {database_path})

        Prevents the remaining tasks in a job from starting or being created.
        The active task and its task group job will still complete.

     INPUTS:
      job_id (Long):
          The job ID of the parent ArcGIS Workflow Manager (Classic) task group
          job that contains the task list derived from the Set Task List tool.
      database_path {File}:
          The ArcGIS Workflow Manager (Classic) database connection file that
          contains the job information. If a connection is not specified, the
          current default ArcGIS Workflow Manager (Classic) database will be
          used.

        """