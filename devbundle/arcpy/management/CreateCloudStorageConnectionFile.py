# Generated documentation for module arcpy.management


class CreateCloudStorageConnectionFile(object):
    """
    Creates a connection file for ArcGIS-supported cloud storage. This tool allows existing raster geoprocessing tools to write cloud raster format (CRF) datasets into the cloud storage bucket or read raster datasets (not limited to CRF) stored in the cloud storage as input.
    """

    @property
    def description(self) -> str:
        return """

        CreateCloudStorageConnectionFile_management(out_folder_path, out_name, service_provider, bucket_name, {access_key_id}, {secret_access_key}, {region}, {end_point}, {config_options;config_options...}, {folder}, {authentication})

        Creates a connection file for ArcGIS-supported cloud storage. This
        tool allows existing raster geoprocessing tools to write cloud raster
        format (CRF) datasets into the cloud storage bucket or read raster
        datasets (not limited to CRF) stored in the cloud storage as input.

     INPUTS:
      out_folder_path (Folder):
          The folder path where the connection file will be created.
      out_name (String):
          The name of the cloud storage connection file.
      service_provider (String):
          Specifies the cloud storage service provider that will be
          used.AZURE-The service provider will be Microsoft Azure.AMAZON-The
          service
          provider will be Amazon S3.GOOGLE-The service provider will be Google
          Cloud Storage.ALIBABA-The service provider will be Alibaba Cloud
          Storage.WEBHDFS-The service provider will be WebHDFS.MINIO-The service
          provider will be MinIO.AZUREDATALAKE-The service provider will be
          Microsoft Azure Data Lake
          Storage.OZONE-The service provider will be Ozone.
      bucket_name (String):
          The name of the cloud storage container where the raster dataset will
          be stored. Many cloud providers also call it a bucket.
      access_key_id {String}:
          The access key ID string for the specific cloud storage type. It can
          also be the account name, as is the case with Azure.
      secret_access_key {Encrypted String}:
          The secret access key string to authenticate the connection to cloud
          storage.
      region {String}:
          The region string for the cloud storage. If provided, the value must
          use the format defined by the cloud storage choice. The default is the
          selected cloud provider's default account.
      end_point {String}:
          The service endpoint (URI) of the cloud storage, such as oss-us-
          west-1.aliyuncs.com. If no value is provided, the default endpoint for
          the selected cloud storage type will be used. The CNAME redirected
          endpoint can also be used if needed.
      config_options {Value Table}:
          The configuration options pertaining to the specific type of cloud
          service. Some services offer options, some do not. You only need to
          set this parameter if you want to turn on the options. Azure
          and Microsoft Azure Data Lake Storage
          AZURE_STORAGE_SAS_TOKEN-Specify a shared access signature.
          Ensure that its value is URL encoded and does not contain leading '?'
          or '&' characters. When using this option, theparameter must be empty.
          Secret Access Key (Account Key)
          AZURE_NO_SIGN_REQUEST-Anonymously connect to buckets
          (containers) that don't require authenticated access. When using this
          option, theparameter must be empty. The default value is False
          Secret Access Key (Account Key)
          AZURE_STORAGE_CONNECTION_STRING-Specify an Azure Storage
          connection string. This string embeds the account name, key, and
          endpoint. When using this option, theandparameters must be empty.
          Access Key ID (Account Name)Secret Access Key (Account
          Key)CPL_AZURE_USE_HTTPS-Set to False to use HTTP requests. Some
          servers
          may be configured to only support HTTPS requests. The default value is
          True.AZURE_IMDS_OBJECT_ID-Specify the Object ID of the managed
          identity
          authenticated using Azure Instance Metadata Service (IMDS) if your
          Azure VM has multiple user-assigned managed identities
          set.AZURE_IMDS_CLIENT_ID-Specify the Client ID of the managed identity
          authenticated using Azure Instance Metadata Service (IMDS) if your
          Azure VM has multiple user-assigned managed identities
          set.AZURE_IMDS_MSI_RES_ID-Specify the Resource ID of the managed
          identity
          authenticated using Azure Instance Metadata Service (IMDS) if your
          Azure VM has multiple user-assigned managed identities set.
          Amazon and MinIO         AWS_NO_SIGN_REQUEST-Anonymously
          connect to buckets (containers) that
          don't require authenticated access. The default value is
          False.AWS_SESSION_TOKEN-Specify temporary
          credentials.AWS_DEFAULT_PROFILE-AWS credential profiles are
          automatically used
          when the access key or ID is missing. This option can be used to
          specify the profile to use.AWS_REQUEST_PAYER-Requester Pays buckets
          can be accessed by setting
          this option to requester.AWS_Virtual_Hosting-If you use Amazon S3 or
          S3-compatible cloud
          providers that support only path-style requests, set this option to
          True. It is recommended that you use virtual hosting if it's
          supported. The default value is
          True.CPL_VSIS3_USE_BASE_RMDIR_RECURSIVE-Some older S3-compatible
          implementations do not support the Bulk Delete operation. Set this
          option to False for these providers. The default value is
          True.AWS_HTTPS-Set to False to use HTTP requests. Some servers may be
          configured to only support HTTPS requests. The default value is True.
          Google         GS_NO_SIGN_REQUEST-Anonymously connect to
          buckets (containers) that do
          not require authenticated access. The default value is
          TrueGS_USER_PROJECT-Requester Pays buckets can be accessed by setting
          OAuth2 keys and a project for billing. Set the project using this
          option and set OAuth2 keys using other options and not HMAC keys as a
          secret access key or ID.GS_OAUTH2_REFRESH_TOKEN-Specify OAuth2 Refresh
          Access Token. Set
          OAuth2 client credentials using GS_OAUTH2_CLIENT_ID and
          GS_OAUTH2_CLIENT_SECRET.GOOGLE_APPLICATION_CREDENTIALS-Specify Service
          Account OAuth2
          credentials using a .json file containing a private key and client
          email address.GS_OAUTH2_ PRIVATE_KEY-Specify Service Account OAuth2
          credentials
          using a private key string. GS_AUTH2_CLIENT_EMAIL must be
          set.GS_OAUTH2_ PRIVATE_KEY_FILE-Specify Service Account OAuth2
          credentials
          using a private key from a file. GS_AUTH2_CLIENT_EMAIL must be
          set.GS_AUTH2_CLIENT_EMAIL-Specify Service Account OAuth2 credentials
          using
          a client email address.GS_AUTH2_SCOPE-Specify Service Account OAuth2
          scope. Valid values are
          https://www.googleapis.com/auth/devstorage.read_write (the default)
          and https://www.googleapis.com/auth/devstorage.read_only.GDAL_HTTP_HEA
          DER_FILE-Specify bearer authentication credentials stored
          in an external file. Alibaba         OSS_Virtual_Hosting-If
          you use Alibaba or
          S3-compatible cloud
          providers that support only path-style requests, set this option to
          True. It is recommended that you use virtual hosting if it's
          supported. The default value is True.OSS_HTTPS-Set to False to use
          HTTP requests. Some servers may be
          configured to only support HTTPS requests. The default value is True.
          WebHDFS         WEBHDFS_REPLICATION (integer)-The replication
          value is used when
          creating a fileWEBHDFS_PERMISSION (decimal)-A permission mask is used
          when creating a
          file.If multiple authentication parameters are provided, precedence is
          as
          follows:Azure-AZURE_STORAGE_CONNECTION_STRING, account name or key,
          AZURE_STORAGE_SAS_TOKEN, AZURE_NO_SIGN_REQUEST, or
          RBAC.Amazon-AWS_NO_SIGN_REQUEST, access ID or key or
          AWS_SESSION_TOKEN, AWS
          Credential Profile, or IAM Role.Google-GS_NO_SIGN_REQUEST, access ID
          or key, GDAL_HTTP_HEADER_FILE,
          (GS_OAUTH2_REFRESH_TOKEN or GS_OAUTH2_CLIENT_ID and
          GS_OAUTH2_CLIENT_SECRET), GOOGLE_APPLICATION_CREDENTIALS,
          (GS_OAUTH2_PRIVATE_KEY or GS_OAUTH2_CLIENT_EMAIL),
          (GS_OAUTH2_PRIVATE_KEY_FILE or GS_OAUTH2_CLIENT_EMAIL), or IAM Role.
          Ozone         AWS_DEFAULT_PROFILE-AWS credential profiles are
          automatically used
          when the access key or ID is missing. This option can be used to
          specify the profile to use.AWS_Virtual_Hosting-If you use Amazon S3 or
          S3-compatible cloud
          providers that support only path-style requests, set this option to
          True. It is recommended that you use virtual hosting if it's
          supported. The default value is True.AWS_HTTPS-Set to False to use
          HTTP requests. Some servers may be
          configured to only support HTTPS requests. The default value is
          True.CPL_VSIS3_USE_BASE_RMDIR_RECURSIVE-Some older S3-compatible
          implementations do not support the Bulk Delete operation. Set this
          option to False for these providers. The default value is True.x-amz-
          storage-class-Specify REDUCED_REDUNDANCY for writing to a single
          container ozone as it has a single data node.In addition to the
          provider options listed above, the ARC_DEEP_CRAWL
          option can be used with all the service providers. If True, it is used
          to identify CRFs with no extension and cloud-enabled raster products
          in the cloud. This is operation intensive and it is recommended that
          you set this option to False for faster catalog browsing and crawling.
          The default value is False.Custom token vending services-such as
          Planetary Computer's data
          collection, for example-can be authenticated using the
          ARC_TOKEN_SERVICE_API (URL of the token vendor) and
          ARC_TOKEN_OPTION_NAME (type of token from the service provider)
          provider options.The GDAL_DISABLE_READDIR_ON_OPEN option is available
          with all the
          service providers. To improve the performance of loading cloud-based
          rasters, this option is set to NO by default. If the raster resides in
          a folder that contains more than 30,000 items, set this option to YES.
      folder {String}:
          The folder in the bucket_name parameter value where the raster dataset
          will be stored.
      authentication {String}:
          The connection name of OAuth 2.0 authentication

        """