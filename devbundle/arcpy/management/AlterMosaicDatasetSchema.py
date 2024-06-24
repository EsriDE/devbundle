# Generated documentation for module arcpy.management


class AlterMosaicDatasetSchema(object):
    """
    Defines the editing operations that nonowners have when editing a mosaic dataset in an enterprise geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        AlterMosaicDatasetSchema_management(in_mosaic_dataset, {side_tables;side_tables...}, {raster_type_names;raster_type_names...}, {editor_tracking})

        Defines the editing operations that nonowners have when editing a
        mosaic dataset in an enterprise geodatabase.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset on which the permitted operations will be changed.
      side_tables {String}:
          Specifies the operations that will be permissible for the mosaic
          dataset.ANALYSIS-A nonowner will be allowed to run the Analyze Mosaic
          Dataset
          tool on the mosaic dataset.BOUNDARY-A nonowner will be allowed to
          create or edit the boundary of
          the mosaic dataset. This is also required if a nonowner will add
          rasters outside of the existing boundary.CACHE-A nonowner will be
          allowed to create a cache for the mosaic
          dataset.COLOR_CORRECTION-A nonowner will be allowed to color correct
          the
          mosaic dataset.DEFINITION-A nonowner will be allowed to add
          multidimensional data or
          a processing template to the mosaic dataset.LEVELS-A nonowner will be
          allowed to calculate cell size ranges or
          create seamlines for the mosaic dataset.LOG-A nonowner will be allowed
          to create a log table for the mosaic
          dataset.OVERVIEW-A nonowner will be allowed to create overviews for
          the mosaic
          dataset.SEAMLINE-A nonowner will be allowed to create seamlines for
          the mosaic
          dataset.STEREO-A nonowner will be allowed to define stereo pairs for
          the
          mosaic dataset.VIEW-A nonowner will be allowed to edit the image
          service. The
          editor_tracking parameter will be automatically enabled when this
          option is specified, since the View table must have editor tracking
          turned on.
      raster_type_names {String}:
          Specifies the raster types that nonowners can add to the mosaic
          dataset.To select a custom raster type, provide the location of the
          custom
          raster type file.ADS-The Leica ADS raster type can be added.Altum-The
          Altum raster type
          can be added.ASTER-The ASTER raster type can be added.BlackSky-The
          BlackSky raster type can be added.CADRG/ECRG-The CADRG/ECRG raster
          type can be added.CIB-The CIB raster type can be added.Capella-The
          Capella raster type can be added.DEIMOS-2-The Deimos-2 raster type can
          be added.DTED-The DTED raster type can be added.DMCii-The DMCii raster
          type can be added.DubaiSat-2-The DubaiSat-2 raster type can be
          added.EMIT-The EMIT raster type can be added.FORMOSAT-2-The FORMOSAT-2
          raster type can be added.Frame Camera-The Frame Camera raster type can
          be added.GeoEye-1-The GeoEye-1 raster type can be added.GF-1 PMS-The
          GF-1 PMS raster type can be added.GF-1 WFV-The GF-1 WFV raster type
          can be added.GF-2 PMS-The GF-2 PMS raster type can be added.GF-4
          PMI-The GF-4 PMI raster type can be added.GRIB-The GRIB raster type
          can be added.HDF-The HDF raster type can be added.HJ 1A/1B CCD-The HJ
          1A/HJ 1B CCD raster type can be added.HRE-The HRE raster type can be
          added.ICEYE-The ICEYE raster type can be added.IKONOS-The IKONOS
          raster type can be added.Jilin-1-The Jilin-1 raster type can be
          added.KOMPSAT-2-The KOMPSAT-2 raster type can be added.KOMPSAT-3-The
          KOMPSAT-3 raster type can be added.LAS-The LAS raster type can be
          added.Landsat 1-5 MSS-The Landsat 1-5 MSS raster type can be
          added.Landsat 4-5 TM-The Landsat 4-5 TM raster type can be
          added.Landsat 7 ETM+-The Landsat 7 ETM+ raster type can be
          added.Landsat 8-The Landsat 8 raster type can be added.Landsat 9-The
          Landsat 9 raster type can be added. can be added.MAXAR-The Maxar
          raster type can be added.Match-AT-The Match-AT raster type can be
          added.NCDRD-The NCDRD raster type can be added.NITF-The NITF raster
          type can be added.NetCDF-The NetCDF raster type can be
          added.PlanetScope-The PlanetScope raster type can be added.Pleiades
          Neo-The Pleiades Neo raster type can be added.Pleiades-1-The
          Pleiades-1 raster type can be added.QuickBird-The Quickbird raster
          type can be added.RADARSAT-2-The RADARSAT-2 raster type can be
          added.RCM-The RCM raster type can be added.RapidEye-The RapidEye
          raster type can be added.Raster Process Definition-The Raster Process
          Definition raster type
          can be added.RedEdge-The RedEdge raster type can be added.SOCET
          SET-The SOCET SET raster type can be added.Scanned Aerial Imagery-The
          Scanned Aerial Imagery raster type can be
          added.Sentinel-1-The Sentinel-1 raster type can be
          added.Sentinel-2-The Sentinel-2 raster type can be
          added.Sentinel-3-The Sentinel-3 raster type can be added.SkySat-The
          SkySat-C raster type can be added.SPOT 5-The SPOT 5 raster type can be
          added.SPOT 6-The SPOT 6 raster type can be added.SPOT 7-The SPOT 7
          raster type can be added.SuperView-1-The SuperView-1 raster type can
          be added.TeLEOS-1-The TelEOS-1 raster type can be added.TH-01-The
          TH-01 raster type can be added.UAV/UAS-The UAV/UAS raster type can be
          added.Vision-1-The Vision-1 raster type can be added.WorldView-1-The
          WorldView-1 raster type can be added.WorldView-2-The WorldView-2
          raster type can be added.WorldView-3-The WorldView-3 raster type can
          be added.WorldView-4-The WorldView-4 raster type can be added.ZY1-02C
          HRC-The ZY1-02C HRC raster type can be added.ZY1-02C PMS-The ZY1-02C
          PMS raster type can be added.ZY3-CRESDA-The ZY3-CRESDA raster type can
          be added.ZY3-SASMAC-The ZY3-SASMAC raster type can be added.
      editor_tracking {Boolean}:
          Specifies whether editor tracking will be enabled.Editor tracking can
          help you maintain accountability and enforce
          quality-control standards.NO_EDITOR_TRACKING-Editor tracking will not
          be enabled. This is the
          default.EDITOR_TRACKING-Editor tracking will be enabled.If the VIEW
          keyword is specified for the side_tables parameter, editor
          tracking will be automatically enabled.

        """