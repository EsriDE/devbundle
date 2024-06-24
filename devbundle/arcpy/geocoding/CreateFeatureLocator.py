# Generated documentation for module arcpy.geocoding


class CreateFeatureLocator(object):
    """
    Creates a locator using reference data that contains a unique name or value for every feature stored in a single field. A locator created with this tool has broad applications. It can be used to search for names or unique attributes of features, such as water meters, short place names, cell towers, or alphanumeric strings used to identify locations (for example, N1N115).
    """

    @property
    def description(self) -> str:
        return """

        CreateFeatureLocator_geocoding(in_features, search_fields, output_locator, {locator_fields}, {custom_output_fields;custom_output_fields...})

        Creates a locator using reference data that contains a unique name or
        value for every feature stored in a single field. A locator created
        with this tool has broad applications. It can be used to search for
        names or unique attributes of features, such as water meters, short
        place names, cell towers, or alphanumeric strings used to identify
        locations (for example, N1N115).

     INPUTS:
      in_features (Feature Layer):
          The reference data feature class or feature layer that will be used to
          create the locator.Feature classes represented as services are
          supported data types for
          use as reference data.When a definition query is defined for the
          reference data or there are
          selected features, only the queried and selected features are included
          when the locator is created.When creating a locator with reference
          data that contains millions of
          features, you must have at least three to four times the size of the
          data in free disk space on the drive containing your temp directory,
          as files used to build the locator are written to this location before
          the locator is copied to the output location. If you do not have
          enough disk space, the tool will fail when it runs out of space. Also,
          when creating large locators, your machine must have enough RAM to
          handle large memory-intensive processes.
      search_fields (Field Info):
          Maps the reference data field to the field used for search in
          the in_features parameter value. The search_fields mapping is done in
          the following format in whichis the name of the field supported by the
          locator role, andis the name of the field used for search in the
          in_features parameter. <locator field name><data field name>#
          <locator field name> <data field name> # This shows an example:
          reference_data_field_map = ''' "'Name' AssetName" '''The selected
          field will be indexed and used for search. Map the
          relevant field for the reference data in the in_features parameter.
      locator_fields {Field Info}:
          Maps additional fields for extent and rank if they exist in
          the data. Thefield is used to sort results for ambiguous queries or
          candidates with the same name and score. The extent fields help set
          the map extent for displaying geocoded results. The locator_fields
          mapping is done in the following format:        Rank# <additional
          locator field name> <additional data field name> # This
          shows an example: additional_fields_map = ''' "'Rank' RANK;'Min X'
          Xmin; 'Max X' Xmax;'Min Y' Ymin; 'Max Y' Ymax" '''        Thefield is
          the name of the additional fields supported by the
          locator, and thefield is the name of the field in the in_features
          parameter. Map the relevant fields for the reference data in the
          in_features parameter. <additional locator field
          name><additional data field name>
      custom_output_fields {String}:
          Adds user-defined output fields to the locator. The values specified
          for this parameter will define the names of the custom output fields
          that will be returned in the geocode result; however, each new field
          must be mapped to a field in the reference data. The maximum number of
          fields supported in the locator is 50.You must first include the
          custom output field names in the
          field_mapping parameter; then list the names in the
          custom_output_fields parameter.

     OUTPUTS:
      output_locator (Address Locator):
          The output locator file to be created in a file folder. Once the
          locator is created, additional properties and options can be modified
          in the locator's settings.

        """