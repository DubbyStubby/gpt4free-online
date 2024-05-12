from g4f import Provider, models
from langchain.llms.base import LLM
from langchain_g4f import G4FLLM
from g4f.gui import run_gui
run_gui()


def main():
    llm: LLM = G4FLLM(
        model="gemini",  # Pass the model name as a string
        provider=Provider.Gemini,
    )

    res = llm("generate a picture of a white siamese cat")
    print(res)


if __name__ == "__main__":
    main()