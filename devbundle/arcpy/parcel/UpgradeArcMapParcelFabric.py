# Generated documentation for module arcpy.parcel


class UpgradeArcMapParcelFabric(object):
    """
    Upgrades an ArcMap parcel fabric to an ArcGIS Pro parcel fabric.
    """

    @property
    def description(self) -> str:
        return """

        UpgradeArcMapParcelFabric_parcel(in_parcel_fabric, target_dataset, name, {delete_identical})

        Upgrades an ArcMap parcel fabric to an ArcGIS Pro parcel fabric.

     INPUTS:
      in_parcel_fabric (Parcel Fabric Layer for ArcMap):
          The ArcMap parcel fabric that will be upgraded to an ArcGIS Pro parcel
          fabric.
      target_dataset (Feature Dataset):
          The feature dataset that will contain the upgraded ArcGIS Pro parcel
          fabric.
      name (String):
          The name of the upgraded ArcGIS Pro parcel fabric.
      delete_identical {Boolean}:
          Specifies whether identical overlapping lines will be deleted.
          When DELETE_IDENTICAL_ LINES is used, overlapping lines will be
          deleted if the line shapes are identical (lines are coincident) and
          they have the following matching attributes:
          Directions in thefield. This includes directions that are
          reversed by 180 degrees. Direction          Distances in
          thefield. Distances are rounded to four decimal
          places. Distance          Records in thefield.
          Created By Record          Records in thefield. Retired By
          RecordDELETE_IDENTICAL_LINES-Identical overlapping lines will be
          deleted.KEEP_IDENTICAL_LINES-Identical overlapping lines will not be
          deleted.
          This is the default.

        """