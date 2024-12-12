import autogen

def main():
    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list": [
                {
                    "model": "llama3.1",
                    "base_url": "http://localhost:11434/v1",
                    "api_key": "ollama"
                }
            ]
        }
    )

    user_proxy = autogen.UserProxyAgent(
        name="user",
        human_input_mode="NEVER", # OPTIONS: ALWAYS, NEVER, TERMINATE
        code_execution_config={
            "work_dir": "examples/01-two-way-chat/coding",
            "use_docker": False
        }
    )

    user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock prices over the last year.")

if __name__ == '__main__':
    main()