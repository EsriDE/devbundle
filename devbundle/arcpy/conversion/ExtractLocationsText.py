# Generated documentation for module arcpy.conversion


class ExtractLocationsText(object):
    """
    Analyzes input text or a text file and extracts locations to a point feature class
    """

    @property
    def description(self) -> str:
        return """

        ExtractLocationsText_conversion(in_text, out_feature_class, {in_template}, {coord_dd_latlon}, {coord_dd_xydeg}, {coord_dd_xyplain}, {coord_dm_latlon}, {coord_dm_xymin}, {coord_dms_latlon}, {coord_dms_xysec}, {coord_dms_xysep}, {coord_utm}, {coord_ups_north}, {coord_ups_south}, {coord_mgrs}, {coord_mgrs_northpolar}, {coord_mgrs_southpolar}, {comma_decimal}, {coord_use_lonlat}, {in_coor_system}, {in_custom_locations}, {fuzzy_match}, {max_features_extracted}, {ignore_first_features}, {date_monthname}, {date_m_d_y}, {date_yyyymmdd}, {date_yymmdd}, {date_yyjjj}, {max_dates_extracted}, {ignore_first_dates}, {date_range_begin}, {date_range_end}, {in_custom_attributes}, {file_link}, {file_mod_datetime}, {pre_text_length}, {post_text_length}, {std_coord_fmt}, {req_word_breaks})

        Analyzes input text or a text file and extracts locations to a point
        feature class

     INPUTS:
      in_text (String):
          The text that will be scanned for locations (coordinates or custom
          locations), dates, and custom attributes; or text defining a file
          path, whose contents will be scanned for locations. For geoprocessing
          services, when a file path is provided, the file must be accessible
          from the service, as the file is not transferred to the server.
      in_template {File}:
          The template file (*.lxttmpl) that determines the setting to use for
          each tool parameter. When a template file is provided, all values
          specified for other parameters will be ignored except those that
          determine the input content that will be processed and the output
          feature class. Some settings that are available in thepane are
          only available
          to this tool when the settings are saved to a template file, and the
          template file is referenced in this parameter. These settings are as
          follows:        Extract LocationsSpatial coordinates in x,y
          format-Allows two sequential numbers such
          as 630084 4833438 or 981075.652ftUS 607151.272ftUS to be recognized as
          coordinates when they are valid for a planar coordinate system
          associated with the input documents. You can specify whether numbers
          with and without units are recognized or only numbers with units of
          measure are recognized as coordinates.Custom coordinate and date
          formats-Allows you to customize how text is
          recognized as a spatial coordinate or a date, particularly when
          written in a language other than English or using a format that is not
          common in the United States. For example, a spatial coordinate written
          as 30 20 10 N x 060 50 40 W can be recognized with a customization to
          recognize the character x as valid text between the latitude and
          longitude. Coordinates and dates such as 60.91°N, 147.34°O and 17
          juillet, 2018 can be recognized when customizations are specified to
          accommodate the language of the documents, in this case French. Also,
          when two-digit years are used, you can control the range of years to
          which they are matched.Preferences for some ambiguous dates-Dates such
          as 10/12/2019 are
          ambiguous because they can be interpreted as either October 12, 2019,
          or December 10, 2019. Some countries use the m/d/yy date format as a
          standard, and other countries use the d/m/yy format. A preference can
          be set for how these ambiguous dates are interpreted, either as m/d/yy
          or d/m/yy, to suit the country of origin of the documents.
          Length of fields in the output feature class-You can specify
          the length of the fields containing text surrounding spatial
          coordinates that are extracted from a document using
          the(pre_text_length in Python) and(post_text_length in Python)
          parameters. Thepane allows you to control the length of several
          additional fields in the attribute table, including fields containing
          dates extracted from the document, the original text that was
          converted to dates, the file name from which the information was
          extracted, and so on. Pre-Text Field LengthPost-Text Field
          LengthExtract Locations
      coord_dd_latlon {Boolean}:
          Specifies whether to search for coordinates stored as decimal degrees
          formatted as latitude and longitude (infrequent false positives).
          Examples are: 33.8N 77.035W and W77N38.88909.FIND_DD_LATLON-The tool
          will search for decimal degrees coordinates
          formatted as latitude and longitude. This is the
          default.DONT_FIND_DD_LATLON-The tool will not search for decimal
          degrees
          coordinates formatted as latitude and longitude.
      coord_dd_xydeg {Boolean}:
          Specifies whether to search for coordinates stored as decimal degrees
          formatted as X Y with degree symbols (infrequent false positives).
          Examples are: 38.8° -77.035° and -077d+38.88909d.FIND_DD_XYDEG-The
          tool will search for decimal degrees coordinates
          formatted as X Y with degree symbols. This is the
          default.DONT_FIND_DD_XYDEG-The tool will not search for decimal
          degrees
          coordinates formatted as X Y with degree symbols.
      coord_dd_xyplain {Boolean}:
          Specifies whether to search for coordinates stored as decimal degrees
          formatted as X Y with no symbols (frequent false positives). Examples
          are: 38.8 -77.035 and -077.0, +38.88909.FIND_DD_XYPLAIN-The tool will
          search for decimal degrees coordinates
          formatted as X Y with no symbols (frequent false positives). This is
          the default.DONT_FIND_DD_XYPLAIN-The tool will not search for decimal
          degrees
          coordinates formatted as X Y with no symbols.
      coord_dm_latlon {Boolean}:
          Specifies whether to search for coordinates stored as degrees decimal
          minutes formatted as latitude and longitude (infrequent false
          positives). Examples are: 3853.3N 7702.100W and
          W7702N3853.3458.FIND_DM_LATLON-The tool will search for degrees
          decimal minutes
          coordinates formatted as latitude and longitude. This is the
          default.DONT_FIND_DM_LATLON-The tool will not search for degrees
          decimal
          minutes coordinates formatted as latitude and longitude.
      coord_dm_xymin {Boolean}:
          Specifies whether to search for coordinates stored as degrees decimal
          minutes formatted as X Y with minutes symbols (infrequent false
          positives). Examples are: 3853' -7702.1' and
          -07702m+3853.3458m.FIND_DM_XYMIN-The tool will search for degrees
          decimal minutes
          coordinates formatted as X Y with minutes symbols. This is the
          default.DONT_FIND_DM_XYMIN-The tool will not search for degrees
          decimal
          minutes coordinates formatted as X Y with minutes symbols.
      coord_dms_latlon {Boolean}:
          Specifies whether to search for coordinates stored as degrees minutes
          seconds formatted as latitude and longitude (infrequent false
          positives). Examples are: 385320.7N 770206.000W and
          W770206N385320.76.FIND_DMS_LATLON-The tool will search for degrees
          minutes seconds
          coordinates formatted as latitude and longitude. This is the
          default.DONT_FIND_DMS_LATLON-The tool will not search for degrees
          minutes
          seconds coordinates formatted as latitude and longitude.
      coord_dms_xysec {Boolean}:
          Specifies whether to search for coordinates stored as degrees minutes
          seconds formatted as X Y with seconds symbols (infrequent false
          positives). Examples are: 385320" -770206.0" and
          -0770206.0s+385320.76s.FIND_DMS_XYSEC-The tool will search for degrees
          minutes seconds
          coordinates formatted as X Y with seconds symbols. This is the
          default.DONT_FIND_DMS_XYSEC-The tool will not search for degrees
          minutes
          seconds coordinates formatted as X Y with seconds symbols.
      coord_dms_xysep {Boolean}:
          Specifies whether to search for coordinates stored as degrees minutes
          seconds formatted as X Y with separators (moderate false positives).
          Examples are: 8:53:20 -77:2:6.0 and
          -077/02/06/+38/53/20.76.FIND_DMS_XYSEP-The tool will search for
          degrees minutes seconds
          coordinates formatted as X Y with separators. This is the
          default.DONT_FIND_DMS_XYSEP-The tool will not search for degrees
          minutes
          seconds coordinates formatted as X Y with separators.
      coord_utm {Boolean}:
          Specifies whether to search for Universal Transverse Mercator (UTM)
          coordinates (infrequent false positives). Examples are: 18S 323503
          4306438 and 18 north 323503.25 4306438.39.FIND_UTM_MAINWORLD-The tool
          will search for UTM coordinates. This is
          the default.DONT_FIND_UTM_MAINWORLD-The tool will not search for UTM
          coordinates.
      coord_ups_north {Boolean}:
          Specifies whether to search for Universal Polar Stereographic (UPS)
          coordinates in the north polar area (infrequent false positives).
          Examples are: Y 2722399 2000000 and north 2722399
          2000000.FIND_UTM_NORTHPOLAR-The tool will search for UPS coordinates
          in the
          north polar area. This is the default.DONT_FIND_UTM_NORTHPOLAR-The
          tool will not search for UPS coordinates
          in the north polar area.
      coord_ups_south {Boolean}:
          Specifies whether to search for Universal Polar Stereographic (UPS)
          coordinates in the south polar area (infrequent false positives).
          Examples are: A 2000000 3168892 and south 2000000
          3168892.FIND_UTM_SOUTHPOLAR-The tool will search for UPS coordinates
          in the
          south polar area. This is the default.DONT_FIND_UTM_SOUTHPOLAR-The
          tool will not search for UPS coordinates
          in the south polar area.
      coord_mgrs {Boolean}:
          Specifies whether to search for Military Grid Reference System (MGRS)
          coordinates (infrequent false positives). Examples are: 18S UJ 13503
          06438 and 18SUJ0306.FIND_MGRS_MAINWORLD-The tool will search for MGRS
          coordinates. This is
          the default.DONT_FIND_MGRS_MAINWORLD-The tool will not search for MGRS
          coordinates.
      coord_mgrs_northpolar {Boolean}:
          Specifies whether to search for Military Grid Reference System (MGRS)
          coordinates in the north polar area (infrequent false positives).
          Examples are: Y TG 56814 69009 and YTG5669.FIND_MGRS_NORTHPOLAR-The
          tool will search for MGRS coordinates in the
          north polar area. This is the default.DONT_FIND_MGRS_NORTHPOLAR-The
          tool will not search for MGRS
          coordinates in the north polar area.
      coord_mgrs_southpolar {Boolean}:
          Specifies whether to search for Military Grid Reference System (MGRS)
          coordinates in the south polar area (moderate false positives).
          Examples are: A TN 56814 30991 and ATN5630.FIND_MGRS_SOUTHPOLAR-The
          tool will search for MGRS coordinates in the
          south polar area. This is the default.DONT_FIND_MGRS_SOUTHPOLAR-The
          tool will not search for MGRS
          coordinates in the south polar area.
      comma_decimal {Boolean}:
          Specifies whether a comma (,) will be recognized as a decimal
          separator. By default, content is scanned for spatial coordinates
          defined by numbers that use a period (.) or a middle dot (·) as the
          decimal separator, for example: Lat 01° 10·80' N Long 103° 28·60' E.
          If you are working with content in which spatial coordinates are
          defined by numbers that use a comma (,) as the decimal separator, for
          example: 52° 8′ 32,14″ N; 5° 24′ 56,09″ E, set this parameter to
          recognize a comma as the decimal separator instead. This parameter is
          not set automatically based on the regional setting for your
          computer's operating system.USE_COMMA_DECIMAL_MARK-A comma will be
          recognized as the decimal
          separator.USE_DOT_DECIMAL_MARK-A period or a middle dot will be
          recognized as
          the decimal separator. This is the default.
      coord_use_lonlat {Boolean}:
          When numbers resemble x,y coordinates, both numbers are less than 90,
          and there are no symbols or notations to indicate which number
          represents the latitude or longitude, results can be ambiguous.
          Interpret the numbers as a longitude-latitude coordinate (x,y) instead
          of a latitude-longitude coordinate (y,x).PREFER_LONLAT-x,y coordinates
          will be interpreted as longitude-
          latitude.PREFER_LATLON-x,y coordinates will be interpreted as
          latitude-
          longitude. This is the default.
      in_coor_system {Spatial Reference}:
          The coordinate system that will be used to interpret the spatial
          coordinates defined in the input. GCS-WGS-84 is the default.
      in_custom_locations {File}:
          The custom location file (.lxtgaz) that will be used when scanning the
          input content. A point is created to represent each occurrence of each
          place name in the custom location file up to the limits established by
          other tool parameters.
      fuzzy_match {Boolean}:
          Specifies whether fuzzy matching will be used for searching the custom
          location file.USE_FUZZY-Fuzzy matching will be used when searching the
          custom
          location file.DONT_USE_FUZZY-Exact matching will be used when
          searching the custom
          location file. This is the default.
      max_features_extracted {Long}:
          The maximum number of features that can be extracted. The tool will
          stop scanning the input content for locations when the maximum number
          is reached. When running as a geoprocessing service, the service and
          the server may have separate limits on the number of features allowed.
      ignore_first_features {Long}:
          The number of features detected and ignored before extracting all
          other features. This parameter can be used to focus the search on a
          specific portion of the data.
      date_monthname {Boolean}:
          Specifies whether to search for dates in which the month name appears
          (infrequent false positives). 12 May 2003 and January 15, 1997 are
          examples.FIND_DATE_MONTHNAME-The tool will search for dates in which
          the month
          name appears. This is the default.DONT_FIND_DATE_MONTHNAME-The tool
          will not search for dates in which
          the month name appears.
      date_m_d_y {Boolean}:
          Specifies whether to search for dates in which numbers are in the
          M/D/Y or D/M/Y format (moderate false positives). 5/12/03 and
          1-15-1997 are examples.FIND_DATE_M_D_Y-The tool will search for dates
          in which numbers are in
          the M/D/Y or D/M/Y format (moderate false positives). This is the
          default.DONT_FIND_DATE_M_D_Y-The tool will not search for dates in
          which
          numbers are in the M/D/Y or D/M/Y format.
      date_yyyymmdd {Boolean}:
          Specifies whether to search for dates in which numbers are in the
          YYYYMMDD format (moderate false positives). 20030512 and 19970115 are
          examples.FIND_DATE_YYYYMMDD-The tool will search for dates in which
          numbers are
          in the YYYYMMDD format (moderate false positives). This is the
          default.DONT_FIND_DATE_YYYYMMDD-The tool will not search for dates in
          which
          numbers are in the YYYYMMDD format.
      date_yymmdd {Boolean}:
          Specifies whether to search for dates in which numbers are in the
          YYMMDD format (frequent false positives). 030512 and 970115 are
          examples.FIND_DATE_YYMMDD-The tool will search for dates in which
          numbers are
          in the YYMMDD format (frequent false positives). This is the
          default.DONT_FIND_DATE_YYMMDD-The tool will not search for dates in
          which
          numbers are in the YYMMDD format.
      date_yyjjj {Boolean}:
          Specifies whether to search for dates in which numbers are in the
          YYJJJ or YYYYJJJ format (frequent false positives). 03132 and 97015
          are examples.FIND_DATE_YYJJJ-The tool will search for dates in which
          numbers are in
          the YYJJJ or YYYYJJJ format (frequent false positives). This is the
          default.DONT_FIND_DATE_YYJJJ-The tool will not search for dates in
          which
          numbers are in the YYJJJ or YYYYJJJ format.
      max_dates_extracted {Long}:
          The maximum number of dates that will be extracted.
      ignore_first_dates {Long}:
          The number of dates that will be detected and ignored before
          extracting all other dates.
      date_range_begin {Date}:
          The earliest acceptable date to extract. Detected dates matching this
          value or later will be extracted.
      date_range_end {Date}:
          The latest acceptable date to extract. Detected dates matching this
          value or earlier will be extracted.
      in_custom_attributes {File}:
          The custom attribute file (.lxtca) that will be used to scan the input
          content. Fields will be created in the output feature class's
          attribute table for all custom attributes defined in the file. When
          the input content is scanned, it will be examined to see if it
          contains text associated with all custom attributes specified in the
          file. When a match is found, the appropriate text is extracted from
          the input content and stored in the appropriate field.
      file_link {String}:
          The file path that will be used as the file name in the output
          data when theparameter (in_file in Python) is transferred to the
          server. If this parameter is not specified, the path of thewill be
          used, which may be an unreachable folder on a server. This parameter
          has no effect when theis not specified. Input FileInput
          FileInput File
      file_mod_datetime {Date}:
          The UTC date and time that the file was modified will be used
          as the modified attribute in the output data when theparameter
          (in_file in Python) is transferred to the server. If this parameter is
          not specified, the current modified time of the input file will be
          used. This parameter has no effect when theis not specified.
          Input FileInput File
      pre_text_length {Long}:
          Content is extracted from the input document to provide
          context for the location that was found. This parameter defines the
          maximum number of characters that will be extracted preceding the text
          that defines the location. The extracted text is stored in thefield in
          the output feature class's attribute table. The default is 254.
          Thefield's data type will also have this length. The length of a text
          field in a shapefile is limited to 254 characters; when the output is
          a shapefile, a larger number of characters will be truncated to 254.
          Pre-TextPre-Text
      post_text_length {Long}:
          Content is extracted from the input document to provide
          context for the location that was found. This parameter defines the
          maximum number of characters that will be extracted following the text
          that defines the location. The extracted text is stored in thefield in
          the output feature class's attribute table. The default is 254.
          Thefield's data type will also have this length. The length of a text
          field in a shapefile is limited to 254 characters; when the output is
          a shapefile, a larger number of characters will be truncated to 254.
          Post-TextPost-Text
      std_coord_fmt {String}:
          Specifies the coordinate format that will be used to store the
          coordinate location. A standard representation of the spatial
          coordinate that defines the point feature is recorded in a field in
          the attribute table.STD_COORD_FMT_DD-The coordinate location is
          recorded in decimal
          degrees format. This is the default.STD_COORD_FMT_DM-The coordinate
          location is recorded in degrees
          decimal minutes format.STD_COORD_FMT_DMS-The coordinate location is
          recorded in degrees
          minutes seconds format.STD_COORD_FMT_UTM-The coordinate location is
          recorded in Universal
          Transverse Mercator format.STD_COORD_FMT_MGRS-The coordinate location
          is recorded in Military
          Grid Reference System format.
      req_word_breaks {Boolean}:
          Specifies whether to search for text using word breaks. A word break
          occurs when words (text) are bounded by whitespace or punctuation
          characters as in European languages.This setting can produce frequent
          false positives or infrequent false
          positives depending on the language of the text. For example, when
          word breaks are not required, the English text Bernard will produce a
          match against the text San Bernardino, which would likely be
          considered a false positive. However, when text is written using a
          language that does not use word breaks, you cannot find words if word
          breaks are required. For example, with the text I flew to Tokyo in
          Japanese, 私は東京に飛んで, you would only be able to find the word Tokyo, 東京,
          when word breaks are not required.REQ_WORD_BREAKS-The tool will search
          for words that are bounded by
          whitespace or punctuation characters. This is the
          default.DONT_REQ_WORD_BREAKS-The tool will not search for words that
          are
          bounded by whitespace or punctuation characters.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing point features that represent the
          locations that were found.

        """