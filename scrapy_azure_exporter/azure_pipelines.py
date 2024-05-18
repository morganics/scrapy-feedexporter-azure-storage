from scrapy_azure_exporter.azure_store import AzureFilesStore
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline


class AzurePipelineMixin:
    @classmethod
    def from_settings(cls, settings):
        // upstream from_settings need the 'azure' key to be available
        cls.STORE_SCHEMES.update(
            {
                "azure": AzureFilesStore.new(settings),
                "azurite": AzureFilesStore.new(settings),
            }
        )
        
        pipeline = super().from_settings(settings)
        return pipeline


class AzureFilesPipeline(AzurePipelineMixin, FilesPipeline):
    pass


class AzureImagesPipeline(AzurePipelineMixin, ImagesPipeline):
    pass
