from abc import abstractmethod
from lib.core.ports.secondary.client_repository import ClientRepositoryOutputPort
from lib.core.ports.secondary.file_repository import FileRepositoryOutputPort
from lib.core.sdk.presenter import BasePresenter
from lib.core.sdk.usecase import BaseUseCase
from lib.core.usecase_models.new_source_data_usecase_models import (
    NewSourceDataError,
    NewSourceDataRequest,
    NewSourceDataResponse,
)
from lib.core.view_model.new_source_data_view_model import NewSourceDataViewModel


class NewSourceDataInputPort(BaseUseCase[NewSourceDataRequest, NewSourceDataResponse, NewSourceDataError]):
    def __init__(
        self,
        client_repository: ClientRepositoryOutputPort,
        file_repository: FileRepositoryOutputPort,
    ) -> None:
        self._client_repository = client_repository
        self._file_repository = file_repository

    @property
    def client_repository(self) -> ClientRepositoryOutputPort:
        return self._client_repository

    @property
    def file_repository(self) -> FileRepositoryOutputPort:
        return self._file_repository

    @abstractmethod
    def execute(self, request: NewSourceDataRequest) -> NewSourceDataResponse | NewSourceDataError:
        raise NotImplementedError("This method must be implemented by the usecase.")


class NewSourceDataOutputPort(BasePresenter[NewSourceDataResponse, NewSourceDataError, NewSourceDataViewModel]):
    @abstractmethod
    def convert_error_response_to_view_model(self, response: NewSourceDataError) -> NewSourceDataViewModel:
        raise NotImplementedError(
            "You must implement the convert_error_response_to_view_model method in your presenter"
        )

    @abstractmethod
    def convert_response_to_view_model(self, response: NewSourceDataResponse) -> NewSourceDataViewModel:
        raise NotImplementedError("You must implement the convert_response_to_view_model method in your presenter")
