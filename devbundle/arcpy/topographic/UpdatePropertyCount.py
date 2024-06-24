# Generated documentation for module arcpy.topographic


class UpdatePropertyCount(object):
    """
    Increases the value in an extended property by the update value each time the tool is run so that metrics are recorded.
    """

    @property
    def description(self) -> str:
        return """

        UpdatePropertyCount_topographic(job_id, properties_table_name, property_field, update_value, {database_path})

        Increases the value in an extended property by the update value each
        time the tool is run so that metrics are recorded.

     INPUTS:
      job_id (Long):
          The ID of the Workflow Manager (Classic) job that will be updated.
      properties_table_name (String):
          The name of the extended properties table that will be updated.
      property_field (String):
          The property to be updated in the selected extended properties table.
      update_value (Long):
          The value by which the selected extended property will be increased.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """