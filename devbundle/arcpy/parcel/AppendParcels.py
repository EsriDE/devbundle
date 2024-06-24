# Generated documentation for module arcpy.parcel


class AppendParcels(object):
    """
    Appends parcels from an input parcel fabric to a target parcel fabric. If the input parcel fabric is a parcel fabric layer with selected polygons, the corresponding parcel features will be appended.
    """

    @property
    def description(self) -> str:
        return """

        AppendParcels_parcel(in_parcel_fabric, target_parcel_fabric)

        Appends parcels from an input parcel fabric to a target parcel fabric.
        If the input parcel fabric is a parcel fabric layer with selected
        polygons, the corresponding parcel features will be appended.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The input parcels that will be appended to the target parcel fabric.
          The input parcel fabric can be from a file, enterprise, or mobile
          geodatabase, or a feature service.
      target_parcel_fabric (Parcel Layer):
          The target parcel fabric to which the parcels will be appended. The
          target parcel fabric can be from a file, enterprise, or mobile
          geodatabase.

        """