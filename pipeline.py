import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda
from dotenv import load_dotenv

from models import TopicAnalysis

load_dotenv()

llm = ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.environ.get("HF_API_KEY"),
    temperature=0,
    max_new_tokens=512,
))

str_parser = StrOutputParser()

final_parser = PydanticOutputParser(pydantic_object=TopicAnalysis)

summary_prompt = PromptTemplate(
    template="Explain the topic '{topic}' in 3 sentences.",
    input_variables=['topic']
)

keywords_prompt = PromptTemplate(
    template="List the 5 most important keywords for '{topic}'. Return comma-separated only.",
    input_variables=['topic']
)

quiz_prompt = PromptTemplate(
    template="Create 3 quiz question-answer pairs for '{topic}'. Return strictly JSON list of objects: {{'q': '...', 'a': '...'}}.",
    input_variables=['topic']
)

difficulty_prompt = PromptTemplate(
    template= "Rate how difficult '{topic}' is to learn on a scale of 1-5. Return only the number.",
    input_variables=['topic']
)

def build_chains(
        llm=llm,
        str_parser=str_parser,
        summary_prompt=summary_prompt,
        keywords_prompt=keywords_prompt,
        quiz_prompt=quiz_prompt,
        difficulty_prompt=difficulty_prompt
    ):
    summary_chain = RunnableSequence(summary_prompt, llm, str_parser)

    keywords_chain = RunnableSequence(keywords_prompt, llm, str_parser, CommaSeparatedListOutputParser())

    quiz_chain = RunnableSequence(quiz_prompt, llm, str_parser, JsonOutputParser())

    difficulty_chain = RunnableSequence(difficulty_prompt, llm, str_parser, RunnableLambda(lambda x: int(str(x).strip())))

    parallel_block = RunnableParallel(
        summary=summary_chain,
        keywords=keywords_chain,
        quiz=quiz_chain,
        difficulty=difficulty_chain
    )

    final_chain = parallel_block | RunnableLambda(lambda x: TopicAnalysis(**x))

    return {
        "summary_chain": summary_chain,
        "keywords_chain": keywords_chain,
        "quiz_chain": quiz_chain,
        "difficulty_chain": difficulty_chain,
        "parallel_chain": parallel_block,
        "final_chain": final_chain,
    }