# Generated documentation for module arcpy.management


class RemoveAttachments(object):
    """
    Removes attachments from geodatabase feature class or table records.
    """

    @property
    def description(self) -> str:
        return """

        RemoveAttachments_management(in_dataset, in_join_field, in_match_table, in_match_join_field, {in_match_name_field})

        Removes attachments from geodatabase feature class or table records.

     INPUTS:
      in_dataset (Table View):
          A geodatabase table or feature class from which attachments will be
          removed. Attachments are not removed directly from this table; they
          are removed from the related attachment table that stores the
          attachments. The dataset must have attachments enabled.
      in_join_field (Field):
          A field from the in_dataset parameter value that contains values that
          match the values in the in_match_join_field parameter value. Records
          that have join field values that match the in_dataset parameter value
          and the in_match_table parameter value will have attachments removed.
          This field can be an Object ID field or any other identifying
          attribute.
      in_match_table (Table View):
          A table that identifies which input records will have attachments
          removed.
      in_match_join_field (Field):
          A field from the match table that indicates which records in the
          in_dataset parameter value will have specified attachments removed.
          This field can have values that match the in_dataset Object ID field
          or some other identifying attribute.
      in_match_name_field {Field}:
          A field from the match table that contains the names of the
          attachments that will be removed from the in_dataset parameter value's
          records. If no name field is specified, all attachments will be
          removed from each record specified in the in_match_join_field
          parameter value. If a name field is specified but a record has a null
          or empty value in the name field, all attachments will be removed from
          that record. This field's values should be the short names of the
          attachments to remove, not the full paths to the files used to make
          the original attachments.

        """