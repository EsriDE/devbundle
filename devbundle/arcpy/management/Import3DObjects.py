# Generated documentation for module arcpy.management


class Import3DObjects(object):
    """
    Imports 3D models from one or more 3D file formats and creates or updates a 3D object feature layer.
    """

    @property
    def description(self) -> str:
        return """

        Import3DObjects_management(files_and_folders;files_and_folders..., updated_features, {update}, {translate}, {elevation}, {scale}, {rotate}, {y_is_up})

        Imports 3D models from one or more 3D file formats and creates or
        updates a 3D object feature layer.

     INPUTS:
      files_and_folders (Folder / File):
          The 3D files or folders containing 3D files that will be imported.
          When a folder is provided, all supported 3D models contained in it and
          its subdirectories will be imported.The following models are
          supported:COLLADA (.dae)Drawing (.dwg)Autodesk Filmbox (.fbx)Graphics
          Library
          Transmission (.glb)JSON Graphics Library Transmission (.gltf)Industry
          Foundation Class (.ifc)Wavefront Object (.obj)Universal Scene
          Description (.usdc)Compressed Universal Scene Description (.usdz)
      update {String}:
          Specifies how an existing 3D object feature class will be
          updated.REPLACE_ALL-All existing features in the 3D object feature
          class will
          be removed and only the 3D models that are specified as input will be
          added.UPDATE_EXISTING-3D models that exist in the 3D object feature
          class
          will be updated. New models will be skipped.UPDATE_EXISTING_ADD_NEW-3D
          models that exist in the 3D object feature
          class will be updated and new models will be appended. This is the
          default.ADD_ALL-All 3D models will be added without replacing any that
          currently exist in the 3D object feature class.
      translate {Point}:
          The x- and y-coordinate offset that will be applied to the imported
          models.
      elevation {Double}:
          The height offset that will be applied to the imported models.
      scale {Double}:
          The scale factor that will be used to resize the 3D models being
          imported.
      rotate {Double}:
          The degree rotation angle that will be applied to the imported models.
          Rotation is applied with the assumption of zero degrees (0°)
          representing north and angular values incrementing in the clockwise
          direction.
      y_is_up {Boolean}:
          Specifies whether y coordinates will be interpreted as height or along
          the horizontal plane. This parameter is only supported for Wavefront
          Object files (.obj).Y_IS_UP-Y coordinates will be interpreted as
          height. This is the
          default.Z_IS_UP-Z coordinates will be interpreted as height.

     OUTPUTS:
      updated_features (Feature Layer):
          The 3D object feature layer that will be created or updated.

        """