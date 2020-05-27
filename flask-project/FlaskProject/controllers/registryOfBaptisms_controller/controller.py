from sqlalchemy import and_
from ..cities_controller.controller import CityController
from ..listItems_controller.controller import ListItemController
from ..persons_controller.controller import PersonController
from ... import RegistryOfBaptisms, Person, City, ListItem, FlaskProjectLogException
from ...controllers.base_controller import BaseController
from ...general import Status, obj_to_dict


class RegistryOfBaptismsController(BaseController):
    def __init__(self, baptism=RegistryOfBaptisms()):
        self.baptism = baptism

    def create(self):
        """
         Method used for creating registry of baptism
        :return: Status object or raise FlaskProjectLogException
        """

        if RegistryOfBaptisms.query.check_if_already_exist_by_identity_number(
                self.baptism.identity_number):
            raise FlaskProjectLogException(
                Status.status_identity_number_already_exist())

        if self.baptism.person_id is not None:
            person = PersonController.get_one(
                self.baptism.person_id)

            if person.person is None:
                raise FlaskProjectLogException(
                    Status.status_person_not_exist())

        if self.baptism.best_man is not None:
            best_man = PersonController.get_one(
                self.baptism.best_man)

            if best_man.person is None:
                raise FlaskProjectLogException(
                    Status.status_person_not_exist())

        if self.baptism.birth_place is not None:
            birth_place = CityController.get_one(
                self.baptism.birth_place)

            if birth_place.city is None:
                raise FlaskProjectLogException(
                    Status.status_city_not_exist())

        if self.baptism.child is not None:
            child = ListItemController.get_one(
                self.baptism.child)

            if child.list_item is None:
                raise FlaskProjectLogException(
                    Status.status_list_item_not_exist())

        self.baptism.add()
        self.baptism.commit_or_rollback()

        return Status.status_successfully_inserted().__dict__

    def alter(self):
        raise NotImplementedError("To be implemented")

    def inactivate(self):
        raise NotImplementedError("To be implemented")

    def activate(self):
        raise NotImplementedError("To be implemented")

    @classmethod
    def get_one(cls, identifier):
        return cls(baptism=RegistryOfBaptisms.query.get_one(identifier))

    @staticmethod
    def get_one_details(identifier):
        """
       Use this method to get an registry of baptism by identifier
       :param identifier: Registry of baptism identifier
       :return: Dict object
       """
        return RegistryOfBaptismsController.__custom_sql(
            RegistryOfBaptisms.query.get_one_details(identifier))

    @staticmethod
    def list_autocomplete(search):
        raise NotImplementedError("To be implemented")

    @staticmethod
    def list_search(search):
        raise NotImplementedError("To be implemented")

    @staticmethod
    def get_list_pagination(start, limit, **kwargs):
        """
        Method for getting all registry of baptisms by filter_data in pagination form
        :return: dict with total, data and status
        """
        raise NotImplementedError("To be implemented")

    @staticmethod
    def __custom_sql(row_data):
        if row_data is not None:
            return_dict = obj_to_dict(row_data.RegistryOfBaptisms)
            return_dict['person'] = obj_to_dict(row_data.Person)
            return_dict['best_man'] = obj_to_dict(row_data.Person)
            return_dict['birth_place'] = obj_to_dict(row_data.City)
            return_dict['child'] = obj_to_dict(row_data.ListItem)
            return return_dict
        return None

