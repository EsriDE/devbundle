# Generated documentation for module arcpy.management


class AddAttachments(object):
    """
    Adds file attachments to the records of a geodatabase feature class or table. The attachments are stored in the geodatabase in a separate attachment table that maintains linkage to the target dataset. Attachments are added to the target dataset using a match table that indicates for each input record (or an attribute group of records) the path to a file to add as an attachment to that record.
    """

    @property
    def description(self) -> str:
        return """

        AddAttachments_management(in_dataset, in_join_field, in_match_table, in_match_join_field, in_match_path_field, {in_working_folder})

        Adds file attachments to the records of a geodatabase feature class or
        table. The attachments are stored in the geodatabase in a separate
        attachment table that maintains linkage to the target dataset.
        Attachments are added to the target dataset using a match table that
        indicates for each input record (or an attribute group of records) the
        path to a file to add as an attachment to that record.

     INPUTS:
      in_dataset (Table View):
          The geodatabase table or feature class where attachments will be
          added. Attachments are not added directly to this table, but to a
          related attachment table that maintains linkage to the input
          dataset.The dataset must be stored in a version 10.0 or later
          geodatabase, and
          the table must have attachments enabled.
      in_join_field (Field):
          A field from the in_dataset parameter value that has matching values
          in the in_match_join_field parameter value. Records with matching
          values will have attachments added. This field can be an Object ID
          field or any other identifying attribute.
      in_match_table (Table View):
          A table that identifies which input records will have attachments
          added and the paths to those attachments.
      in_match_join_field (Field):
          A field from the in_match_table parameter value that indicates which
          records in the in_dataset parameter value will have specified
          attachments added.
      in_match_path_field (Field):
          A field from theparameter value that contains paths to the
          attachments to add to the records of theparameter value. Match
          TableInput DatasetA field from the in_match_table parameter value that
          contains paths to
          the attachments to add to the records of the in_dataset parameter
          value.
      in_working_folder {Folder}:
          A folder or workspace where attachment files are centralized. By
          specifying a working folder, the paths in the in_match_path_field
          parameter value can be the short names of files relative to the
          working folder.For example, if loading attachments with paths such as
          C:\MyPictures\image1.jpg and C:\MyPictures\image2.jpg, use a parameter
          value of C:\MyPictures. Then the paths in the in_match_path_field
          parameter value can be the short names such as image1.jpg and
          image2.jpg, instead of the full paths.

        """