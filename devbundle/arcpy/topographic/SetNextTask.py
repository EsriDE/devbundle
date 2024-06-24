# Generated documentation for module arcpy.topographic


class SetNextTask(object):
    """
    Sets the next task in a workflow from the task list.
    """

    @property
    def description(self) -> str:
        return """

        SetNextTask_topographic(job_id, {database_path})

        Sets the next task in a workflow from the task list.

     INPUTS:
      job_id (Long):
          The ID of the Workflow Manager (Classic) job that will be updated.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """