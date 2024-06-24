# Generated documentation for module arcpy.geocoding


class GeocodeAddresses(object):
    """
    Geocodes a table of addresses. This process requires a table that stores the addresses you want to geocode and an address locator or a composite address locator. This tool matches the stored addresses against the locator and saves the result for each input record in a new point feature class. When using the ArcGIS World Geocoding Service, this operation may consume credits.
    """

    @property
    def description(self) -> str:
        return """

        GeocodeAddresses_geocoding(in_table, address_locator, in_address_fields, out_feature_class, {out_relationship_type}, {country;country...}, {location_type}, {category;category...}, {output_fields})

        Geocodes a table of addresses. This process requires a table that
        stores the addresses you want to geocode and an address locator or a
        composite address locator. This tool matches the stored addresses
        against the locator and saves the result for each input record in a
        new point feature class. When using the ArcGIS World Geocoding
        Service, this operation may consume credits.

     INPUTS:
      in_table (Table View):
          The table of addresses to geocode.
      address_locator (Address Locator):
          The address locator that will be used to geocode the table of
          addresses. Including the .loc extension after the locator name
          at the end of the
          locator path is optional.
      in_address_fields (Field Info):
          Each field mapping in this parameter is in the format
          input_address_field, table_field_name in whichis the name of the input
          address field specified by the address locator, andis the name of the
          corresponding field in the table of addresses you want to geocode.
          input_address_fieldtable_field_name        You can specify a single
          input field that stores the complete
          address, for example, 303 Peachtree St NE, Atlanta, GA 30308.
          Alternatively, you can specify multiple fields if the input addresses
          are divided into multiple fields such as,,, andfor a general United
          States address. You can also specify a single input field that stores
          the complete address, for example, 303 Peachtree St NE, Atlanta, GA
          30308, and a field that stores the country associated with the
          address, for example, USA. AddressCityStateZIP        Some
          locators support multiple input address fields, such as,,
          and. In this case, the address component can be separated into
          multiple fields, and the address fields will be concatenated at the
          time of geocoding. For example, 100, Main st, and Apt 140 across three
          fields, or 100 Main st and Apt 140 across two fields, both become 100
          Main st Apt 140 when geocoding. AddressAddress2Address3If you
          do not map an optional input address field used by the address
          locator to a field in the input table of addresses, specify that there
          is no mapping using <None> in place of the field name.
      out_relationship_type {Boolean}:
          STATIC-A static copy of the fields input address table will be created
          in the output feature class. This is the only permissible
          value.DYNAMIC-This option is not applicable in ArcGIS Pro. See the
          ArcGIS
          Desktop help for this tool.
      country {String}:
          The country or countries that will be searched for the geocoded
          addresses. This parameter is available for locators that
          support a
          country parameter and will limit geocoding to the selected countries.
          Specifying a country will improve the accuracy of geocoding in most
          cases. If a field representing countries in the in_table parameter is
          mapped to thefield in the input_address_field parameter value, the
          country value from the in_table parameter will override the country
          parameter. CountryThis is limited to the specified country or
          countries. When no country
          is specified, geocoding is performed using all supported countries of
          the locator.Specify the value as either two-character or three-
          character country
          codes in a comma-separated list. See the Supported Country Codes
          column for the input value to use.The country parameter is not
          supported for all locators.
      location_type {String}:
          Specifies the preferred output geometry for POINT_ADDRESS matches. The
          options for this parameter are ROUTING_LOCATION, which is the side of
          street location that can be used for routing and ADDRESS_LOCATION,
          which is the location that represents the rooftop, parcel centroid for
          the address, or front door. If the preferred location does not exist
          in the data, the default location of ROUTING_LOCATION will be
          returned. For geocode results with Addr_type = PointAddress, the x,y
          attribute values describe the coordinates of the address along the
          street, and the DisplayX and DisplayY values describe the rooftop or
          building centroid coordinates. See the ArcGIS REST API web help for
          details about the locationType parameter for geocodeAddresses.This
          parameter is not supported for all locators.ADDRESS_LOCATION-Geometry
          for geocode results that represent an
          address location such as rooftop location, parcel centroid, or front
          door will be returned.ROUTING_LOCATION-Geometry for geocode results
          that represent a
          location close to the side of the street that can be used for vehicle
          routing will be returned. This is the default.
      category {String}:
          Limits the types of places the locator searches, eliminating
          false positive matches and potentially speeding up the search process.
          When no category is used, geocoding is performed using all supported
          categories. Not all category values are supported for all locations
          and countries. In general, this parameter can be used for the
          following:        Limit matches to specific place types or address
          levelsAvoid fallback
          matches to unwanted address levelsDisambiguate coordinate searchesThis
          parameter is not supported for all locators.See the ArcGIS REST API
          web help for details about category filtering.
      output_fields {String}:
          Specifies the locator output fields that will be returned in the
          geocode results.This parameter can be used with input locators created
          with the Create
          Locator or Create Feature Locator tool stored on disk or published to
          Enterprise 10.9 or later. Composite locators that contain at least one
          locator created with the Create Address Locator tool do not support
          this parameter.ALL-Includes all available locator output fields in
          the geocode
          results. This is the default. LOCATION_ONLY-Stores thefield in
          the geocode results. The
          original field names from the in_table parameter value will be
          maintained with their original field names. Shape
          MINIMAL-Adds the following fields that describe the location
          and how well it matches information in the locator in the geocode
          results:,,,,, and. The original field names from the in_table
          parameter value will be maintained.
          ShapeStatusScoreMatch_typeMatch_addrAddr_type
          MINIMAL_AND_USER-Adds the following fields that describe the
          location and how well it matches information in the locator in the
          geocode results, as well as any user-defined custom output
          fields:,,,,, and. The original field names from the in_table parameter
          value will be maintained.
          ShapeStatusScoreMatch_typeMatch_addrAddr_type

     OUTPUTS:
      out_feature_class (Feature Class):
          The output geocoded feature class.Saving the output to shapefile
          format is not supported due to
          shapefile limitations.

        """