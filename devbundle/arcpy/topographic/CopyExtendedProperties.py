# Generated documentation for module arcpy.topographic


class CopyExtendedProperties(object):
    """
    Copies extended property values from one job to another job in the same Workflow Manager (Classic) repository.
    """

    @property
    def description(self) -> str:
        return """

        CopyExtendedProperties_topographic(source_job_id, target_job_id, property_table_name, property_fields;property_fields..., {database_path})

        Copies extended property values from one job to another job in the
        same Workflow Manager (Classic) repository.

     INPUTS:
      source_job_id (Long):
          The Job ID of the Workflow Manager (Classic) job that contains the
          properties to copy.
      target_job_id (Long):
          The Job ID of the target job that will have its properties updated.
      property_table_name (String):
          The name of the extended properties table that will be updated.
      property_fields (String):
          The properties to be copied from the source job to the target job.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """