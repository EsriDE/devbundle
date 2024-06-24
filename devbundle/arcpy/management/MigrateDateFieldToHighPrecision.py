# Generated documentation for module arcpy.management


class MigrateDateFieldToHighPrecision(object):
    """
    Migrates date fields in a table to high precision.
    """

    @property
    def description(self) -> str:
        return """

        MigrateDateFieldToHighPrecision_management(in_table, date_fields;date_fields...)

        Migrates date fields in a table to high precision.

     INPUTS:
      in_table (Table View):
          The geodatabase table or feature class containing the date fields that
          will be migrated to high precision.
      date_fields (Field):
          The date fields that will be migrated to high precision.

        """