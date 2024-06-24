# Generated documentation for module arcpy.geocoding


class SplitAddressIntoComponents(object):
    """
    Splits street address information into address components and creates a table or feature class with the additional components added as unique fields.
    """

    @property
    def description(self) -> str:
        return """

        SplitAddressIntoComponents_geocoding(country_code, in_address_data, in_address_fields;in_address_fields..., out_address_data, {in_exceptions})

        Splits street address information into address components and creates
        a table or feature class with the additional components added as
        unique fields.

     INPUTS:
      country_code (String):
          Specifies the country addressing structure that will be used to split
          addresses into components.The default is the regional setting of the
          operating system.AUS-The address structure of Australia will be
          used.AUT-The address
          structure of Austria will be used.BEL-The address structure of Belgium
          will be used.CAN-The address structure of Canada will be used.CHE-The
          address structure of Switzerland will be used.CZE-The address
          structure of Czechia will be used.DEU-The address structure of Germany
          will be used.ESP-The address structure of Spain will be used.EST-The
          address structure of Estonia will be used.FRA-The address structure of
          France will be used.GBR-The address structure of Great Britain will be
          used.ISR-The address structure of Israel will be used.ITA-The address
          structure of Italy will be used.LTU-The address structure of Lithuania
          will be used.LVA-The address structure of Latvia will be used.NLD-The
          address structure of Netherlands will be used.PRI-The address
          structure of Puerto Rico will be used.SWE-The address structure of
          Sweden will be used.USA-The address structure of United States will
          be used.ZAF-The address structure of South Africa will be used.
      in_address_data (Table View):
          The table or feature class containing street address information that
          will be split into individual address components.Zone information,
          such as city, neighborhood, subregion, and postal
          code, is not supported.
      in_address_fields (String):
          The field or fields in the input table or feature class that, when
          concatenated, will form the street address to be split. Zone
          information, such as city, neighborhood, subregion, and postal code,
          is not supported.The order in which the fields are selected is the
          order the fields
          will be concatenated.
      in_exceptions {Table View}:
          The table that contains street parsing exceptions.The table can be in
          any supported table format.

     OUTPUTS:
      out_address_data (Dataset):
          The output feature class or table that will contain the split street
          address data.

        """