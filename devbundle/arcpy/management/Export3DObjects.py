# Generated documentation for module arcpy.management


class Export3DObjects(object):
    """
    Exports 3D object features to one or more 3D model file formats.
    """

    @property
    def description(self) -> str:
        return """

        Export3DObjects_management(in_features, target_folder, formats;formats..., {name_field}, {overwrite})

        Exports 3D object features to one or more 3D model file formats.

     INPUTS:
      in_features (Feature Layer):
          The 3D object feature layer that will be exported.
      target_folder (Folder):
          The existing directory that will contain the output 3D models.
      formats (String):
          Specifies the 3D formats that will be exported.FMT3D_DAE-The COLLADA
          format will be exported.FMT3D_DWG-The DWG format
          will be exported.FMT3D_FBX-The Autodesk FilmBox format will be
          exported.FMT3D_GLB-The binary Graphics Library Transmission format
          will be
          exported.FMT3D_GLTF-The JSON Graphics Library Transmission format will
          be
          exported.FMT3D_IFC-The Industry Foundation Classes format will be
          exported.FMT3D_OBJ-The Wavefront format will be exported.FMT3D_USDC-
          The Universal Scene Description format will be exported.FMT3D_USDZ-
          The compressed version of the Universal Scene Description
          format will be exported.
      name_field {Field}:
          The text field in the input feature's attribute table that contains
          the name to be used for each output model. If no name field is
          provided, the output models will be named after the object ID of the
          input features.
      overwrite {Boolean}:
          Specifies whether existing 3D models in the output directory will be
          overwritten.OVERWRITE-Existing 3D models in the output directory will
          be
          overwritten.NO_OVERWRITE-Existing 3D models in the output directory
          will not be
          overwritten. This is the default.

        """