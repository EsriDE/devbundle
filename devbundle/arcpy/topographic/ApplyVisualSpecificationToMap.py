# Generated documentation for module arcpy.topographic


class ApplyVisualSpecificationToMap(object):
    """
    Applies symbols and Arcade expressions to layers in a map based on the symbols and rules defined in a visual specification database.
    """

    @property
    def description(self) -> str:
        return """

        ApplyVisualSpecificationToMap_topographic(in_map, vs_workspace, specification, {in_style_file})

        Applies symbols and Arcade expressions to layers in a map based on the
        symbols and rules defined in a visual specification database.

     INPUTS:
      in_map (Map):
          The map containing layers to which symbols and Arcade expressions will
          be applied.
      vs_workspace (Workspace):
          The database containing the visual specification rules.
      specification (String):
          The specification rules that will be converted to Arcade and applied
          to the map layers.
      in_style_file {String}:
          The style file (.stylx) that contains the symbols defined in the
          visual specification rules.

        """