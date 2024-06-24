# Generated documentation for module arcpy.maritime


class CreateS57ExchangeSet(object):
    """
    Allows a mariner to view the Electronic Navigational Chart (ENC) datasets in an Electronic Chart Display and Information System (ECDIS) for shipboard navigation.
    """

    @property
    def description(self) -> str:
        return """

        CreateS57ExchangeSet_maritime(in_directories;in_directories..., out_directory, {layout_format}, {updates_only}, {lfil_file})

        Allows a mariner to view the Electronic Navigational Chart (ENC)
        datasets in an Electronic Chart Display and Information System (ECDIS)
        for shipboard navigation.

     INPUTS:
      in_directories (Folder):
          Folders that contain at least one S-57 base cell (*.000) and,
          optionally, any of the following:        S-57 update
          datasetsREADME.txt fileAny referenced files in the S-57
          cells (*.txt, *.tif, and *.jpg)
      out_directory (Folder):
          The location of an empty folder where the ENC_ROOT folder will be
          written. The folder must be empty for the tool to run successfully.
      layout_format {String}:
          Specifies the directory and folder structure of the exchange
          set.VERSION_LAYOUT-The exchange set will be written in the format
          ENC_ROOT\CATALOG.031, ENC_ROOT\<Agency>\<ProductName>\<MajorEdition>\<
          MinorEdition>\<S57Product>, <Referenced Files>. This is the
          default.PRODUCT_LAYOUT-The exchange set will be written in the format
          ENC_ROOT\CATALOG.031, ENC_ROOT\<ProductName>\<S57Product>, <Referenced
          Files>.FLAT_LAYOUT-The exchange set will be written in the format
          ENC_ROOT\CATALOG.031, <S57Product(s)>, <Referenced Files>.
      updates_only {Boolean}:
          Specifies how S-57 update datasets in the input folder will be
          processed.INCLUDE_ALL-The output exchange set will include the S-57
          base dataset
          and any updates. This is the default.INCLUDE_ONLY_UPDATES-The output
          exchange set will include all the
          updates but not the S-57 base dataset. If there are no updates, the
          output will include the S-57 base dataset.
      lfil_file {File}:
          A text file that will be used to match file names in the output
          exchange set to the long file descriptions populated on the catalog
          file records.

        """