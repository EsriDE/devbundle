# Generated documentation for module arcpy.ca


class AddDateAttributes(object):
    """
    Adds fields containing date or time properties from an input date field, for example, day full name, day of the month, month, and year.
    """

    @property
    def description(self) -> str:
        return """

        AddDateAttributes_ca(in_table, date_field, {date_attributes;date_attributes...})

        Adds fields containing date or time properties from an input date
        field, for example, day full name, day of the month, month, and year.

     INPUTS:
      in_table (Table View):
          The layer or table that contains the field with the date values that
          will be extracted.
      date_field (Field):
          The date field from which data and time properties will be extracted
          to populate the new field values.
      date_attributes {Value Table}:
          The date and time properties and fields that will be added to the
          input table. Output Time Format-The date or time property that
          will be
          added to. Output Field NameOutput Field Name-The name of the
          field that will be added to the
          input table. Theoptions are as follows:        Output Time
          FormatHour-The hour value between 0 and 23.Day Full Name-The full name
          of
          the day of the week, for example,
          Wednesday.Day Numeric Value-The day of the week value between 1 and
          7.Month-The month value between 1 and 12.Day of the Month-The day of
          the month value between 1 and 31.Year-The year value in yyyy format,
          for example, 1983.

        """