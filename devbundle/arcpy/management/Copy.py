# Generated documentation for module arcpy.management


class Copy(object):
    """
    Makes a copy of the input data.
    """

    @property
    def description(self) -> str:
        return """

        Copy_management(in_data, out_data, {data_type}, {associated_data;associated_data...})

        Makes a copy of the input data.

     INPUTS:
      in_data (Data Element):
          The data to be copied.
      data_type {String}:
          The type of the data on disk to be copied.This parameter is only
          necessary in the event of a name conflict
          between two different data types. For example, a geodatabase can
          contain a relationship class with an identical name to a feature
          class. If that is the case, specify the relevant
          keyword.FeatureClass-In the event of duplicate names, the feature
          class will
          be used.FeatureDataset-In the event of duplicate names, the feature
          dataset
          will be used.MosaicDataset-In the event of duplicate names, the mosaic
          dataset will
          be used.ParcelFabric-In the event of duplicate names, the parcel
          fabric will
          be used.RelationshipClass-In the event of duplicate names, the
          relationship
          class will be used.Topology-In the event of duplicate names, the
          topology will be used.
      associated_data {Value Table}:
          When the input has associated data, this parameter can be used to
          control the associated output data's name and config
          keyword.from_name-The data associated with the input data, which will
          also be
          copied.data_type-The type of the data on disk to be copied. The only
          time you
          need to provide a value is when a geodatabase contains a feature
          dataset and a feature class with the same name. In this case, use the
          correct data type, FeatureDataset or FeatureClass, of the item you
          want to copy.to_name-The name of the copied data in the out_data
          parameter value.config_keyword-The geodatabase storage parameters
          (configuration).The from_name and to_name column names will be
          identical if the
          to_name value is not already used in out_data. If a name already
          exists in the out_data value, a unique to_name value will be created
          by appending an underscore plus a number (for example, rivers_1).

     OUTPUTS:
      out_data (Data Element):
          The location and name of the output data. The file name extension of
          the output data must match the extension of the input data. For
          example, if you are copying a file geodatabase, the output data
          element must have .gdb as a suffix.

        """