from abc import ABC, abstractmethod
import logging

from lib.core.dto.research_context_repository_dto import (
    GetResearchContextDTO,
    GetResearchContextClientDTO,
    ListResearchContextConversationsDTO,
    ListSourceDataDTO,
    NewResearchContextConversationDTO,
)


class ResearchContextRepositoryOutputPort(ABC):
    """
    Abstract base class for the research context repository output port.

    @cvar logger: The logger for this class
    @type logger: logging.Logger
    """

    def __init__(self) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    @abstractmethod
    def get_research_context(self, research_context_id: int) -> GetResearchContextDTO:
        """
        Gets a research context by ID.

        @param research_context_id: The ID of the research context to get.
        @type research_context_id: int
        @return: A DTO containing the result of the operation.
        @rtype: GetResearchContextDTO
        """
        raise NotImplementedError

    @abstractmethod
    def get_research_context_client(self, research_context_id: int) -> GetResearchContextClientDTO:
        """
        Gets the client that created a research context.

        @param research_context_id: The ID of the research context to get the client for.
        @type research_context_id: int
        @return: A DTO containing the result of the operation.
        @rtype: GetResearchContextClientDTO
        """
        raise NotImplementedError

    @abstractmethod
    def new_conversation(self, research_context_id: int, conversation_title: str) -> NewResearchContextConversationDTO:
        """
        Creates a new conversation in the research context.

        @param research_context_id: The ID of the research context to create the conversation in.
        @type research_context_id: int
        @param conversation_title: The title of the conversation.
        @type conversation_title: str
        @return: A DTO containing the result of the operation.
        @rtype: ConversationDTO
        """
        raise NotImplementedError

    @abstractmethod
    def list_conversations(self, research_context_id: int) -> ListResearchContextConversationsDTO:
        """
        Lists all conversations in a research context.

        @param research_context_id: The ID of the research context to list conversations for.
        @type research_context_id: int
        @return: A DTO containing the result of the operation.
        @rtype: ListResearchContextConversationsDTO
        """
        raise NotImplementedError

    @abstractmethod
    def list_source_data(self, research_context_id: int) -> ListSourceDataDTO:
        """
        Lists all source data related to a research context.

        @param research_context_id: The ID of the research context to list source data for.
        @type research_context_id: int
        @return: A DTO containing the result of the operation.
        @rtype: ListResearchContextSourceDataDTO
        """
        raise NotImplementedError
