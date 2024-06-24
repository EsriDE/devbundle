# Generated documentation for module arcpy.parcel


class CopyParcels(object):
    """
    Copies parcels from an input parcel fabric to a new parcel fabric in a new feature dataset.
    """

    @property
    def description(self) -> str:
        return """

        CopyParcels_parcel(in_parcel_fabric, target_database, {out_dataset_name}, {out_fabric_name})

        Copies parcels from an input parcel fabric to a new parcel fabric in a
        new feature dataset.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The input parcels that will be copied to a new parcel fabric. The
          input parcel fabric can be from a file, enterprise, or mobile
          geodatabase, or from a feature service.
      target_database (Workspace):
          The geodatabase in which the new parcel fabric will be created. The
          geodatabase can be a file, enterprise, or mobile geodatabase.
      out_dataset_name {String}:
          The name of the feature dataset that will be created for the new
          parcel fabric.
      out_fabric_name {String}:
          The name of the new parcel fabric.

        """