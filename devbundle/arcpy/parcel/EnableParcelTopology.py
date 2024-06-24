# Generated documentation for module arcpy.parcel


class EnableParcelTopology(object):
    """
    Enables geodatabase topology on a parcel fabric.
    """

    @property
    def description(self) -> str:
        return """

        EnableParcelTopology_parcel(in_parcel_fabric)

        Enables geodatabase topology on a parcel fabric.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The parcel fabric for which the geodatabase topology will be enabled.
          The input parcel fabric can be from a file, enterprise, or mobile
          geodatabase.

        """