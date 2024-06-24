# Generated documentation for module arcpy.management


class CreateMosaicDataset(object):
    """
    Creates an empty mosaic dataset in a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateMosaicDataset_management(in_workspace, in_mosaicdataset_name, coordinate_system, {num_bands}, {pixel_type}, {product_definition}, {product_band_definitions;product_band_definitions...})

        Creates an empty mosaic dataset in a geodatabase.

     INPUTS:
      in_workspace (Workspace):
          The path to the geodatabase.Starting at ArcGIS Pro 1.4, mosaic
          datasets created in Oracle,
          PostgreSQL, and SQL Server geodatabases will be created with the
          RASTERBLOB keyword. The RASTERBLOB keyword implements a transfer of
          the mosaic dataset catalog items to the DBMS. Mosaic datasets
          created with the RASTERBLOB keyword cannot be
          opened with earlier versions of the software. To create mosaic
          datasets that are backward compatible with earlier versions, alter the
          configuration keyword for RASTER_STORAGE to one of the following
          compatible keywords:        BINARY for PostgreSQL and SQL ServerBLOB
          for Oracle
      in_mosaicdataset_name (String):
          The name of the new mosaic dataset.
      coordinate_system (Coordinate System):
          The coordinate system that will be used for all of the items in the
          mosaic dataset.
      num_bands {Long}:
          The number of bands the raster datasets will have in the mosaic
          dataset.
      pixel_type {String}:
          Specifies the bit depth, or radiometric resolution, that will be used
          for the mosaic dataset. If not defined, the pixel type of the first
          raster dataset will be used.1_BIT-The pixel type will be a 1-bit
          unsigned integer. The values can
          be 0 or 1.2_BIT-The pixel type will be a 2-bit unsigned integer. The
          values
          supported can range from 0 to 3.4_BIT-The pixel type will be a 4-bit
          unsigned integer. The values
          supported can range from 0 to 15.8_BIT_UNSIGNED-The pixel type will be
          an unsigned 8-bit data type. The
          values supported can range from 0 to 255.8_BIT_SIGNED-The pixel type
          will be a signed 8-bit data type. The
          values supported can range from -128 to 127.16_BIT_UNSIGNED-The pixel
          type will be a 16-bit unsigned data type.
          The values can range from 0 to 65,535.16_BIT_SIGNED-The pixel type
          will be a 16-bit signed data type. The
          values can range from -32,768 to 32,767.32_BIT_UNSIGNED-The pixel type
          will be a 32-bit unsigned data type.
          The values can range from 0 to 4,294,967,295.32_BIT_SIGNED-The pixel
          type will be a 32-bit signed data type. The
          values can range from -2,147,483,648 to 2,147,483,647.32_BIT_FLOAT-The
          pixel type will be a 32-bit data type supporting
          decimals.64_BIT-The pixel type will be a 64-bit data type supporting
          decimals.
      product_definition {String}:
          Specifies whether a template is specific to the type of imagery you
          are working with or is generic. The generic options include the
          following standard raster data types:NONE-No band ordering is
          specified for the mosaic dataset. This is the
          default.NATURAL_COLOR_RGB-A 3-band mosaic dataset, with red, green,
          and blue
          wavelength ranges will be created. This is designed for natural color
          imagery.NATURAL_COLOR_RGBI-A 4-band mosaic dataset, with red, green,
          blue, and
          near infrared wavelength ranges will be created.VECTOR_FIELD_UV-A
          mosaic dataset displaying two variables will be
          created.VECTOR_FIELD_MAGNITUDE_DIRECTION-A mosaic dataset displaying
          magnitude
          and direction will be created.FALSE_COLOR_IRG-A 3-band mosaic dataset,
          with near infrared, red, and
          green wavelength ranges will be created.BLACKSKY-A 3-band mosaic
          dataset using the BlackSky wavelength ranges
          will be createdDMCII_3BANDS-A 3-band mosaic dataset using the DMCii
          wavelength ranges
          will be created.DEIMOS2_4BANDS-A 4-band mosaic dataset using the
          Deimos-2 wavelength
          ranges will be created.DUBAISAT-2_4BANDS-A 4-band mosaic dataset using
          the DubaiSat-2
          wavelength ranges will be created.FORMOSAT-2_4BANDS-A 4-band mosaic
          dataset using the FORMOSAT-2
          wavelength ranges will be created.GEOEYE-1_4BANDS-A 4-band mosaic
          dataset using the GeoEye-1 wavelength
          ranges will be created.GF-1 PMS_4BANDS-A 4-band mosaic dataset using
          the Gaofen-1
          Panchromatic Multispectral Sensor wavelength ranges will be
          created.GF-1 WFV_4BANDS-A 4-band mosaic dataset using the Gaofen-1
          Wide Field
          of View Sensor wavelength ranges will be created.GF-2 PMS_4BANDS-A
          4-band mosaic dataset using the Gaofen-2
          Panchromatic Multispectral Sensor wavelength ranges will be
          created.GF-4 PMI_4BANDS-A 4-band mosaic dataset using the Gaofen-4
          panchromatic and multispectral wavelength ranges will be created.HJ
          1A/1B CCD_4BANDS-A 4-band mosaic dataset using the Huan Jing-1 CCD
          Multispectral or Hyperspectral Sensor wavelength ranges will be
          created.IKONOS_4BANDS-A 4-band mosaic dataset using the IKONOS
          wavelength
          ranges will be created.JILIN-1_3BANDS-A 3-band mosaic dataset using
          the Jilin-1 wavelength
          ranges will be created.KOMPSAT-2_4BANDS-A 4-band mosaic dataset using
          the KOMPSAT-2
          wavelength ranges will be created.KOMPSAT-3_4BANDS-A 4-band mosaic
          dataset using the KOMPSAT-3
          wavelength ranges will be created.LANDSAT_6BANDS-A 6-band mosaic
          dataset using the Landsat 5 and 7
          wavelength ranges from the TM and ETM+ sensors will be
          created.LANDSAT_8BANDS-An 8-band mosaic dataset using the Landsat 8
          wavelength
          ranges will be created.LANDSAT_9BANDS-An 8-band mosaic dataset using
          the Landsat 9 wavelength
          ranges will be created.LANDSAT_MSS_4BANDS-A 4-band mosaic dataset
          using the Landsat
          wavelength ranges from the MSS sensor will be created.PLANETSCOPE-A
          5-band mosaic dataset using the PlanetScope wavelength
          ranges will be created.PLEIADES-1_4BANDS-A 4-band mosaic dataset using
          the Pleiades 1
          wavelength ranges will be created.PLEIADES_NEO_6BANDS-A 6-band mosaic
          dataset using the Pleiades Neo
          wavelength ranges will be created.QUICKBIRD_4BANDS-A 4-band mosaic
          dataset using the QuickBird
          wavelength ranges will be created.RAPIDEYE_5BANDS-A 5-band mosaic
          dataset using the RapidEye wavelength
          ranges will be created.SENTINEL2_13BANDS-A 13-band mosaic dataset
          using the Sentinel 2 MSI
          wavelength ranges will be created.SKYSAT_4BANDS-A 4-band mosaic
          dataset using the SkySat-C MSI
          wavelength ranges will be created.SPOT-5_4BANDS-A 4-band mosaic
          dataset using the SPOT-5 wavelength
          ranges will be created.SPOT-6_4BANDS-A 4-band mosaic dataset using the
          SPOT-6 wavelength
          ranges will be created.SPOT-7_4BANDS-A 4-band mosaic dataset using the
          SPOT-7 wavelength
          ranges will be created.SUPERVIEW-1_4BANDS-A 4-band mosaic dataset
          using the SuperView-1
          wavelength ranges will be created.TH-01_4BANDS-A 4-band mosaic dataset
          using the Tian Hui-1 wavelength
          ranges will be created.WORLDVIEW-2_8BANDS-An 8-band mosaic dataset
          using the WorldView-2
          wavelength ranges will be created.WORLDVIEW-3_8BANDS-An 8-band mosaic
          dataset using the WorldView-3
          wavelength ranges will be created.WORLDVIEW-4_4BANDS-A 4-band mosaic
          dataset using the WorldView-4
          wavelength ranges will be created.VISION-1_4BANDS-A 4-band mosaic
          dataset using the Vision-1 wavelength
          ranges will be created.ZY1-02C PMS_3BANDS-A 3-band mosaic dataset
          using the ZiYuan-1
          panchromatic/multispectral wavelength ranges will be
          created.ZY3-CRESDA_4BANDS-A 4-band mosaic dataset using the ZiYuan-3
          CRESDA
          wavelength ranges will be created.ZY3-SASMAC_4BANDS-A 4-band mosaic
          dataset using the ZiYuan-3 SASMAC
          wavelength ranges will be created. CUSTOM-The number of bands
          and the average wavelength for
          each band are defined using theparameter (product_band_definitions in
          Python). Product Band Definitions
      product_band_definitions {Value Table}:
          The definitions of the bands. Edit product_definition when using the
          CUSTOM keyword by adjusting the wavelength ranges, changing the band
          order, and adding new bands.

        """