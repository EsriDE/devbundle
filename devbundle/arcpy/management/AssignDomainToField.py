# Generated documentation for module arcpy.management


class AssignDomainToField(object):
    """
    Sets the domain for a particular field and, optionally, for a subtype. If no subtype is specified, the domain is only assigned to the specified field.
    """

    @property
    def description(self) -> str:
        return """

        AssignDomainToField_management(in_table, field_name, domain_name, {subtype_code;subtype_code...})

        Sets the domain for a particular field and, optionally, for a subtype.
        If no subtype is specified, the domain is only assigned to the
        specified field.

     INPUTS:
      in_table (Table View):
          The name of the table or feature class containing the field that will
          be assigned a domain.
      field_name (Field):
          The name of the field to be assigned a domain.
      domain_name (String):
          The name of a geodatabase domain to assign to the field name.
          Available domains will automatically be loaded.
      subtype_code {String}:
          The subtype code to be assigned a domain.

        """