# Generated documentation for module arcpy.geocoding


class CreateCompositeAddressLocator(object):
    """
    Creates a composite locator. A composite locator consists of two or more individual locators that allow addresses and places to be matched using multiple locators.
    """

    @property
    def description(self) -> str:
        return """

        CreateCompositeAddressLocator_geocoding(in_address_locators;in_address_locators..., in_field_map, {in_selection_criteria;in_selection_criteria...}, out_composite_address_locator, {in_result_ordering})

        Creates a composite locator. A composite locator consists of two or
        more individual locators that allow addresses and places to be matched
        using multiple locators.

     INPUTS:
      in_address_locators (Value Table):
          The locators that will be used to create the composite locator. The
          order of the participating locators determines how candidates are
          searched and a place or address is matched. When you geocode a single
          place or address, the place or address will be matched using all
          participating locators unless the locator is specified with a
          selection criterion. All the found candidates will be displayed based
          on the order of the listed participating locators. If you geocode a
          table of addresses or places, addresses or places will be matched
          automatically to the first best candidate found from the first
          participating locators. If the address or place fails to match, it
          will fall back to the subsequent locator in the list.A reference name
          for each participating locator is required. This is
          the name of the locator referred to by the composite locator. Do not
          use spaces or special symbols in the name. The maximum length of the
          name is 14 characters.
      in_field_map (Field Mappings):
          The mapping of input fields used by each participating locator to the
          input fields of the composite address locator.For each locator input
          field, format the field information as in this
          sample string: "Address 'Address or Intersection' true true false 4
          Text 0 0 ,First,'#',Street". The information in this string is
          composed of the following:         New field name (Address)-The new
          locator field name for the
          composite locator. One locator in the composite may have an
          Address field and the other
          locator may have a Street Address field. You can designate the new
          composite locator field as Address, which references both original
          locator fields. Alias for the new field name ('Address or
          Intersection')-The
          new locator field name alias for the composite locator. For a
          composite locator with the new field name Address, you can
          designate an alias of 'Address or Intersection' for the
          field.isEditable (true)-Specifies whether the new composite locator
          field is
          editable. The options are true or false.Allow NULL Values
          (true)-Specifies whether the new composite locator
          field allows null values. The options are true or false.Required
          (false)-Specifies whether the new composite locator field is
          a required field. The options are true or false.Length (4)-The length
          of the new composite locator field.Type (Text)-The data type of the
          new composite locator field. This
          value should always be Text for a locator.Scale (0)-The scale of the
          new composite locator field. Any value
          between 1 and 100 can be used. This value does not apply to locators,
          but a valid value must be used.Precision (0)-The precision of the new
          composite locator field. Any
          value between 1 and 100 can be used. This value does not apply to
          locators, but a valid value must be used.Merge rule (First)-The merge
          rule for the new composite locator field.
          Any merge rule value can be used. This value does not apply to
          locators, but a valid value must be used.Delimiter ('#')-The delimiter
          for the new composite locator field. Any
          supported delimiter can be used.Original locator field name
          (Street)-The locator field name in the
          original participating locator.
      in_selection_criteria {Value Table}:
          The selection criteria for each participating locator. Only one
          selection criterion is supported for each participating locator.Using
          selection criteria will disqualify participating locators that
          do not meet the criteria for a particular address or place so that the
          geocoding process will be more efficient. See Fundamentals of
          combining multiple locators into a composite locator to learn more
          about the use of selection criteria in the geocoding process.
      in_result_ordering {String}:
          Specifies the fallback order of the participating locators to which
          addresses can be matched to increase the probability of finding the
          best match when geocoding. Use locator order-Participating
          locators will be in the order
          they were added and adhere to the fallback order described in Combine
          multiple locators into a composite locator. This is the default.
          Syntax is a comma delimited string of locator names.For a composite
          locator containing two locators (Atlanta.loc and
          Memphis.loc, for example), the syntax should be "Atlanta, Memphis".
          Order by role and score-Individual roles of participating
          locators will be grouped and ordered from most to least precise.
          Results will be returned for more precise roles first followed by less
          precise roles, and for results that are returned for different
          locators with the same role, results will be returned based on score.
          It is recommended that you use this option if you have a multirole
          locator and several single role locators or if you have more than one
          multirole locator. This automatically orders the locators and roles
          into a recommended, optimal fallback order. Syntax is a comma
          delimited string of role groupings structured as
          [LocatorRole1](LocatorName1.LocatorRole1,
          LocatorName2.LocatorRole1).For a composite locator containing two
          multirole locators (Atlanta.loc
          and Memphis.loc, for example) each containing a PointAddress role and
          a StreetAddress role, the syntax should be
          "[PointAddress](Atlanta.PointAddress, Memphis.PointAddress),[StreetAdd
          ress](Memphis.StreetAddress,Atlanta.StreetAddress)".Roles must be
          ordered from most precise to least precise. Custom order-A
          customizable fallback order for participating
          locators will be used that allows you to insert locators between the
          roles of a multirole locator. Syntax is a comma delimited
          string of locator names and roles
          structured as LocatorName.LocatorRole.For a composite locator
          containing two multirole locators (Atlanta.loc
          and Memphis.loc, for example) each containing a PointAddress role and
          a StreetAddress role, the syntax should be "Atlanta.StreetAddress,Memp
          his.PointAddress,Memphis.StreetAddres,Atlanta.PointAddress".Locators
          and roles can be placed in any order, but placing less
          precise roles before more precise roles may result in unexpected
          behavior. To generate the correct Python syntax, first run the
          tool from
          thepane. Then, open themenu and select. GeoprocessingRunCopy
          Python Command

     OUTPUTS:
      out_composite_address_locator (Address Locator):
          The composite address locator that will be created. ArcGIS Pro only
          supports saving locators in a file folder.

        """