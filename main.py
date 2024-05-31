import os

import autogen

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

config_list = [
    {
        'model': 'gpt-4',
        'api_key': OPENAI_API_KEY,
    }
]

# create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name='AI assistant',
    llm_config={
        'seed': 42,
        'config_list': config_list,
        'temperature': 0,
    },
)

# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name='user_proxy',
    human_input_mode='NEVER',
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get('content', '')
    .rstrip()
    .endswith('TERMINATE'),
    code_execution_config={
        'work_dir': 'code',
        'use_docker': False,
    },
)
PROMT = """SYSTEM PROMPT:
Get Price [coingecko.com limit news article to 5]
Get News [newsapi.org api-key 2a009d59e361430b97a1305cc997e68f]

QUERY:
На сколько изменилась цена биткойна за 7 дней? Объясни на основании новостей почему?"""

user_proxy.initiate_chat(
    assistant,
    message=PROMT,
)
