# Generated documentation for module arcpy.tn


class SetFlowDirection(object):
    """
    Sets the flow direction of line features in a version 1 trace network.
    """

    @property
    def description(self) -> str:
        return """

        SetFlowDirection_tn(input_trace_network, in_edges;in_edges..., flow_direction)

        Sets the flow direction of line features in a version 1 trace network.

     INPUTS:
      input_trace_network (Trace Network / Trace Network Layer):
          The trace network that contains the line feature class on which the
          flow direction will be set.
      in_edges (Feature Layer):
          The polyline features that participate in the input trace network.
      flow_direction (String):
          Specifies the flow direction of the
          edges.WITH_DIGITIZED_DIRECTION-Flow direction will be along the
          digitized
          direction of the edges.AGAINST_DIGITIZED_DIRECTION-Flow direction will
          be against the
          digitized direction of the edges.INDETERMINATE-Flow direction will be
          indeterminate.

        """