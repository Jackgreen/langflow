from langflow.interface.document_loaders.custom import CommonFileLoader

CUSTOM_LOADERS = {"CommonFileLoader": CommonFileLoader}

ALL_TOOLS_NAMES = {
    **CUSTOM_LOADERS,
}
