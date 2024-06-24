# Generated documentation for module arcpy.management


class CreateTable(object):
    """
    Creates a geodatabase table or a dBASE table.
    """

    @property
    def description(self) -> str:
        return """

        CreateTable_management(out_path, out_name, {template;template...}, {config_keyword}, {out_alias}, {oid_type})

        Creates a geodatabase table or a dBASE table.

     INPUTS:
      out_path (Workspace):
          The workspace where the output table will be created.
      out_name (String):
          The name of the table that will be created.
      template {Table View}:
          One or more datasets from which the attribute schema will be used to
          define the output table. Fields in the template datasets will be added
          to the output table.
      config_keyword {String}:
          The configuration keyword that determines the storage parameters of
          the table in an enterprise geodatabase.
      out_alias {String}:
          The alternate name of the output table that will be created.
      oid_type {String}:
          Specifies whether the output Object ID field will be 32 bit or 64
          bit.SAME_AS_TEMPLATE-The output Object ID field type (32 bit or 64
          bit)
          will be the same as the Object ID field of the first template dataset.
          This is the default.64_BIT-The output Object ID field will be 64
          bit.32_BIT-The output Object ID field will be 32 bit.

        """