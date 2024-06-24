# Generated documentation for module arcpy.topographic


class UpdateTaskGroupMetrics(object):
    """
    Updates and summarizes task group metrics that are part of the standard Topographic Workflow deployment of Workflow Manager (Classic).
    """

    @property
    def description(self) -> str:
        return """

        UpdateTaskGroupMetrics_topographic(job_id, {status_layer}, {status_field}, {database_path})

        Updates and summarizes task group metrics that are part of the
        standard Topographic Workflow deployment of Workflow Manager
        (Classic).

     INPUTS:
      job_id (Long):
          The job ID of the job that will be updated.
      status_layer {Feature Layer}:
          The feature class containing status polygons that keep track of the
          last time work occurred over an extent. Only use this parameter to
          update a polygon feature class that is not the standard status
          polygons created by the Topographic Workflow.
      status_field {Field}:
          The text or date field in which the last modified date will be
          stored. This parameter is enabled if aparameter value is defined.
          Status Layer
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """