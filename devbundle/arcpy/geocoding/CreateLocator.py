# Generated documentation for module arcpy.geocoding


class CreateLocator(object):
    """
    Creates a locator that can find the location of an address or a place, convert a table of addresses or places to a collection of point features, or identify the address of a point location.
    """

    @property
    def description(self) -> str:
        return """

        CreateLocator_geocoding(country_code, primary_reference_data;primary_reference_data..., field_mapping;field_mapping..., out_locator, language_code, {alternatename_tables;alternatename_tables...}, {alternate_field_mapping;alternate_field_mapping...}, {custom_output_fields;custom_output_fields...}, {precision_type})

        Creates a locator that can find the location of an address or a place,
        convert a table of addresses or places to a collection of point
        features, or identify the address of a point location.

     INPUTS:
      country_code (String):
          Specifies where country-specific geocoding logic will be applied to
          the reference data for the locator.It can be specified using
          AS_DEFINED_IN_DATA and a value can be mapped
          from primary_reference_data in field_mapping, or it can be applied to
          the entire dataset by specifying the three-character country code
          name-for example, USA for the United States of America, CAN for
          Canada, or PRI for Puerto Rico.It provides a country template
          containing the expected field names
          that are available for use by the field_mapping parameter for the
          specified country of the locator to be created.AS_DEFINED_IN_DATA-The
          three-character country code value defined in
          the reference data for each feature will be used.ASM-American
          SamoaAUS-AustraliaAUT-AustriaBEL-BelgiumCAN-CanadaCHE-SwitzerlandCZE-
          CzechiaDEU-GermanyESP-SpainEST-EstoniaFRA-FranceGBR-Great
          BritainGUM-GuamISR-IsraelITA-ItalyJPN-JapanKOR-South KoreaLTU-
          LithuaniaLVA-LatviaMNP-Northern Mariana
          IslandsNLD-NetherlandsPRI-Puerto RicoSWE-SwedenVIR-U.S. Virgin
          IslandsUSA-United StatesUMI-Minor Outlying Islands of the United
          StatesZAF-South Africa
      primary_reference_data (Value Table):
          The reference data feature classes and their roles that will be used
          to create the locator. Only one primary table can be used per
          role.Feature classes represented as services are supported data types
          for
          use as primary reference data.When a definition query is defined for
          the primary reference data or
          there are selected features, only the queried and selected features
          will be included when the locator is created.When creating a locator
          with reference data that contains millions of
          features, you must have at least three to four times the size of the
          data in free disk space on the drive containing your temp directory,
          as files used to build the locator are written to this location before
          the locator is copied to the output location. If you do not have
          enough disk space, the tool will fail when it runs out of space. Also,
          when creating large locators, your machine must have enough RAM to
          handle large memory-intensive processes.
      field_mapping (String):
          The mapping of primary reference dataset fields to the fields
          supported by the locator role. Each field mapping in this parameter is
          in the following format in which <role name> is the locator role
          name,is the name of the field supported by the locator role, <primary
          data> is the name of the data used in the primary_reference_data
          parameter, andis the name of the field in the primary reference
          dataset:        <locator role field name><primary data field name>#
          <role name>.<locator role field name> <primary data>.<primary data
          field name> # This shows an example: primary_reference_data_field_map
          = ["StreetAddress.HOUSE_NUMBER_FROM_LEFT 'streets'.L_F_ADD",\
          "StreetAddress.HOUSE_NUMBER_TO_LEFT 'streets'.L_T_ADD",\
          "StreetAddress.HOUSE_NUMBER_FROM_RIGHT 'streets'.R_F_ADD",\
          "StreetAddress.HOUSE_NUMBER_TO_RIGHT 'streets'.R_T_ADD",\
          "StreetAddress.STREET_PREFIX_DIR 'streets'.PREFIX",\
          "StreetAddress.STREET_PREFIX_TYPE 'streets'.PRE_TYPE",\
          "StreetAddress.STREET_NAME 'streets'.NAME",\
          "StreetAddress.STREET_SUFFIX_TYPE 'streets'.TYPE",\
          "StreetAddress.STREET_SUFFIX_DIR 'streets'.SUFFIX",\
          "StreetAddress.CITY_LEFT 'streets'.CITYL",\ "StreetAddress.CITY_RIGHT
          'streets'.CITYR",\ "StreetAddress.REGION_LEFT 'streets'.STATE_ABBR",\
          "StreetAddress.REGION_RIGHT 'streets'.STATE_ABBR",\
          "StreetAddress.POSTAL_LEFT 'streets'.ZIPL",\
          "StreetAddress.POSTAL_RIGHT 'streets'.ZIPR"]Map the relevant fields
          for each table from the primary_reference_data
          parameter. If you do not map an optional reference data field used by
          the locator role to a field in a reference dataset, it is not
          necessary to specify that there is no mapping using <None> in place of
          a field name. To determine thevalue for a reference data field
          used by a
          locator role, open the Create Locator tool in ArcGIS Pro and choose
          the locator role. The name that appears in thecolumn of theparameter
          is the field's role field name. <locator role field name>Field
          NameField MappingIf you are using an alternate name table, map Join ID
          in the
          primary_reference_data parameter value. To add custom output
          fields, the names of the fields must be
          defined in the custom_output_fields parameter as well as the
          field_mapping parameter. The field_mapping parameter will use the
          format '<locator role field name> <primary data field name>' in
          whichis defined as 'RoleName.CustomFieldName', andis the name of the
          field in the primary reference dataset as shown in the mapped fields
          in the example above. If a custom field is added to a Street Address
          role, you will need to map 'StreetAddress.CustomFieldName_Left' and
          'StreetAddress.CustomFieldName_Right' for each side of the street.
          <locator role field name><primary data field name>
      language_code (String):
          Specifies where language-specific geocoding logic will be applied to
          the reference data for the locator.If a language code field exists in
          the primary reference data,
          providing a language code can improve the results of the geocoding.It
          can be specified by setting AS_DEFINED_IN_DATA as the language_code
          value and mapping a value from primary_reference_data in
          field_mapping, or it can be applied to the entire dataset by
          specifying a language using the three-character language code
          representing the language of the address, such as ENG for
          English.AS_DEFINED_IN_DATA-The three-character language code value
          defined in
          the reference data for each feature will be
          used.BAQ-BasqueCAT-CatalanCZE-CzechDUT-DutchENG-EnglishEST-EstonianFR
          E-FrenchGER-GermanGLG-GalicianHEB-HebrewITA-ItalianJPN-JapaneseKOR-
          KoreanLIT-LithuanianLAV-LatvianSPA-SpanishSWE-Swedish
      alternatename_tables {Value Table}:
          The tables that contain alternate names for the features in the
          primary role tables.Tables represented as services are supported data
          types for use as
          alternate name tables.When a definition query is defined for the
          alternate name table or
          there are selected records, only the queried and selected records will
          be included when the locator is created.
      alternate_field_mapping {String}:
          Maps alternate name table fields to the alternate data fields
          supported by the locator role. Each field mapping must use the
          following format in which <alternate name table role> is the name of
          the alternate name table role,is the name of the alternate data field
          supported by the alternate name table locator role, <alternate data
          table> is the name of the alternate name table, andis the name of the
          field in the alternate name table. Map the relevant fields for each
          table in alternatename_tables. <locator role alternate field
          name><alternate data table field name># <alternate name table
          role>.<locator role alternate field name>
          <alternate data table>.<alternate data table field name> # This shows
          an example: alternate_data__table_field_map =
          ["AlternateStreetName.STREET_NAME_JOIN_ID 'altname'.JOINID",\
          "AlternateStreetName.STREET_PREFIX_DIR 'altname'.PRE_DIR",\
          "AlternateStreetName.STREET_PREFIX_TYPE 'altname'.PRE_TYPE",\
          "AlternateStreetName.STREET_NAME 'altname'.ST_NAME",\
          "AlternateStreetName.STREET_SUFFIX_TYPE 'altname'.ST_TYPE",\
          "AlternateStreetName.STREET_SUFFIX_DIR 'altname'.SUF_DIR"]        If
          the data is normalized and the primary table does not
          contain city name values but the alternate name table does, thefield
          can be mapped to a field in the alternate name table that contains a
          value that indicates whether the record is the primary field (for
          example, true/false or Yes/No). If this field is not mapped, the first
          record in the alternate name table will be used as the primary value.
          Primary Name Indicator
      custom_output_fields {String}:
          Adds user-defined output fields to the locator. The values specified
          for this parameter will define the names of the custom output fields
          that will be returned in the geocode result; however, each new field
          must be mapped to a field in the reference data. This new output field
          will apply for all roles that were used in the locator. If the locator
          role has a left and right side, _left and _right will be appended to
          the end of the field name. The maximum number of fields supported in
          the locator is 50.You must first include the custom output field names
          in the
          field_mapping parameter; then list the names in the
          custom_output_fields parameter.
      precision_type {String}:
          Specifies the precision of the locator.Locators created with
          GLOBAL_EXTRA_HIGH or LOCAL_EXTRA_HIGH precision
          can be used in ArcGIS Pro 2.6 or later and Enterprise 10.8.1 or
          later.GLOBAL_EXTRA_HIGH-The precision is approximately 1 centimeter,
          which
          is consistent globally.GLOBAL_HIGH-The precision is approximately 0.5
          meter, which is
          consistent globally. This is the default.LOCAL_EXTRA_HIGH-Increased
          precision is used for local areas.

     OUTPUTS:
      out_locator (Address Locator):
          The output address locator file.

        """