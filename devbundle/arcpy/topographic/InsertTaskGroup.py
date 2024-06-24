# Generated documentation for module arcpy.topographic


class InsertTaskGroup(object):
    """
    Adds tasks from the chosen task group to a job when required by workflow execution.
    """

    @property
    def description(self) -> str:
        return """

        InsertTaskGroup_topographic(job_id, task_group_id, {database_path})

        Adds tasks from the chosen task group to a job when required by
        workflow execution.

     INPUTS:
      job_id (Long):
          The ID of the Workflow Manager (Classic) job that will be updated.
          This is the ID for the parent task group job, not the task job.
      task_group_id (Long):
          The ID of the task group that defines the tasks that will be inserted
          into the selected job's task list.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """