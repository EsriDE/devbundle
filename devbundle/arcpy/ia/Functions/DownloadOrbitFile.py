# Generated documentation for module arcpy.ia.Functions


class DownloadOrbitFile(object):
    """
    Downloads the updated orbit files for Sentinel-1 synthetic aperture radar (SAR) data.
    """

    @property
    def description(self) -> str:
        return """

        DownloadOrbitFile_ia(in_radar_data, {orbit_type}, {username}, {password}, {cloud_storage}, {folder})

        Downloads the updated orbit files for Sentinel-1 synthetic aperture
        radar (SAR) data.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      orbit_type {String}:
          Specifies the OSV type that will be
          downloaded.SENTINEL_RESTITUTED-Approximate OSV data will be
          downloaded. This is
          available several hours after data
          acquisition.SENTINEL_PRECISE-Refined OSV data will be downloaded. This
          is
          available 20 days after data acquisition. This is the default.
      username {String}:
          The Copernicus Data Space Ecosystem login credential username.This
          parameter is only valid when the input data has Sentinel
          restituted or Sentinel precise orbit types.
      password {Encrypted String}:
          The Copernicus Data Space Ecosystem login credential password.This
          parameter is only valid when the input data has Sentinel
          restituted or Sentinel precise orbit types.
      cloud_storage {File}:
          The Copernicus Data Space Ecosystem cloud storage connection file.
      folder {Folder}:
          An alternate folder location where the downloaded orbit state vector
          file will be stored. The default folder is the input radar data .SAFE
          folder.

        """