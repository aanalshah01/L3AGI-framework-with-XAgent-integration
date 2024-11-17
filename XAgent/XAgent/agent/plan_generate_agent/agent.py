from typing import List
from XAgent.agent.base_agent import BaseAgent
from XAgent.utils import RequiredAbilities
from XAgent.ai_functions import function_manager, objgenerator
from XAgent.message_history import Message


class PlanGenerateAgent(BaseAgent):
    """
    This class is responsible for plan generation. It is a subclass of BaseAgent.

    Attributes:
        abilities: A set indicating the abilities required by this agent.
    """
    abilities = set([RequiredAbilities.plan_generation])

    def parse(
        self,
        placeholders: dict = {},
        arguments: dict = None,
        functions=None,
        function_call=None,
        stop=None,
        additional_messages: List[Message] = [],
        *args,
        **kwargs
    ):
        """
        This method is used to parse placeholders, arguments, function calls, and additional messages 
        to generate a plan.

        Args:
            placeholders (dict, optional): A dictionary containing placeholders to fill in the messages.
            arguments (dict, optional): A dictionary containing arguments to be used in the functions.
            functions: The functions to be used during plan generation.
            function_call: The object representing a function call.
            stop: The condition to stop the plan generation process if specified.
            additional_messages (List[Message], optional): A list of additional messages to be added to 
            the initial prompt messages.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            This method returns the result of the plan generated by the "generate" method.
        """
        prompt_messages = self.fill_in_placeholders(placeholders)
        messages = prompt_messages + additional_messages

        return self.generate(
            messages=messages,
            arguments=arguments,
            functions=functions,
            function_call=function_call,
            stop=stop,
            *args, **kwargs
        )