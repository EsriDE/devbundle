# Generated documentation for module arcpy.management


class UploadFileToPortal(object):
    """
    Uploads a file to the active portal. Supported file types are .lyrx, .mapx, .pagx, .pdf, .rptt, .rptx, and .stylx.
    """

    @property
    def description(self) -> str:
        return """

        UploadFileToPortal_management(in_file, title, {folder}, {summary}, {tags}, {sharing_level}, {groups;groups...})

        Uploads a file to the active portal. Supported file types are .lyrx,
        .mapx, .pagx, .pdf, .rptt, .rptx, and .stylx.

     INPUTS:
      in_file (File):
          The file that will be uploaded to the active portal. Supported file
          types are layer (.lyrx), layout (.pagx), map (.mapx), PDF (.pdf),
          report (.rptx), report template (.rptt), and style (.stylx).
      title (String):
          The title of the portal item.
      folder {String}:
          The name of an existing folder or a new folder on the portal.
      summary {String}:
          A short description of the item.
      tags {String}:
          The keywords or terms that describe the item. Separate individual tags
          with a comma.
      sharing_level {String}:
          Specifies the sharing level of the item.OWNER-Only the owner of the
          item will have access.ORGANIZATION-All
          members of the organization will have accessEVERYONE-Everyone,
          including people outside the organization, will
          have access
      groups {String}:
          The groups with which the item will be shared.

        """