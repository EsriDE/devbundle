# Generated documentation for module arcpy.management


class Remove3DFormats(object):
    """
    Removes the 3D formats referenced by a 3D object feature layer.
    """

    @property
    def description(self) -> str:
        return """

        Remove3DFormats_management(in_features, multipatch_materials, {formats;formats...})

        Removes the 3D formats referenced by a 3D object feature layer.

     INPUTS:
      in_features (Feature Layer):
          The multipatch feature class that was converted to a 3D object feature
          class.
      multipatch_materials (Boolean):
          This parameter is no longer supported. The option to control whether
          multipatch materials were used was removed to improve this tool's
          usability. Materials will always be used when they are available
          through the 3D object feature layer, and they will be automatically
          removed when the 3D object feature layer capabilities are removed from
          the multipatch. Additional parameters are available using the
          dedicated API for multipatches.
      formats {String}:
          Specifies the 3D model formats referenced by the 3D object feature
          layer that will be removed. Only the formats that have been linked to
          the input features can be specified.FMT3D_DAE-The COLLADA format will
          be removed.FMT3D_DWG-The DWG format
          will be removed.FMT3D_FBX-The Autodesk FilmBox format will be
          removed.FMT3D_GLB-The binary Graphics Library Transmission format will
          be
          removed.FMT3D_GLTF-The JSON Graphics Library Transmission format will
          be
          removed.FMT3D_IFC-The Industry Foundation Classes format will be
          removed.FMT3D_OBJ-The Wavefront format will be removed.FMT3D_USDC-The
          Universal Scene Description format will be removed.FMT3D_USDZ-The
          compressed version of the Universal Scene Description
          format will be removed.

        """