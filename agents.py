import autogen


def agents_defination(gpt4_config: dict) -> tuple:
    friend = autogen.AssistantAgent(
        name="Friend",
        system_message="""Friend. A supportive figure who guides you towards the right direction, offering constructive criticism and honest advice. This agent helps in identifying the best possible solutions and advises on avoiding pitfalls.""",
        llm_config=gpt4_config,
    )

    foe = autogen.AssistantAgent(
        name="Foe",
        system_message="""Foe. An agent designed to challenge and question your decisions, often attempting to undermine or belittle your efforts. This agent might provide harsh criticism and might look for faults in your plans or actions.""",
        llm_config=gpt4_config,
    )

    return (
        friend,
        foe,
    )
