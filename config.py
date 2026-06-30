from enum import Enum
VICUNA_PATH = "/home/pchao/vicuna-13b-v1.5"
LLAMA_PATH = "/home/pchao/Llama-2-7b-chat-hf"

ATTACK_TEMP = 1
TARGET_TEMP = 0
ATTACK_TOP_P = 0.9
TARGET_TOP_P = 1


## MODEL PARAMETERS ##
class Model(Enum):
    vicuna = "vicuna-13b-v1.5"
    llama_2 = "llama-2-7b-chat-hf"
    gpt_3_5 = "gpt-3.5-turbo-1106"
    gpt_4 = "gpt-4-0125-preview"
    claude_1 = "claude-instant-1.2"
    claude_2 = "claude-2.1"
    gemini = "gemini-2.5-flash-lite"  
    mixtral = "mixtral"

MODEL_NAMES = [model.value for model in Model]


HF_MODEL_NAMES: dict[Model, str] = {
    Model.llama_2: "meta-llama/Llama-2-7b-chat-hf",
    Model.vicuna: "lmsys/vicuna-13b-v1.5",
    Model.mixtral: "mistralai/Mixtral-8x7B-Instruct-v0.1"
}

TOGETHER_MODEL_NAMES: dict[Model, str] = {
    Model.llama_2: "together_ai/togethercomputer/llama-2-7b-chat",
    Model.vicuna: "together_ai/lmsys/vicuna-13b-v1.5",
    Model.mixtral: "together_ai/mistralai/Mixtral-8x7B-Instruct-v0.1"
}

FASTCHAT_TEMPLATE_NAMES: dict[Model, str] = {
    Model.gpt_3_5: "gpt-3.5-turbo",
    Model.gpt_4: "gpt-4",
    Model.claude_1: "claude-instant-1.2",
    Model.claude_2: "claude-2.1",
    Model.gemini: "gemini-pro",
    Model.vicuna: "vicuna_v1.1",
    Model.llama_2: "llama-2-7b-chat-hf",
    Model.mixtral: "mixtral",
}

API_KEY_NAMES: dict[Model, str] = {
    Model.gpt_3_5:  "OPENAI_API_KEY",
    Model.gpt_4:    "OPENAI_API_KEY",
    Model.claude_1: "ANTHROPIC_API_KEY",
    Model.claude_2: "ANTHROPIC_API_KEY",
    Model.gemini:   "GEMINI_API_KEY",
    Model.vicuna:   "TOGETHER_API_KEY",
    Model.llama_2:  "TOGETHER_API_KEY",
    Model.mixtral:  "TOGETHER_API_KEY",
}

## CUSTOM OPENAI-COMPATIBLE PROVIDERS (DaiSec, KISSKI) ##
DAISEC_BASE_URL = "https://chat.daisec.eu/ollama/v1"
DAISEC_API_KEY_ENV = "DAISEC_APIKEY"
DAISEC_MODELS = [
    "qwen3:30b", "llama4:scout", "deepseek-r1:32b", "gpt-oss:20b",
    "llama3:70b", "gemma3:27b", "openthinker:32b", "qwen3-next:80b",
]

KISSKI_BASE_URL = "https://chat-ai.academiccloud.de/v1/"
KISSKI_API_KEY_ENV = "KISSKI_APIKEY"
KISSKI_MODELS = [
    "qwen3-coder-30b-a3b-instruct", "glm-4.7", "qwen3.6-35b-a3b",
    "apertus-70b-instruct-2509", "qwen3-omni-30b-a3b-instruct",
    "devstral-2-123b-instruct-2512", "internvl3.5-30b-a3b", "qwen3.5-122b-a10b",
    "qwen3.5-397b-a17b", "gemma-4-31b-it", "mistral-large-3-675b-instruct-2512",
    "meta-llama-3.1-8b-instruct", "openai-gpt-oss-120b",
    "qwen3-30b-a3b-instruct-2507", "medgemma-27b-it",
    "deepseek-r1-distill-llama-70b", "teuken-7b-instruct-research",
]

CUSTOM_PROVIDER_MODELS: dict[str, dict] = {}
for _m in DAISEC_MODELS:
    CUSTOM_PROVIDER_MODELS[_m] = {"api_base": DAISEC_BASE_URL, "api_key_env": DAISEC_API_KEY_ENV}
for _m in KISSKI_MODELS:
    CUSTOM_PROVIDER_MODELS[_m] = {"api_base": KISSKI_BASE_URL, "api_key_env": KISSKI_API_KEY_ENV}


def is_custom_provider_model(model_name: str) -> bool:
    return model_name in CUSTOM_PROVIDER_MODELS


LITELLM_TEMPLATES: dict[Model, dict] = {
    Model.vicuna: {"roles":{
                    "system": {"pre_message": "", "post_message": " "},
                    "user": {"pre_message": "USER: ", "post_message": " ASSISTANT:"},
                    "assistant": {
                        "pre_message": "",
                        "post_message": "",
                    },
                },
                "post_message":"</s>",
                "initial_prompt_value" : "",
                "eos_tokens": ["</s>"]         
                },
    Model.llama_2: {"roles":{
                    "system": {"pre_message": "[INST] <<SYS>>\n", "post_message": "\n<</SYS>>\n\n"},
                    "user": {"pre_message": "", "post_message": " [/INST]"},
                    "assistant": {"pre_message": "", "post_message": ""},
                },
                "post_message" : " </s><s>",
                "initial_prompt_value" : "",
                "eos_tokens" :  ["</s>", "[/INST]"]  
            },
    Model.mixtral: {"roles":{
                    "system": {
                        "pre_message": "[INST] ",
                        "post_message": " [/INST]"
                    },
                    "user": { 
                        "pre_message": "[INST] ",
                        "post_message": " [/INST]"
                    }, 
                    "assistant": {
                        "pre_message": " ",
                        "post_message": "",
                    }
                },
                "post_message": "</s>",
                "initial_prompt_value" : "<s>",
                "eos_tokens": ["</s>", "[/INST]"]
    }
}