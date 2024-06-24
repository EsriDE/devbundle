# Generated documentation for module arcpy.management


class PackageLocator(object):
    """
    Packages a locator or composite locator and creates a single compressed .gcpk file.
    """

    @property
    def description(self) -> str:
        return """

        PackageLocator_management(in_locator, output_file, {copy_arcsde_locator}, {additional_files;additional_files...}, {summary}, {tags})

        Packages a locator or composite locator and creates a single
        compressed .gcpk file.

     INPUTS:
      in_locator (Address Locator):
          The locator or composite locator that will be packaged.
      copy_arcsde_locator {Boolean}:
          This parameter has no effect in ArcGIS Pro. It remains only to support
          backward compatibility.
      additional_files {File}:
          The additional files that will be added to a package. Additional
          files, such as .doc, .txt, .pdf, and so on, are used to provide more
          information about the contents and purpose of the package.
      summary {String}:
          The summary information that will be added to the properties of the
          package.
      tags {String}:
          The tag information that will be added to the properties of the
          package. Multiple tags can be added or separated by a comma or
          semicolon.

     OUTPUTS:
      output_file (File):
          The name and location of the output locator package (.gcpk).

        """