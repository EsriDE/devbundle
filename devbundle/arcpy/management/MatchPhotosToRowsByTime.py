# Generated documentation for module arcpy.management


class MatchPhotosToRowsByTime(object):
    """
    Matches photo files to table or feature class rows according to the photo and row time stamps. The row with the time stamp closest to the capture time of a photo will be matched to that photo. A new table is created that contains the object ID values from the input rows and their matching photo paths. You can also use this tool to add matching photo files to the rows of the input table as geodatabase attachments.
    """

    @property
    def description(self) -> str:
        return """

        MatchPhotosToRowsByTime_management(Input_Folder, Input_Table, Time_Field, Output_Table, {Unmatched_Photos_Table}, {Add_Photos_As_Attachments}, {Time_Tolerance}, {Clock_Offset})

        Matches photo files to table or feature class rows according to the
        photo and row time stamps. The row with the time stamp closest to the
        capture time of a photo will be matched to that photo. A new table is
        created that contains the object ID values from the input rows and
        their matching photo paths. You can also use this tool to add matching
        photo files to the rows of the input table as geodatabase attachments.

     INPUTS:
      Input_Folder (Folder):
          The folder where photo files (.jpg or .tif) are located. This folder
          is scanned recursively for photo files; any photos in the base level
          of the folder, as well as in any subfolders, will be added to the
          output.
      Input_Table (Table View):
          The table or feature class whose rows will be matched with photo
          files. The input table will typically be a point feature class
          representing GPS recordings.
      Time_Field (Field):
          The date field from the input table that indicates when each row was
          captured or created. The field must be of type date; it cannot be of
          type string or numeric.
      Add_Photos_As_Attachments {Boolean}:
          Specifies whether the photo files will be added to the rows of the
          input table as geodatabase attachments.Adding attachments requires
          that the output feature class be in a
          version 10 or later geodatabase.ADD_ATTACHMENTS-Photo files will be
          added to the rows of the input
          table as geodatabase attachments. Geodatabase attachments are copied
          internally to the geodatabase. This is the default.NO_ATTACHMENTS-
          Photo files will not be added to the rows of the input
          table as geodatabase attachments.
      Time_Tolerance {Double}:
          The maximum difference (in seconds) between the date/time of an input
          row and a photo file that will be matched. If an input row and a photo
          file have time stamps that are different by more than this tolerance,
          no match will occur. To match a photo file to a row with the closest
          time stamp, regardless of how large the date/time difference might be,
          set the tolerance to 0. The sign of this value (- or +) is irrelevant;
          the absolute value of the number specified will be used. Do not
          use this parameter to adjust for consistent shifts or
          offsets between the times recorded by the GPS and the digital camera.
          Use theparameter or the Convert Time Zone tool to shift the time
          stamps of the input rows to match those of the photos. Clock
          Offset
      Clock_Offset {Double}:
          The difference (in seconds) between the internal clock of the digital
          camera used to capture the photos and the GPS unit. If the clock of
          the digital camera is behind the clock of the GPS unit, use a positive
          value; if the clock of the digital camera is ahead of the clock of the
          GPS unit, use a negative value. For example, if a photo with a
          time stamp of 11:35:17 should
          match a row with a time stamp of 11:35:32, use avalue of 15.
          Clock Offset

     OUTPUTS:
      Output_Table (Table):
          The output table containing the object ID values from the input table
          that match a photo, and the matching photo path. Only object ID values
          from the input table that match a photo are included in the output
          table.
      Unmatched_Photos_Table {Table}:
          The optional output table that will list any photo files in the input
          folder with an invalid time stamp or any photos that cannot be matched
          because there is no input row within the time tolerance.If no path is
          specified, this table will not be created.

        """