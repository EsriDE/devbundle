# Generated documentation for module arcpy.topographic


class SetTaskList(object):
    """
    Populates the list of expected tasks for a job based on the selected task group.
    """

    @property
    def description(self) -> str:
        return """

        SetTaskList_topographic(job_id, {database_path})

        Populates the list of expected tasks for a job based on the selected
        task group.

     INPUTS:
      job_id (Long):
          The ID of the Workflow Manager (Classic) job that will be updated.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """