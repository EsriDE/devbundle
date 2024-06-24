# Generated documentation for module arcpy.management


class UpgradeDataset(object):
    """
    Upgrades the schema of a mosaic dataset, network dataset, annotation dataset, dimension dataset, parcel fabric, trace network, utility network, or 3D object feature class to the current ArcGIS release. Upgrading a dataset enables it to use new functionality in the current software release.
    """

    @property
    def description(self) -> str:
        return """

        UpgradeDataset_management(in_dataset)

        Upgrades the schema of a mosaic dataset, network dataset, annotation
        dataset, dimension dataset, parcel fabric, trace network, utility
        network, or 3D object feature class to the current ArcGIS release.
        Upgrading a dataset enables it to use new functionality in the current
        software release.

     INPUTS:
      in_dataset (Parcel Fabric Layer for ArcMap / Parcel Layer / Mosaic Layer / Network Dataset Layer / Utility Network Layer / Trace Network Layer / Annotation Layer / Dimension Layer / 3D Object Feature Layer / Catalog Layer):
          The dataset that will be upgraded to the current ArcGIS client
          release.

        """