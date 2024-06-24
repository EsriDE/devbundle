# Generated documentation for module arcpy.topographic


class SetTaskStatus(object):
    """
    Updates the status of a task based on the state of the Workflow Manager (Classic) job created for the task.
    """

    @property
    def description(self) -> str:
        return """

        SetTaskStatus_topographic(job_id, parent_id, status, {database_path})

        Updates the status of a task based on the state of the Workflow
        Manager (Classic) job created for the task.

     INPUTS:
      job_id (Long):
          The job ID of the task job that has a change in status.
      parent_id (Long):
          The job ID of the task group job that is the parent to the task job.
      status (String):
          Specifies the status of the selected task.WORKING-Work has begun for
          the task.COMPLETE-Work has been completed
          for the task.RESTART-Work will be restarted by creating a new job of
          the same type.
      database_path {File}:
          The Workflow Manager (Classic) database connection file that contains
          the job information. If no connection file is specified, the current
          default Workflow Manager (Classic) database will be used.

        """