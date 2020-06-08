from flask import current_app, url_for
from flask_script import Command
from ..controllers.states_controller.controller import StateController
from ..controllers.cities_controller.controller import CityController
from ..controllers.roles_controller.controller import RoleController
from ..controllers.districts_controller.controller import DistrictController
from ..controllers.users_controller.controller import UserController
from ..controllers.permissions_controller.controller import PermissionController
from ..controllers.privileges_controller.controller import PrivilegeController
from ..controllers.archdioceses_controller.controller import ArchdioceseController
from ..controllers.lists_controller.controller import ListController
from ..controllers.listItems_controller.controller import ListItemController
from ..controllers.persons_controller.controller import PersonController
from ..controllers.registryOfBaptisms_controller.controller import RegistryOfBaptismsController
from ..controllers.documents_controller.controller import DocumentController
from ..controllers.counter_controller.controller import CounterController
from ..models.states import State, StateQuery
from ..models.cities import City, CityQuery
from ..models.roles import Role
from ..models.districts import District
from ..models.users import User
from ..models.privileges import Privilege
from ..models.permissions import Permission
from ..models.archdioceses import Archdiocese
from ..models.lists import List
from ..models.listItems import ListItem
from ..models.persons import Person
from ..models.registryOfBaptisms import RegistryOfBaptisms
from ..models.documents import Document
from ..models.counter import Counter
from werkzeug.security import generate_password_hash, check_password_hash
import re
import datetime


class Seed(Command):
    """Seeds database with fake but realistic data"""

    def run(self):
        current_app.logger.info('Seeding database with test data...')
        controller = StateController(
            state=State(
                name='BiH'
            ))
        controller.create()
        controller = ArchdioceseController(
            archdiocese=Archdiocese(
                name='Mostarsko-duvanjska biskupija'
            ))
        controller.create()
        state = State.query.filter_by(name='BiH').first()
        controller = CityController(
            city=City(
                name='Grude',
                state_id=state.id
            ))
        controller.create()
        city = City.query.filter_by(name='Grude').first()
        archdiocese = Archdiocese.query.filter_by(name='Mostarsko-duvanjska biskupija').first()
        controller = DistrictController(
            district=District(
                name='Gorica-Sovići',
                address='Podkrstina bb',
                city_id=city.id,
                archdiocese_id=archdiocese.id
            ))
        controller.create()
        controller = RoleController(
            role=Role(
                name='admin'
            ))
        controller.create()
        controller = RoleController(
            role=Role(
                name='fratar'
            ))
        controller.create()
        role = Role.query.filter_by(name='admin').first()
        district = District.query.filter_by(name='Gorica-Sovići').first()
        controller = UserController(
            user=User(
                first_name='Anđela',
                last_name='Bošnjak',
                username='andjelabosnjak',
                email='andjela.bosnjak30@gmail.com',
                password_hash=generate_password_hash('123456', method='sha256'),
                roles_id=role.id,
                districts_id=district.id
            ))
        controller.create()
        role = Role.query.filter_by(name='fratar').first()
        controller = UserController(
            user=User(
                first_name='Stipe',
                last_name='Marković',
                username='stipemarkovic',
                email='stipemarkovic@gmail.com',
                password_hash=generate_password_hash('123456', method='sha256'),
                roles_id=role.id,
                districts_id=district.id
            ))
        controller.create()
        controller = UserController(
            user=User(
                first_name='Marija',
                last_name='Bošnjak',
                username='marijabosnjak',
                email='marijabosnjak998@gmail.com',
                password_hash=generate_password_hash('123456', method='sha256'),
                roles_id=role.id,
                districts_id=district.id
            ))
        controller.create()

        for rule in current_app.url_map.iter_rules():
            for method in rule.methods:
                if method == 'OPTIONS' or method == 'HEAD':
                    pass
                else:
                    controller = PermissionController(
                        permission=Permission(
                            name=re.sub(
                                '<[^>]+>', "", str(rule.rule[0].replace("/", "") + rule.rule[1:].replace("/", " "))),
                            route=str(rule.rule),
                            method=str(method)

                        ))
                    controller.create()

        permissions = Permission.query.all()
        for permission in permissions:
            if any(path in permission.route for path in ['/permission', '/privilege', '/role', '/user', '/city', '/district', '/state', '/archdiocese']):
                controller = PrivilegeController(
                    privilege=Privilege(
                        roles_id=role.id,
                        permissions_id=permission.id

                    ))
                controller.create()
        controller = ListController(
            list=List(
                id='ea83b091-0bd1-465f-a2dd-79499fee4364',
                name='child'
            ))
        controller.create()
        controller = ListController(
            list=List(
                id='47a17b46-b37e-4639-98eb-fb3c3d347721',
                name='religions'
            ))
        controller.create()
        controller = ListController(
            list=List(
                id='afe25137-6e32-43d3-8957-8caa7365173b',
                name='document_types'
            ))
        controller.create()
        controller = ListController(
            list=List(
                id='a5e4d6d8-6f27-4094-b06a-79d00bb98859',
                name='yes/no list'
            ))
        controller.create()
        list = List.query.filter_by(name='child').first()
        controller = ListItemController(
            list_item=ListItem(
                value='Sin',
                list_id=list.id
            ))
        controller.create()
        controller = ListItemController(
            list_item=ListItem(
                value='Kći',
                list_id=list.id
            ))
        controller.create()
        list = List.query.filter_by(name='religions').first()
        controller = ListItemController(
            list_item=ListItem(
                value='Kršćanstvo',
                list_id=list.id
            ))
        controller.create()
        religion = ListItem.query.filter_by(value='Kršćanstvo').first()
        controller = ListItemController(
            list_item=ListItem(
                value='Islam',
                list_id=list.id
            ))
        controller.create()
        list = List.query.filter_by(name='yes/no list').first()
        controller = ListItemController(
            list_item=ListItem(
                value='Da',
                list_id=list.id
            ))
        controller.create()
        list_item = ListItem.query.filter_by(value='Da').first()
        controller = ListItemController(
            list_item=ListItem(
                value='Ne',
                list_id=list.id
            ))
        controller.create()
        list = List.query.filter_by(name='document_types').first()
        controller = ListItemController(
            list_item=ListItem(
                id='5faf077f-bd10-4136-8619-a41447e41871',
                value='Matica krštenih',
                list_id=list.id
            ))
        controller.create()
        document_type_value = ListItem.query.filter_by(value='Matica krštenih').first()
        controller = ListItemController(
            list_item=ListItem(
                id='78c884e9-fb9a-4f0e-a9de-2e1ea53dd618',
                value='Matica vjenčanih',
                list_id=list.id
            ))
        controller.create()
        controller = ListItemController(
            list_item=ListItem(
                id='8b90de67-3244-4f48-9136-6f4c7fd6b12c',
                value='Matica umrlih',
                list_id=list.id
            ))
        controller.create()
        controller = ListController(
            list=List(
                id='177eda0f-dd0c-4531-a7dc-c7c9ceb1756a',
                name='methods'
            ))
        controller.create()
        methods = List.query.filter_by(name='methods').first()
        controller = ListItemController(
            list_item=ListItem(
                value='GET',
                list_id=methods.id
            ))
        controller.create()
        controller = ListItemController(
            list_item=ListItem(
                value='PUT',
                list_id=methods.id
            ))
        controller.create()
        controller = ListItemController(
            list_item=ListItem(
                value='POST',
                list_id=methods.id
            ))
        controller.create()
        controller = ListItemController(
            list_item=ListItem(
                value='DELETE',
                list_id=methods.id
            ))
        controller.create()
        controller = PersonController(
            person=Person(
                first_name='Mirjana',
                last_name='Bošnjak',
                maiden_name='Marijanović',
                birth_date='17/01/1973',
                birth_place=city.id,
                identity_number='1701973155631',
                domicile='Bobanova Draga bb, 88345 Sovići',
                district=district.id,
                religion=religion.id
            ))
        controller.create()
        controller = PersonController(
            person=Person(
                first_name='Ivo',
                last_name='Ivić',
                birth_date='10/05/1985',
                birth_place=city.id,
                identity_number='1005985997875',
                domicile='Bobanova Draga bb, 88345 Sovići',
                district=district.id,
                religion=religion.id
            ))
        controller.create()
        controller = PersonController(
            person=Person(
                first_name='Ante',
                last_name='Bošnjak',
                birth_date='11/06/2005',
                birth_place=city.id,
                identity_number='11062005655131',
                domicile='Bobanova Draga bb, 88345 Sovići',
                district=district.id,
                religion=religion.id
            ))
        controller.create()
        mother = Person.query.filter_by(identity_number='1701973155631').first()
        best_man = Person.query.filter_by(identity_number='11062005655131').first()
        controller = PersonController(
            person=Person(
                first_name='Marija',
                last_name='Bošnjak',
                birth_date='25/06/1998',
                birth_place=city.id,
                identity_number='2506998155631',
                domicile='Bobanova Draga bb, 88345 Sovići',
                mother_id=mother.id,
                district=district.id,
                religion=religion.id
            ))
        controller.create()
        controller = CounterController(
            counter=Counter(
                id='ed33ab9d-3bb9-4251-b527-d897981df675',
                name='document_number',
                expression='$d/$m/$y-$c',
                description='Counter koji služi za generiranje broja dokumenata.',
                day=datetime.datetime.today().day,
                month=datetime.datetime.today().month,
                restart_on='$y',
                start_from=1,
                year=datetime.datetime.today().year,
                value=10,
                restart_time=datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.min.time())
            ))
        controller.create()
        person = Person.query.filter_by(identity_number='2506998155631').first()
        user = User.query.filter_by(username='stipemarkovic').first()
        controller = DocumentController(
            document=Document(
                id='95e923dd-0121-4ac5-a321-c1de097a14d9',
                document_type=document_type_value.id,
                person_id=person.id,
                act_date='24/07/1998',
                act_performed=user.id,
                document_number='K - ' + CounterController.generate(Counter.counters['document_number']),
                district=district.id,
                volume=10,
                year=1998,
                page=1,
                number=10,
                user_created=user.id
            ))
        controller.create()
        document = Document.query.filter_by(id='95e923dd-0121-4ac5-a321-c1de097a14d9').first()
        child = ListItem.query.filter_by(value='Kći').first()
        controller = RegistryOfBaptismsController(
            baptism=RegistryOfBaptisms(
                id=document.id,
                person_id=person.id,
                best_man=best_man.id,
                name=person.first_name,
                surname=person.last_name,
                birth_date=person.birth_date,
                birth_place=city.id,
                identity_number=person.identity_number,
                child=child.id,
                parents_canonically_married=list_item.id
            ))
        controller.create()
        person = Person.query.filter_by(identity_number='1005985997875').first()
        controller = DocumentController(
            document=Document(
                id='13771757-26ef-4d08-bc62-6e3b172bfb38',
                document_type=document_type_value.id,
                person_id=person.id,
                act_date='20/06/1985',
                act_performed=user.id,
                document_number='K - ' + CounterController.generate(Counter.counters['document_number']),
                district=district.id,
                volume=10,
                year=1998,
                page=1,
                number=10,
                user_created=user.id
            ))
        controller.create()
        document = Document.query.filter_by(id='13771757-26ef-4d08-bc62-6e3b172bfb38').first()
        child = ListItem.query.filter_by(value='Sin').first()
        controller = RegistryOfBaptismsController(
            baptism=RegistryOfBaptisms(
                id=document.id,
                person_id=person.id,
                best_man=best_man.id,
                name=person.first_name,
                surname=person.last_name,
                birth_date=person.birth_date,
                birth_place=city.id,
                identity_number=person.identity_number,
                child=child.id,
                parents_canonically_married=list_item.id
            ))
        controller.create()

