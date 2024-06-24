# Generated documentation for module arcpy.management


class CalculateEndTime(object):
    """
    Calculates the end time of features based on the time values stored in another field.
    """

    @property
    def description(self) -> str:
        return """

        CalculateEndTime_management(in_table, start_field, end_field, {fields;fields...})

        Calculates the end time of features based on the time values stored in
        another field.

     INPUTS:
      in_table (Table View):
          The feature class or table for which anis calculated based on
          thespecified. End Time FieldStart Time Field
      start_field (Field):
          The field containing values that will be used to calculate
          values for the. Theand themust be of the same type. For example, if
          theis of type LONG, theshould be of type LONG as well. End Time
          FieldStart Time FieldEnd Time FieldStart Time FieldEnd Time Field
      end_field (Field):
          The field that will be populated with values based on
          thespecified. Theand themust be of the same format. Start Time
          FieldStart Time FieldEnd Time Field
      fields {Field}:
          The name of the field or fields that can be used to uniquely identify
          spatial entities. These fields are used to first sort based on entity
          type if there is more than one entity. For instance, for a feature
          class representing population values per state over time, the state
          name could be the unique value field (the entity). If population
          figures are per county, you would need to set the county name and
          state name as the unique value fields, since some county names are the
          same for different states. If there is only one entity, this parameter
          can be ignored.

        """