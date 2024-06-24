# Generated documentation for module arcpy.management


class BuildOverviews(object):
    """
    Defines and generates overviews on a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        BuildOverviews_management(in_mosaic_dataset, {where_clause}, {define_missing_tiles}, {generate_overviews}, {generate_missing_images}, {regenerate_stale_images})

        Defines and generates overviews on a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset where you want to build overviews.
      where_clause {SQL Expression}:
          An SQL statement to select specific rasters within the mosaic dataset.
          The selected rasters will have their overview built.
      define_missing_tiles {Boolean}:
          Identify where overviews are needed and define
          them.DEFINE_MISSING_TILES-Automatically identify where overviews are
          needed
          and define them. This is the default.NO_DEFINE_MISSING_TILES-Do not
          define new overviews.
      generate_overviews {Boolean}:
          Generate all overviews that need to be created or re-created. This
          includes missing overviews and stale
          overviews.GENERATE_OVERVIEWS-Generate all overviews, including those
          that
          already exist. This is the default.NO_GENERATE_OVERVIEWS-Generate only
          the overviews that have been
          defined but not yet generated.
      generate_missing_images {Boolean}:
          Use if overviews have been defined but not
          generated.GENERATE_MISSING_IMAGES-Generate overviews that have been
          defined but
          not generated. This is the default.IGNORE_MISSING_IMAGES-Do not
          generate overviews that have been
          defined but not generated.
      regenerate_stale_images {Boolean}:
          Overviews become stale when you change the underlying raster datasets
          or modify their properties.REGENERATE_STALE_IMAGES-Identify and
          regenerate stale overviews. This
          is the default.IGNORE_STALE_IMAGES-Do not regenerate stale overviews.

        """