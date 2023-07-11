from langflow.template import frontend_node

# These should always be instantiated
CUSTOM_NODES = {
    "prompts": {
        "ZeroShotPrompt": frontend_node.prompts.ZeroShotPromptNode(),
        "CustomPrompt": frontend_node.prompts.CustomPromptNode(),
        "CustomPrompt2": frontend_node.prompts.CustomPromptNode2(),
    },
    "tools": {
        "PythonFunctionTool": frontend_node.tools.PythonFunctionToolNode(),
        "PythonFunction": frontend_node.tools.PythonFunctionNode(),
        "Tool": frontend_node.tools.ToolNode(),
        "InnerAlgo": frontend_node.tools.InnerAlgo(),
        "MappingTool": frontend_node.tools.MappingTool(),
    },
    "agents": {
        "JsonAgent": frontend_node.agents.JsonAgentNode(),
        "CSVAgent": frontend_node.agents.CSVAgentNode(),
        "AgentInitializer": frontend_node.agents.InitializeAgentNode(),
        "VectorStoreAgent": frontend_node.agents.VectorStoreAgentNode(),
        "VectorStoreRouterAgent": frontend_node.agents.VectorStoreRouterAgentNode(),
        "SQLAgent": frontend_node.agents.SQLAgentNode(),
    },
    "utilities": {
        "SQLDatabase": frontend_node.agents.SQLDatabaseNode(),
    },
    "chains": {
        "SeriesCharacterChain": frontend_node.chains.SeriesCharacterChainNode(),
        "TimeTravelGuideChain": frontend_node.chains.TimeTravelGuideChainNode(),
        "MidJourneyPromptChain": frontend_node.chains.MidJourneyPromptChainNode(),
        "load_qa_chain": frontend_node.chains.CombineDocsChainNode(),
    },
}


def get_custom_nodes(node_type: str):
    """Get custom nodes."""
    return CUSTOM_NODES.get(node_type, {})
