# Generated documentation for module arcpy.ca


class UpdateFeaturesWithIncidentRecords(object):
    """
    Updates an existing table or converts a nonspatial table to point features based on x,y-coordinates or street addresses and updates an existing dataset with the new or updated record information from the table.
    """

    @property
    def description(self) -> str:
        return """

        UpdateFeaturesWithIncidentRecords_ca(in_table, target_features, {location_type}, {x_field}, {y_field}, {coordinate_system}, {address_locator}, {address_type}, {address_fields;address_fields...}, {invalid_records_table}, {where_clause}, {update_target}, {match_fields;match_fields...}, {in_date_field}, {target_date_field}, {update_matching}, {update_geometry}, {field_matching_type}, {field_mapping}, {time_format})

        Updates an existing table or converts a nonspatial table to point
        features based on x,y-coordinates or street addresses and updates an
        existing dataset with the new or updated record information from the
        table.

     INPUTS:
      in_table (Table View):
          The nonspatial table or table containing the x- and y-coordinates or
          addresses that define the locations of the records.
      target_features (Feature Layer / Table View):
          The point feature class, point feature layer, or table that will be
          updated.
      location_type {String}:
          Specifies whether features will be created using x,y-coordinates or
          addresses.COORDINATES-Features will be created using the
          x,y-coordinates of the
          input record.ADDRESSES-Features will be created using the address of
          the input
          record using a locator.This parameter is only enabled when the
          target_features parameter
          value is a feature class or layer.
      x_field {Field}:
          The field in the input table that contains the x-coordinates (or
          longitude).This parameter is only enabled when the location_type
          parameter is set
          to COORDINATES and the target_features parameter value is a feature
          class or layer.
      y_field {Field}:
          The field in the input table that contains the y-coordinates (or
          latitude).This parameter is only enabled when the location_type
          parameter is set
          to COORDINATES and the target_features parameter value is a feature
          class or layer.
      coordinate_system {Coordinate System}:
          The coordinate system of the x- and y-coordinates.This parameter is
          only enabled when the location_type parameter is set
          to COORDINATES and the target_features parameter value is a feature
          class or layer.
      address_locator {Address Locator}:
          The address locator that will be used to geocode the table of
          addresses.When this parameter is set to use ArcGIS World Geocoding
          Service, this
          operation may consume credits.When using a local address locator,
          adding the .loc extension after
          the locator name at the end of the locator path is optional.This
          parameter is only enabled when the location_type parameter is set
          to ADDRESSES and the target_features parameter value is a feature
          class or layer.
      address_type {String}:
          Specifies how address fields used by the address locator will be
          mapped to fields in the input table of
          addresses.MULTI_FIELD_ADDRESS-Addresses will be divided into multiple
          fields.SINGLE_FIELD_ADDRESS-Addresses will be contained in one
          field.Select SINGLE_FIELD_ADDRESS if the complete address is stored in
          one
          field in the input table, for example, 303 Peachtree St NE, Atlanta,
          GA 30308. Select MULTI_FIELD_ADDRESS if the input addresses are
          divided into multiple fields such as Address, City, State, and ZIP for
          a general United States address.This parameter is only enabled when
          the location_type parameter is set
          to ADDRESSES and the target_features parameter value is a feature
          class or layer.
      address_fields {Value Table}:
          The input table fields that correspond to the locator address fields
          of the address locator. Some locators support multiple input
          address fields, such as,,
          and. In this case, the address component can be separated into
          multiple fields, and the address fields will be concatenated at the
          time of geocoding. For example, 100, Main st, and Apt 140 across three
          fields or 100 Main st and Apt 140 across two fields, both become 100
          Main st Apt 140 when geocoding. AddressAddress2Address3If you
          do not map an optional input address field used by the address
          locator to a field in the input table of addresses, specify that there
          is no mapping by leaving the field name blank.This parameter is only
          enabled when the location_type parameter is set
          to ADDRESSES.
      where_clause {SQL Expression}:
          The SQL expression that will be used to select a subset of the input
          datasets' records. If multiple input datasets are specified, they will
          all be evaluated using the expression. If no records match the
          expression for an input dataset, no records from that dataset will be
          appended to the target.For more information about SQL syntax, see SQL
          reference for query
          expressions used in ArcGIS.
      update_target {Boolean}:
          Specifies whether existing records will be updated in the
          target_features parameter value.UPDATE-Records from the in_table
          parameter value will be updated in
          the target_features parameter value if they exist there.APPEND-Records
          from the in_table parameter value will be appended to
          the target_features parameter value. This is the default.
      match_fields {Value Table}:
          The ID field or fields that will be used to determine matches between
          the in_table values and the target_features values.This parameter is
          only enabled when the update_target parameter is set
          to UPDATE.
      in_date_field {Field}:
          The field containing the last modified date of the in_table
          records.Date and string field types are supported.This parameter is
          only enabled when the update_target parameter is set
          to UPDATE.
      target_date_field {Field}:
          The field containing the last modified date of the target_features
          records.This field must be a date field type.This parameter is only
          enabled when the update_target parameter is set
          to UPDATE.
      update_matching {Boolean}:
          Specifies whether only existing records will be updated or existing
          records will be updated and new records will be
          added.UPDATE_MATCHING_ONLY-Only existing records will be
          updated.UPSERT-Existing records will be updated and new records will
          be added.
          This is the default.This parameter is only enabled when the
          update_target parameter is set
          to UPDATE.
      update_geometry {Boolean}:
          Specifies whether the geometry of existing features will be
          updated.UPDATE_GEOMETRY-The geometry of existing records will be
          updated when
          the geometry information from the in_table parameter value is
          different than the geometry of the target_features parameter value.
          This is the default.KEEP_GEOMETRY-The geometry of existing records
          will not be updated.This parameter is only enabled when the
          update_target parameter is set
          to UPDATE and the target_features parameter value is a feature class
          or layer.
      field_matching_type {String}:
          Specifies whether the fields of the input table must match the fields
          of the target features for data to be appended.AUTOMATIC-Fields from
          the input dataset match the fields of the target
          dataset. Fields that do not match will be ignored. This is the default
          FIELD_MAP-Fields from the input dataset do not need to match
          the fields of the target dataset. Fields from the input dataset that
          do not match the fields of the target dataset will not be mapped to
          the target dataset unless the mapping is explicitly set in
          theparameter. Field Map
      field_mapping {Field Mappings}:
          Controls how the attribute fields from the input table will be
          transferred or mapped to the target features.This parameter is only
          enabled if the field_matching_type parameter is
          set to FIELD_MAP.Because the input table values are appended to an
          existing target
          feature that has predefined fields, you cannot add, remove, or change
          the type of the fields in the field map. You can, however, set merge
          rules for each output field.The field map can also be used to combine
          values from two or more
          input fields into a single output field.In Python, use the
          FieldMappings class to define this parameter.
      time_format {String}:
          The format of the input field containing the time values. The
          type can be short, long, float, double, text, or date. You can either
          choose a standard time format from the drop-down list or provide a
          custom format. The format strings are case sensitive.If the
          data type of the time field is date, date only, or timestamp
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
          in secondsunix_hex-UNIX time in hexadecimalThis parameter is only
          enabled when the in_date_field parameter value
          is a text field and the target_date_field parameter value is a date
          field, or the field_mapping parameter input value is a text field and
          the output value is a date fieldThis parameter is only enabled when
          the update_target parameter is set
          to UPDATE.

     OUTPUTS:
      invalid_records_table {Table}:
          The output table containing a list of invalid records and associated
          invalidation codes.

        """