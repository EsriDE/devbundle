# Generated documentation for module arcpy.management


class FindIdentical(object):
    """
    Reports any records in a feature class or table that have identical values in a list of fields, and generates a table listing these identical records. If the field Shape is selected, feature geometries are compared.
    """

    @property
    def description(self) -> str:
        return """

        FindIdentical_management(in_dataset, out_dataset, fields;fields..., {xy_tolerance}, {z_tolerance}, {output_record_option})

        Reports any records in a feature class or table that have identical
        values in a list of fields, and generates a table listing these
        identical records. If the field Shape is selected, feature geometries
        are compared.

     INPUTS:
      in_dataset (Table View):
          The table or feature class for which identical records will be found.
      fields (Field):
          The field or fields whose values will be compared to find identical
          records.
      xy_tolerance {Linear Unit}:
          The xy tolerance that will be applied to each vertex when
          evaluating if there is an identical vertex in another feature. This
          parameter is enabled only whenis selected as one of the fields.
          Shape
      z_tolerance {Double}:
          The Z tolerance that will be applied to each vertex when
          evaluating if there is an identical vertex in another feature. This
          parameter is enabled only whenis selected as one of the fields.
          Shape
      output_record_option {Boolean}:
          Choose if you want only duplicated records in the output table.ALL-All
          input records will have corresponding records in the output
          table. This is the default.ONLY_DUPLICATES-Only duplicate records will
          have corresponding records
          in the output table. The output will be empty if no duplicate is
          found.

     OUTPUTS:
      out_dataset (Table):
          The output table reporting identical records. Thefield in the
          output table will have the same value for identical records.
          FEAT_SEQ

        """