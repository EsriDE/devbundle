# Generated documentation for module arcpy.parcel


class CreateParcelSeeds(object):
    """
    Creates parcel seeds for closed loops of lines that are associated with the specified parcel record.
    """

    @property
    def description(self) -> str:
        return """

        CreateParcelSeeds_parcel(in_parcel_fabric, record_name)

        Creates parcel seeds for closed loops of lines that are associated
        with the specified parcel record.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The parcel fabric for which parcel seeds will be created. The parcel
          fabric can be from a file, enterprise, or mobile geodatabase, or from
          a feature service.
      record_name (String):
          The name of the parcel fabric record for which parcel seeds will be
          created. The record must already exist. The record name is not case
          sensitive.

        """