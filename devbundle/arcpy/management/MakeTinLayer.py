# Generated documentation for module arcpy.management


class MakeTinLayer(object):
    """
    Creates a triangulated irregular network (TIN) layer from an input TIN dataset or layer file. The layer that is created by the tool is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved.
    """

    @property
    def description(self) -> str:
        return """

        MakeTinLayer_management(in_tin, out_layer)

        Creates a triangulated irregular network (TIN) layer from an input TIN
        dataset or layer file. The layer that is created by the tool is
        temporary and will not persist after the session ends unless the layer
        is saved to disk or the map document is saved.

     INPUTS:
      in_tin (TIN Layer):
          The input TIN dataset or layer from which the new layer will be
          created.

     OUTPUTS:
      out_layer (TIN Layer):
          The name of the TIN layer to be created. The output layer can be used
          as an input to any geoprocessing tool that accepts a TIN layer as
          input.

        """