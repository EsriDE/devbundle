# Generated documentation for module arcpy.nd


class UpdateDiagram(object):
    """
    Updates one or more network diagrams that are related to a given utility network or trace network.
    """

    @property
    def description(self) -> str:
        return """

        UpdateDiagram_nd(in_diagrams, {template_names;template_names...}, {diagram_names;diagram_names...}, {update_option}, {autolayout_option})

        Updates one or more network diagrams that are related to a given
        utility network or trace network.

     INPUTS:
      in_diagrams (Utility Network / Trace Network / Utility Network Layer / Trace Network Layer / Diagram Layer):
          The input network diagram layer that will be updated, or the utility
          network or trace network-on which the set of specified input diagram
          names are based-that will be updated.
      template_names {String}:
          The names of the templates for which the related diagrams will be
          processed.
      diagram_names {String}:
          The names of the diagrams to be processed.
      update_option {Boolean}:
          Specifies whether only inconsistent diagrams (the default) or all
          diagrams regardless of their consistency state will be
          updated.INCONSISTENT_DIAGRAMS_ONLY-Only inconsistent diagrams will be
          updated.
          This is the default.ALL_SELECTED_DIAGRAMS-Both consistent and
          inconsistent diagrams will
          be updated.
      autolayout_option {Boolean}:
          Specifies whether automatic layouts that are configured on the
          template on which the diagrams are based will be reapplied during the
          update process. By default, when automatic layouts are specified on a
          template, they are not reapplied during the update
          process.REAPPLY_AUTOLAYOUT-The automatic layouts that are configured
          on the
          template will be reapplied to diagrams at the end of the update
          process.DO_NOT_REAPPLY_AUTOLAYOUT-None of the automatic layouts
          configured on
          the template will be reapplied to diagrams during the update process.
          This is the default.

        """