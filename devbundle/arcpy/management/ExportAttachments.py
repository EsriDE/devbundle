# Generated documentation for module arcpy.management


class ExportAttachments(object):
    """
    Exports file attachments from the records of a geodatabase feature class or table to a specified folder. Attachments can also be exported to subdirectories based on an attribute value from a specified attribute column. Exported attachments can be renamed using one or more field attribute values.
    """

    @property
    def description(self) -> str:
        return """

        ExportAttachments_management(in_dataset, out_location, {subdirectory_field}, {name_format}, {name_fields;name_fields...})

        Exports file attachments from the records of a geodatabase feature
        class or table to a specified folder. Attachments can also be exported
        to subdirectories based on an attribute value from a specified
        attribute column. Exported attachments can be renamed using one or
        more field attribute values.

     INPUTS:
      in_dataset (Table View):
          The geodatabase table or feature class from which attachments will be
          exported.The input must be stored in a version 10.0 or later
          geodatabase, and
          the table must have attachments enabled.
      out_location (Folder):
          The folder where the attachment files will be exported.
      subdirectory_field {Field}:
          A field from the in_dataset parameter value that will be used to
          create subdirectory names.
      name_format {String}:
          Specifies the format that will be used for naming exported
          attachments.ORIGINAL-The output file names will use the original file
          names stored
          in the geodatabase.REPLACE-The output file names will use the field
          values of the
          name_fields parameter values.PREFIX-The output file names will use the
          original file names with a
          prefix from the field values of the name_fields parameter
          values.SUFFIX-The output file names will use the original file names
          with a
          suffix from the field values of the name_fields parameter values.
      name_fields {Field}:
          The fields from the in_dataset parameter value that will be used to
          rename the exported attachments. If multiple fields are specified, the
          output files will use the field values concatenated with an underscore
          in the order they are specified. For example, if two field
          names are specified, and name_format
          parameter is set to REPLACE, the field values for the first record
          areand, and the attachment is a .jpg file, the exported file will be
          named Main_Street.jpg. MainStreetThis parameter is enabled when
          the name_format parameter is set to
          REPLACE, PREFIX, or SUFFIX.

        """