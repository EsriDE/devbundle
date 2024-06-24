# Generated documentation for module arcpy.management


class MakeSceneLayer(object):
    """
    Creates a scene layer from a scene layer package (.slpk) or scene service.
    """

    @property
    def description(self) -> str:
        return """

        MakeSceneLayer_management(in_dataset, out_layer)

        Creates a scene layer from a scene layer package (.slpk) or scene
        service.

     INPUTS:
      in_dataset (Scene Layer / Building Scene Layer / File):
          The input scene layer package (.slpk) or scene service from which the
          new scene layer will be created.

     OUTPUTS:
      out_layer (Scene Layer):
          The name of the scene layer to be created.

        """