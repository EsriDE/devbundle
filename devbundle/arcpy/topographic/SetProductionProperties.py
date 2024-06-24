# Generated documentation for module arcpy.topographic


class SetProductionProperties(object):
    """
    Updates the production properties extended properties table of a Workflow Manager (Classic) job based on its production type to ensure that the job and any associated tasks use the correct data and maps.
    """

    @property
    def description(self) -> str:
        return """

        SetProductionProperties_topographic(job_id, {database_path})

        Updates the production properties extended properties table of a
        Workflow Manager (Classic) job based on its production type to ensure
        that the job and any associated tasks use the correct data and maps.

     INPUTS:
      job_id (Long):
          The ID of the Workflow Manager (Classic) job that will be updated.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """