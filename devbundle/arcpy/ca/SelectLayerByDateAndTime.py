# Generated documentation for module arcpy.ca


class SelectLayerByDateAndTime(object):
    """
    Selects records based on date and time ranges or date properties, for example, single date, time range, time period, days of the week, month, or year.
    """

    @property
    def description(self) -> str:
        return """

        SelectLayerByDateAndTime_ca(in_layer_or_view, selection_type, time_type, {date_field}, {start_date_field}, {end_date_field}, {selection_options;selection_options...}, {date_selection_type}, {single_date}, {start_date}, {end_date}, {use_system_time}, {time_slice}, {start_time}, {end_time}, {days_of_week;days_of_week...}, {months;months...}, {years;years...})

        Selects records based on date and time ranges or date properties, for
        example, single date, time range, time period, days of the week,
        month, or year.

     INPUTS:
      in_layer_or_view (Table View / Feature Layer):
          The data containing a date field to which the selection will be
          applied.
      selection_type (String):
          Specifies how the selection will be applied and what will occur if a
          selection already exists.NEW_SELECTION-The resulting selection will
          replace the current
          selection. This is the default.ADD_TO_SELECTION-The resulting
          selection will be added to the current
          selection if one exists. If no selection exists, this is the same as
          the new selection option.REMOVE_FROM_SELECTION-The resulting
          selection will be removed from
          the current selection. If no selection exists, this option has no
          effect.SUBSET_SELECTION-The resulting selection will be combined with
          the
          current selection. Only records that are common to both remain
          selected.
      time_type (String):
          Specifies how date and time fields will be used to select
          records.SINGLE_TIME_FIELD-Records will be selected based on a single
          time
          field on the input feature.TIME_RANGE_FIELDS-Records will be selected
          based on start and end time
          fields on the input feature.
      date_field {Field}:
          The date field from the input layer on which the selection will be
          based. This parameter is only active if the time_type parameter is set
          to SINGLE_TIME_FIELD.
      start_date_field {Field}:
          The start date field from the time range on which the selection will
          be based. This parameter is only active if the time_type parameter is
          set to TIME_RANGE_FIELDS.
      end_date_field {Field}:
          The end date field from the time range on which the selection will be
          based. This parameter is only active if the time_type parameter is set
          to TIME_RANGE_FIELDS.
      selection_options {String}:
          Specifies how date and time selections will be made.DATE-The selection
          will be by date.TIME-The selection will be by time
          of day.DAY_OF_WEEK-The selection will be by day of the week.MONTH-The
          selection will be by month.YEAR-The selection will be by year.
      date_selection_type {String}:
          Specifies whether records will be selected based on a date range,
          single date, recency period, or comparative time period.This parameter
          is only active when the selection_options parameter is
          set to DATE.DATE_RANGE-Records will be selected based on a start and
          end date
          range.SINGLE_DATE-Records will be selected based on the a single
          specified
          date.RECENCY-Records will be selected based on a time period in
          relation to
          the current date (system date and time), for example, within the last
          14 days. COMPARATIVE-Records will be selected based on the
          time period
          immediately preceding a recent time period in relation to the current
          date (system date and time). For example, if the current date is
          January 29 and the time slice is 14 days, records occurring between
          January 1 and January 14 will be selected. This option can be used in
          combination with a subsequent(RECENCY in Python) selection to compare
          record counts between two adjacent time periods (for example, the two
          14-day time periods of January 1-14 and January 15-28). By
          Recency
      single_date {Date}:
          The single date and time to be selected.This parameter is only active
          when the date_selection_type parameter
          is set to SINGLE_DATE.
      start_date {Date}:
          The start date of the date range.This parameter is only active when
          the date_selection_type parameter
          is set to DATE_RANGE.
      end_date {Date}:
          The end date of the date range.This parameter is only active when the
          date_selection_type parameter
          is set to DATE_RANGE.
      use_system_time {Boolean}:
          Specifies whether records from the current day (local system time)
          will be included in the selection if they exist in the recent time
          period.SYSTEM_TIME-Records from the current day will be included in
          the
          selection.NO_SYSTEM_TIME-Records from the current day will not be
          included in
          the selection. This is the default.For example, the time slice
          specified is 14 days, the local system
          time is 5:00 p.m. on January 15 when the tool runs, the recency time
          period includes all records between 5:00 p.m. on the date 14 days ago
          and 5:00 p.m. on the day the tool runs, and SYSTEM_TIME is selected.
          In this example, the selection will be January 1, 2017 5:00:00 PM to
          January 15, 2017 5:00:00 PM. Using this same example with
          NO_SYSTEM_TIME selected, the recent period uses the beginning of the
          current day as the end time (based on local system time). In this
          case, the selection will be January 1, 2017 12:00:00 AM to January 15,
          12:00:00 AM for the 14-day time slice.This parameter is only active
          when the date_selection_type parameter
          is set to COMPARATIVE or RECENCY.
      time_slice {Time Unit}:
          The number of time units (minutes, hours, days, weeks, months, or
          years) defining the recent time period on which the selection will be
          based, for example, events within the last 14 days.This parameter is
          only active when the date_selection_type parameter
          is set to COMPARATIVE or RECENCY.
      start_time {Date}:
          The start time of the time range.This parameter is only active when
          the selection_options parameter is
          set to TIME.
      end_time {Date}:
          The end time of the time range.This parameter is only active when the
          selection_options parameter is
          set to TIME.
      days_of_week {String}:
          Specifies the day or days of the week that will be used to select
          records.MONDAY-Records occurring on Monday will be
          selected.TUESDAY-Records
          occurring on Tuesday will be selected.WEDNESDAY-Records occurring on
          Wednesday will be selected.THURSDAY-Records occurring on Thursday will
          be selected.FRIDAY-Records occurring on Friday will be
          selected.SATURDAY-Records occurring on Saturday will be
          selected.SUNDAY-Records occurring on Sunday will be selected.This
          parameter is only active when the selection_options parameter is
          set to DAY_OF_WEEK.
      months {String}:
          Specifies the month or months that will be used to select
          records.JANUARY-Records occurring in January will be
          selected.FEBRUARY-Records
          occurring in February will be selected.MARCH-Records occurring in
          March will be selected.APRIL-Records occurring in April will be
          selected.MAY-Records occurring in May will be selected.JUNE-Records
          occurring in June will be selected.JULY-Records occurring in July will
          be selected.AUGUST-Records occurring in August will be
          selected.SEPTEMBER-Records occurring in September will be
          selected.OCTOBER-Records occurring in October will be
          selected.NOVEMBER-Records occurring in November will be
          selected.DECEMBER-Records occurring in December will be selected.This
          parameter is only active when the selection_options parameter is
          set to MONTH.
      years {Long}:
          The year or years that will be used to select records.This parameter
          is only active when the selection_options parameter is
          set to YEAR.

        """