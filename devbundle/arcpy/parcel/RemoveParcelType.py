# Generated documentation for module arcpy.parcel


class RemoveParcelType(object):
    """
    Removes a parcel type from a parcel fabric.
    """

    @property
    def description(self) -> str:
        return """

        RemoveParcelType_parcel(in_parcel_fabric, name)

        Removes a parcel type from a parcel fabric.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The parcel fabric from which the parcel type will be removed. The
          parcel fabric can be from a file, enterprise, or mobile geodatabase.
      name (String):
          The name of the parcel type.

        """