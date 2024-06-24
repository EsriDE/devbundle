# Generated documentation for module arcpy.management


class GetRasterProperties(object):
    """
    Retrieves information from the metadata and descriptive statistics about a raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        GetRasterProperties_management(in_raster, {property_type}, {band_index})

        Retrieves information from the metadata and descriptive statistics
        about a raster dataset.

     INPUTS:
      in_raster (Composite Geodataset):
          The raster containing the properties to retrieve.
      property_type {String}:
          The property to be obtained from the input raster.MINIMUM-Smallest
          value of all cells in the input
          raster.MAXIMUM-Largest value of all cells in the input
          raster.MEAN-Average of all cells in the input raster.STD-Standard
          deviation of all cells in the input raster.UNIQUEVALUECOUNT-Number of
          unique values in the input raster.TOP-Top or YMax value of the
          extent.LEFT-Left or XMin value of the extent.RIGHT-Right or XMax value
          of the extent.BOTTOM-Bottom or YMin value of the extent.CELLSIZEX-Cell
          size in the x-direction.CELLSIZEY-Cell size in the y-direction.
          VALUETYPE-                  Type of the cell value in the
          input raster:          0 =
          1-bit1 = 2-bit2 = 4-bit3 = 8-bit unsigned integer4 = 8-bit signed
          integer5 = 16-bit unsigned integer6 = 16-bit signed integer7 = 32-bit
          unsigned integer8 = 32-bit signed integer9 = 32-bit floating point10 =
          64-bit double precision11 = 8-bit complex12 = 16-bit complex13 =
          32-bit complex14 = 64-bit complexCOLUMNCOUNT-Number of columns in the
          input raster.ROWCOUNT-Number of rows in the input
          raster.BANDCOUNT-Number of bands in the input raster.ANYNODATA-Returns
          whether there is NoData in the raster.ALLNODATA-Returns whether all
          the pixels are NoData. This is the same
          as ISNULL.SENSORNAME-Name of the sensor.PRODUCTNAME-Product name
          related to the sensor.ACQUISITIONDATE-Date that the data was
          captured.SOURCETYPE-Source type.CLOUDCOVER-Amount of cloud cover as a
          percentage.SUNAZIMUTH-Sun azimuth, in degrees.SUNELEVATION-Sun
          elevation, in degrees.SENSORAZIMUTH-Sensor azimuth, in
          degrees.SENSORELEVATION-Sensor elevation, in degrees.OFFNADIR-Off-
          nadir angle, in degrees.WAVELENGTH-Wavelength range of the band, in
          nanometers.
      band_index {String}:
          Choose the band name from which to get the properties. If no band is
          chosen, then the first band will be used.

        """