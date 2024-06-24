# Generated documentation for module arcpy.management


class AddPortalItemsToCatalogDataset(object):
    """
    Adds ArcGIS Online or ArcGIS Enterprise portal service items-such as feature, map, image, scene, and tile services-to an existing catalog dataset.
    """

    @property
    def description(self) -> str:
        return """

        AddPortalItemsToCatalogDataset_management(target_catalog_dataset, {input_portal_itemtypes;input_portal_itemtypes...}, {content}, {portal_folders;portal_folders...}, {portal_groups;portal_groups...}, {access_level})

        Adds ArcGIS Online or ArcGIS Enterprise portal service items-such as
        feature, map, image, scene, and tile services-to an existing catalog
        dataset.

     INPUTS:
      target_catalog_dataset (Catalog Layer):
          The catalog dataset to which portal items will be added.
      input_portal_itemtypes {String}:
          Specifies the item types that will be added to the catalog dataset
          from the portal. All supported item types will be added by
          default.FEATURE_SERVICE-Feature layers will be added. This option does
          not add
          feature collections.IMAGE_SERVICE-Imagery layers will be
          added.MAP_SERVICE-Map image and tile layers will be
          added.SCENE_SERVICE-Scene layers will be
          added.VECTOR_TILE_SERVICE-Vector tile layers will be added.WFS-Web
          Feature Service (WFS) layers will be added.WMS-Web Map Service (WMS)
          layers will be added.WMTS-Web Map Tile Service (WMTS) layers will be
          added.
      content {String}:
          Specifies the collection in the active portal from which items will be
          added to the catalog dataset.MY_CONTENT-Items from your My Content
          collection will be added. This
          is the default.MY_GROUPS-Items from groups to which you belong will be
          added.MY_ORGANIZATION-Items from your ArcGIS organization will be
          added.
      portal_folders {String}:
          The portal folders from which items will be added to the catalog
          dataset.
      portal_groups {String}:
          The portal groups from which items will be added to the catalog
          dataset.
      access_level {String}:
          Specifies the sharing level that portal items must have to be added to
          the catalog dataset.PUBLIC-Items that are shared with the public will
          be added to the
          catalog dataset. This is the default.ORG-Items that are shared with
          the organization, as well as items you
          own will be added to the catalog dataset. Items that are shared with
          the organization and one or more groups will also be
          added.SHARED-Items shared with one or more groups, item owners, and
          those
          who have access to the item through group membership will be added to
          the catalog dataset.PRIVATE-Items owned by you will be added to the
          catalog dataset. Only
          you or administrators who have access to your content can add these
          items.

        """