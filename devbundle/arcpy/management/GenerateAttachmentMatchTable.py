# Generated documentation for module arcpy.management


class GenerateAttachmentMatchTable(object):
    """
    Creates a match table to be used with the Add Attachments and Remove Attachments tools.
    """

    @property
    def description(self) -> str:
        return """

        GenerateAttachmentMatchTable_management(in_dataset, in_folder, out_match_table, in_key_field, {in_file_filter}, {in_use_relative_paths}, {match_pattern})

        Creates a match table to be used with the Add Attachments and Remove
        Attachments tools.

     INPUTS:
      in_dataset (Table View):
          A dataset containing records that will have files attached.
      in_folder (Folder):
          A folder containing files to attach.
      in_key_field (Field):
          The field from which values will be used to match the names of the
          files from the input folder. The matching behavior will compare field
          values with each file name, disregarding the file extension. This
          allows multiple files with various file extensions to match a single
          record in the input dataset. For example, a field value ofwill
          match a file named
          lot5986.jpg if the match_pattern parameter value is EXACT.
          lot5986
      in_file_filter {String}:
          A data filter that will be used to limit the files considered for
          matching.Wild cards (*) can be used for more flexible filtering
          options.
          Multiple filters delimited by semicolons are also supported.For
          example, you have an input directory with a variety of file types.
          To limit the possible matches to only .jpg files, , use a value of
          *.jpg. To limit the possible matches to only .pdf and .doc files, use
          a value of *.pdf; *.doc.To limit possible matches to only file names
          that contain the text
          arc, use a value of *arc*.
      in_use_relative_paths {Boolean}:
          Specifies whether the output match table fieldwill contain
          full paths or only the file names. FILENAMERELATIVE-The field
          will contain only the file names (relative paths).
          This is the default.ABSOLUTE-The field will contain full paths.
      match_pattern {String}:
          Specifies the type of match pattern that will be used to match file
          names with the specified key_field parameter value.EXACT-File names
          that are an exact match to the values in the key
          field will be matched. This is the default.PREFIX-File names that have
          the key field value at the beginning of
          the file name will be matched.SUFFIX-File names that have the key
          field value at the end of the file
          name will be matched.ANY-File names that have the key field value
          anywhere in the file name
          will be matched.

     OUTPUTS:
      out_match_table (Table):
          The output match table with theandfields.
          MATCHIDFILENAME

        """