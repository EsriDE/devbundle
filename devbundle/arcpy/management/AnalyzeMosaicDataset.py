# Generated documentation for module arcpy.management


class AnalyzeMosaicDataset(object):
    """
    Performs checks on a mosaic dataset for errors and possible improvements.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeMosaicDataset_management(in_mosaic_dataset, {where_clause}, {checker_keywords;checker_keywords...})

        Performs checks on a mosaic dataset for errors and possible
        improvements.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset you want to analyze.
      where_clause {SQL Expression}:
          An SQL statement that confines your analysis to specific raster
          datasets within this mosaic dataset.
      checker_keywords {String}:
          Choose which parts of the mosaic dataset you want to analyze for known
          issues.FOOTPRINT-Analyze the footprint geometry of each selected
          mosaic
          dataset item. This is checked on by default.FUNCTION-Analyze the
          function chains for each selected mosaic dataset
          item.RASTER-Analyze the original raster datasets. This is checked on
          by
          default.PATHS-Check for broken paths. This is checked on by
          default.SOURCE_VALIDITY-Analyze potential problems with the source
          data
          associated with each mosaic dataset item in the selected mosaic
          dataset. This is a good way to detect issues that may arise during
          synchronization workflows. STALE-Overviews are stale when the
          underlying source data
          has changed. Once the mosaic dataset is analyzed, you can select which
          items are stale by right-clicking on the error and clickingon the
          context menu. Select Associated ItemsPYRAMIDS-Analyze the
          raster pyramids associated with each mosaic
          dataset item in the selected mosaic dataset. Test for disconnected
          auxiliary files, which can occur when they are stored in a raster
          proxy location.STATISTICS-Test for disconnected auxiliary statistics
          files if they
          are stored in the raster proxy location. Analyze the covariance matrix
          associated with the raster, when the Gram-Schmidt pan-sharpening
          method is enabled. Analyze the radiometric pixel depth of a mosaic
          dataset item against the pixel depth of the mosaic
          dataset.PERFORMANCE-Factors that increase performance include
          compression
          during transmission and caching items with many raster
          functions.INFORMATION-Generate general information about the mosaic
          dataset.

        """