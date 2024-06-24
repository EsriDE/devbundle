# Generated documentation for module arcpy.management


class Rename(object):
    """
    Changes the name of a dataset. This includes a variety of data types, including feature dataset, raster, table, and shapefile.
    """

    @property
    def description(self) -> str:
        return """

        Rename_management(in_data, out_data, {data_type})

        Changes the name of a dataset. This includes a variety of data types,
        including feature dataset, raster, table, and shapefile.

     INPUTS:
      in_data (Data Element):
          The input data to be renamed.
      data_type {String}:
          The type of data to be renamed.This parameter is only necessary in the
          event of a name conflict
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

     OUTPUTS:
      out_data (Data Element):
          The name of the output data.

        """