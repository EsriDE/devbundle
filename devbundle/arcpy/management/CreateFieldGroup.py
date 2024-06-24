# Generated documentation for module arcpy.management


class CreateFieldGroup(object):
    """
    Create a field group for a feature class or table. Field groups are used when creating contingent values.
    """

    @property
    def description(self) -> str:
        return """

        CreateFieldGroup_management(target_table, name, fields;fields..., {is_restrictive})

        Create a field group for a feature class or table. Field groups are
        used when creating contingent values.

     INPUTS:
      target_table (Table View):
          The input geodatabase table or feature class in which the field group
          will be created.
      name (String):
          The name of the field group that will be created. This name must be
          unique to the feature class or table that will contain the field
          group.
      fields (String):
          The names of the fields in the field group.
      is_restrictive {Boolean}:
          Specifies if the field group is restrictive. This parameter allows you
          to control the editing experience when using contingent
          values.RESTRICT-The field group is restrictive. Values entered on a
          field in
          the field group are restricted to those specified as contingent
          values. This is the default.DO_NOT_RESTRICT-The field group is not
          restrictive. Values can be
          committed to a field in a field group even if they are not specified
          as contingent values.

        """