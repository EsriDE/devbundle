# Generated documentation for module arcpy.ia.Functions


class ApplyOrbitCorrection(object):
    """
    Updates the orbital information in the Sentinel-1 synthetic aperture radar (SAR) data using a more accurate orbit state vector (OSV) file.
    """

    @property
    def description(self) -> str:
        return """

        ApplyOrbitCorrection_ia(in_radar_data, {in_orbit_file}, {folder})

        Updates the orbital information in the Sentinel-1 synthetic aperture
        radar (SAR) data using a more accurate orbit state vector (OSV) file.

     INPUTS:
      in_radar_data (Raster Dataset / Raster Layer):
          The input radar data.
      in_orbit_file {File}:
          The input orbit file.
      folder {Folder}:
          The alternate folder location that will be searched for the downloaded
          orbit state vector files. The default folder is the input radar data
          .SAFE folder.

        """