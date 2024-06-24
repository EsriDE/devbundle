# Generated documentation for module arcpy.maritime


class ConvertS57ToS101(object):
    """
    Converts the S-57 vector product for storing nautical charting data to the new vector S-101 format.
    """

    @property
    def description(self) -> str:
        return """

        ConvertS57ToS101_maritime(in_feature_catalogue, in_config_file, input_s57, out_location)

        Converts the S-57 vector product for storing nautical charting data to
        the new vector S-101 format.

     INPUTS:
      in_feature_catalogue (File):
          An .xml file that follows the S-100 Feature Catalogue format as
          defined by the IHO. It describes the content of a data product and its
          specifications. The default file location for S-100 catalogue files is
          <installation location>\ArcGIS Maritime\Product
          Files\<version>\S-101\, provided the Maritime product files are
          installed.
      in_config_file (File):
          The input .xml file that can be used to customize some aspects of the
          conversion process.
      input_s57 (File / Folder):
          The input S-57 file with a .000 extension or a CATALOG.031 file that
          references a collection of S-57 files.
      out_location (Folder):
          The directory where the converted cell will be written.

        """