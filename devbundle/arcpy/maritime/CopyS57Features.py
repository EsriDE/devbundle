# Generated documentation for module arcpy.maritime


class CopyS57Features(object):
    """
    Copies features from a layer or multiple layers to a target geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CopyS57Features_maritime(in_features;in_features..., target_workspace, {compilation_scale})

        Copies features from a layer or multiple layers to a target
        geodatabase.

     INPUTS:
      in_features (Feature Layer):
          The input features that will be copied to the target_workspace
          parameter value.
      target_workspace (Workspace):
          The geodatabase to which the output data will be written.
      compilation_scale {Long}:
          The compilation scale attribute value that will be applied to the
          copied features.

        """