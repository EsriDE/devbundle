# Generated documentation for module arcpy.locref


class OverlayEvents(object):
    """
    Overlays one or more linear event feature layers onto a target network and outputs a feature class or table that represents the dynamic segmentation of the inputs.
    """

    @property
    def description(self) -> str:
        return """

        OverlayEvents_locref(in_route_features, event_layers;event_layers..., output_dataset, {include_geometry}, {network_fields;network_fields...})

        Overlays one or more linear event feature layers onto a target network
        and outputs a feature class or table that represents the dynamic
        segmentation of the inputs.

     INPUTS:
      in_route_features (Feature Layer):
          The target network onto which the event layers will be dynamically
          segmented.
      event_layers (Feature Layer):
          The event layers that will be dynamically segmented together onto a
          target network. The centerline layer can be used as an input to
          dynamically segment events.
      include_geometry {Boolean}:
          Specifies whether the output_dataset parameter value will include
          event geometry.EXCLUDE_GEOMETRY-The output_dataset parameter value
          will not include
          event geometry. Event records will be stored as a table. This is the
          default.INCLUDE_GEOMETRY-The output_dataset parameter value will
          include event
          geometry. Event records will be stored as a feature class.
      network_fields {Field}:
          Fields from the network layer that will be included in the output.

     OUTPUTS:
      output_dataset (Table):
          The table or feature class containing the output event records that
          will be created.

        """