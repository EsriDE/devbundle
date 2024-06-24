# Generated documentation for module arcpy.management


class AddContingentValue(object):
    """
    Adds a contingent value to a field group on a feature class or table.
    """

    @property
    def description(self) -> str:
        return """

        AddContingentValue_management(target_table, field_group_name, values;values..., {subtype}, {retire_value})

        Adds a contingent value to a field group on a feature class or table.

     INPUTS:
      target_table (Table View):
          The input geodatabase feature class or table to which the contingent
          value will be added.
      field_group_name (String):
          The field group to which the contingent value will be added.
      values (Value Table):
          The field name, field value type, and associated field values
          that will be used for the new contingent value. Field name-The
          name of the field that participates in the field group.
          Field value type-The type of contingent value. The ANY and
          NULL types will ignore any value specified in the field value field.
          ANY-The value can be any field value.NULL-The value is
          null.CODED_VALUE-The value is from a coded value domain.RANGE-The
          value is a minimum/maximum subset of a range domain.Field value-The
          specific field value. If the field value type is
          CODED_VALUE, specify the code. If the field value type is RANGE,
          specify the minimum and maximum values in the format min;max (for
          example, 10;100).
      subtype {String}:
          The input table subtype to which the contingent value will be added.
      retire_value {Boolean}:
          Specifies whether the contingent value will be retired. The
          contingent value is considered retired when it is no longer created
          but can still be used in an existing field. When a contingent value is
          retired, it will still be shown in the list of valid values for a
          field, such as in thepane. An example is using asbestos as a building
          material. New construction cannot use asbestos as a building material,
          but existing structures may still have this attribute. For more
          information about retired values, see Create and manage contingent
          values. AttributeRETIRE-The contingent value will be
          retired.DO_NOT_RETIRE-The
          contingent value will not be retired. This is the
          default.

        """