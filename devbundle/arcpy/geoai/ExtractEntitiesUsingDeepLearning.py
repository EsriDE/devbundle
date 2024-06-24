# Generated documentation for module arcpy.geoai


class ExtractEntitiesUsingDeepLearning(object):
    """
    Runs a trained named entity recognizer model on text files in a folder to extract entities and locations (such as addresses, place or person names, dates, and monetary values) in a table. If the extracted entities contain an address, the tool geocodes the addresses using the specified locator and produces a feature class as an output.
    """

    @property
    def description(self) -> str:
        return """

        ExtractEntitiesUsingDeepLearning_geoai(in_folder, out_table, in_model_definition_file, {model_arguments;model_arguments...}, {batch_size}, {location_zone}, {in_locator})

        Runs a trained named entity recognizer model on text files in a folder
        to extract entities and locations (such as addresses, place or person
        names, dates, and monetary values) in a table. If the extracted
        entities contain an address, the tool geocodes the addresses using the
        specified locator and produces a feature class as an output.

     INPUTS:
      in_folder (Folder):
          The folder containing the text files on which named entity extraction
          will be performed.
      in_model_definition_file (File):
          The trained model that will be used for classification. The model
          definition file can be an Esri model definition JSON file (.emd) or a
          deep learning model package (.dlpk) that is stored locally or hosted
          on ArcGIS Living Atlas (.dlpk_remote).
      model_arguments {Value Table}:
          Additional arguments, such as a confidence threshold, that will be
          used to adjust the sensitivity of the model.The names of the arguments
          will be populated by the tool.
      batch_size {Double}:
          The number of training samples that will be processed at one time. The
          default value is 4.Increasing the batch size can improve tool
          performance; however, as
          the batch size increases, more memory is used. If an out of memory
          error occurs, use a smaller batch size.
      location_zone {String}:
          The geographic region or zone in which the addresses are expected to
          be located. The specified text will be appended to the address
          extracted by the model.The locator uses the location zone information
          to identify the region
          or geographic area in which the address is located and produces better
          results.
      in_locator {Address Locator}:
          The locator that will be used to geocode addresses found in the input
          text documents. A point is generated for each address that is geocoded
          successfully and stored in the output feature class.

     OUTPUTS:
      out_table (Feature Class / Table / Feature Layer):
          The output feature class or table that will contain the extracted
          entities. If a locator is provided and the model extracts addresses,
          the feature class will be produced by geocoding the extracted
          addresses.

        """