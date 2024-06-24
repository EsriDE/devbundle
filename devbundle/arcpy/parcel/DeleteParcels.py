# Generated documentation for module arcpy.parcel


class DeleteParcels(object):
    """
    Deletes the selected parcels from the input parcel fabric. If the parcel polygon layer has no selection, all parcels will be deleted.
    """

    @property
    def description(self) -> str:
        return """

        DeleteParcels_parcel(in_parcel_polygon_features)

        Deletes the selected parcels from the input parcel fabric. If the
        parcel polygon layer has no selection, all parcels will be deleted.

     INPUTS:
      in_parcel_polygon_features (Feature Layer):
          The parcel fabric polygon feature class containing the parcels that
          will be deleted.

        """