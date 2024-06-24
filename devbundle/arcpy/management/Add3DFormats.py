# Generated documentation for module arcpy.management


class Add3DFormats(object):
    """
    Converts a multipatch to a 3D object feature layer by linking the feature class with one or more 3D model formats.
    """

    @property
    def description(self) -> str:
        return """

        Add3DFormats_management(in_features, multipatch_materials, {formats;formats...})

        Converts a multipatch to a 3D object feature layer by linking the
        feature class with one or more 3D model formats.

     INPUTS:
      in_features (Feature Layer):
          The input geodatabase multipatch feature that will be converted to a
          3D object feature layer.
      multipatch_materials (Boolean):
          This parameter is no longer supported. The option to control whether
          multipatch materials were used was removed to improve this tool's
          usability. Materials will always be used when they are available
          through the 3D object feature layer, and they will be automatically
          removed when the 3D object feature layer capabilities are removed from
          the multipatch. Additional parameters are available using the
          dedicated API for multipatches.
      formats {String}:
          Specifies the 3D formats that will be associated with the multipatch
          features. Each input feature will be duplicated for each selected
          format. The available options depend on the codecs installed on the
          computer.FMT3D_DAE-The COLLADA format will be added.FMT3D_DWG-The DWG
          format
          will be added.FMT3D_FBX-The Autodesk FilmBox format will be
          added.FMT3D_GLB-The binary Graphics Library Transmission format will
          be
          added.FMT3D_GLTF-The JSON Graphics Library Transmission format will be
          added.FMT3D_IFC-The Industry Foundation Classes format will be
          added.FMT3D_OBJ-The Wavefront format will be added.FMT3D_USDC-The
          Universal Scene Description format will be added.FMT3D_USDZ-The
          compressed version of the Universal Scene Description
          format will be added.

        """