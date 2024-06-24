# Generated documentation for module arcpy.server


class ReplaceWebLayer(object):
    """
    Replaces the content of a web layer in a portal with the content of another web layer.
    """

    @property
    def description(self) -> str:
        return """

        ReplaceWebLayer_server(target_layer, archive_layer_name, update_layer, {replace_item_info}, {create_new_item})

        Replaces the content of a web layer in a portal with the content of
        another web layer.

     INPUTS:
      target_layer (Vector Tile Layer / Internet Tiled Layer / Scene Layer):
          The web layer that will be replaced. Provide a layer or
          catalog path, or provide the item ID or service URL of one of the
          following:        Vector tile layer published from vector tile
          packageTile layer
          Scene layer published from one of the following sources:
          Scene layer packageReferenced scene cache in folder or cloud data
          stores
      archive_layer_name (String):
          A unique name for the archive layer. The web layer that is replaced
          remains in the portal as an archive layer.
      update_layer (Vector Tile Layer / Internet Tiled Layer / Scene Layer):
          The replacement web layer. Provide a layer or catalog path, or
          provide the item ID or service URL of one of the following:
          Vector tile layer published from vector tile packageTile layer
          Scene layer published from one of the following sources:
          Scene layer packageReferenced scene cache in folder or cloud data
          stores
      replace_item_info {Boolean}:
          Specifies whether the target layer's item information (thumbnail
          image, summary, description, and tags) will be replaced. With either
          option, the item's credits (attribution), terms of use, and created-
          from information will not be replaced.KEEP-The target layer's item
          information will not be replaced when the
          layer is updated. This is the default.REPLACE-The target layer's item
          information will be replaced by the
          update layer's item information.
      create_new_item {Boolean}:
          Specifies whether an item will be created for the archive layer. This
          parameter is supported on portals in ArcGIS Online and ArcGIS
          Enterprise 10.8 or later.TRUE-An item ID will be created for the
          archive layer. This is the
          default for scene layers.FALSE-The item ID of the update layer will be
          used for the archive
          layer. This is the default for vector tile layers and tile layers.

        """