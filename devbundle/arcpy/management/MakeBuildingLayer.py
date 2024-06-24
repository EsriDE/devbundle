# Generated documentation for module arcpy.management


class MakeBuildingLayer(object):
    """
    Creates a composite building layer from a dataset, either a BIM file workspace or a geodatabase dataset, such as the output of the BIM File To Geodatabase tool.
    """

    @property
    def description(self) -> str:
        return """

        MakeBuildingLayer_management(in_feature_dataset, out_layer)

        Creates a composite building layer from a dataset, either a BIM file
        workspace or a geodatabase dataset, such as the output of the BIM File
        To Geodatabase tool.

     INPUTS:
      in_feature_dataset (Feature Dataset / BIM File Workspace):
          The input dataset from which the new building feature layers will be
          made. The building layer keeps the structure and the symbology grouped
          together.

     OUTPUTS:
      out_layer (Building Layer):
          The name of the feature layer that will be created. The layer can be
          used as input to any geoprocessing tool that accepts a feature layer
          as input.

        """