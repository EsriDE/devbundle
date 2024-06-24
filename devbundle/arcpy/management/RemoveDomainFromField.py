# Generated documentation for module arcpy.management


class RemoveDomainFromField(object):
    """
    Removes an attribute domain association from a feature class or table field.
    """

    @property
    def description(self) -> str:
        return """

        RemoveDomainFromField_management(in_table, field_name, {subtype_code;subtype_code...})

        Removes an attribute domain association from a feature class or table
        field.

     INPUTS:
      in_table (Table View):
          The input table containing the attribute domain that will be removed.
      field_name (Field):
          The field that will no longer be associated with an attribute domain.
      subtype_code {String}:
          The subtype code(s) that will no longer be associated with an
          attribute domain.

        """