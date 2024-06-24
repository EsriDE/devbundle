# Generated documentation for module arcpy.management


class ConvertTimeField(object):
    """
    Transfers temporal values stored in a field to another field. The tool can be used to convert between field types (text, numeric, or datetime fields) or to convert the values to a different format such as dd/MM/yy HH:mm:ss to yyyy-MM-dd.
    """

    @property
    def description(self) -> str:
        return """

        ConvertTimeField_management(in_table, input_time_field, {input_time_format}, output_time_field, {output_time_type}, {output_time_format}, {timezone_or_field})

        Transfers temporal values stored in a field to another field. The tool
        can be used to convert between field types (text, numeric, or datetime
        fields) or to convert the values to a different format such as
        dd/MM/yy HH:mm:ss to yyyy-MM-dd.

     INPUTS:
      in_table (Table View):
          The layer or table that contains the field containing the time values
          that will be converted.
      input_time_field (Field):
          The field containing the time values. The field can be of type short,
          long, float, double, text, date, timestamp offset, or date only.
      input_time_format {String}:
          The format of the time values in the input_time_field parameter value.
          The parameter is not supported when the input time field is of type
          date.The format strings are case sensitive.If the data type of the
          time
          field is date, date only, or timestamp
          offset, no time format is required.If the data type of the time field
          is numeric (short, long, float,
          double, or big integer), a list of standard numeric time formats is
          provided in the drop-down list.If the data type of the time field is
          string, a list of standard
          string time formats is provided in the drop-down list. For string
          fields, you can also specify a custom time format. For example, the
          time values may have been stored in a string field in one of the
          standard formats such as yyyy/MM/dd HH:mm:ss or in a custom format
          such as dd/MM/yyyy HH:mm:ss. For the custom format, you can also
          specify the a.m. or p.m. designator.For ISO-8601 compliant strings,
          use yyyy-MM-ddTHH:mm:ss.s as the input
          format. This input selection can handle inputs that use either a UTC
          designator (Z) or UTC offsets (±hh:mm). Commonly used formats
          are listed below:          yyyy-Year
          represented by four digitsMM-Month as digits with leading
          zero for single-digit monthsMMM-Month as a three-letter
          abbreviationdd-Day of month as digits with leading zero for single-
          digit daysddd-Day of week as a three-letter abbreviationhh-Hours with
          leading zero for single-digit hours and a 12-hour clockHH-Hours with
          leading zero for single-digit hours and a 24-hour clockmm-Minutes with
          leading zero for single-digit minutesss-Seconds with leading zero for
          single-digit secondst-One character time marker string, such as A or
          Ptt-Multicharacter time marker string, such as AM or PMunix_us-UNIX
          time in microsecondsunix_ms-UNIX time in millisecondsunix_s-UNIX time
          in secondsunix_hex-UNIX time in hexadecimal
      output_time_field (String):
          The name of the field to be added in which the converted time values
          will be stored.
      output_time_type {String}:
          Specifies the field type of the output time field.DATE-The field type
          will be date. Date fields support date and time
          values.DATEONLY-The field type will be date only. Date only fields
          support
          date values with no time values.TIMEONLY-The field type will be time
          only. Time only fields support
          time values with no date values.TIMESTAMPOFFSET-The field type will be
          timestamp offset. Timestamp
          offset fields support a date, time, and offset from a UTC
          value.TEXT-The field type will be text. Text fields support a string
          of
          characters.LONG-The field type will be long. Long fields support whole
          numbers
          between -2,147,483,648 and 2,147,483,647.SHORT-The field type will be
          short. Short fields support whole numbers
          between -32,768 and 32,767.DOUBLE-The field type will be double.
          Double fields support fractional
          numbers between -2.2E308 and 1.8E308.FLOAT-The field type will be
          float. Float fields support fractional
          numbers between -3.4E38 and 1.2E38. BIGINTEGER-The field type
          will be big integer. Big integer
          fields support whole numbers between -(2) and 2. 5353
      output_time_format {String}:
          The format of the output time values. Supported output time formats
          depend on the output_time_type parameter value. A custom format can
          also be used to convert the value to a different format or to extract
          a portion of the value (such as the year). For a list of custom
          formats, see the input_time_format parameter explanation. This
          parameter is not used when the output_time_type parameter value is
          DATE.If the data type of the output time field isn't long enough to
          store
          the converted time value, the output value will be truncated.
      timezone_or_field {String / Field}:
          The time zone or field containing a numeric offset from the input
          table that will be used as the output time zone.If the Time Zone
          environment is specified, the tool will use the that
          environment value by default.UTC-The time zone will be
          UTC.Dateline_Standard_Time-The time zone
          will be Dateline Standard Time
          (UTC-12:00).UTC-11-The time zone will be UTC-11
          (UTC-11:00).Aleutian_Standard_Time-The time zone will be Aleutian
          Standard Time
          (UTC-10:00).Hawaiian_Standard_Time-The time zone will be Hawaiian
          Standard Time
          (UTC-10:00).Marquesas_Standard_Time-The time zone will be Marquesas
          Standard Time
          (UTC-09:30).Alaskan_Standard_Time-The time zone will be Alaskan
          Standard Time
          (UTC-09:00).UTC-09-The time zone will be UTC-09
          (UTC-09:00).Pacific_Standard_Time_(Mexico)-The time zone will be
          Pacific Standard
          Time (Mexico) (UTC-08:00).UTC-08-The time zone will be UTC-08
          (UTC-08:00).Pacific_Standard_Time-The time zone will be Pacific
          Standard Time
          (UTC-08:00).US_Mountain_Standard_Time-The time zone will be US
          Mountain Standard
          Time (UTC-07:00).Mountain_Standard_Time_(Mexico)-The time zone will be
          Mountain
          Standard Time (Mexico) (UTC-07:00).Mountain_Standard_Time-The time
          zone will be Mountain Standard Time
          (UTC-07:00).Yukon_Standard_Time-The time zone will be Yukon Standard
          Time
          (UTC-07:00).Central_America_Standard_Time-The time zone will be
          Central America
          Standard Time (UTC-06:00).Central_Standard_Time-The time zone will be
          Central Standard Time
          (UTC-06:00).Easter_Island_Standard_Time-The time zone will be Easter
          Island
          Standard Time (UTC-06:00).Central_Standard_Time_(Mexico)-The time zone
          will be Central Standard
          Time (Mexico) (UTC-06:00).Canada_Central_Standard_Time-The time zone
          will be Canada Central
          Standard Time (UTC-06:00).SA_Pacific_Standard_Time-The time zone will
          be SA Pacific Standard
          Time (UTC-05:00).Eastern_Standard_Time_(Mexico)-The time zone will be
          Eastern Standard
          Time (Mexico) (UTC-05:00).Eastern_Standard_Time-The time zone will be
          Eastern Standard Time
          (UTC-05:00).Haiti_Standard_Time-The time zone will be Haiti Standard
          Time
          (UTC-05:00).Cuba_Standard_Time-The time zone will be Cuba Standard
          Time
          (UTC-05:00).US_Eastern_Standard_Time-The time zone will be US Eastern
          Standard
          Time (UTC-05:00).Turks_And_Caicos_Standard_Time-The time zone will be
          Turks And Caicos
          Standard Time (UTC-04:00).Paraguay_Standard_Time-The time zone will be
          Paraguay Standard Time
          (UTC-04:00).Atlantic_Standard_Time-The time zone will be Atlantic
          Standard Time
          (UTC-04:00).Venezuela_Standard_Time-The time zone will be Venezuela
          Standard Time
          (UTC-04:00).Central_Brazilian_Standard_Time-The time zone will be
          Central
          Brazilian Standard Time (UTC-04:00).SA_Western_Standard_Time-The time
          zone will be SA Western Standard
          Time (UTC-04:00).Pacific_SA_Standard_Time-The time zone will be
          Pacific SA Standard
          Time (UTC-04:00).Newfoundland_Standard_Time-The time zone will be
          Newfoundland Standard
          Time (UTC-03:30).Tocantins_Standard_Time-The time zone will be
          Tocantins Standard Time
          (UTC-03:00).E._South_America_Standard_Time-The time zone will be E.
          South America
          Standard Time (UTC-03:00).SA_Eastern_Standard_Time-The time zone will
          be SA Eastern Standard
          Time (UTC-03:00).Argentina_Standard_Time-The time zone will be
          Argentina Standard Time
          (UTC-03:00).Greenland_Standard_Time-The time zone will be Greenland
          Standard Time
          (UTC-03:00).Montevideo_Standard_Time-The time zone will be Montevideo
          Standard
          Time (UTC-03:00).Magallanes_Standard_Time-The time zone will be
          Magallanes Standard
          Time (UTC-03:00).Saint_Pierre_Standard_Time-The time zone will be
          Saint Pierre Standard
          Time (UTC-03:00).Bahia_Standard_Time-The time zone will be Bahia
          Standard Time
          (UTC-03:00).UTC-02-The time zone will be UTC-02 (UTC-02:00).Mid-
          Atlantic_Standard_Time-The time zone will be Mid-Atlantic Standard
          Time (UTC-02:00).Azores_Standard_Time-The time zone will be Azores
          Standard Time
          (UTC-01:00).Cape_Verde_Standard_Time-The time zone will be Cape Verde
          Standard
          Time (UTC-01:00).GMT_Standard_Time-The time zone will be GMT Standard
          Time (UTC+00:00).Greenwich_Standard_Time-The time zone will be
          Greenwich Standard Time
          (UTC+00:00).Sao_Tome_Standard_Time-The time zone will be Sao Tome
          Standard Time
          (UTC+00:00).Morocco_Standard_Time-The time zone will be Morocco
          Standard Time
          (UTC+00:00).W._Europe_Standard_Time-The time zone will be W. Europe
          Standard Time
          (UTC+01:00).Central_Europe_Standard_Time-The time zone will be Central
          Europe
          Standard Time (UTC+01:00).Romance_Standard_Time-The time zone will be
          Romance Standard Time
          (UTC+01:00).Central_European_Standard_Time-The time zone will be
          Central European
          Standard Time (UTC+01:00).W._Central_Africa_Standard_Time-The time
          zone will be W. Central
          Africa Standard Time (UTC+01:00).Jordan_Standard_Time-The time zone
          will be Jordan Standard Time
          (UTC+02:00).GTB_Standard_Time-The time zone will be GTB Standard Time
          (UTC+02:00).Middle_East_Standard_Time-The time zone will be Middle
          East Standard
          Time (UTC+02:00).Egypt_Standard_Time-The time zone will be Egypt
          Standard Time
          (UTC+02:00).E._Europe_Standard_Time-The time zone will be E. Europe
          Standard Time
          (UTC+02:00).Syria_Standard_Time-The time zone will be Syria Standard
          Time
          (UTC+02:00).West_Bank_Standard_Time-The time zone will be West Bank
          Standard Time
          (UTC+02:00).South_Africa_Standard_Time-The time zone will be South
          Africa Standard
          Time (UTC+02:00).FLE_Standard_Time-The time zone will be FLE Standard
          Time (UTC+02:00).Israel_Standard_Time-The time zone will be Israel
          Standard
          (UTC+02:00).South_Sudan_Standard_Time-The time zone will be South
          Sudan Standard
          Time (UTC+02:00).Kaliningrad_Standard_Time-The time zone will be
          Kaliningrad Standard
          Time (UTC+02:00).Sudan_Standard_Time-The time zone will be Sudan
          Standard Time
          (UTC+02:00).Libya_Standard_Time-The time zone will be Libya Standard
          Time
          (UTC+02:00).Namibia_Standard_Time-The time zone will be Namibia
          Standard Time
          (UTC+02:00).Arabic_Standard_Time-The time zone will be Arabic Standard
          Time
          (UTC+03:00).Turkey_Standard_Time-The time zone will be Turkey Standard
          Time
          (UTC+03:00).Arab_Standard_Time-The time zone will be Arab Standard
          Time
          (UTC+03:00).Belarus_Standard_Time-The time zone will be Belarus
          Standard Time
          (UTC+03:00).Russian_Standard_Time-The time zone will be Russian
          Standard Time
          (UTC+03:00).E._Africa_Standard_Time-The time zone will be E. Africa
          Standard Time
          (UTC+03:00).Volgograd_Standard_Time-The time zone will be Volgograd
          Standard Time
          (UTC+03:00).Iran_Standard_Time-The time zone will be Iran Standard
          Time
          (UTC+03:30).Arabian_Standard_Time-The time zone will be Arabian
          Standard Time
          (UTC+04:00).Astrakhan_Standard_Time-The time zone will be Astrakhan
          Standard Time
          (UTC+04:00).Azerbaijan_Standard_Time-The time zone will be Azerbaijan
          Standard
          Time (UTC+04:00).Russia_Time_Zone_3-The time zone will be Russia Time
          Zone 3
          (UTC+04:00).Mauritius_Standard_Time-The time zone will be Mauritius
          Standard Time
          (UTC+04:00).Saratov_Standard_Time-The time zone will be Saratov
          Standard Time
          (UTC+04:00).Georgian_Standard_Time-The time zone will be Georgian
          Standard Time
          (UTC+04:00).Caucasus_Standard_Time-The time zone will be Caucasus
          Standard Time
          (UTC+04:00).Afghanistan_Standard_Time-The time zone will be
          Afghanistan Standard
          Time (UTC+04:30).West_Asia_Standard_Time-The time zone will be West
          Asia Standard Time
          (UTC+05:00).Ekaterinburg_Standard_Time-The time zone will be
          Ekaterinburg Standard
          Time (UTC+05:00).Pakistan_Standard_Time-The time zone will be Pakistan
          Standard Time
          (UTC+05:00).Qyzylorda_Standard_Time-The time zone will be Qyzylorda
          Standard Time
          (UTC+05:00).India_Standard_Time-The time zone will be India Standard
          Time
          (UTC+05:30).Sri_Lanka_Standard_Time-The time zone will be Sri Lanka
          Standard Time
          (UTC+05:30).Nepal_Standard_Time-The time zone will be Nepal Standard
          Time
          (UTC+05:45).Central_Asia_Standard_Time-The time zone will be Central
          Asia Standard
          Time (UTC+06:00).Bangladesh_Standard_Time-The time zone will be
          Bangladesh Standard
          Time (UTC+06:00).Omsk_Standard_Time-The time zone will be Omsk
          Standard Time
          (UTC+06:00).Myanmar_Standard_Time-The time zone will be Myanmar
          Standard Time
          (UTC+06:30).SE_Asia_Standard_Time-The time zone will be SE Asia
          Standard Time
          (UTC+07:00).Altai_Standard_Time-The time zone will be Altai Standard
          Time
          (UTC+07:00).W._Mongolia_Standard_Time-The time zone will be W.
          Mongolia Standard
          Time (UTC+07:00).North_Asia_Standard_Time-The time zone will be North
          Asia Standard
          Time (UTC+07:00).N._Central_Asia_Standard_Time-The time zone will be
          N. Central Asia
          Standard Time (UTC+07:00).Tomsk_Standard_Time-The time zone will be
          Tomsk Standard Time
          (UTC+07:00).China_Standard_Time-The time zone will be China Standard
          Time
          (UTC+08:00).North_Asia_East_Standard_Time-The time zone will be North
          Asia East
          Standard Time (UTC+08:00).Singapore_Standard_Time-The time zone will
          be Singapore Standard Time
          (UTC+08:00).W._Australia_Standard_Time-The time zone will be W.
          Australia Standard
          Time (UTC+08:00).Taipei_Standard_Time-The time zone will be Taipei
          Standard Time
          (UTC+08:00).Ulaanbaatar_Standard_Time-The time zone will be
          Ulaanbaatar Standard
          Time (UTC+08:00).Aus_Central_W._Standard_Time-The time zone will be
          Aus Central W.
          Standard Time (UTC+08:45).Transbaikal_Standard_Time-The time zone will
          be Transbaikal Standard
          Time (UTC+09:00).Tokyo_Standard_Time-The time zone will be Tokyo
          Standard Time
          (UTC+09:00).North_Korea_Standard_Time-The time zone will be North
          Korea Standard
          Time (UTC+09:00).Korea_Standard_Time-The time zone will be Korea
          Standard Time
          (UTC+09:00).Yakutsk_Standard_Time-The time zone will be Yakutsk
          Standard Time
          (UTC+09:00).Cen._Australia_Standard_Time-The time zone will be Cen.
          Australia
          Standard Time (UTC+09:30).AUS_Central_Standard_Time-The time zone will
          be AUS Central Standard
          Time (UTC+09:30).E._Australia_Standard_Time-The time zone will be E.
          Australia Standard
          Time (UTC+10:00).AUS_Eastern_Standard_Time-The time zone will be AUS
          Eastern Standard
          Time (UTC+10:00).West_Pacific_Standard_Time-The time zone will be West
          Pacific Standard
          Time (UTC+10:00).Tasmania_Standard_Time-The time zone will be Tasmania
          Standard Time
          (UTC+10:00).Vladivostok_Standard_Time-The time zone will be
          Vladivostok Standard
          Time (UTC+10:00).Lord_Howe_Standard_Time-The time zone will be Lord
          Howe Standard Time
          (UTC+10:30).Bougainville_Standard_Time-The time zone will be
          Bougainville Standard
          Time (UTC+11:00).Russia_Time_Zone_10-The time zone will be Russia Time
          Zone 10
          (UTC+11:00).Magadan_Standard_Time-The time zone will be Magadan
          Standard Time
          (UTC+11:00).Norfolk_Standard_Time-The time zone will be Norfolk
          Standard Time
          (UTC+11:00).Sakhalin_Standard_Time-The time zone will be Sakhalin
          Standard Time
          (UTC+11:00).Central_Pacific_Standard_Time-The time zone will be
          Central Pacific
          Standard Time (UTC+11:00).Russia_Time_Zone_11-The time zone will be
          Russia Time Zone 11
          (UTC+11:00).New_Zealand_Standard_Time-The time zone will be New
          Zealand Standard
          Time (UTC+12:00).UTC+12-The time zone will be UTC+12
          (UTC+12:00).Fiji_Standard_Time-The time zone will be Fiji Standard
          Time
          (UTC+12:00).Kamchatka_Standard_Time-The time zone will be Kamchatka
          Standard Time
          (UTC+12:00).Chatham_Islands_Standard_Time-The time zone will be
          Chatham Islands
          Standard Time (UTC+12:45).UTC+13-The time zone will be UTC+13
          (UTC+13:00).Tonga_Standard_Time-The time zone will be Tonga Standard
          Time
          (UTC+13:00).Samoa_Standard_Time-The time zone will be Samoa Standard
          Time
          (UTC+13:00).Line_Islands_Standard_Time-The time zone will be Line
          Islands Standard
          Time (UTC+14:00).

        """