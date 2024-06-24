# Generated documentation for module arcpy.management


class AlterFieldGroup(object):
    """
    Alters the properties of a field group.
    """

    @property
    def description(self) -> str:
        return """

        AlterFieldGroup_management(target_table, name, {new_name}, {fields;fields...}, {is_restrictive})

        Alters the properties of a field group.

     INPUTS:
      target_table (Table View):
          The table containing the field group to be altered.
      name (String):
          The name of the field group to be altered.
      new_name {String}:
          The new, unique name for the field group.
      fields {String}:
          The fields that participate in the field group. To modify the fields,
          enter new field names. Provided values will replace, not append, the
          current list of fields that participates in the field group. If no
          values are provided, the fields will not be altered.
      is_restrictive {Boolean}:
          Specifies whether the field group is restrictive. This parameter
          allows you to control the editing experience when using contingent
          values.RESTRICT-The field group is restrictive. Values entered on a
          field in
          the field group are restricted to those specified as contingent
          values. This is the default.DO_NOT_RESTRICT-The field group is not
          restrictive. Values can be
          committed to a field in a field group even if they are not specified
          as contingent values.

        """