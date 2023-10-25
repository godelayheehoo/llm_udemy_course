from typing import Tuple

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from output_parsers import person_intel_parser, PersonIntel
from third_parties import linkedin
from Agents.linkedin_url_agent import (
    lookup as linkedin_lookup_agent,
    HARDCODED_PROFILE_URL,
)


def icebreak_main(name: str) -> Tuple[PersonIntel, str]:
    print("Hello world")

    linkedin_profile_url = linkedin_lookup_agent(name=name)
    print(f"URL: {linkedin_profile_url}")

    summary_template = """
    given the linkedin information {information} about a person from I want you to create
    1. a short summary
    2. two interesting facts about them
    3. A topic that may interest them
    4. 2 creative ice breakers to open a conversation with them. 
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = linkedin.scraped_linkedin_profile("not_used")

    result = chain.run(information=linkedin_data)

    # return person_intel_parser.parse(result),linkedin_data.get('profile_pic_url')
    return person_intel_parser.parse(result), HARDCODED_PROFILE_URL


if __name__ == "__main__":
    result = icebreak_main("Eden Marco")
    print(result)
