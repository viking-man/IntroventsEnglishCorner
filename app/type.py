from enum import Enum


class ChatGPTModel(Enum):
    GPT4 = "gpt-4-0613"
    GPT3 = "gpt-3.5-turbo-0613"

    @staticmethod
    def get_values():
        return [i.value for i in ChatGPTModel]

    @staticmethod
    def get_value(version):
        for model in ChatGPTModel:
            if model.name == version:
                return model.value
            return ChatGPTModel.GPT3.value


class AudioType(Enum):
    INPUT = 'input',
    OUTPUT = 'output'

    @staticmethod
    def get_values():
        return [i.value for i in AudioType]
