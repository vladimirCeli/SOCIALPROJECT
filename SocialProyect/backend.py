from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'vcdjango' # <storage_account_name>
    account_key = 'HIpxtFjB/t3+2zc72Qqtzpns8AiLi0TFOe1U0xleZQFNQegSn3alJLYHWxKYAxC+vjEQRjKOC2f1U9KRDue8CQ==' # <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'vcdjango' # <storage_account_name>
    account_key = 'WthYsDJ3d+NvOyEwt4FHDYzCXgTWa7GNHleKr76G0a1u56ZEQCYtmqoeKeE8zTIqQoN1gmSNmPb+V9RzhU4kcw==' # <storage_account_key>
    azure_container = 'static'
    expiration_secs = None