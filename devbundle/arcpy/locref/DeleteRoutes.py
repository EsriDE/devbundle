# Generated documentation for module arcpy.locref


class DeleteRoutes(object):
    """
    Deletes routes and associated data elements from the LRS Network.
    """

    @property
    def description(self) -> str:
        return """

        DeleteRoutes_locref(in_route_features, {delete_associated_calibration_points}, {delete_associated_events}, {delete_associated_centerlines})

        Deletes routes and associated data elements from the LRS Network.

     INPUTS:
      in_route_features (Feature Layer):
          The route feature class registered with the network.
      delete_associated_calibration_points {Boolean}:
          Specifies whether calibration points associated with the deleted
          routes will be deleted.DELETE_CALIBRATION_POINTS-Calibration points
          associated with the
          routes will be deleted.NO_DELETE_CALIBRATION_POINTS-Calibration points
          associated with the
          routes will not be deleted. This is the default.
      delete_associated_events {Boolean}:
          Specifies whether events associated with the deleted routes will be
          deleted.DELETE_EVENTS-Events associated with the routes will be
          deleted.NO_DELETE_EVENTS-Events associated with the routes will not be
          deleted. This is the default.
      delete_associated_centerlines {Boolean}:
          Specifies whether centerlines that are exclusively associated with the
          deleted routes will be deleted.DELETE_CENTERLINES-Centerlines
          exclusively associated with the
          selected routes will be deleted. If centerlines are shared between
          networks, those common centerlines will not be
          deleted.NO_DELETE_CENTERLINES-Centerlines will not be deleted. This is
          the
          default.

        """