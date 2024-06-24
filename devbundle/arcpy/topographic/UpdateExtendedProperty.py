# Generated documentation for module arcpy.topographic


class UpdateExtendedProperty(object):
    """
    Updates an extended property in the identified properties table for the chosen job.
    """

    @property
    def description(self) -> str:
        return """

        UpdateExtendedProperty_topographic(job_id, properties_table_name, property_field, value, {increment_value}, {database_path})

        Updates an extended property in the identified properties table for
        the chosen job.

     INPUTS:
      job_id (Long):
          The Job ID of the Workflow Manager (Classic) job that will be updated.
      properties_table_name (String):
          The name of the extended properties table that will be updated.
      property_field (String):
          The property to be updated in the extended properties table.
      value (String):
          The value that will be set for the extended property.
      increment_value {Boolean}:
          If a value already exists for the chosen property, this parameter
          specifies whether the increment value will be added to the current
          value or will replace the current value.INCREMENT-The specified value
          will be added to any existing value for
          the property.REPLACE-The specified value will replace the existing
          value for the
          property.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """