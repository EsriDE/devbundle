# Generated documentation for module arcpy.management


class Delete(object):
    """
    Permanently deletes data. All types of geographic data supported by ArcGIS, as well as toolboxes and workspaces (folders and geodatabases), can be deleted. If the specified item is a workspace, all contained items will also be deleted.
    """

    @property
    def description(self) -> str:
        return """

        Delete_management(in_data;in_data..., {data_type})

        Permanently deletes data. All types of geographic data supported by
        ArcGIS, as well as toolboxes and workspaces (folders and
        geodatabases), can be deleted. If the specified item is a workspace,
        all contained items will also be deleted.

     INPUTS:
      in_data (Data Element / Layer / Table View / Graph / Utility Network):
          The input data that will be deleted.
      data_type {String}:
          The type of data on disk to be deleted.This parameter is only
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

        """