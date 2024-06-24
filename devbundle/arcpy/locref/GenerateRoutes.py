# Generated documentation for module arcpy.locref


class GenerateRoutes(object):
    """
    Re-creates shapes and applies calibration changes for route features in an LRS Network.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRoutes_locref(in_route_features, {record_calibration_changes})

        Re-creates shapes and applies calibration changes for route features
        in an LRS Network.

     INPUTS:
      in_route_features (Feature Layer):
          The LRS Network for which route shapes will be regenerated and
          calibration changes will be applied.
      record_calibration_changes {Boolean}:
          This parameter is not supported. Any value provided will be ignored.

        """