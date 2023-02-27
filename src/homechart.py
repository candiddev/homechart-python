#!/usr/bin/env python3
# Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
"""Implements the client for Homechart."""

# pylint: skip-file
# pydocstyle: add-ignore=D105,D107,D401

import contextlib
import json
from typing import Any, BinaryIO, Dict, List, MutableMapping, Optional, cast

import requests
import requests.auth


def from_obj(obj: Any, expected: List[type], path: str = '') -> Any:
    """
    Checks and converts the given obj along the expected types.

    :param obj: to be converted
    :param expected: list of types representing the (nested) structure
    :param path: to the object used for debugging
    :return: the converted object
    """
    if not expected:
        raise ValueError("`expected` is empty, but at least one type needs to be specified.")

    exp = expected[0]

    if exp == float:
        if isinstance(obj, int):
            return float(obj)

        if isinstance(obj, float):
            return obj

        raise ValueError(
            'Expected object of type int or float at {!r}, but got {}.'.format(path, type(obj)))

    if exp in [bool, int, str, list, dict]:
        if not isinstance(obj, exp):
            raise ValueError(
                'Expected object of type {} at {!r}, but got {}.'.format(exp, path, type(obj)))

    if exp in [bool, int, float, str]:
        return obj

    if exp == list:
        lst = []  # type: List[Any]
        for i, value in enumerate(obj):
            lst.append(
                from_obj(value, expected=expected[1:], path='{}[{}]'.format(path, i)))

        return lst

    if exp == dict:
        adict = dict()  # type: Dict[str, Any]
        for key, value in obj.items():
            if not isinstance(key, str):
                raise ValueError(
                    'Expected a key of type str at path {!r}, got: {}'.format(path, type(key)))

            adict[key] = from_obj(value, expected=expected[1:], path='{}[{!r}]'.format(path, key))

        return adict

    if exp == AuthAccount:
        return auth_account_from_obj(obj, path=path)

    if exp == AuthAccountPreferences:
        return auth_account_preferences_from_obj(obj, path=path)

    if exp == AuthAccountPreferencesNotificationsHousehold:
        return auth_account_preferences_notifications_household_from_obj(obj, path=path)

    if exp == AuthAccountPrivateKey:
        return auth_account_private_key_from_obj(obj, path=path)

    if exp == AuthHousehold:
        return auth_household_from_obj(obj, path=path)

    if exp == AuthHouseholdFeatureVote:
        return auth_household_feature_vote_from_obj(obj, path=path)

    if exp == AuthHouseholdMember:
        return auth_household_member_from_obj(obj, path=path)

    if exp == AuthHouseholdPermissions:
        return auth_household_permissions_from_obj(obj, path=path)

    if exp == AuthHouseholdPreferences:
        return auth_household_preferences_from_obj(obj, path=path)

    if exp == AuthSession:
        return auth_session_from_obj(obj, path=path)

    if exp == Bookmark:
        return bookmark_from_obj(obj, path=path)

    if exp == BudgetAccount:
        return budget_account_from_obj(obj, path=path)

    if exp == BudgetCategory:
        return budget_category_from_obj(obj, path=path)

    if exp == BudgetMonth:
        return budget_month_from_obj(obj, path=path)

    if exp == BudgetMonthCategory:
        return budget_month_category_from_obj(obj, path=path)

    if exp == BudgetPayee:
        return budget_payee_from_obj(obj, path=path)

    if exp == BudgetRecurrence:
        return budget_recurrence_from_obj(obj, path=path)

    if exp == BudgetRecurrenceTemplate:
        return budget_recurrence_template_from_obj(obj, path=path)

    if exp == BudgetTransaction:
        return budget_transaction_from_obj(obj, path=path)

    if exp == BudgetTransactionAccount:
        return budget_transaction_account_from_obj(obj, path=path)

    if exp == BudgetTransactionCategory:
        return budget_transaction_category_from_obj(obj, path=path)

    if exp == CalendarEvent:
        return calendar_event_from_obj(obj, path=path)

    if exp == Change:
        return change_from_obj(obj, path=path)

    if exp == CivilDate:
        return civil_date_from_obj(obj, path=path)

    if exp == CookMealPlan:
        return cook_meal_plan_from_obj(obj, path=path)

    if exp == CookMealTime:
        return cook_meal_time_from_obj(obj, path=path)

    if exp == CookRecipe:
        return cook_recipe_from_obj(obj, path=path)

    if exp == CookRecipeNote:
        return cook_recipe_note_from_obj(obj, path=path)

    if exp == HealthItem:
        return health_item_from_obj(obj, path=path)

    if exp == HealthLog:
        return health_log_from_obj(obj, path=path)

    if exp == ID:
        return id_from_obj(obj, path=path)

    if exp == InventoryCollection:
        return inventory_collection_from_obj(obj, path=path)

    if exp == InventoryCollectionSort:
        return inventory_collection_sort_from_obj(obj, path=path)

    if exp == InventoryItem:
        return inventory_item_from_obj(obj, path=path)

    if exp == NotesPage:
        return notes_page_from_obj(obj, path=path)

    if exp == NotesPageVersion:
        return notes_page_version_from_obj(obj, path=path)

    if exp == Permissions:
        return permissions_from_obj(obj, path=path)

    if exp == PlanProject:
        return plan_project_from_obj(obj, path=path)

    if exp == PlanTask:
        return plan_task_from_obj(obj, path=path)

    if exp == Recurrence:
        return recurrence_from_obj(obj, path=path)

    if exp == Response:
        return response_from_obj(obj, path=path)

    if exp == RewardCard:
        return reward_card_from_obj(obj, path=path)

    if exp == SecretsValue:
        return secrets_value_from_obj(obj, path=path)

    if exp == SecretsVault:
        return secrets_vault_from_obj(obj, path=path)

    if exp == SecretsVaultKey:
        return secrets_vault_key_from_obj(obj, path=path)

    if exp == ShopCategory:
        return shop_category_from_obj(obj, path=path)

    if exp == ShopItem:
        return shop_item_from_obj(obj, path=path)

    if exp == ShopList:
        return shop_list_from_obj(obj, path=path)

    if exp == TableNotify:
        return table_notify_from_obj(obj, path=path)

    if exp == EncryptionEncryptedValue:
        return encryption_encrypted_value_from_obj(obj, path=path)

    if exp == ModelsCalendarICalendar:
        return models_calendar_i_calendar_from_obj(obj, path=path)

    if exp == UuidNullUUID:
        return uuid_null_u_u_id_from_obj(obj, path=path)

    raise ValueError("Unexpected `expected` type: {}".format(exp))


def to_jsonable(obj: Any, expected: List[type], path: str = "") -> Any:
    """
    Checks and converts the given object along the expected types to a JSON-able representation.

    :param obj: to be converted
    :param expected: list of types representing the (nested) structure
    :param path: path to the object used for debugging
    :return: JSON-able representation of the object
    """
    if not expected:
        raise ValueError("`expected` is empty, but at least one type needs to be specified.")

    exp = expected[0]
    if not isinstance(obj, exp):
        raise ValueError('Expected object of type {} at path {!r}, but got {}.'.format(
            exp, path, type(obj)))

    # Assert on primitive types to help type-hinting.
    if exp == bool:
        assert isinstance(obj, bool)
        return obj

    if exp == int:
        assert isinstance(obj, int)
        return obj

    if exp == float:
        assert isinstance(obj, float)
        return obj

    if exp == str:
        assert isinstance(obj, str)
        return obj

    if exp == list:
        assert isinstance(obj, list)

        lst = []  # type: List[Any]
        for i, value in enumerate(obj):
            lst.append(
                to_jsonable(value, expected=expected[1:], path='{}[{}]'.format(path, i)))

        return lst

    if exp == dict:
        assert isinstance(obj, dict)

        adict = dict()  # type: Dict[str, Any]
        for key, value in obj.items():
            if not isinstance(key, str):
                raise ValueError(
                    'Expected a key of type str at path {!r}, got: {}'.format(path, type(key)))

            adict[key] = to_jsonable(
                value,
                expected=expected[1:],
                path='{}[{!r}]'.format(path, key))

        return adict

    if exp == AuthAccount:
        assert isinstance(obj, AuthAccount)
        return auth_account_to_jsonable(obj, path=path)

    if exp == AuthAccountPreferences:
        assert isinstance(obj, AuthAccountPreferences)
        return auth_account_preferences_to_jsonable(obj, path=path)

    if exp == AuthAccountPreferencesNotificationsHousehold:
        assert isinstance(obj, AuthAccountPreferencesNotificationsHousehold)
        return auth_account_preferences_notifications_household_to_jsonable(obj, path=path)

    if exp == AuthAccountPrivateKey:
        assert isinstance(obj, AuthAccountPrivateKey)
        return auth_account_private_key_to_jsonable(obj, path=path)

    if exp == AuthHousehold:
        assert isinstance(obj, AuthHousehold)
        return auth_household_to_jsonable(obj, path=path)

    if exp == AuthHouseholdFeatureVote:
        assert isinstance(obj, AuthHouseholdFeatureVote)
        return auth_household_feature_vote_to_jsonable(obj, path=path)

    if exp == AuthHouseholdMember:
        assert isinstance(obj, AuthHouseholdMember)
        return auth_household_member_to_jsonable(obj, path=path)

    if exp == AuthHouseholdPermissions:
        assert isinstance(obj, AuthHouseholdPermissions)
        return auth_household_permissions_to_jsonable(obj, path=path)

    if exp == AuthHouseholdPreferences:
        assert isinstance(obj, AuthHouseholdPreferences)
        return auth_household_preferences_to_jsonable(obj, path=path)

    if exp == AuthSession:
        assert isinstance(obj, AuthSession)
        return auth_session_to_jsonable(obj, path=path)

    if exp == Bookmark:
        assert isinstance(obj, Bookmark)
        return bookmark_to_jsonable(obj, path=path)

    if exp == BudgetAccount:
        assert isinstance(obj, BudgetAccount)
        return budget_account_to_jsonable(obj, path=path)

    if exp == BudgetCategory:
        assert isinstance(obj, BudgetCategory)
        return budget_category_to_jsonable(obj, path=path)

    if exp == BudgetMonth:
        assert isinstance(obj, BudgetMonth)
        return budget_month_to_jsonable(obj, path=path)

    if exp == BudgetMonthCategory:
        assert isinstance(obj, BudgetMonthCategory)
        return budget_month_category_to_jsonable(obj, path=path)

    if exp == BudgetPayee:
        assert isinstance(obj, BudgetPayee)
        return budget_payee_to_jsonable(obj, path=path)

    if exp == BudgetRecurrence:
        assert isinstance(obj, BudgetRecurrence)
        return budget_recurrence_to_jsonable(obj, path=path)

    if exp == BudgetRecurrenceTemplate:
        assert isinstance(obj, BudgetRecurrenceTemplate)
        return budget_recurrence_template_to_jsonable(obj, path=path)

    if exp == BudgetTransaction:
        assert isinstance(obj, BudgetTransaction)
        return budget_transaction_to_jsonable(obj, path=path)

    if exp == BudgetTransactionAccount:
        assert isinstance(obj, BudgetTransactionAccount)
        return budget_transaction_account_to_jsonable(obj, path=path)

    if exp == BudgetTransactionCategory:
        assert isinstance(obj, BudgetTransactionCategory)
        return budget_transaction_category_to_jsonable(obj, path=path)

    if exp == CalendarEvent:
        assert isinstance(obj, CalendarEvent)
        return calendar_event_to_jsonable(obj, path=path)

    if exp == Change:
        assert isinstance(obj, Change)
        return change_to_jsonable(obj, path=path)

    if exp == CivilDate:
        assert isinstance(obj, CivilDate)
        return civil_date_to_jsonable(obj, path=path)

    if exp == CookMealPlan:
        assert isinstance(obj, CookMealPlan)
        return cook_meal_plan_to_jsonable(obj, path=path)

    if exp == CookMealTime:
        assert isinstance(obj, CookMealTime)
        return cook_meal_time_to_jsonable(obj, path=path)

    if exp == CookRecipe:
        assert isinstance(obj, CookRecipe)
        return cook_recipe_to_jsonable(obj, path=path)

    if exp == CookRecipeNote:
        assert isinstance(obj, CookRecipeNote)
        return cook_recipe_note_to_jsonable(obj, path=path)

    if exp == HealthItem:
        assert isinstance(obj, HealthItem)
        return health_item_to_jsonable(obj, path=path)

    if exp == HealthLog:
        assert isinstance(obj, HealthLog)
        return health_log_to_jsonable(obj, path=path)

    if exp == ID:
        assert isinstance(obj, ID)
        return id_to_jsonable(obj, path=path)

    if exp == InventoryCollection:
        assert isinstance(obj, InventoryCollection)
        return inventory_collection_to_jsonable(obj, path=path)

    if exp == InventoryCollectionSort:
        assert isinstance(obj, InventoryCollectionSort)
        return inventory_collection_sort_to_jsonable(obj, path=path)

    if exp == InventoryItem:
        assert isinstance(obj, InventoryItem)
        return inventory_item_to_jsonable(obj, path=path)

    if exp == NotesPage:
        assert isinstance(obj, NotesPage)
        return notes_page_to_jsonable(obj, path=path)

    if exp == NotesPageVersion:
        assert isinstance(obj, NotesPageVersion)
        return notes_page_version_to_jsonable(obj, path=path)

    if exp == Permissions:
        assert isinstance(obj, Permissions)
        return permissions_to_jsonable(obj, path=path)

    if exp == PlanProject:
        assert isinstance(obj, PlanProject)
        return plan_project_to_jsonable(obj, path=path)

    if exp == PlanTask:
        assert isinstance(obj, PlanTask)
        return plan_task_to_jsonable(obj, path=path)

    if exp == Recurrence:
        assert isinstance(obj, Recurrence)
        return recurrence_to_jsonable(obj, path=path)

    if exp == Response:
        assert isinstance(obj, Response)
        return response_to_jsonable(obj, path=path)

    if exp == RewardCard:
        assert isinstance(obj, RewardCard)
        return reward_card_to_jsonable(obj, path=path)

    if exp == SecretsValue:
        assert isinstance(obj, SecretsValue)
        return secrets_value_to_jsonable(obj, path=path)

    if exp == SecretsVault:
        assert isinstance(obj, SecretsVault)
        return secrets_vault_to_jsonable(obj, path=path)

    if exp == SecretsVaultKey:
        assert isinstance(obj, SecretsVaultKey)
        return secrets_vault_key_to_jsonable(obj, path=path)

    if exp == ShopCategory:
        assert isinstance(obj, ShopCategory)
        return shop_category_to_jsonable(obj, path=path)

    if exp == ShopItem:
        assert isinstance(obj, ShopItem)
        return shop_item_to_jsonable(obj, path=path)

    if exp == ShopList:
        assert isinstance(obj, ShopList)
        return shop_list_to_jsonable(obj, path=path)

    if exp == TableNotify:
        assert isinstance(obj, TableNotify)
        return table_notify_to_jsonable(obj, path=path)

    if exp == EncryptionEncryptedValue:
        assert isinstance(obj, EncryptionEncryptedValue)
        return encryption_encrypted_value_to_jsonable(obj, path=path)

    if exp == ModelsCalendarICalendar:
        assert isinstance(obj, ModelsCalendarICalendar)
        return models_calendar_i_calendar_to_jsonable(obj, path=path)

    if exp == UuidNullUUID:
        assert isinstance(obj, UuidNullUUID)
        return uuid_null_u_u_id_to_jsonable(obj, path=path)

    raise ValueError("Unexpected `expected` type: {}".format(exp))


class AuthAccount:
    def __init__(
            self,
            child: Optional[bool] = None,
            collapsed_notes_pages: Optional[List[str]] = None,
            collapsed_plan_projects: Optional[List[str]] = None,
            collapsed_plan_tasks: Optional[List[str]] = None,
            created: Optional[str] = None,
            daily_agenda_next: Optional[str] = None,
            daily_agenda_time: Optional[str] = None,
            email_address: Optional[str] = None,
            hide_calendar_i_calendars: Optional[List[str]] = None,
            icalendar_id: Optional[Any] = None,
            id: Optional[str] = None,
            last_activity: Optional[str] = None,
            name: Optional[str] = None,
            oidc_code: Optional[str] = None,
            oidc_provider_source: Optional[Any] = None,
            oidc_provider_type: Optional[Any] = None,
            password: Optional[str] = None,
            password_reset_token: Optional[Any] = None,
            permissions_account: Optional[Any] = None,
            permissions_households: Optional[List['AuthHouseholdPermissions']] = None,
            platform: Optional[Any] = None,
            preferences: Optional[Any] = None,
            primary_auth_household_id: Optional[Any] = None,
            private_keys: Optional[List['AuthAccountPrivateKey']] = None,
            public_key: Optional[str] = None,
            remember_me: Optional[bool] = None,
            self_hosted_id: Optional[Any] = None,
            setup: Optional[bool] = None,
            subscription_referrer_code: Optional[str] = None,
            time_zone: Optional[str] = None,
            tos_accepted: Optional[bool] = None,
            totp_backup: Optional[str] = None,
            totp_code: Optional[str] = None,
            totp_enabled: Optional[bool] = None,
            totp_q_r: Optional[str] = None,
            totp_secret: Optional[str] = None,
            updated: Optional[str] = None,
            verified: Optional[bool] = None) -> None:
        """Initializes with the given values."""
        # Restricts account settings.
        self.child = child

        # A list of IDs to collapse.
        self.collapsed_notes_pages = collapsed_notes_pages

        # A list of IDs to collapse.
        self.collapsed_plan_projects = collapsed_plan_projects

        # A list of IDs to collapse.
        self.collapsed_plan_tasks = collapsed_plan_tasks

        # Timestamp account was created.
        self.created = created

        # The next timestamp for the agenda.
        self.daily_agenda_next = daily_agenda_next

        # When to send the daily agenda.
        self.daily_agenda_time = daily_agenda_time

        # Primary email address of user.
        self.email_address = email_address

        # A list of iCalendar IDs to hide.
        self.hide_calendar_i_calendars = hide_calendar_i_calendars

        # ICalendarID for the account.
        self.icalendar_id = icalendar_id

        # ID of the account.
        self.id = id

        # Timestamp of the last time the account signed in.
        self.last_activity = last_activity

        # Name of the AuthAccount user.
        self.name = name

        # Code from OIDC provider to check during sign in/up.
        self.oidc_code = oidc_code

        # Used to determine which OIDC provider to use.
        self.oidc_provider_source = oidc_provider_source

        # Used to determine which OIDC provider to use.
        self.oidc_provider_type = oidc_provider_type

        # Password to use for sign in/up.
        self.password = password

        # Password reset token, used for password resets.
        self.password_reset_token = password_reset_token

        # Permissions for the account when creating a new session.
        self.permissions_account = permissions_account

        # Permissions for the households when creating a new session.
        self.permissions_households = permissions_households

        # Sets the platform for the initial session after account creation.
        self.platform = platform

        # Preferences for the account.
        self.preferences = preferences

        # The primary AuthHouseholdID, used by short links.
        self.primary_auth_household_id = primary_auth_household_id

        # PrivateKeys for decrypting secrets.
        self.private_keys = private_keys

        # PublicKey for encrypting secrets.
        self.public_key = public_key

        # Sets a longer timeout for the AuthSession.
        self.remember_me = remember_me

        # SelfHosted ID of the account, used when creating CloudHouseholds.
        self.self_hosted_id = self_hosted_id

        # Whether the account has gone through setup.
        self.setup = setup

        # Subscription referrer when account was setup.
        self.subscription_referrer_code = subscription_referrer_code

        # Used by notifications and UI to determine local times.
        self.time_zone = time_zone

        # ToS must be accepted to use the app.
        self.tos_accepted = tos_accepted

        # Backup code to recover TOTP.
        self.totp_backup = totp_backup

        # Code from the TOTP generator.
        self.totp_code = totp_code

        # Will check for TOTP code during sign in.
        self.totp_enabled = totp_enabled

        # QR Code version of the TOTPSecret.
        self.totp_q_r = totp_q_r

        # Secret to setup a TOTP generator.
        self.totp_secret = totp_secret

        # Timestamp for when account was last updated.
        self.updated = updated

        # Accounts must be verified to receive email notifications.
        self.verified = verified

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_account_to_jsonable.

        :return: JSON-able representation
        """
        return auth_account_to_jsonable(self)


def new_auth_account() -> AuthAccount:
    """Generates an instance of AuthAccount with default values."""
    return AuthAccount()


def auth_account_from_obj(obj: Any, path: str = "") -> AuthAccount:
    """
    Generates an instance of AuthAccount from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthAccount
    :param path: path to the object used for debugging
    :return: parsed instance of AuthAccount
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_child = obj.get('child', None)
    if obj_child is not None:
        child_from_obj = from_obj(
            obj_child,
            expected=[bool],
            path=path + '.child')  # type: Optional[bool]
    else:
        child_from_obj = None

    obj_collapsed_notes_pages = obj.get('collapsedNotesPages', None)
    if obj_collapsed_notes_pages is not None:
        collapsed_notes_pages_from_obj = from_obj(
            obj_collapsed_notes_pages,
            expected=[list, str],
            path=path + '.collapsedNotesPages')  # type: Optional[List[str]]
    else:
        collapsed_notes_pages_from_obj = None

    obj_collapsed_plan_projects = obj.get('collapsedPlanProjects', None)
    if obj_collapsed_plan_projects is not None:
        collapsed_plan_projects_from_obj = from_obj(
            obj_collapsed_plan_projects,
            expected=[list, str],
            path=path + '.collapsedPlanProjects')  # type: Optional[List[str]]
    else:
        collapsed_plan_projects_from_obj = None

    obj_collapsed_plan_tasks = obj.get('collapsedPlanTasks', None)
    if obj_collapsed_plan_tasks is not None:
        collapsed_plan_tasks_from_obj = from_obj(
            obj_collapsed_plan_tasks,
            expected=[list, str],
            path=path + '.collapsedPlanTasks')  # type: Optional[List[str]]
    else:
        collapsed_plan_tasks_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_daily_agenda_next = obj.get('dailyAgendaNext', None)
    if obj_daily_agenda_next is not None:
        daily_agenda_next_from_obj = from_obj(
            obj_daily_agenda_next,
            expected=[str],
            path=path + '.dailyAgendaNext')  # type: Optional[str]
    else:
        daily_agenda_next_from_obj = None

    obj_daily_agenda_time = obj.get('dailyAgendaTime', None)
    if obj_daily_agenda_time is not None:
        daily_agenda_time_from_obj = from_obj(
            obj_daily_agenda_time,
            expected=[str],
            path=path + '.dailyAgendaTime')  # type: Optional[str]
    else:
        daily_agenda_time_from_obj = None

    obj_email_address = obj.get('emailAddress', None)
    if obj_email_address is not None:
        email_address_from_obj = from_obj(
            obj_email_address,
            expected=[str],
            path=path + '.emailAddress')  # type: Optional[str]
    else:
        email_address_from_obj = None

    obj_hide_calendar_i_calendars = obj.get('hideCalendarICalendars', None)
    if obj_hide_calendar_i_calendars is not None:
        hide_calendar_i_calendars_from_obj = from_obj(
            obj_hide_calendar_i_calendars,
            expected=[list, str],
            path=path + '.hideCalendarICalendars')  # type: Optional[List[str]]
    else:
        hide_calendar_i_calendars_from_obj = None

    icalendar_id_from_obj = obj.get('icalendarID', None)

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_last_activity = obj.get('lastActivity', None)
    if obj_last_activity is not None:
        last_activity_from_obj = from_obj(
            obj_last_activity,
            expected=[str],
            path=path + '.lastActivity')  # type: Optional[str]
    else:
        last_activity_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_oidc_code = obj.get('oidcCode', None)
    if obj_oidc_code is not None:
        oidc_code_from_obj = from_obj(
            obj_oidc_code,
            expected=[str],
            path=path + '.oidcCode')  # type: Optional[str]
    else:
        oidc_code_from_obj = None

    oidc_provider_source_from_obj = obj.get('oidcProviderSource', None)

    oidc_provider_type_from_obj = obj.get('oidcProviderType', None)

    obj_password = obj.get('password', None)
    if obj_password is not None:
        password_from_obj = from_obj(
            obj_password,
            expected=[str],
            path=path + '.password')  # type: Optional[str]
    else:
        password_from_obj = None

    password_reset_token_from_obj = obj.get('passwordResetToken', None)

    permissions_account_from_obj = obj.get('permissionsAccount', None)

    obj_permissions_households = obj.get('permissionsHouseholds', None)
    if obj_permissions_households is not None:
        permissions_households_from_obj = from_obj(
            obj_permissions_households,
            expected=[list, AuthHouseholdPermissions],
            path=path + '.permissionsHouseholds')  # type: Optional[List['AuthHouseholdPermissions']]
    else:
        permissions_households_from_obj = None

    platform_from_obj = obj.get('platform', None)

    preferences_from_obj = obj.get('preferences', None)

    primary_auth_household_id_from_obj = obj.get('primaryAuthHouseholdID', None)

    obj_private_keys = obj.get('privateKeys', None)
    if obj_private_keys is not None:
        private_keys_from_obj = from_obj(
            obj_private_keys,
            expected=[list, AuthAccountPrivateKey],
            path=path + '.privateKeys')  # type: Optional[List['AuthAccountPrivateKey']]
    else:
        private_keys_from_obj = None

    obj_public_key = obj.get('publicKey', None)
    if obj_public_key is not None:
        public_key_from_obj = from_obj(
            obj_public_key,
            expected=[str],
            path=path + '.publicKey')  # type: Optional[str]
    else:
        public_key_from_obj = None

    obj_remember_me = obj.get('rememberMe', None)
    if obj_remember_me is not None:
        remember_me_from_obj = from_obj(
            obj_remember_me,
            expected=[bool],
            path=path + '.rememberMe')  # type: Optional[bool]
    else:
        remember_me_from_obj = None

    self_hosted_id_from_obj = obj.get('selfHostedID', None)

    obj_setup = obj.get('setup', None)
    if obj_setup is not None:
        setup_from_obj = from_obj(
            obj_setup,
            expected=[bool],
            path=path + '.setup')  # type: Optional[bool]
    else:
        setup_from_obj = None

    obj_subscription_referrer_code = obj.get('subscriptionReferrerCode', None)
    if obj_subscription_referrer_code is not None:
        subscription_referrer_code_from_obj = from_obj(
            obj_subscription_referrer_code,
            expected=[str],
            path=path + '.subscriptionReferrerCode')  # type: Optional[str]
    else:
        subscription_referrer_code_from_obj = None

    obj_time_zone = obj.get('timeZone', None)
    if obj_time_zone is not None:
        time_zone_from_obj = from_obj(
            obj_time_zone,
            expected=[str],
            path=path + '.timeZone')  # type: Optional[str]
    else:
        time_zone_from_obj = None

    obj_tos_accepted = obj.get('tosAccepted', None)
    if obj_tos_accepted is not None:
        tos_accepted_from_obj = from_obj(
            obj_tos_accepted,
            expected=[bool],
            path=path + '.tosAccepted')  # type: Optional[bool]
    else:
        tos_accepted_from_obj = None

    obj_totp_backup = obj.get('totpBackup', None)
    if obj_totp_backup is not None:
        totp_backup_from_obj = from_obj(
            obj_totp_backup,
            expected=[str],
            path=path + '.totpBackup')  # type: Optional[str]
    else:
        totp_backup_from_obj = None

    obj_totp_code = obj.get('totpCode', None)
    if obj_totp_code is not None:
        totp_code_from_obj = from_obj(
            obj_totp_code,
            expected=[str],
            path=path + '.totpCode')  # type: Optional[str]
    else:
        totp_code_from_obj = None

    obj_totp_enabled = obj.get('totpEnabled', None)
    if obj_totp_enabled is not None:
        totp_enabled_from_obj = from_obj(
            obj_totp_enabled,
            expected=[bool],
            path=path + '.totpEnabled')  # type: Optional[bool]
    else:
        totp_enabled_from_obj = None

    obj_totp_q_r = obj.get('totpQR', None)
    if obj_totp_q_r is not None:
        totp_q_r_from_obj = from_obj(
            obj_totp_q_r,
            expected=[str],
            path=path + '.totpQR')  # type: Optional[str]
    else:
        totp_q_r_from_obj = None

    obj_totp_secret = obj.get('totpSecret', None)
    if obj_totp_secret is not None:
        totp_secret_from_obj = from_obj(
            obj_totp_secret,
            expected=[str],
            path=path + '.totpSecret')  # type: Optional[str]
    else:
        totp_secret_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    obj_verified = obj.get('verified', None)
    if obj_verified is not None:
        verified_from_obj = from_obj(
            obj_verified,
            expected=[bool],
            path=path + '.verified')  # type: Optional[bool]
    else:
        verified_from_obj = None

    return AuthAccount(
        child=child_from_obj,
        collapsed_notes_pages=collapsed_notes_pages_from_obj,
        collapsed_plan_projects=collapsed_plan_projects_from_obj,
        collapsed_plan_tasks=collapsed_plan_tasks_from_obj,
        created=created_from_obj,
        daily_agenda_next=daily_agenda_next_from_obj,
        daily_agenda_time=daily_agenda_time_from_obj,
        email_address=email_address_from_obj,
        hide_calendar_i_calendars=hide_calendar_i_calendars_from_obj,
        icalendar_id=icalendar_id_from_obj,
        id=id_from_obj,
        last_activity=last_activity_from_obj,
        name=name_from_obj,
        oidc_code=oidc_code_from_obj,
        oidc_provider_source=oidc_provider_source_from_obj,
        oidc_provider_type=oidc_provider_type_from_obj,
        password=password_from_obj,
        password_reset_token=password_reset_token_from_obj,
        permissions_account=permissions_account_from_obj,
        permissions_households=permissions_households_from_obj,
        platform=platform_from_obj,
        preferences=preferences_from_obj,
        primary_auth_household_id=primary_auth_household_id_from_obj,
        private_keys=private_keys_from_obj,
        public_key=public_key_from_obj,
        remember_me=remember_me_from_obj,
        self_hosted_id=self_hosted_id_from_obj,
        setup=setup_from_obj,
        subscription_referrer_code=subscription_referrer_code_from_obj,
        time_zone=time_zone_from_obj,
        tos_accepted=tos_accepted_from_obj,
        totp_backup=totp_backup_from_obj,
        totp_code=totp_code_from_obj,
        totp_enabled=totp_enabled_from_obj,
        totp_q_r=totp_q_r_from_obj,
        totp_secret=totp_secret_from_obj,
        updated=updated_from_obj,
        verified=verified_from_obj)


def auth_account_to_jsonable(
        auth_account: AuthAccount,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthAccount.

    :param auth_account: instance of AuthAccount to be JSON-ized
    :param path: path to the auth_account used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_account.child is not None:
        res['child'] = auth_account.child

    if auth_account.collapsed_notes_pages is not None:
        res['collapsedNotesPages'] = to_jsonable(
        auth_account.collapsed_notes_pages,
        expected=[list, str],
        path='{}.collapsedNotesPages'.format(path))

    if auth_account.collapsed_plan_projects is not None:
        res['collapsedPlanProjects'] = to_jsonable(
        auth_account.collapsed_plan_projects,
        expected=[list, str],
        path='{}.collapsedPlanProjects'.format(path))

    if auth_account.collapsed_plan_tasks is not None:
        res['collapsedPlanTasks'] = to_jsonable(
        auth_account.collapsed_plan_tasks,
        expected=[list, str],
        path='{}.collapsedPlanTasks'.format(path))

    if auth_account.created is not None:
        res['created'] = auth_account.created

    if auth_account.daily_agenda_next is not None:
        res['dailyAgendaNext'] = auth_account.daily_agenda_next

    if auth_account.daily_agenda_time is not None:
        res['dailyAgendaTime'] = auth_account.daily_agenda_time

    if auth_account.email_address is not None:
        res['emailAddress'] = auth_account.email_address

    if auth_account.hide_calendar_i_calendars is not None:
        res['hideCalendarICalendars'] = to_jsonable(
        auth_account.hide_calendar_i_calendars,
        expected=[list, str],
        path='{}.hideCalendarICalendars'.format(path))

    if auth_account.icalendar_id is not None:
        res['icalendarID'] = auth_account.icalendar_id

    if auth_account.id is not None:
        res['id'] = auth_account.id

    if auth_account.last_activity is not None:
        res['lastActivity'] = auth_account.last_activity

    if auth_account.name is not None:
        res['name'] = auth_account.name

    if auth_account.oidc_code is not None:
        res['oidcCode'] = auth_account.oidc_code

    if auth_account.oidc_provider_source is not None:
        res['oidcProviderSource'] = auth_account.oidc_provider_source

    if auth_account.oidc_provider_type is not None:
        res['oidcProviderType'] = auth_account.oidc_provider_type

    if auth_account.password is not None:
        res['password'] = auth_account.password

    if auth_account.password_reset_token is not None:
        res['passwordResetToken'] = auth_account.password_reset_token

    if auth_account.permissions_account is not None:
        res['permissionsAccount'] = auth_account.permissions_account

    if auth_account.permissions_households is not None:
        res['permissionsHouseholds'] = to_jsonable(
        auth_account.permissions_households,
        expected=[list, AuthHouseholdPermissions],
        path='{}.permissionsHouseholds'.format(path))

    if auth_account.platform is not None:
        res['platform'] = auth_account.platform

    if auth_account.preferences is not None:
        res['preferences'] = auth_account.preferences

    if auth_account.primary_auth_household_id is not None:
        res['primaryAuthHouseholdID'] = auth_account.primary_auth_household_id

    if auth_account.private_keys is not None:
        res['privateKeys'] = to_jsonable(
        auth_account.private_keys,
        expected=[list, AuthAccountPrivateKey],
        path='{}.privateKeys'.format(path))

    if auth_account.public_key is not None:
        res['publicKey'] = auth_account.public_key

    if auth_account.remember_me is not None:
        res['rememberMe'] = auth_account.remember_me

    if auth_account.self_hosted_id is not None:
        res['selfHostedID'] = auth_account.self_hosted_id

    if auth_account.setup is not None:
        res['setup'] = auth_account.setup

    if auth_account.subscription_referrer_code is not None:
        res['subscriptionReferrerCode'] = auth_account.subscription_referrer_code

    if auth_account.time_zone is not None:
        res['timeZone'] = auth_account.time_zone

    if auth_account.tos_accepted is not None:
        res['tosAccepted'] = auth_account.tos_accepted

    if auth_account.totp_backup is not None:
        res['totpBackup'] = auth_account.totp_backup

    if auth_account.totp_code is not None:
        res['totpCode'] = auth_account.totp_code

    if auth_account.totp_enabled is not None:
        res['totpEnabled'] = auth_account.totp_enabled

    if auth_account.totp_q_r is not None:
        res['totpQR'] = auth_account.totp_q_r

    if auth_account.totp_secret is not None:
        res['totpSecret'] = auth_account.totp_secret

    if auth_account.updated is not None:
        res['updated'] = auth_account.updated

    if auth_account.verified is not None:
        res['verified'] = auth_account.verified

    return res


class AuthAccountPreferences:
    def __init__(
            self,
            color_accent: Optional[int] = None,
            color_negative: Optional[int] = None,
            color_positive: Optional[int] = None,
            color_primary: Optional[int] = None,
            color_secondary: Optional[int] = None,
            dark_mode: Optional[bool] = None,
            format_date_order: Optional[int] = None,
            format_date_separator: Optional[int] = None,
            format_time24: Optional[bool] = None,
            format_week8601: Optional[bool] = None,
            hide_calendar_budget_recurrences: Optional[bool] = None,
            hide_calendar_cook_meal_plans: Optional[bool] = None,
            hide_calendar_events: Optional[bool] = None,
            hide_calendar_health_logs: Optional[List[str]] = None,
            hide_calendar_plan_tasks: Optional[bool] = None,
            hide_components: Optional[List[str]] = None,
            ignore_device_calendar_event: Optional[bool] = None,
            ignore_device_plan_task: Optional[bool] = None,
            ignore_email_calendar_event: Optional[bool] = None,
            ignore_email_newsletter: Optional[bool] = None,
            ignore_email_plan_task: Optional[bool] = None,
            notifications_households: Optional[List['AuthAccountPreferencesNotificationsHousehold']] = None,
            show_calendar_event_astronomy: Optional[bool] = None,
            show_calendar_event_holidays_c_a: Optional[bool] = None,
            show_calendar_event_holidays_u_k: Optional[bool] = None,
            show_calendar_event_holidays_u_s: Optional[bool] = None) -> None:
        """Initializes with the given values."""
        self.color_accent = color_accent

        self.color_negative = color_negative

        self.color_positive = color_positive

        self.color_primary = color_primary

        self.color_secondary = color_secondary

        self.dark_mode = dark_mode

        self.format_date_order = format_date_order

        self.format_date_separator = format_date_separator

        self.format_time24 = format_time24

        self.format_week8601 = format_week8601

        self.hide_calendar_budget_recurrences = hide_calendar_budget_recurrences

        self.hide_calendar_cook_meal_plans = hide_calendar_cook_meal_plans

        self.hide_calendar_events = hide_calendar_events

        self.hide_calendar_health_logs = hide_calendar_health_logs

        self.hide_calendar_plan_tasks = hide_calendar_plan_tasks

        self.hide_components = hide_components

        self.ignore_device_calendar_event = ignore_device_calendar_event

        self.ignore_device_plan_task = ignore_device_plan_task

        self.ignore_email_calendar_event = ignore_email_calendar_event

        self.ignore_email_newsletter = ignore_email_newsletter

        self.ignore_email_plan_task = ignore_email_plan_task

        self.notifications_households = notifications_households

        self.show_calendar_event_astronomy = show_calendar_event_astronomy

        # nolint: tagliatelle
        self.show_calendar_event_holidays_c_a = show_calendar_event_holidays_c_a

        # nolint: tagliatelle
        self.show_calendar_event_holidays_u_k = show_calendar_event_holidays_u_k

        # nolint: tagliatelle
        self.show_calendar_event_holidays_u_s = show_calendar_event_holidays_u_s

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_account_preferences_to_jsonable.

        :return: JSON-able representation
        """
        return auth_account_preferences_to_jsonable(self)


def new_auth_account_preferences() -> AuthAccountPreferences:
    """Generates an instance of AuthAccountPreferences with default values."""
    return AuthAccountPreferences()


def auth_account_preferences_from_obj(obj: Any, path: str = "") -> AuthAccountPreferences:
    """
    Generates an instance of AuthAccountPreferences from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthAccountPreferences
    :param path: path to the object used for debugging
    :return: parsed instance of AuthAccountPreferences
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_color_accent = obj.get('colorAccent', None)
    if obj_color_accent is not None:
        color_accent_from_obj = from_obj(
            obj_color_accent,
            expected=[int],
            path=path + '.colorAccent')  # type: Optional[int]
    else:
        color_accent_from_obj = None

    obj_color_negative = obj.get('colorNegative', None)
    if obj_color_negative is not None:
        color_negative_from_obj = from_obj(
            obj_color_negative,
            expected=[int],
            path=path + '.colorNegative')  # type: Optional[int]
    else:
        color_negative_from_obj = None

    obj_color_positive = obj.get('colorPositive', None)
    if obj_color_positive is not None:
        color_positive_from_obj = from_obj(
            obj_color_positive,
            expected=[int],
            path=path + '.colorPositive')  # type: Optional[int]
    else:
        color_positive_from_obj = None

    obj_color_primary = obj.get('colorPrimary', None)
    if obj_color_primary is not None:
        color_primary_from_obj = from_obj(
            obj_color_primary,
            expected=[int],
            path=path + '.colorPrimary')  # type: Optional[int]
    else:
        color_primary_from_obj = None

    obj_color_secondary = obj.get('colorSecondary', None)
    if obj_color_secondary is not None:
        color_secondary_from_obj = from_obj(
            obj_color_secondary,
            expected=[int],
            path=path + '.colorSecondary')  # type: Optional[int]
    else:
        color_secondary_from_obj = None

    obj_dark_mode = obj.get('darkMode', None)
    if obj_dark_mode is not None:
        dark_mode_from_obj = from_obj(
            obj_dark_mode,
            expected=[bool],
            path=path + '.darkMode')  # type: Optional[bool]
    else:
        dark_mode_from_obj = None

    obj_format_date_order = obj.get('formatDateOrder', None)
    if obj_format_date_order is not None:
        format_date_order_from_obj = from_obj(
            obj_format_date_order,
            expected=[int],
            path=path + '.formatDateOrder')  # type: Optional[int]
    else:
        format_date_order_from_obj = None

    obj_format_date_separator = obj.get('formatDateSeparator', None)
    if obj_format_date_separator is not None:
        format_date_separator_from_obj = from_obj(
            obj_format_date_separator,
            expected=[int],
            path=path + '.formatDateSeparator')  # type: Optional[int]
    else:
        format_date_separator_from_obj = None

    obj_format_time24 = obj.get('formatTime24', None)
    if obj_format_time24 is not None:
        format_time24_from_obj = from_obj(
            obj_format_time24,
            expected=[bool],
            path=path + '.formatTime24')  # type: Optional[bool]
    else:
        format_time24_from_obj = None

    obj_format_week8601 = obj.get('formatWeek8601', None)
    if obj_format_week8601 is not None:
        format_week8601_from_obj = from_obj(
            obj_format_week8601,
            expected=[bool],
            path=path + '.formatWeek8601')  # type: Optional[bool]
    else:
        format_week8601_from_obj = None

    obj_hide_calendar_budget_recurrences = obj.get('hideCalendarBudgetRecurrences', None)
    if obj_hide_calendar_budget_recurrences is not None:
        hide_calendar_budget_recurrences_from_obj = from_obj(
            obj_hide_calendar_budget_recurrences,
            expected=[bool],
            path=path + '.hideCalendarBudgetRecurrences')  # type: Optional[bool]
    else:
        hide_calendar_budget_recurrences_from_obj = None

    obj_hide_calendar_cook_meal_plans = obj.get('hideCalendarCookMealPlans', None)
    if obj_hide_calendar_cook_meal_plans is not None:
        hide_calendar_cook_meal_plans_from_obj = from_obj(
            obj_hide_calendar_cook_meal_plans,
            expected=[bool],
            path=path + '.hideCalendarCookMealPlans')  # type: Optional[bool]
    else:
        hide_calendar_cook_meal_plans_from_obj = None

    obj_hide_calendar_events = obj.get('hideCalendarEvents', None)
    if obj_hide_calendar_events is not None:
        hide_calendar_events_from_obj = from_obj(
            obj_hide_calendar_events,
            expected=[bool],
            path=path + '.hideCalendarEvents')  # type: Optional[bool]
    else:
        hide_calendar_events_from_obj = None

    obj_hide_calendar_health_logs = obj.get('hideCalendarHealthLogs', None)
    if obj_hide_calendar_health_logs is not None:
        hide_calendar_health_logs_from_obj = from_obj(
            obj_hide_calendar_health_logs,
            expected=[list, str],
            path=path + '.hideCalendarHealthLogs')  # type: Optional[List[str]]
    else:
        hide_calendar_health_logs_from_obj = None

    obj_hide_calendar_plan_tasks = obj.get('hideCalendarPlanTasks', None)
    if obj_hide_calendar_plan_tasks is not None:
        hide_calendar_plan_tasks_from_obj = from_obj(
            obj_hide_calendar_plan_tasks,
            expected=[bool],
            path=path + '.hideCalendarPlanTasks')  # type: Optional[bool]
    else:
        hide_calendar_plan_tasks_from_obj = None

    obj_hide_components = obj.get('hideComponents', None)
    if obj_hide_components is not None:
        hide_components_from_obj = from_obj(
            obj_hide_components,
            expected=[list, str],
            path=path + '.hideComponents')  # type: Optional[List[str]]
    else:
        hide_components_from_obj = None

    obj_ignore_device_calendar_event = obj.get('ignoreDeviceCalendarEvent', None)
    if obj_ignore_device_calendar_event is not None:
        ignore_device_calendar_event_from_obj = from_obj(
            obj_ignore_device_calendar_event,
            expected=[bool],
            path=path + '.ignoreDeviceCalendarEvent')  # type: Optional[bool]
    else:
        ignore_device_calendar_event_from_obj = None

    obj_ignore_device_plan_task = obj.get('ignoreDevicePlanTask', None)
    if obj_ignore_device_plan_task is not None:
        ignore_device_plan_task_from_obj = from_obj(
            obj_ignore_device_plan_task,
            expected=[bool],
            path=path + '.ignoreDevicePlanTask')  # type: Optional[bool]
    else:
        ignore_device_plan_task_from_obj = None

    obj_ignore_email_calendar_event = obj.get('ignoreEmailCalendarEvent', None)
    if obj_ignore_email_calendar_event is not None:
        ignore_email_calendar_event_from_obj = from_obj(
            obj_ignore_email_calendar_event,
            expected=[bool],
            path=path + '.ignoreEmailCalendarEvent')  # type: Optional[bool]
    else:
        ignore_email_calendar_event_from_obj = None

    obj_ignore_email_newsletter = obj.get('ignoreEmailNewsletter', None)
    if obj_ignore_email_newsletter is not None:
        ignore_email_newsletter_from_obj = from_obj(
            obj_ignore_email_newsletter,
            expected=[bool],
            path=path + '.ignoreEmailNewsletter')  # type: Optional[bool]
    else:
        ignore_email_newsletter_from_obj = None

    obj_ignore_email_plan_task = obj.get('ignoreEmailPlanTask', None)
    if obj_ignore_email_plan_task is not None:
        ignore_email_plan_task_from_obj = from_obj(
            obj_ignore_email_plan_task,
            expected=[bool],
            path=path + '.ignoreEmailPlanTask')  # type: Optional[bool]
    else:
        ignore_email_plan_task_from_obj = None

    obj_notifications_households = obj.get('notificationsHouseholds', None)
    if obj_notifications_households is not None:
        notifications_households_from_obj = from_obj(
            obj_notifications_households,
            expected=[list, AuthAccountPreferencesNotificationsHousehold],
            path=path + '.notificationsHouseholds')  # type: Optional[List['AuthAccountPreferencesNotificationsHousehold']]
    else:
        notifications_households_from_obj = None

    obj_show_calendar_event_astronomy = obj.get('showCalendarEventAstronomy', None)
    if obj_show_calendar_event_astronomy is not None:
        show_calendar_event_astronomy_from_obj = from_obj(
            obj_show_calendar_event_astronomy,
            expected=[bool],
            path=path + '.showCalendarEventAstronomy')  # type: Optional[bool]
    else:
        show_calendar_event_astronomy_from_obj = None

    obj_show_calendar_event_holidays_c_a = obj.get('showCalendarEventHolidaysCA', None)
    if obj_show_calendar_event_holidays_c_a is not None:
        show_calendar_event_holidays_c_a_from_obj = from_obj(
            obj_show_calendar_event_holidays_c_a,
            expected=[bool],
            path=path + '.showCalendarEventHolidaysCA')  # type: Optional[bool]
    else:
        show_calendar_event_holidays_c_a_from_obj = None

    obj_show_calendar_event_holidays_u_k = obj.get('showCalendarEventHolidaysUK', None)
    if obj_show_calendar_event_holidays_u_k is not None:
        show_calendar_event_holidays_u_k_from_obj = from_obj(
            obj_show_calendar_event_holidays_u_k,
            expected=[bool],
            path=path + '.showCalendarEventHolidaysUK')  # type: Optional[bool]
    else:
        show_calendar_event_holidays_u_k_from_obj = None

    obj_show_calendar_event_holidays_u_s = obj.get('showCalendarEventHolidaysUS', None)
    if obj_show_calendar_event_holidays_u_s is not None:
        show_calendar_event_holidays_u_s_from_obj = from_obj(
            obj_show_calendar_event_holidays_u_s,
            expected=[bool],
            path=path + '.showCalendarEventHolidaysUS')  # type: Optional[bool]
    else:
        show_calendar_event_holidays_u_s_from_obj = None

    return AuthAccountPreferences(
        color_accent=color_accent_from_obj,
        color_negative=color_negative_from_obj,
        color_positive=color_positive_from_obj,
        color_primary=color_primary_from_obj,
        color_secondary=color_secondary_from_obj,
        dark_mode=dark_mode_from_obj,
        format_date_order=format_date_order_from_obj,
        format_date_separator=format_date_separator_from_obj,
        format_time24=format_time24_from_obj,
        format_week8601=format_week8601_from_obj,
        hide_calendar_budget_recurrences=hide_calendar_budget_recurrences_from_obj,
        hide_calendar_cook_meal_plans=hide_calendar_cook_meal_plans_from_obj,
        hide_calendar_events=hide_calendar_events_from_obj,
        hide_calendar_health_logs=hide_calendar_health_logs_from_obj,
        hide_calendar_plan_tasks=hide_calendar_plan_tasks_from_obj,
        hide_components=hide_components_from_obj,
        ignore_device_calendar_event=ignore_device_calendar_event_from_obj,
        ignore_device_plan_task=ignore_device_plan_task_from_obj,
        ignore_email_calendar_event=ignore_email_calendar_event_from_obj,
        ignore_email_newsletter=ignore_email_newsletter_from_obj,
        ignore_email_plan_task=ignore_email_plan_task_from_obj,
        notifications_households=notifications_households_from_obj,
        show_calendar_event_astronomy=show_calendar_event_astronomy_from_obj,
        show_calendar_event_holidays_c_a=show_calendar_event_holidays_c_a_from_obj,
        show_calendar_event_holidays_u_k=show_calendar_event_holidays_u_k_from_obj,
        show_calendar_event_holidays_u_s=show_calendar_event_holidays_u_s_from_obj)


def auth_account_preferences_to_jsonable(
        auth_account_preferences: AuthAccountPreferences,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthAccountPreferences.

    :param auth_account_preferences: instance of AuthAccountPreferences to be JSON-ized
    :param path: path to the auth_account_preferences used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_account_preferences.color_accent is not None:
        res['colorAccent'] = auth_account_preferences.color_accent

    if auth_account_preferences.color_negative is not None:
        res['colorNegative'] = auth_account_preferences.color_negative

    if auth_account_preferences.color_positive is not None:
        res['colorPositive'] = auth_account_preferences.color_positive

    if auth_account_preferences.color_primary is not None:
        res['colorPrimary'] = auth_account_preferences.color_primary

    if auth_account_preferences.color_secondary is not None:
        res['colorSecondary'] = auth_account_preferences.color_secondary

    if auth_account_preferences.dark_mode is not None:
        res['darkMode'] = auth_account_preferences.dark_mode

    if auth_account_preferences.format_date_order is not None:
        res['formatDateOrder'] = auth_account_preferences.format_date_order

    if auth_account_preferences.format_date_separator is not None:
        res['formatDateSeparator'] = auth_account_preferences.format_date_separator

    if auth_account_preferences.format_time24 is not None:
        res['formatTime24'] = auth_account_preferences.format_time24

    if auth_account_preferences.format_week8601 is not None:
        res['formatWeek8601'] = auth_account_preferences.format_week8601

    if auth_account_preferences.hide_calendar_budget_recurrences is not None:
        res['hideCalendarBudgetRecurrences'] = auth_account_preferences.hide_calendar_budget_recurrences

    if auth_account_preferences.hide_calendar_cook_meal_plans is not None:
        res['hideCalendarCookMealPlans'] = auth_account_preferences.hide_calendar_cook_meal_plans

    if auth_account_preferences.hide_calendar_events is not None:
        res['hideCalendarEvents'] = auth_account_preferences.hide_calendar_events

    if auth_account_preferences.hide_calendar_health_logs is not None:
        res['hideCalendarHealthLogs'] = to_jsonable(
        auth_account_preferences.hide_calendar_health_logs,
        expected=[list, str],
        path='{}.hideCalendarHealthLogs'.format(path))

    if auth_account_preferences.hide_calendar_plan_tasks is not None:
        res['hideCalendarPlanTasks'] = auth_account_preferences.hide_calendar_plan_tasks

    if auth_account_preferences.hide_components is not None:
        res['hideComponents'] = to_jsonable(
        auth_account_preferences.hide_components,
        expected=[list, str],
        path='{}.hideComponents'.format(path))

    if auth_account_preferences.ignore_device_calendar_event is not None:
        res['ignoreDeviceCalendarEvent'] = auth_account_preferences.ignore_device_calendar_event

    if auth_account_preferences.ignore_device_plan_task is not None:
        res['ignoreDevicePlanTask'] = auth_account_preferences.ignore_device_plan_task

    if auth_account_preferences.ignore_email_calendar_event is not None:
        res['ignoreEmailCalendarEvent'] = auth_account_preferences.ignore_email_calendar_event

    if auth_account_preferences.ignore_email_newsletter is not None:
        res['ignoreEmailNewsletter'] = auth_account_preferences.ignore_email_newsletter

    if auth_account_preferences.ignore_email_plan_task is not None:
        res['ignoreEmailPlanTask'] = auth_account_preferences.ignore_email_plan_task

    if auth_account_preferences.notifications_households is not None:
        res['notificationsHouseholds'] = to_jsonable(
        auth_account_preferences.notifications_households,
        expected=[list, AuthAccountPreferencesNotificationsHousehold],
        path='{}.notificationsHouseholds'.format(path))

    if auth_account_preferences.show_calendar_event_astronomy is not None:
        res['showCalendarEventAstronomy'] = auth_account_preferences.show_calendar_event_astronomy

    if auth_account_preferences.show_calendar_event_holidays_c_a is not None:
        res['showCalendarEventHolidaysCA'] = auth_account_preferences.show_calendar_event_holidays_c_a

    if auth_account_preferences.show_calendar_event_holidays_u_k is not None:
        res['showCalendarEventHolidaysUK'] = auth_account_preferences.show_calendar_event_holidays_u_k

    if auth_account_preferences.show_calendar_event_holidays_u_s is not None:
        res['showCalendarEventHolidaysUS'] = auth_account_preferences.show_calendar_event_holidays_u_s

    return res


class AuthAccountPreferencesNotificationsHousehold:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            ignore_device_calendar_event: Optional[bool] = None,
            ignore_device_cook_meal_plan_cook: Optional[bool] = None,
            ignore_device_cook_meal_plan_prep: Optional[bool] = None,
            ignore_device_plan_task: Optional[bool] = None,
            ignore_device_plan_task_complete: Optional[bool] = None,
            ignore_email_calendar_event: Optional[bool] = None,
            ignore_email_cook_meal_plan_cook: Optional[bool] = None,
            ignore_email_cook_meal_plan_prep: Optional[bool] = None,
            ignore_email_plan_task: Optional[bool] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.ignore_device_calendar_event = ignore_device_calendar_event

        self.ignore_device_cook_meal_plan_cook = ignore_device_cook_meal_plan_cook

        self.ignore_device_cook_meal_plan_prep = ignore_device_cook_meal_plan_prep

        self.ignore_device_plan_task = ignore_device_plan_task

        self.ignore_device_plan_task_complete = ignore_device_plan_task_complete

        self.ignore_email_calendar_event = ignore_email_calendar_event

        self.ignore_email_cook_meal_plan_cook = ignore_email_cook_meal_plan_cook

        self.ignore_email_cook_meal_plan_prep = ignore_email_cook_meal_plan_prep

        self.ignore_email_plan_task = ignore_email_plan_task

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_account_preferences_notifications_household_to_jsonable.

        :return: JSON-able representation
        """
        return auth_account_preferences_notifications_household_to_jsonable(self)


def new_auth_account_preferences_notifications_household() -> AuthAccountPreferencesNotificationsHousehold:
    """Generates an instance of AuthAccountPreferencesNotificationsHousehold with default values."""
    return AuthAccountPreferencesNotificationsHousehold()


def auth_account_preferences_notifications_household_from_obj(obj: Any, path: str = "") -> AuthAccountPreferencesNotificationsHousehold:
    """
    Generates an instance of AuthAccountPreferencesNotificationsHousehold from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthAccountPreferencesNotificationsHousehold
    :param path: path to the object used for debugging
    :return: parsed instance of AuthAccountPreferencesNotificationsHousehold
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_ignore_device_calendar_event = obj.get('ignoreDeviceCalendarEvent', None)
    if obj_ignore_device_calendar_event is not None:
        ignore_device_calendar_event_from_obj = from_obj(
            obj_ignore_device_calendar_event,
            expected=[bool],
            path=path + '.ignoreDeviceCalendarEvent')  # type: Optional[bool]
    else:
        ignore_device_calendar_event_from_obj = None

    obj_ignore_device_cook_meal_plan_cook = obj.get('ignoreDeviceCookMealPlanCook', None)
    if obj_ignore_device_cook_meal_plan_cook is not None:
        ignore_device_cook_meal_plan_cook_from_obj = from_obj(
            obj_ignore_device_cook_meal_plan_cook,
            expected=[bool],
            path=path + '.ignoreDeviceCookMealPlanCook')  # type: Optional[bool]
    else:
        ignore_device_cook_meal_plan_cook_from_obj = None

    obj_ignore_device_cook_meal_plan_prep = obj.get('ignoreDeviceCookMealPlanPrep', None)
    if obj_ignore_device_cook_meal_plan_prep is not None:
        ignore_device_cook_meal_plan_prep_from_obj = from_obj(
            obj_ignore_device_cook_meal_plan_prep,
            expected=[bool],
            path=path + '.ignoreDeviceCookMealPlanPrep')  # type: Optional[bool]
    else:
        ignore_device_cook_meal_plan_prep_from_obj = None

    obj_ignore_device_plan_task = obj.get('ignoreDevicePlanTask', None)
    if obj_ignore_device_plan_task is not None:
        ignore_device_plan_task_from_obj = from_obj(
            obj_ignore_device_plan_task,
            expected=[bool],
            path=path + '.ignoreDevicePlanTask')  # type: Optional[bool]
    else:
        ignore_device_plan_task_from_obj = None

    obj_ignore_device_plan_task_complete = obj.get('ignoreDevicePlanTaskComplete', None)
    if obj_ignore_device_plan_task_complete is not None:
        ignore_device_plan_task_complete_from_obj = from_obj(
            obj_ignore_device_plan_task_complete,
            expected=[bool],
            path=path + '.ignoreDevicePlanTaskComplete')  # type: Optional[bool]
    else:
        ignore_device_plan_task_complete_from_obj = None

    obj_ignore_email_calendar_event = obj.get('ignoreEmailCalendarEvent', None)
    if obj_ignore_email_calendar_event is not None:
        ignore_email_calendar_event_from_obj = from_obj(
            obj_ignore_email_calendar_event,
            expected=[bool],
            path=path + '.ignoreEmailCalendarEvent')  # type: Optional[bool]
    else:
        ignore_email_calendar_event_from_obj = None

    obj_ignore_email_cook_meal_plan_cook = obj.get('ignoreEmailCookMealPlanCook', None)
    if obj_ignore_email_cook_meal_plan_cook is not None:
        ignore_email_cook_meal_plan_cook_from_obj = from_obj(
            obj_ignore_email_cook_meal_plan_cook,
            expected=[bool],
            path=path + '.ignoreEmailCookMealPlanCook')  # type: Optional[bool]
    else:
        ignore_email_cook_meal_plan_cook_from_obj = None

    obj_ignore_email_cook_meal_plan_prep = obj.get('ignoreEmailCookMealPlanPrep', None)
    if obj_ignore_email_cook_meal_plan_prep is not None:
        ignore_email_cook_meal_plan_prep_from_obj = from_obj(
            obj_ignore_email_cook_meal_plan_prep,
            expected=[bool],
            path=path + '.ignoreEmailCookMealPlanPrep')  # type: Optional[bool]
    else:
        ignore_email_cook_meal_plan_prep_from_obj = None

    obj_ignore_email_plan_task = obj.get('ignoreEmailPlanTask', None)
    if obj_ignore_email_plan_task is not None:
        ignore_email_plan_task_from_obj = from_obj(
            obj_ignore_email_plan_task,
            expected=[bool],
            path=path + '.ignoreEmailPlanTask')  # type: Optional[bool]
    else:
        ignore_email_plan_task_from_obj = None

    return AuthAccountPreferencesNotificationsHousehold(
        auth_household_id=auth_household_id_from_obj,
        ignore_device_calendar_event=ignore_device_calendar_event_from_obj,
        ignore_device_cook_meal_plan_cook=ignore_device_cook_meal_plan_cook_from_obj,
        ignore_device_cook_meal_plan_prep=ignore_device_cook_meal_plan_prep_from_obj,
        ignore_device_plan_task=ignore_device_plan_task_from_obj,
        ignore_device_plan_task_complete=ignore_device_plan_task_complete_from_obj,
        ignore_email_calendar_event=ignore_email_calendar_event_from_obj,
        ignore_email_cook_meal_plan_cook=ignore_email_cook_meal_plan_cook_from_obj,
        ignore_email_cook_meal_plan_prep=ignore_email_cook_meal_plan_prep_from_obj,
        ignore_email_plan_task=ignore_email_plan_task_from_obj)


def auth_account_preferences_notifications_household_to_jsonable(
        auth_account_preferences_notifications_household: AuthAccountPreferencesNotificationsHousehold,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthAccountPreferencesNotificationsHousehold.

    :param auth_account_preferences_notifications_household: instance of AuthAccountPreferencesNotificationsHousehold to be JSON-ized
    :param path: path to the auth_account_preferences_notifications_household used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_account_preferences_notifications_household.auth_household_id is not None:
        res['authHouseholdID'] = auth_account_preferences_notifications_household.auth_household_id

    if auth_account_preferences_notifications_household.ignore_device_calendar_event is not None:
        res['ignoreDeviceCalendarEvent'] = auth_account_preferences_notifications_household.ignore_device_calendar_event

    if auth_account_preferences_notifications_household.ignore_device_cook_meal_plan_cook is not None:
        res['ignoreDeviceCookMealPlanCook'] = auth_account_preferences_notifications_household.ignore_device_cook_meal_plan_cook

    if auth_account_preferences_notifications_household.ignore_device_cook_meal_plan_prep is not None:
        res['ignoreDeviceCookMealPlanPrep'] = auth_account_preferences_notifications_household.ignore_device_cook_meal_plan_prep

    if auth_account_preferences_notifications_household.ignore_device_plan_task is not None:
        res['ignoreDevicePlanTask'] = auth_account_preferences_notifications_household.ignore_device_plan_task

    if auth_account_preferences_notifications_household.ignore_device_plan_task_complete is not None:
        res['ignoreDevicePlanTaskComplete'] = auth_account_preferences_notifications_household.ignore_device_plan_task_complete

    if auth_account_preferences_notifications_household.ignore_email_calendar_event is not None:
        res['ignoreEmailCalendarEvent'] = auth_account_preferences_notifications_household.ignore_email_calendar_event

    if auth_account_preferences_notifications_household.ignore_email_cook_meal_plan_cook is not None:
        res['ignoreEmailCookMealPlanCook'] = auth_account_preferences_notifications_household.ignore_email_cook_meal_plan_cook

    if auth_account_preferences_notifications_household.ignore_email_cook_meal_plan_prep is not None:
        res['ignoreEmailCookMealPlanPrep'] = auth_account_preferences_notifications_household.ignore_email_cook_meal_plan_prep

    if auth_account_preferences_notifications_household.ignore_email_plan_task is not None:
        res['ignoreEmailPlanTask'] = auth_account_preferences_notifications_household.ignore_email_plan_task

    return res


class AuthAccountPrivateKey:
    def __init__(
            self,
            key: Optional['EncryptionEncryptedValue'] = None,
            name: Optional[str] = None,
            provider: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.key = key

        self.name = name

        self.provider = provider

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_account_private_key_to_jsonable.

        :return: JSON-able representation
        """
        return auth_account_private_key_to_jsonable(self)


def new_auth_account_private_key() -> AuthAccountPrivateKey:
    """Generates an instance of AuthAccountPrivateKey with default values."""
    return AuthAccountPrivateKey()


def auth_account_private_key_from_obj(obj: Any, path: str = "") -> AuthAccountPrivateKey:
    """
    Generates an instance of AuthAccountPrivateKey from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthAccountPrivateKey
    :param path: path to the object used for debugging
    :return: parsed instance of AuthAccountPrivateKey
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_key = obj.get('key', None)
    if obj_key is not None:
        key_from_obj = from_obj(
            obj_key,
            expected=[EncryptionEncryptedValue],
            path=path + '.key')  # type: Optional['EncryptionEncryptedValue']
    else:
        key_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_provider = obj.get('provider', None)
    if obj_provider is not None:
        provider_from_obj = from_obj(
            obj_provider,
            expected=[str],
            path=path + '.provider')  # type: Optional[str]
    else:
        provider_from_obj = None

    return AuthAccountPrivateKey(
        key=key_from_obj,
        name=name_from_obj,
        provider=provider_from_obj)


def auth_account_private_key_to_jsonable(
        auth_account_private_key: AuthAccountPrivateKey,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthAccountPrivateKey.

    :param auth_account_private_key: instance of AuthAccountPrivateKey to be JSON-ized
    :param path: path to the auth_account_private_key used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_account_private_key.key is not None:
        res['key'] = to_jsonable(
        auth_account_private_key.key,
        expected=[EncryptionEncryptedValue],
        path='{}.key'.format(path))

    if auth_account_private_key.name is not None:
        res['name'] = auth_account_private_key.name

    if auth_account_private_key.provider is not None:
        res['provider'] = auth_account_private_key.provider

    return res


class AuthHousehold:
    def __init__(
            self,
            backup_encryption_key: Optional[str] = None,
            cloud_push_notifications: Optional[bool] = None,
            count_members: Optional[int] = None,
            created: Optional[str] = None,
            demo: Optional[bool] = None,
            feature_votes: Optional[List['AuthHouseholdFeatureVote']] = None,
            id: Optional[str] = None,
            members: Optional[List['AuthHouseholdMember']] = None,
            name: Optional[str] = None,
            preferences: Optional['AuthHouseholdPreferences'] = None,
            self_hosted_id: Optional['UuidNullUUID'] = None,
            self_hosted_url: Optional[str] = None,
            subscription_customer_id: Optional[str] = None,
            subscription_expires: Optional[str] = None,
            subscription_id: Optional[str] = None,
            subscription_last_transaction_id: Optional[str] = None,
            subscription_processor: Optional[int] = None,
            subscription_referral_code: Optional[str] = None,
            subscription_referral_count: Optional[int] = None,
            subscription_referrer_code: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.backup_encryption_key = backup_encryption_key

        self.cloud_push_notifications = cloud_push_notifications

        self.count_members = count_members

        self.created = created

        self.demo = demo

        self.feature_votes = feature_votes

        self.id = id

        self.members = members

        self.name = name

        self.preferences = preferences

        self.self_hosted_id = self_hosted_id

        self.self_hosted_url = self_hosted_url

        self.subscription_customer_id = subscription_customer_id

        self.subscription_expires = subscription_expires

        self.subscription_id = subscription_id

        self.subscription_last_transaction_id = subscription_last_transaction_id

        self.subscription_processor = subscription_processor

        self.subscription_referral_code = subscription_referral_code

        self.subscription_referral_count = subscription_referral_count

        self.subscription_referrer_code = subscription_referrer_code

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_household_to_jsonable.

        :return: JSON-able representation
        """
        return auth_household_to_jsonable(self)


def new_auth_household() -> AuthHousehold:
    """Generates an instance of AuthHousehold with default values."""
    return AuthHousehold()


def auth_household_from_obj(obj: Any, path: str = "") -> AuthHousehold:
    """
    Generates an instance of AuthHousehold from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthHousehold
    :param path: path to the object used for debugging
    :return: parsed instance of AuthHousehold
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_backup_encryption_key = obj.get('backupEncryptionKey', None)
    if obj_backup_encryption_key is not None:
        backup_encryption_key_from_obj = from_obj(
            obj_backup_encryption_key,
            expected=[str],
            path=path + '.backupEncryptionKey')  # type: Optional[str]
    else:
        backup_encryption_key_from_obj = None

    obj_cloud_push_notifications = obj.get('cloudPushNotifications', None)
    if obj_cloud_push_notifications is not None:
        cloud_push_notifications_from_obj = from_obj(
            obj_cloud_push_notifications,
            expected=[bool],
            path=path + '.cloudPushNotifications')  # type: Optional[bool]
    else:
        cloud_push_notifications_from_obj = None

    obj_count_members = obj.get('countMembers', None)
    if obj_count_members is not None:
        count_members_from_obj = from_obj(
            obj_count_members,
            expected=[int],
            path=path + '.countMembers')  # type: Optional[int]
    else:
        count_members_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_demo = obj.get('demo', None)
    if obj_demo is not None:
        demo_from_obj = from_obj(
            obj_demo,
            expected=[bool],
            path=path + '.demo')  # type: Optional[bool]
    else:
        demo_from_obj = None

    obj_feature_votes = obj.get('featureVotes', None)
    if obj_feature_votes is not None:
        feature_votes_from_obj = from_obj(
            obj_feature_votes,
            expected=[list, AuthHouseholdFeatureVote],
            path=path + '.featureVotes')  # type: Optional[List['AuthHouseholdFeatureVote']]
    else:
        feature_votes_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_members = obj.get('members', None)
    if obj_members is not None:
        members_from_obj = from_obj(
            obj_members,
            expected=[list, AuthHouseholdMember],
            path=path + '.members')  # type: Optional[List['AuthHouseholdMember']]
    else:
        members_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_preferences = obj.get('preferences', None)
    if obj_preferences is not None:
        preferences_from_obj = from_obj(
            obj_preferences,
            expected=[AuthHouseholdPreferences],
            path=path + '.preferences')  # type: Optional['AuthHouseholdPreferences']
    else:
        preferences_from_obj = None

    obj_self_hosted_id = obj.get('selfHostedID', None)
    if obj_self_hosted_id is not None:
        self_hosted_id_from_obj = from_obj(
            obj_self_hosted_id,
            expected=[UuidNullUUID],
            path=path + '.selfHostedID')  # type: Optional['UuidNullUUID']
    else:
        self_hosted_id_from_obj = None

    obj_self_hosted_url = obj.get('selfHostedURL', None)
    if obj_self_hosted_url is not None:
        self_hosted_url_from_obj = from_obj(
            obj_self_hosted_url,
            expected=[str],
            path=path + '.selfHostedURL')  # type: Optional[str]
    else:
        self_hosted_url_from_obj = None

    obj_subscription_customer_id = obj.get('subscriptionCustomerID', None)
    if obj_subscription_customer_id is not None:
        subscription_customer_id_from_obj = from_obj(
            obj_subscription_customer_id,
            expected=[str],
            path=path + '.subscriptionCustomerID')  # type: Optional[str]
    else:
        subscription_customer_id_from_obj = None

    obj_subscription_expires = obj.get('subscriptionExpires', None)
    if obj_subscription_expires is not None:
        subscription_expires_from_obj = from_obj(
            obj_subscription_expires,
            expected=[str],
            path=path + '.subscriptionExpires')  # type: Optional[str]
    else:
        subscription_expires_from_obj = None

    obj_subscription_id = obj.get('subscriptionID', None)
    if obj_subscription_id is not None:
        subscription_id_from_obj = from_obj(
            obj_subscription_id,
            expected=[str],
            path=path + '.subscriptionID')  # type: Optional[str]
    else:
        subscription_id_from_obj = None

    obj_subscription_last_transaction_id = obj.get('subscriptionLastTransactionID', None)
    if obj_subscription_last_transaction_id is not None:
        subscription_last_transaction_id_from_obj = from_obj(
            obj_subscription_last_transaction_id,
            expected=[str],
            path=path + '.subscriptionLastTransactionID')  # type: Optional[str]
    else:
        subscription_last_transaction_id_from_obj = None

    obj_subscription_processor = obj.get('subscriptionProcessor', None)
    if obj_subscription_processor is not None:
        subscription_processor_from_obj = from_obj(
            obj_subscription_processor,
            expected=[int],
            path=path + '.subscriptionProcessor')  # type: Optional[int]
    else:
        subscription_processor_from_obj = None

    obj_subscription_referral_code = obj.get('subscriptionReferralCode', None)
    if obj_subscription_referral_code is not None:
        subscription_referral_code_from_obj = from_obj(
            obj_subscription_referral_code,
            expected=[str],
            path=path + '.subscriptionReferralCode')  # type: Optional[str]
    else:
        subscription_referral_code_from_obj = None

    obj_subscription_referral_count = obj.get('subscriptionReferralCount', None)
    if obj_subscription_referral_count is not None:
        subscription_referral_count_from_obj = from_obj(
            obj_subscription_referral_count,
            expected=[int],
            path=path + '.subscriptionReferralCount')  # type: Optional[int]
    else:
        subscription_referral_count_from_obj = None

    obj_subscription_referrer_code = obj.get('subscriptionReferrerCode', None)
    if obj_subscription_referrer_code is not None:
        subscription_referrer_code_from_obj = from_obj(
            obj_subscription_referrer_code,
            expected=[str],
            path=path + '.subscriptionReferrerCode')  # type: Optional[str]
    else:
        subscription_referrer_code_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return AuthHousehold(
        backup_encryption_key=backup_encryption_key_from_obj,
        cloud_push_notifications=cloud_push_notifications_from_obj,
        count_members=count_members_from_obj,
        created=created_from_obj,
        demo=demo_from_obj,
        feature_votes=feature_votes_from_obj,
        id=id_from_obj,
        members=members_from_obj,
        name=name_from_obj,
        preferences=preferences_from_obj,
        self_hosted_id=self_hosted_id_from_obj,
        self_hosted_url=self_hosted_url_from_obj,
        subscription_customer_id=subscription_customer_id_from_obj,
        subscription_expires=subscription_expires_from_obj,
        subscription_id=subscription_id_from_obj,
        subscription_last_transaction_id=subscription_last_transaction_id_from_obj,
        subscription_processor=subscription_processor_from_obj,
        subscription_referral_code=subscription_referral_code_from_obj,
        subscription_referral_count=subscription_referral_count_from_obj,
        subscription_referrer_code=subscription_referrer_code_from_obj,
        updated=updated_from_obj)


def auth_household_to_jsonable(
        auth_household: AuthHousehold,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthHousehold.

    :param auth_household: instance of AuthHousehold to be JSON-ized
    :param path: path to the auth_household used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_household.backup_encryption_key is not None:
        res['backupEncryptionKey'] = auth_household.backup_encryption_key

    if auth_household.cloud_push_notifications is not None:
        res['cloudPushNotifications'] = auth_household.cloud_push_notifications

    if auth_household.count_members is not None:
        res['countMembers'] = auth_household.count_members

    if auth_household.created is not None:
        res['created'] = auth_household.created

    if auth_household.demo is not None:
        res['demo'] = auth_household.demo

    if auth_household.feature_votes is not None:
        res['featureVotes'] = to_jsonable(
        auth_household.feature_votes,
        expected=[list, AuthHouseholdFeatureVote],
        path='{}.featureVotes'.format(path))

    if auth_household.id is not None:
        res['id'] = auth_household.id

    if auth_household.members is not None:
        res['members'] = to_jsonable(
        auth_household.members,
        expected=[list, AuthHouseholdMember],
        path='{}.members'.format(path))

    if auth_household.name is not None:
        res['name'] = auth_household.name

    if auth_household.preferences is not None:
        res['preferences'] = to_jsonable(
        auth_household.preferences,
        expected=[AuthHouseholdPreferences],
        path='{}.preferences'.format(path))

    if auth_household.self_hosted_id is not None:
        res['selfHostedID'] = to_jsonable(
        auth_household.self_hosted_id,
        expected=[UuidNullUUID],
        path='{}.selfHostedID'.format(path))

    if auth_household.self_hosted_url is not None:
        res['selfHostedURL'] = auth_household.self_hosted_url

    if auth_household.subscription_customer_id is not None:
        res['subscriptionCustomerID'] = auth_household.subscription_customer_id

    if auth_household.subscription_expires is not None:
        res['subscriptionExpires'] = auth_household.subscription_expires

    if auth_household.subscription_id is not None:
        res['subscriptionID'] = auth_household.subscription_id

    if auth_household.subscription_last_transaction_id is not None:
        res['subscriptionLastTransactionID'] = auth_household.subscription_last_transaction_id

    if auth_household.subscription_processor is not None:
        res['subscriptionProcessor'] = auth_household.subscription_processor

    if auth_household.subscription_referral_code is not None:
        res['subscriptionReferralCode'] = auth_household.subscription_referral_code

    if auth_household.subscription_referral_count is not None:
        res['subscriptionReferralCount'] = auth_household.subscription_referral_count

    if auth_household.subscription_referrer_code is not None:
        res['subscriptionReferrerCode'] = auth_household.subscription_referrer_code

    if auth_household.updated is not None:
        res['updated'] = auth_household.updated

    return res


class AuthHouseholdFeatureVote:
    def __init__(
            self,
            amount: Optional[int] = None,
            comment: Optional[str] = None,
            feature: Optional[int] = None) -> None:
        """Initializes with the given values."""
        self.amount = amount

        self.comment = comment

        self.feature = feature

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_household_feature_vote_to_jsonable.

        :return: JSON-able representation
        """
        return auth_household_feature_vote_to_jsonable(self)


def new_auth_household_feature_vote() -> AuthHouseholdFeatureVote:
    """Generates an instance of AuthHouseholdFeatureVote with default values."""
    return AuthHouseholdFeatureVote()


def auth_household_feature_vote_from_obj(obj: Any, path: str = "") -> AuthHouseholdFeatureVote:
    """
    Generates an instance of AuthHouseholdFeatureVote from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthHouseholdFeatureVote
    :param path: path to the object used for debugging
    :return: parsed instance of AuthHouseholdFeatureVote
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_amount = obj.get('amount', None)
    if obj_amount is not None:
        amount_from_obj = from_obj(
            obj_amount,
            expected=[int],
            path=path + '.amount')  # type: Optional[int]
    else:
        amount_from_obj = None

    obj_comment = obj.get('comment', None)
    if obj_comment is not None:
        comment_from_obj = from_obj(
            obj_comment,
            expected=[str],
            path=path + '.comment')  # type: Optional[str]
    else:
        comment_from_obj = None

    obj_feature = obj.get('feature', None)
    if obj_feature is not None:
        feature_from_obj = from_obj(
            obj_feature,
            expected=[int],
            path=path + '.feature')  # type: Optional[int]
    else:
        feature_from_obj = None

    return AuthHouseholdFeatureVote(
        amount=amount_from_obj,
        comment=comment_from_obj,
        feature=feature_from_obj)


def auth_household_feature_vote_to_jsonable(
        auth_household_feature_vote: AuthHouseholdFeatureVote,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthHouseholdFeatureVote.

    :param auth_household_feature_vote: instance of AuthHouseholdFeatureVote to be JSON-ized
    :param path: path to the auth_household_feature_vote used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_household_feature_vote.amount is not None:
        res['amount'] = auth_household_feature_vote.amount

    if auth_household_feature_vote.comment is not None:
        res['comment'] = auth_household_feature_vote.comment

    if auth_household_feature_vote.feature is not None:
        res['feature'] = auth_household_feature_vote.feature

    return res


class AuthHouseholdMember:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            child: Optional[bool] = None,
            color: Optional[int] = None,
            email_address: Optional[str] = None,
            id: Optional[str] = None,
            invite_token: Optional[str] = None,
            name: Optional[str] = None,
            permissions: Optional['Permissions'] = None,
            public_key: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.child = child

        self.color = color

        self.email_address = email_address

        self.id = id

        self.invite_token = invite_token

        self.name = name

        self.permissions = permissions

        self.public_key = public_key

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_household_member_to_jsonable.

        :return: JSON-able representation
        """
        return auth_household_member_to_jsonable(self)


def new_auth_household_member() -> AuthHouseholdMember:
    """Generates an instance of AuthHouseholdMember with default values."""
    return AuthHouseholdMember()


def auth_household_member_from_obj(obj: Any, path: str = "") -> AuthHouseholdMember:
    """
    Generates an instance of AuthHouseholdMember from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthHouseholdMember
    :param path: path to the object used for debugging
    :return: parsed instance of AuthHouseholdMember
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_child = obj.get('child', None)
    if obj_child is not None:
        child_from_obj = from_obj(
            obj_child,
            expected=[bool],
            path=path + '.child')  # type: Optional[bool]
    else:
        child_from_obj = None

    obj_color = obj.get('color', None)
    if obj_color is not None:
        color_from_obj = from_obj(
            obj_color,
            expected=[int],
            path=path + '.color')  # type: Optional[int]
    else:
        color_from_obj = None

    obj_email_address = obj.get('emailAddress', None)
    if obj_email_address is not None:
        email_address_from_obj = from_obj(
            obj_email_address,
            expected=[str],
            path=path + '.emailAddress')  # type: Optional[str]
    else:
        email_address_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_invite_token = obj.get('inviteToken', None)
    if obj_invite_token is not None:
        invite_token_from_obj = from_obj(
            obj_invite_token,
            expected=[str],
            path=path + '.inviteToken')  # type: Optional[str]
    else:
        invite_token_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_permissions = obj.get('permissions', None)
    if obj_permissions is not None:
        permissions_from_obj = from_obj(
            obj_permissions,
            expected=[Permissions],
            path=path + '.permissions')  # type: Optional['Permissions']
    else:
        permissions_from_obj = None

    obj_public_key = obj.get('publicKey', None)
    if obj_public_key is not None:
        public_key_from_obj = from_obj(
            obj_public_key,
            expected=[str],
            path=path + '.publicKey')  # type: Optional[str]
    else:
        public_key_from_obj = None

    return AuthHouseholdMember(
        auth_household_id=auth_household_id_from_obj,
        child=child_from_obj,
        color=color_from_obj,
        email_address=email_address_from_obj,
        id=id_from_obj,
        invite_token=invite_token_from_obj,
        name=name_from_obj,
        permissions=permissions_from_obj,
        public_key=public_key_from_obj)


def auth_household_member_to_jsonable(
        auth_household_member: AuthHouseholdMember,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthHouseholdMember.

    :param auth_household_member: instance of AuthHouseholdMember to be JSON-ized
    :param path: path to the auth_household_member used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_household_member.auth_household_id is not None:
        res['authHouseholdID'] = auth_household_member.auth_household_id

    if auth_household_member.child is not None:
        res['child'] = auth_household_member.child

    if auth_household_member.color is not None:
        res['color'] = auth_household_member.color

    if auth_household_member.email_address is not None:
        res['emailAddress'] = auth_household_member.email_address

    if auth_household_member.id is not None:
        res['id'] = auth_household_member.id

    if auth_household_member.invite_token is not None:
        res['inviteToken'] = auth_household_member.invite_token

    if auth_household_member.name is not None:
        res['name'] = auth_household_member.name

    if auth_household_member.permissions is not None:
        res['permissions'] = to_jsonable(
        auth_household_member.permissions,
        expected=[Permissions],
        path='{}.permissions'.format(path))

    if auth_household_member.public_key is not None:
        res['publicKey'] = auth_household_member.public_key

    return res


class AuthHouseholdPermissions:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            permissions: Optional['Permissions'] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.permissions = permissions

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_household_permissions_to_jsonable.

        :return: JSON-able representation
        """
        return auth_household_permissions_to_jsonable(self)


def new_auth_household_permissions() -> AuthHouseholdPermissions:
    """Generates an instance of AuthHouseholdPermissions with default values."""
    return AuthHouseholdPermissions()


def auth_household_permissions_from_obj(obj: Any, path: str = "") -> AuthHouseholdPermissions:
    """
    Generates an instance of AuthHouseholdPermissions from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthHouseholdPermissions
    :param path: path to the object used for debugging
    :return: parsed instance of AuthHouseholdPermissions
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_permissions = obj.get('permissions', None)
    if obj_permissions is not None:
        permissions_from_obj = from_obj(
            obj_permissions,
            expected=[Permissions],
            path=path + '.permissions')  # type: Optional['Permissions']
    else:
        permissions_from_obj = None

    return AuthHouseholdPermissions(
        auth_household_id=auth_household_id_from_obj,
        permissions=permissions_from_obj)


def auth_household_permissions_to_jsonable(
        auth_household_permissions: AuthHouseholdPermissions,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthHouseholdPermissions.

    :param auth_household_permissions: instance of AuthHouseholdPermissions to be JSON-ized
    :param path: path to the auth_household_permissions used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_household_permissions.auth_household_id is not None:
        res['authHouseholdID'] = auth_household_permissions.auth_household_id

    if auth_household_permissions.permissions is not None:
        res['permissions'] = to_jsonable(
        auth_household_permissions.permissions,
        expected=[Permissions],
        path='{}.permissions'.format(path))

    return res


class AuthHouseholdPreferences:
    def __init__(
            self,
            color_budget_recurrence_events: Optional[int] = None,
            color_cook_meal_plan_events: Optional[int] = None,
            color_plan_task_events: Optional[int] = None,
            currency: Optional[int] = None,
            hide_components: Optional[List[str]] = None) -> None:
        """Initializes with the given values."""
        self.color_budget_recurrence_events = color_budget_recurrence_events

        self.color_cook_meal_plan_events = color_cook_meal_plan_events

        self.color_plan_task_events = color_plan_task_events

        self.currency = currency

        self.hide_components = hide_components

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_household_preferences_to_jsonable.

        :return: JSON-able representation
        """
        return auth_household_preferences_to_jsonable(self)


def new_auth_household_preferences() -> AuthHouseholdPreferences:
    """Generates an instance of AuthHouseholdPreferences with default values."""
    return AuthHouseholdPreferences()


def auth_household_preferences_from_obj(obj: Any, path: str = "") -> AuthHouseholdPreferences:
    """
    Generates an instance of AuthHouseholdPreferences from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthHouseholdPreferences
    :param path: path to the object used for debugging
    :return: parsed instance of AuthHouseholdPreferences
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_color_budget_recurrence_events = obj.get('colorBudgetRecurrenceEvents', None)
    if obj_color_budget_recurrence_events is not None:
        color_budget_recurrence_events_from_obj = from_obj(
            obj_color_budget_recurrence_events,
            expected=[int],
            path=path + '.colorBudgetRecurrenceEvents')  # type: Optional[int]
    else:
        color_budget_recurrence_events_from_obj = None

    obj_color_cook_meal_plan_events = obj.get('colorCookMealPlanEvents', None)
    if obj_color_cook_meal_plan_events is not None:
        color_cook_meal_plan_events_from_obj = from_obj(
            obj_color_cook_meal_plan_events,
            expected=[int],
            path=path + '.colorCookMealPlanEvents')  # type: Optional[int]
    else:
        color_cook_meal_plan_events_from_obj = None

    obj_color_plan_task_events = obj.get('colorPlanTaskEvents', None)
    if obj_color_plan_task_events is not None:
        color_plan_task_events_from_obj = from_obj(
            obj_color_plan_task_events,
            expected=[int],
            path=path + '.colorPlanTaskEvents')  # type: Optional[int]
    else:
        color_plan_task_events_from_obj = None

    obj_currency = obj.get('currency', None)
    if obj_currency is not None:
        currency_from_obj = from_obj(
            obj_currency,
            expected=[int],
            path=path + '.currency')  # type: Optional[int]
    else:
        currency_from_obj = None

    obj_hide_components = obj.get('hideComponents', None)
    if obj_hide_components is not None:
        hide_components_from_obj = from_obj(
            obj_hide_components,
            expected=[list, str],
            path=path + '.hideComponents')  # type: Optional[List[str]]
    else:
        hide_components_from_obj = None

    return AuthHouseholdPreferences(
        color_budget_recurrence_events=color_budget_recurrence_events_from_obj,
        color_cook_meal_plan_events=color_cook_meal_plan_events_from_obj,
        color_plan_task_events=color_plan_task_events_from_obj,
        currency=currency_from_obj,
        hide_components=hide_components_from_obj)


def auth_household_preferences_to_jsonable(
        auth_household_preferences: AuthHouseholdPreferences,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthHouseholdPreferences.

    :param auth_household_preferences: instance of AuthHouseholdPreferences to be JSON-ized
    :param path: path to the auth_household_preferences used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_household_preferences.color_budget_recurrence_events is not None:
        res['colorBudgetRecurrenceEvents'] = auth_household_preferences.color_budget_recurrence_events

    if auth_household_preferences.color_cook_meal_plan_events is not None:
        res['colorCookMealPlanEvents'] = auth_household_preferences.color_cook_meal_plan_events

    if auth_household_preferences.color_plan_task_events is not None:
        res['colorPlanTaskEvents'] = auth_household_preferences.color_plan_task_events

    if auth_household_preferences.currency is not None:
        res['currency'] = auth_household_preferences.currency

    if auth_household_preferences.hide_components is not None:
        res['hideComponents'] = to_jsonable(
        auth_household_preferences.hide_components,
        expected=[list, str],
        path='{}.hideComponents'.format(path))

    return res


class AuthSession:
    def __init__(
            self,
            admin: Optional[bool] = None,
            auth_account_id: Optional[str] = None,
            child: Optional[bool] = None,
            created: Optional[str] = None,
            expires: Optional[str] = None,
            fcm_token: Optional[str] = None,
            id: Optional[str] = None,
            key: Optional[str] = None,
            name: Optional[str] = None,
            permissions_account: Optional['Permissions'] = None,
            permissions_households: Optional[List['AuthHouseholdPermissions']] = None,
            platform: Optional[int] = None,
            primary_auth_household_id: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.admin = admin

        self.auth_account_id = auth_account_id

        self.child = child

        self.created = created

        self.expires = expires

        self.fcm_token = fcm_token

        self.id = id

        self.key = key

        self.name = name

        self.permissions_account = permissions_account

        self.permissions_households = permissions_households

        self.platform = platform

        self.primary_auth_household_id = primary_auth_household_id

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to auth_session_to_jsonable.

        :return: JSON-able representation
        """
        return auth_session_to_jsonable(self)


def new_auth_session() -> AuthSession:
    """Generates an instance of AuthSession with default values."""
    return AuthSession()


def auth_session_from_obj(obj: Any, path: str = "") -> AuthSession:
    """
    Generates an instance of AuthSession from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of AuthSession
    :param path: path to the object used for debugging
    :return: parsed instance of AuthSession
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_admin = obj.get('admin', None)
    if obj_admin is not None:
        admin_from_obj = from_obj(
            obj_admin,
            expected=[bool],
            path=path + '.admin')  # type: Optional[bool]
    else:
        admin_from_obj = None

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_child = obj.get('child', None)
    if obj_child is not None:
        child_from_obj = from_obj(
            obj_child,
            expected=[bool],
            path=path + '.child')  # type: Optional[bool]
    else:
        child_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_expires = obj.get('expires', None)
    if obj_expires is not None:
        expires_from_obj = from_obj(
            obj_expires,
            expected=[str],
            path=path + '.expires')  # type: Optional[str]
    else:
        expires_from_obj = None

    obj_fcm_token = obj.get('fcmToken', None)
    if obj_fcm_token is not None:
        fcm_token_from_obj = from_obj(
            obj_fcm_token,
            expected=[str],
            path=path + '.fcmToken')  # type: Optional[str]
    else:
        fcm_token_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_key = obj.get('key', None)
    if obj_key is not None:
        key_from_obj = from_obj(
            obj_key,
            expected=[str],
            path=path + '.key')  # type: Optional[str]
    else:
        key_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_permissions_account = obj.get('permissionsAccount', None)
    if obj_permissions_account is not None:
        permissions_account_from_obj = from_obj(
            obj_permissions_account,
            expected=[Permissions],
            path=path + '.permissionsAccount')  # type: Optional['Permissions']
    else:
        permissions_account_from_obj = None

    obj_permissions_households = obj.get('permissionsHouseholds', None)
    if obj_permissions_households is not None:
        permissions_households_from_obj = from_obj(
            obj_permissions_households,
            expected=[list, AuthHouseholdPermissions],
            path=path + '.permissionsHouseholds')  # type: Optional[List['AuthHouseholdPermissions']]
    else:
        permissions_households_from_obj = None

    obj_platform = obj.get('platform', None)
    if obj_platform is not None:
        platform_from_obj = from_obj(
            obj_platform,
            expected=[int],
            path=path + '.platform')  # type: Optional[int]
    else:
        platform_from_obj = None

    obj_primary_auth_household_id = obj.get('primaryAuthHouseholdID', None)
    if obj_primary_auth_household_id is not None:
        primary_auth_household_id_from_obj = from_obj(
            obj_primary_auth_household_id,
            expected=[str],
            path=path + '.primaryAuthHouseholdID')  # type: Optional[str]
    else:
        primary_auth_household_id_from_obj = None

    return AuthSession(
        admin=admin_from_obj,
        auth_account_id=auth_account_id_from_obj,
        child=child_from_obj,
        created=created_from_obj,
        expires=expires_from_obj,
        fcm_token=fcm_token_from_obj,
        id=id_from_obj,
        key=key_from_obj,
        name=name_from_obj,
        permissions_account=permissions_account_from_obj,
        permissions_households=permissions_households_from_obj,
        platform=platform_from_obj,
        primary_auth_household_id=primary_auth_household_id_from_obj)


def auth_session_to_jsonable(
        auth_session: AuthSession,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of AuthSession.

    :param auth_session: instance of AuthSession to be JSON-ized
    :param path: path to the auth_session used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if auth_session.admin is not None:
        res['admin'] = auth_session.admin

    if auth_session.auth_account_id is not None:
        res['authAccountID'] = auth_session.auth_account_id

    if auth_session.child is not None:
        res['child'] = auth_session.child

    if auth_session.created is not None:
        res['created'] = auth_session.created

    if auth_session.expires is not None:
        res['expires'] = auth_session.expires

    if auth_session.fcm_token is not None:
        res['fcmToken'] = auth_session.fcm_token

    if auth_session.id is not None:
        res['id'] = auth_session.id

    if auth_session.key is not None:
        res['key'] = auth_session.key

    if auth_session.name is not None:
        res['name'] = auth_session.name

    if auth_session.permissions_account is not None:
        res['permissionsAccount'] = to_jsonable(
        auth_session.permissions_account,
        expected=[Permissions],
        path='{}.permissionsAccount'.format(path))

    if auth_session.permissions_households is not None:
        res['permissionsHouseholds'] = to_jsonable(
        auth_session.permissions_households,
        expected=[list, AuthHouseholdPermissions],
        path='{}.permissionsHouseholds'.format(path))

    if auth_session.platform is not None:
        res['platform'] = auth_session.platform

    if auth_session.primary_auth_household_id is not None:
        res['primaryAuthHouseholdID'] = auth_session.primary_auth_household_id

    return res


class Bookmark:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            created: Optional[str] = None,
            home: Optional[bool] = None,
            icon_link: Optional[str] = None,
            icon_name: Optional[str] = None,
            id: Optional[str] = None,
            link: Optional[str] = None,
            name: Optional[str] = None,
            new_window: Optional[bool] = None,
            short_id: Optional[str] = None,
            tags: Optional[List[str]] = None,
            updated: Optional[str] = None,
            updated_by: Optional['UuidNullUUID'] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.created = created

        self.home = home

        self.icon_link = icon_link

        self.icon_name = icon_name

        self.id = id

        self.link = link

        self.name = name

        self.new_window = new_window

        self.short_id = short_id

        self.tags = tags

        self.updated = updated

        self.updated_by = updated_by

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to bookmark_to_jsonable.

        :return: JSON-able representation
        """
        return bookmark_to_jsonable(self)


def new_bookmark() -> Bookmark:
    """Generates an instance of Bookmark with default values."""
    return Bookmark()


def bookmark_from_obj(obj: Any, path: str = "") -> Bookmark:
    """
    Generates an instance of Bookmark from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Bookmark
    :param path: path to the object used for debugging
    :return: parsed instance of Bookmark
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_home = obj.get('home', None)
    if obj_home is not None:
        home_from_obj = from_obj(
            obj_home,
            expected=[bool],
            path=path + '.home')  # type: Optional[bool]
    else:
        home_from_obj = None

    obj_icon_link = obj.get('iconLink', None)
    if obj_icon_link is not None:
        icon_link_from_obj = from_obj(
            obj_icon_link,
            expected=[str],
            path=path + '.iconLink')  # type: Optional[str]
    else:
        icon_link_from_obj = None

    obj_icon_name = obj.get('iconName', None)
    if obj_icon_name is not None:
        icon_name_from_obj = from_obj(
            obj_icon_name,
            expected=[str],
            path=path + '.iconName')  # type: Optional[str]
    else:
        icon_name_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_link = obj.get('link', None)
    if obj_link is not None:
        link_from_obj = from_obj(
            obj_link,
            expected=[str],
            path=path + '.link')  # type: Optional[str]
    else:
        link_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_new_window = obj.get('newWindow', None)
    if obj_new_window is not None:
        new_window_from_obj = from_obj(
            obj_new_window,
            expected=[bool],
            path=path + '.newWindow')  # type: Optional[bool]
    else:
        new_window_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_tags = obj.get('tags', None)
    if obj_tags is not None:
        tags_from_obj = from_obj(
            obj_tags,
            expected=[list, str],
            path=path + '.tags')  # type: Optional[List[str]]
    else:
        tags_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    obj_updated_by = obj.get('updatedBy', None)
    if obj_updated_by is not None:
        updated_by_from_obj = from_obj(
            obj_updated_by,
            expected=[UuidNullUUID],
            path=path + '.updatedBy')  # type: Optional['UuidNullUUID']
    else:
        updated_by_from_obj = None

    return Bookmark(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        created=created_from_obj,
        home=home_from_obj,
        icon_link=icon_link_from_obj,
        icon_name=icon_name_from_obj,
        id=id_from_obj,
        link=link_from_obj,
        name=name_from_obj,
        new_window=new_window_from_obj,
        short_id=short_id_from_obj,
        tags=tags_from_obj,
        updated=updated_from_obj,
        updated_by=updated_by_from_obj)


def bookmark_to_jsonable(
        bookmark: Bookmark,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Bookmark.

    :param bookmark: instance of Bookmark to be JSON-ized
    :param path: path to the bookmark used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if bookmark.auth_account_id is not None:
        res['authAccountID'] = bookmark.auth_account_id

    if bookmark.auth_household_id is not None:
        res['authHouseholdID'] = bookmark.auth_household_id

    if bookmark.created is not None:
        res['created'] = bookmark.created

    if bookmark.home is not None:
        res['home'] = bookmark.home

    if bookmark.icon_link is not None:
        res['iconLink'] = bookmark.icon_link

    if bookmark.icon_name is not None:
        res['iconName'] = bookmark.icon_name

    if bookmark.id is not None:
        res['id'] = bookmark.id

    if bookmark.link is not None:
        res['link'] = bookmark.link

    if bookmark.name is not None:
        res['name'] = bookmark.name

    if bookmark.new_window is not None:
        res['newWindow'] = bookmark.new_window

    if bookmark.short_id is not None:
        res['shortID'] = bookmark.short_id

    if bookmark.tags is not None:
        res['tags'] = to_jsonable(
        bookmark.tags,
        expected=[list, str],
        path='{}.tags'.format(path))

    if bookmark.updated is not None:
        res['updated'] = bookmark.updated

    if bookmark.updated_by is not None:
        res['updatedBy'] = to_jsonable(
        bookmark.updated_by,
        expected=[UuidNullUUID],
        path='{}.updatedBy'.format(path))

    return res


class BudgetAccount:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            budget_transaction_amount: Optional[int] = None,
            budget_transaction_amount_cleared: Optional[int] = None,
            budget_transaction_amount_reconciled: Optional[int] = None,
            created: Optional[str] = None,
            hidden: Optional[bool] = None,
            icon: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            short_id: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.budget_transaction_amount = budget_transaction_amount

        self.budget_transaction_amount_cleared = budget_transaction_amount_cleared

        self.budget_transaction_amount_reconciled = budget_transaction_amount_reconciled

        self.created = created

        self.hidden = hidden

        self.icon = icon

        self.id = id

        self.name = name

        self.short_id = short_id

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_account_to_jsonable.

        :return: JSON-able representation
        """
        return budget_account_to_jsonable(self)


def new_budget_account() -> BudgetAccount:
    """Generates an instance of BudgetAccount with default values."""
    return BudgetAccount()


def budget_account_from_obj(obj: Any, path: str = "") -> BudgetAccount:
    """
    Generates an instance of BudgetAccount from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetAccount
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetAccount
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_transaction_amount = obj.get('budgetTransactionAmount', None)
    if obj_budget_transaction_amount is not None:
        budget_transaction_amount_from_obj = from_obj(
            obj_budget_transaction_amount,
            expected=[int],
            path=path + '.budgetTransactionAmount')  # type: Optional[int]
    else:
        budget_transaction_amount_from_obj = None

    obj_budget_transaction_amount_cleared = obj.get('budgetTransactionAmountCleared', None)
    if obj_budget_transaction_amount_cleared is not None:
        budget_transaction_amount_cleared_from_obj = from_obj(
            obj_budget_transaction_amount_cleared,
            expected=[int],
            path=path + '.budgetTransactionAmountCleared')  # type: Optional[int]
    else:
        budget_transaction_amount_cleared_from_obj = None

    obj_budget_transaction_amount_reconciled = obj.get('budgetTransactionAmountReconciled', None)
    if obj_budget_transaction_amount_reconciled is not None:
        budget_transaction_amount_reconciled_from_obj = from_obj(
            obj_budget_transaction_amount_reconciled,
            expected=[int],
            path=path + '.budgetTransactionAmountReconciled')  # type: Optional[int]
    else:
        budget_transaction_amount_reconciled_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_hidden = obj.get('hidden', None)
    if obj_hidden is not None:
        hidden_from_obj = from_obj(
            obj_hidden,
            expected=[bool],
            path=path + '.hidden')  # type: Optional[bool]
    else:
        hidden_from_obj = None

    obj_icon = obj.get('icon', None)
    if obj_icon is not None:
        icon_from_obj = from_obj(
            obj_icon,
            expected=[str],
            path=path + '.icon')  # type: Optional[str]
    else:
        icon_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return BudgetAccount(
        auth_household_id=auth_household_id_from_obj,
        budget_transaction_amount=budget_transaction_amount_from_obj,
        budget_transaction_amount_cleared=budget_transaction_amount_cleared_from_obj,
        budget_transaction_amount_reconciled=budget_transaction_amount_reconciled_from_obj,
        created=created_from_obj,
        hidden=hidden_from_obj,
        icon=icon_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        short_id=short_id_from_obj,
        updated=updated_from_obj)


def budget_account_to_jsonable(
        budget_account: BudgetAccount,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetAccount.

    :param budget_account: instance of BudgetAccount to be JSON-ized
    :param path: path to the budget_account used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_account.auth_household_id is not None:
        res['authHouseholdID'] = budget_account.auth_household_id

    if budget_account.budget_transaction_amount is not None:
        res['budgetTransactionAmount'] = budget_account.budget_transaction_amount

    if budget_account.budget_transaction_amount_cleared is not None:
        res['budgetTransactionAmountCleared'] = budget_account.budget_transaction_amount_cleared

    if budget_account.budget_transaction_amount_reconciled is not None:
        res['budgetTransactionAmountReconciled'] = budget_account.budget_transaction_amount_reconciled

    if budget_account.created is not None:
        res['created'] = budget_account.created

    if budget_account.hidden is not None:
        res['hidden'] = budget_account.hidden

    if budget_account.icon is not None:
        res['icon'] = budget_account.icon

    if budget_account.id is not None:
        res['id'] = budget_account.id

    if budget_account.name is not None:
        res['name'] = budget_account.name

    if budget_account.short_id is not None:
        res['shortID'] = budget_account.short_id

    if budget_account.updated is not None:
        res['updated'] = budget_account.updated

    return res


class BudgetCategory:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            budget_month_category_amount: Optional[int] = None,
            budget_transaction_amount: Optional[int] = None,
            created: Optional[str] = None,
            grouping: Optional[str] = None,
            id: Optional[str] = None,
            income: Optional[bool] = None,
            name: Optional[str] = None,
            short_id: Optional[str] = None,
            target_amount: Optional[int] = None,
            target_month: Optional[int] = None,
            target_year: Optional[int] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.budget_month_category_amount = budget_month_category_amount

        self.budget_transaction_amount = budget_transaction_amount

        self.created = created

        self.grouping = grouping

        self.id = id

        self.income = income

        self.name = name

        self.short_id = short_id

        self.target_amount = target_amount

        self.target_month = target_month

        self.target_year = target_year

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_category_to_jsonable.

        :return: JSON-able representation
        """
        return budget_category_to_jsonable(self)


def new_budget_category() -> BudgetCategory:
    """Generates an instance of BudgetCategory with default values."""
    return BudgetCategory()


def budget_category_from_obj(obj: Any, path: str = "") -> BudgetCategory:
    """
    Generates an instance of BudgetCategory from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetCategory
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetCategory
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_month_category_amount = obj.get('budgetMonthCategoryAmount', None)
    if obj_budget_month_category_amount is not None:
        budget_month_category_amount_from_obj = from_obj(
            obj_budget_month_category_amount,
            expected=[int],
            path=path + '.budgetMonthCategoryAmount')  # type: Optional[int]
    else:
        budget_month_category_amount_from_obj = None

    obj_budget_transaction_amount = obj.get('budgetTransactionAmount', None)
    if obj_budget_transaction_amount is not None:
        budget_transaction_amount_from_obj = from_obj(
            obj_budget_transaction_amount,
            expected=[int],
            path=path + '.budgetTransactionAmount')  # type: Optional[int]
    else:
        budget_transaction_amount_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_grouping = obj.get('grouping', None)
    if obj_grouping is not None:
        grouping_from_obj = from_obj(
            obj_grouping,
            expected=[str],
            path=path + '.grouping')  # type: Optional[str]
    else:
        grouping_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_income = obj.get('income', None)
    if obj_income is not None:
        income_from_obj = from_obj(
            obj_income,
            expected=[bool],
            path=path + '.income')  # type: Optional[bool]
    else:
        income_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_target_amount = obj.get('targetAmount', None)
    if obj_target_amount is not None:
        target_amount_from_obj = from_obj(
            obj_target_amount,
            expected=[int],
            path=path + '.targetAmount')  # type: Optional[int]
    else:
        target_amount_from_obj = None

    obj_target_month = obj.get('targetMonth', None)
    if obj_target_month is not None:
        target_month_from_obj = from_obj(
            obj_target_month,
            expected=[int],
            path=path + '.targetMonth')  # type: Optional[int]
    else:
        target_month_from_obj = None

    obj_target_year = obj.get('targetYear', None)
    if obj_target_year is not None:
        target_year_from_obj = from_obj(
            obj_target_year,
            expected=[int],
            path=path + '.targetYear')  # type: Optional[int]
    else:
        target_year_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return BudgetCategory(
        auth_household_id=auth_household_id_from_obj,
        budget_month_category_amount=budget_month_category_amount_from_obj,
        budget_transaction_amount=budget_transaction_amount_from_obj,
        created=created_from_obj,
        grouping=grouping_from_obj,
        id=id_from_obj,
        income=income_from_obj,
        name=name_from_obj,
        short_id=short_id_from_obj,
        target_amount=target_amount_from_obj,
        target_month=target_month_from_obj,
        target_year=target_year_from_obj,
        updated=updated_from_obj)


def budget_category_to_jsonable(
        budget_category: BudgetCategory,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetCategory.

    :param budget_category: instance of BudgetCategory to be JSON-ized
    :param path: path to the budget_category used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_category.auth_household_id is not None:
        res['authHouseholdID'] = budget_category.auth_household_id

    if budget_category.budget_month_category_amount is not None:
        res['budgetMonthCategoryAmount'] = budget_category.budget_month_category_amount

    if budget_category.budget_transaction_amount is not None:
        res['budgetTransactionAmount'] = budget_category.budget_transaction_amount

    if budget_category.created is not None:
        res['created'] = budget_category.created

    if budget_category.grouping is not None:
        res['grouping'] = budget_category.grouping

    if budget_category.id is not None:
        res['id'] = budget_category.id

    if budget_category.income is not None:
        res['income'] = budget_category.income

    if budget_category.name is not None:
        res['name'] = budget_category.name

    if budget_category.short_id is not None:
        res['shortID'] = budget_category.short_id

    if budget_category.target_amount is not None:
        res['targetAmount'] = budget_category.target_amount

    if budget_category.target_month is not None:
        res['targetMonth'] = budget_category.target_month

    if budget_category.target_year is not None:
        res['targetYear'] = budget_category.target_year

    if budget_category.updated is not None:
        res['updated'] = budget_category.updated

    return res


class BudgetMonth:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            budget_month_categories: Optional[List['BudgetMonthCategory']] = None,
            budget_month_category_amount: Optional[int] = None,
            budget_transaction_amount_income: Optional[int] = None,
            budget_transaction_amount_income_remaining: Optional[int] = None,
            year_month: Optional[int] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.budget_month_categories = budget_month_categories

        self.budget_month_category_amount = budget_month_category_amount

        self.budget_transaction_amount_income = budget_transaction_amount_income

        self.budget_transaction_amount_income_remaining = budget_transaction_amount_income_remaining

        self.year_month = year_month

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_month_to_jsonable.

        :return: JSON-able representation
        """
        return budget_month_to_jsonable(self)


def new_budget_month() -> BudgetMonth:
    """Generates an instance of BudgetMonth with default values."""
    return BudgetMonth()


def budget_month_from_obj(obj: Any, path: str = "") -> BudgetMonth:
    """
    Generates an instance of BudgetMonth from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetMonth
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetMonth
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_month_categories = obj.get('budgetMonthCategories', None)
    if obj_budget_month_categories is not None:
        budget_month_categories_from_obj = from_obj(
            obj_budget_month_categories,
            expected=[list, BudgetMonthCategory],
            path=path + '.budgetMonthCategories')  # type: Optional[List['BudgetMonthCategory']]
    else:
        budget_month_categories_from_obj = None

    obj_budget_month_category_amount = obj.get('budgetMonthCategoryAmount', None)
    if obj_budget_month_category_amount is not None:
        budget_month_category_amount_from_obj = from_obj(
            obj_budget_month_category_amount,
            expected=[int],
            path=path + '.budgetMonthCategoryAmount')  # type: Optional[int]
    else:
        budget_month_category_amount_from_obj = None

    obj_budget_transaction_amount_income = obj.get('budgetTransactionAmountIncome', None)
    if obj_budget_transaction_amount_income is not None:
        budget_transaction_amount_income_from_obj = from_obj(
            obj_budget_transaction_amount_income,
            expected=[int],
            path=path + '.budgetTransactionAmountIncome')  # type: Optional[int]
    else:
        budget_transaction_amount_income_from_obj = None

    obj_budget_transaction_amount_income_remaining = obj.get('budgetTransactionAmountIncomeRemaining', None)
    if obj_budget_transaction_amount_income_remaining is not None:
        budget_transaction_amount_income_remaining_from_obj = from_obj(
            obj_budget_transaction_amount_income_remaining,
            expected=[int],
            path=path + '.budgetTransactionAmountIncomeRemaining')  # type: Optional[int]
    else:
        budget_transaction_amount_income_remaining_from_obj = None

    obj_year_month = obj.get('yearMonth', None)
    if obj_year_month is not None:
        year_month_from_obj = from_obj(
            obj_year_month,
            expected=[int],
            path=path + '.yearMonth')  # type: Optional[int]
    else:
        year_month_from_obj = None

    return BudgetMonth(
        auth_household_id=auth_household_id_from_obj,
        budget_month_categories=budget_month_categories_from_obj,
        budget_month_category_amount=budget_month_category_amount_from_obj,
        budget_transaction_amount_income=budget_transaction_amount_income_from_obj,
        budget_transaction_amount_income_remaining=budget_transaction_amount_income_remaining_from_obj,
        year_month=year_month_from_obj)


def budget_month_to_jsonable(
        budget_month: BudgetMonth,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetMonth.

    :param budget_month: instance of BudgetMonth to be JSON-ized
    :param path: path to the budget_month used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_month.auth_household_id is not None:
        res['authHouseholdID'] = budget_month.auth_household_id

    if budget_month.budget_month_categories is not None:
        res['budgetMonthCategories'] = to_jsonable(
        budget_month.budget_month_categories,
        expected=[list, BudgetMonthCategory],
        path='{}.budgetMonthCategories'.format(path))

    if budget_month.budget_month_category_amount is not None:
        res['budgetMonthCategoryAmount'] = budget_month.budget_month_category_amount

    if budget_month.budget_transaction_amount_income is not None:
        res['budgetTransactionAmountIncome'] = budget_month.budget_transaction_amount_income

    if budget_month.budget_transaction_amount_income_remaining is not None:
        res['budgetTransactionAmountIncomeRemaining'] = budget_month.budget_transaction_amount_income_remaining

    if budget_month.year_month is not None:
        res['yearMonth'] = budget_month.year_month

    return res


class BudgetMonthCategory:
    def __init__(
            self,
            amount: Optional[int] = None,
            auth_household_id: Optional[str] = None,
            balance: Optional[int] = None,
            budget_category: Optional['BudgetCategory'] = None,
            budget_category_id: Optional[str] = None,
            budget_transaction_amount: Optional[int] = None,
            created: Optional[str] = None,
            year_month: Optional[int] = None) -> None:
        """Initializes with the given values."""
        self.amount = amount

        self.auth_household_id = auth_household_id

        self.balance = balance

        self.budget_category = budget_category

        self.budget_category_id = budget_category_id

        self.budget_transaction_amount = budget_transaction_amount

        self.created = created

        self.year_month = year_month

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_month_category_to_jsonable.

        :return: JSON-able representation
        """
        return budget_month_category_to_jsonable(self)


def new_budget_month_category() -> BudgetMonthCategory:
    """Generates an instance of BudgetMonthCategory with default values."""
    return BudgetMonthCategory()


def budget_month_category_from_obj(obj: Any, path: str = "") -> BudgetMonthCategory:
    """
    Generates an instance of BudgetMonthCategory from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetMonthCategory
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetMonthCategory
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_amount = obj.get('amount', None)
    if obj_amount is not None:
        amount_from_obj = from_obj(
            obj_amount,
            expected=[int],
            path=path + '.amount')  # type: Optional[int]
    else:
        amount_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_balance = obj.get('balance', None)
    if obj_balance is not None:
        balance_from_obj = from_obj(
            obj_balance,
            expected=[int],
            path=path + '.balance')  # type: Optional[int]
    else:
        balance_from_obj = None

    obj_budget_category = obj.get('budgetCategory', None)
    if obj_budget_category is not None:
        budget_category_from_obj = from_obj(
            obj_budget_category,
            expected=[BudgetCategory],
            path=path + '.budgetCategory')  # type: Optional['BudgetCategory']
    else:
        budget_category_from_obj = None

    obj_budget_category_id = obj.get('budgetCategoryID', None)
    if obj_budget_category_id is not None:
        budget_category_id_from_obj = from_obj(
            obj_budget_category_id,
            expected=[str],
            path=path + '.budgetCategoryID')  # type: Optional[str]
    else:
        budget_category_id_from_obj = None

    obj_budget_transaction_amount = obj.get('budgetTransactionAmount', None)
    if obj_budget_transaction_amount is not None:
        budget_transaction_amount_from_obj = from_obj(
            obj_budget_transaction_amount,
            expected=[int],
            path=path + '.budgetTransactionAmount')  # type: Optional[int]
    else:
        budget_transaction_amount_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_year_month = obj.get('yearMonth', None)
    if obj_year_month is not None:
        year_month_from_obj = from_obj(
            obj_year_month,
            expected=[int],
            path=path + '.yearMonth')  # type: Optional[int]
    else:
        year_month_from_obj = None

    return BudgetMonthCategory(
        amount=amount_from_obj,
        auth_household_id=auth_household_id_from_obj,
        balance=balance_from_obj,
        budget_category=budget_category_from_obj,
        budget_category_id=budget_category_id_from_obj,
        budget_transaction_amount=budget_transaction_amount_from_obj,
        created=created_from_obj,
        year_month=year_month_from_obj)


def budget_month_category_to_jsonable(
        budget_month_category: BudgetMonthCategory,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetMonthCategory.

    :param budget_month_category: instance of BudgetMonthCategory to be JSON-ized
    :param path: path to the budget_month_category used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_month_category.amount is not None:
        res['amount'] = budget_month_category.amount

    if budget_month_category.auth_household_id is not None:
        res['authHouseholdID'] = budget_month_category.auth_household_id

    if budget_month_category.balance is not None:
        res['balance'] = budget_month_category.balance

    if budget_month_category.budget_category is not None:
        res['budgetCategory'] = to_jsonable(
        budget_month_category.budget_category,
        expected=[BudgetCategory],
        path='{}.budgetCategory'.format(path))

    if budget_month_category.budget_category_id is not None:
        res['budgetCategoryID'] = budget_month_category.budget_category_id

    if budget_month_category.budget_transaction_amount is not None:
        res['budgetTransactionAmount'] = budget_month_category.budget_transaction_amount

    if budget_month_category.created is not None:
        res['created'] = budget_month_category.created

    if budget_month_category.year_month is not None:
        res['yearMonth'] = budget_month_category.year_month

    return res


class BudgetPayee:
    def __init__(
            self,
            address: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            budget_category_id: Optional[str] = None,
            budget_transaction_amount: Optional[int] = None,
            created: Optional[str] = None,
            icon: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            shop_store: Optional[bool] = None,
            short_id: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.address = address

        self.auth_household_id = auth_household_id

        self.budget_category_id = budget_category_id

        self.budget_transaction_amount = budget_transaction_amount

        self.created = created

        self.icon = icon

        self.id = id

        self.name = name

        self.shop_store = shop_store

        self.short_id = short_id

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_payee_to_jsonable.

        :return: JSON-able representation
        """
        return budget_payee_to_jsonable(self)


def new_budget_payee() -> BudgetPayee:
    """Generates an instance of BudgetPayee with default values."""
    return BudgetPayee()


def budget_payee_from_obj(obj: Any, path: str = "") -> BudgetPayee:
    """
    Generates an instance of BudgetPayee from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetPayee
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetPayee
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_address = obj.get('address', None)
    if obj_address is not None:
        address_from_obj = from_obj(
            obj_address,
            expected=[str],
            path=path + '.address')  # type: Optional[str]
    else:
        address_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_category_id = obj.get('budgetCategoryID', None)
    if obj_budget_category_id is not None:
        budget_category_id_from_obj = from_obj(
            obj_budget_category_id,
            expected=[str],
            path=path + '.budgetCategoryID')  # type: Optional[str]
    else:
        budget_category_id_from_obj = None

    obj_budget_transaction_amount = obj.get('budgetTransactionAmount', None)
    if obj_budget_transaction_amount is not None:
        budget_transaction_amount_from_obj = from_obj(
            obj_budget_transaction_amount,
            expected=[int],
            path=path + '.budgetTransactionAmount')  # type: Optional[int]
    else:
        budget_transaction_amount_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_icon = obj.get('icon', None)
    if obj_icon is not None:
        icon_from_obj = from_obj(
            obj_icon,
            expected=[str],
            path=path + '.icon')  # type: Optional[str]
    else:
        icon_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_shop_store = obj.get('shopStore', None)
    if obj_shop_store is not None:
        shop_store_from_obj = from_obj(
            obj_shop_store,
            expected=[bool],
            path=path + '.shopStore')  # type: Optional[bool]
    else:
        shop_store_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return BudgetPayee(
        address=address_from_obj,
        auth_household_id=auth_household_id_from_obj,
        budget_category_id=budget_category_id_from_obj,
        budget_transaction_amount=budget_transaction_amount_from_obj,
        created=created_from_obj,
        icon=icon_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        shop_store=shop_store_from_obj,
        short_id=short_id_from_obj,
        updated=updated_from_obj)


def budget_payee_to_jsonable(
        budget_payee: BudgetPayee,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetPayee.

    :param budget_payee: instance of BudgetPayee to be JSON-ized
    :param path: path to the budget_payee used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_payee.address is not None:
        res['address'] = budget_payee.address

    if budget_payee.auth_household_id is not None:
        res['authHouseholdID'] = budget_payee.auth_household_id

    if budget_payee.budget_category_id is not None:
        res['budgetCategoryID'] = budget_payee.budget_category_id

    if budget_payee.budget_transaction_amount is not None:
        res['budgetTransactionAmount'] = budget_payee.budget_transaction_amount

    if budget_payee.created is not None:
        res['created'] = budget_payee.created

    if budget_payee.icon is not None:
        res['icon'] = budget_payee.icon

    if budget_payee.id is not None:
        res['id'] = budget_payee.id

    if budget_payee.name is not None:
        res['name'] = budget_payee.name

    if budget_payee.shop_store is not None:
        res['shopStore'] = budget_payee.shop_store

    if budget_payee.short_id is not None:
        res['shortID'] = budget_payee.short_id

    if budget_payee.updated is not None:
        res['updated'] = budget_payee.updated

    return res


class BudgetRecurrence:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            budget_account_id: Optional[str] = None,
            created: Optional[str] = None,
            id: Optional[str] = None,
            recurrence: Optional['Recurrence'] = None,
            template: Optional['BudgetRecurrenceTemplate'] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.budget_account_id = budget_account_id

        self.created = created

        self.id = id

        self.recurrence = recurrence

        self.template = template

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_recurrence_to_jsonable.

        :return: JSON-able representation
        """
        return budget_recurrence_to_jsonable(self)


def new_budget_recurrence() -> BudgetRecurrence:
    """Generates an instance of BudgetRecurrence with default values."""
    return BudgetRecurrence()


def budget_recurrence_from_obj(obj: Any, path: str = "") -> BudgetRecurrence:
    """
    Generates an instance of BudgetRecurrence from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetRecurrence
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetRecurrence
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_account_id = obj.get('budgetAccountID', None)
    if obj_budget_account_id is not None:
        budget_account_id_from_obj = from_obj(
            obj_budget_account_id,
            expected=[str],
            path=path + '.budgetAccountID')  # type: Optional[str]
    else:
        budget_account_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_recurrence = obj.get('recurrence', None)
    if obj_recurrence is not None:
        recurrence_from_obj = from_obj(
            obj_recurrence,
            expected=[Recurrence],
            path=path + '.recurrence')  # type: Optional['Recurrence']
    else:
        recurrence_from_obj = None

    obj_template = obj.get('template', None)
    if obj_template is not None:
        template_from_obj = from_obj(
            obj_template,
            expected=[BudgetRecurrenceTemplate],
            path=path + '.template')  # type: Optional['BudgetRecurrenceTemplate']
    else:
        template_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return BudgetRecurrence(
        auth_household_id=auth_household_id_from_obj,
        budget_account_id=budget_account_id_from_obj,
        created=created_from_obj,
        id=id_from_obj,
        recurrence=recurrence_from_obj,
        template=template_from_obj,
        updated=updated_from_obj)


def budget_recurrence_to_jsonable(
        budget_recurrence: BudgetRecurrence,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetRecurrence.

    :param budget_recurrence: instance of BudgetRecurrence to be JSON-ized
    :param path: path to the budget_recurrence used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_recurrence.auth_household_id is not None:
        res['authHouseholdID'] = budget_recurrence.auth_household_id

    if budget_recurrence.budget_account_id is not None:
        res['budgetAccountID'] = budget_recurrence.budget_account_id

    if budget_recurrence.created is not None:
        res['created'] = budget_recurrence.created

    if budget_recurrence.id is not None:
        res['id'] = budget_recurrence.id

    if budget_recurrence.recurrence is not None:
        res['recurrence'] = to_jsonable(
        budget_recurrence.recurrence,
        expected=[Recurrence],
        path='{}.recurrence'.format(path))

    if budget_recurrence.template is not None:
        res['template'] = to_jsonable(
        budget_recurrence.template,
        expected=[BudgetRecurrenceTemplate],
        path='{}.template'.format(path))

    if budget_recurrence.updated is not None:
        res['updated'] = budget_recurrence.updated

    return res


class BudgetRecurrenceTemplate:
    def __init__(
            self,
            accounts: Optional[List['BudgetTransactionAccount']] = None,
            amount: Optional[int] = None,
            auth_household_id: Optional[str] = None,
            balance: Optional[int] = None,
            budget_payee_id: Optional[str] = None,
            budget_payee_name: Optional[str] = None,
            categories: Optional[List['BudgetTransactionCategory']] = None,
            check_number: Optional[int] = None,
            created: Optional[str] = None,
            date: Optional[str] = None,
            id: Optional[str] = None,
            keep: Optional[bool] = None,
            note: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.accounts = accounts

        self.amount = amount

        self.auth_household_id = auth_household_id

        self.balance = balance

        self.budget_payee_id = budget_payee_id

        self.budget_payee_name = budget_payee_name

        self.categories = categories

        self.check_number = check_number

        self.created = created

        self.date = date

        self.id = id

        self.keep = keep

        self.note = note

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_recurrence_template_to_jsonable.

        :return: JSON-able representation
        """
        return budget_recurrence_template_to_jsonable(self)


def new_budget_recurrence_template() -> BudgetRecurrenceTemplate:
    """Generates an instance of BudgetRecurrenceTemplate with default values."""
    return BudgetRecurrenceTemplate()


def budget_recurrence_template_from_obj(obj: Any, path: str = "") -> BudgetRecurrenceTemplate:
    """
    Generates an instance of BudgetRecurrenceTemplate from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetRecurrenceTemplate
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetRecurrenceTemplate
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_accounts = obj.get('accounts', None)
    if obj_accounts is not None:
        accounts_from_obj = from_obj(
            obj_accounts,
            expected=[list, BudgetTransactionAccount],
            path=path + '.accounts')  # type: Optional[List['BudgetTransactionAccount']]
    else:
        accounts_from_obj = None

    obj_amount = obj.get('amount', None)
    if obj_amount is not None:
        amount_from_obj = from_obj(
            obj_amount,
            expected=[int],
            path=path + '.amount')  # type: Optional[int]
    else:
        amount_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_balance = obj.get('balance', None)
    if obj_balance is not None:
        balance_from_obj = from_obj(
            obj_balance,
            expected=[int],
            path=path + '.balance')  # type: Optional[int]
    else:
        balance_from_obj = None

    obj_budget_payee_id = obj.get('budgetPayeeID', None)
    if obj_budget_payee_id is not None:
        budget_payee_id_from_obj = from_obj(
            obj_budget_payee_id,
            expected=[str],
            path=path + '.budgetPayeeID')  # type: Optional[str]
    else:
        budget_payee_id_from_obj = None

    obj_budget_payee_name = obj.get('budgetPayeeName', None)
    if obj_budget_payee_name is not None:
        budget_payee_name_from_obj = from_obj(
            obj_budget_payee_name,
            expected=[str],
            path=path + '.budgetPayeeName')  # type: Optional[str]
    else:
        budget_payee_name_from_obj = None

    obj_categories = obj.get('categories', None)
    if obj_categories is not None:
        categories_from_obj = from_obj(
            obj_categories,
            expected=[list, BudgetTransactionCategory],
            path=path + '.categories')  # type: Optional[List['BudgetTransactionCategory']]
    else:
        categories_from_obj = None

    obj_check_number = obj.get('checkNumber', None)
    if obj_check_number is not None:
        check_number_from_obj = from_obj(
            obj_check_number,
            expected=[int],
            path=path + '.checkNumber')  # type: Optional[int]
    else:
        check_number_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_date = obj.get('date', None)
    if obj_date is not None:
        date_from_obj = from_obj(
            obj_date,
            expected=[str],
            path=path + '.date')  # type: Optional[str]
    else:
        date_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_keep = obj.get('keep', None)
    if obj_keep is not None:
        keep_from_obj = from_obj(
            obj_keep,
            expected=[bool],
            path=path + '.keep')  # type: Optional[bool]
    else:
        keep_from_obj = None

    obj_note = obj.get('note', None)
    if obj_note is not None:
        note_from_obj = from_obj(
            obj_note,
            expected=[str],
            path=path + '.note')  # type: Optional[str]
    else:
        note_from_obj = None

    return BudgetRecurrenceTemplate(
        accounts=accounts_from_obj,
        amount=amount_from_obj,
        auth_household_id=auth_household_id_from_obj,
        balance=balance_from_obj,
        budget_payee_id=budget_payee_id_from_obj,
        budget_payee_name=budget_payee_name_from_obj,
        categories=categories_from_obj,
        check_number=check_number_from_obj,
        created=created_from_obj,
        date=date_from_obj,
        id=id_from_obj,
        keep=keep_from_obj,
        note=note_from_obj)


def budget_recurrence_template_to_jsonable(
        budget_recurrence_template: BudgetRecurrenceTemplate,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetRecurrenceTemplate.

    :param budget_recurrence_template: instance of BudgetRecurrenceTemplate to be JSON-ized
    :param path: path to the budget_recurrence_template used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_recurrence_template.accounts is not None:
        res['accounts'] = to_jsonable(
        budget_recurrence_template.accounts,
        expected=[list, BudgetTransactionAccount],
        path='{}.accounts'.format(path))

    if budget_recurrence_template.amount is not None:
        res['amount'] = budget_recurrence_template.amount

    if budget_recurrence_template.auth_household_id is not None:
        res['authHouseholdID'] = budget_recurrence_template.auth_household_id

    if budget_recurrence_template.balance is not None:
        res['balance'] = budget_recurrence_template.balance

    if budget_recurrence_template.budget_payee_id is not None:
        res['budgetPayeeID'] = budget_recurrence_template.budget_payee_id

    if budget_recurrence_template.budget_payee_name is not None:
        res['budgetPayeeName'] = budget_recurrence_template.budget_payee_name

    if budget_recurrence_template.categories is not None:
        res['categories'] = to_jsonable(
        budget_recurrence_template.categories,
        expected=[list, BudgetTransactionCategory],
        path='{}.categories'.format(path))

    if budget_recurrence_template.check_number is not None:
        res['checkNumber'] = budget_recurrence_template.check_number

    if budget_recurrence_template.created is not None:
        res['created'] = budget_recurrence_template.created

    if budget_recurrence_template.date is not None:
        res['date'] = budget_recurrence_template.date

    if budget_recurrence_template.id is not None:
        res['id'] = budget_recurrence_template.id

    if budget_recurrence_template.keep is not None:
        res['keep'] = budget_recurrence_template.keep

    if budget_recurrence_template.note is not None:
        res['note'] = budget_recurrence_template.note

    return res


class BudgetTransaction:
    def __init__(
            self,
            accounts: Optional[List['BudgetTransactionAccount']] = None,
            amount: Optional[int] = None,
            auth_household_id: Optional[str] = None,
            balance: Optional[int] = None,
            budget_payee_id: Optional[str] = None,
            budget_payee_name: Optional[str] = None,
            categories: Optional[List['BudgetTransactionCategory']] = None,
            check_number: Optional[int] = None,
            created: Optional[str] = None,
            date: Optional[str] = None,
            id: Optional[str] = None,
            keep: Optional[bool] = None,
            note: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.accounts = accounts

        self.amount = amount

        self.auth_household_id = auth_household_id

        self.balance = balance

        self.budget_payee_id = budget_payee_id

        self.budget_payee_name = budget_payee_name

        self.categories = categories

        self.check_number = check_number

        self.created = created

        self.date = date

        self.id = id

        self.keep = keep

        self.note = note

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_transaction_to_jsonable.

        :return: JSON-able representation
        """
        return budget_transaction_to_jsonable(self)


def new_budget_transaction() -> BudgetTransaction:
    """Generates an instance of BudgetTransaction with default values."""
    return BudgetTransaction()


def budget_transaction_from_obj(obj: Any, path: str = "") -> BudgetTransaction:
    """
    Generates an instance of BudgetTransaction from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetTransaction
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetTransaction
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_accounts = obj.get('accounts', None)
    if obj_accounts is not None:
        accounts_from_obj = from_obj(
            obj_accounts,
            expected=[list, BudgetTransactionAccount],
            path=path + '.accounts')  # type: Optional[List['BudgetTransactionAccount']]
    else:
        accounts_from_obj = None

    obj_amount = obj.get('amount', None)
    if obj_amount is not None:
        amount_from_obj = from_obj(
            obj_amount,
            expected=[int],
            path=path + '.amount')  # type: Optional[int]
    else:
        amount_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_balance = obj.get('balance', None)
    if obj_balance is not None:
        balance_from_obj = from_obj(
            obj_balance,
            expected=[int],
            path=path + '.balance')  # type: Optional[int]
    else:
        balance_from_obj = None

    obj_budget_payee_id = obj.get('budgetPayeeID', None)
    if obj_budget_payee_id is not None:
        budget_payee_id_from_obj = from_obj(
            obj_budget_payee_id,
            expected=[str],
            path=path + '.budgetPayeeID')  # type: Optional[str]
    else:
        budget_payee_id_from_obj = None

    obj_budget_payee_name = obj.get('budgetPayeeName', None)
    if obj_budget_payee_name is not None:
        budget_payee_name_from_obj = from_obj(
            obj_budget_payee_name,
            expected=[str],
            path=path + '.budgetPayeeName')  # type: Optional[str]
    else:
        budget_payee_name_from_obj = None

    obj_categories = obj.get('categories', None)
    if obj_categories is not None:
        categories_from_obj = from_obj(
            obj_categories,
            expected=[list, BudgetTransactionCategory],
            path=path + '.categories')  # type: Optional[List['BudgetTransactionCategory']]
    else:
        categories_from_obj = None

    obj_check_number = obj.get('checkNumber', None)
    if obj_check_number is not None:
        check_number_from_obj = from_obj(
            obj_check_number,
            expected=[int],
            path=path + '.checkNumber')  # type: Optional[int]
    else:
        check_number_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_date = obj.get('date', None)
    if obj_date is not None:
        date_from_obj = from_obj(
            obj_date,
            expected=[str],
            path=path + '.date')  # type: Optional[str]
    else:
        date_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_keep = obj.get('keep', None)
    if obj_keep is not None:
        keep_from_obj = from_obj(
            obj_keep,
            expected=[bool],
            path=path + '.keep')  # type: Optional[bool]
    else:
        keep_from_obj = None

    obj_note = obj.get('note', None)
    if obj_note is not None:
        note_from_obj = from_obj(
            obj_note,
            expected=[str],
            path=path + '.note')  # type: Optional[str]
    else:
        note_from_obj = None

    return BudgetTransaction(
        accounts=accounts_from_obj,
        amount=amount_from_obj,
        auth_household_id=auth_household_id_from_obj,
        balance=balance_from_obj,
        budget_payee_id=budget_payee_id_from_obj,
        budget_payee_name=budget_payee_name_from_obj,
        categories=categories_from_obj,
        check_number=check_number_from_obj,
        created=created_from_obj,
        date=date_from_obj,
        id=id_from_obj,
        keep=keep_from_obj,
        note=note_from_obj)


def budget_transaction_to_jsonable(
        budget_transaction: BudgetTransaction,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetTransaction.

    :param budget_transaction: instance of BudgetTransaction to be JSON-ized
    :param path: path to the budget_transaction used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_transaction.accounts is not None:
        res['accounts'] = to_jsonable(
        budget_transaction.accounts,
        expected=[list, BudgetTransactionAccount],
        path='{}.accounts'.format(path))

    if budget_transaction.amount is not None:
        res['amount'] = budget_transaction.amount

    if budget_transaction.auth_household_id is not None:
        res['authHouseholdID'] = budget_transaction.auth_household_id

    if budget_transaction.balance is not None:
        res['balance'] = budget_transaction.balance

    if budget_transaction.budget_payee_id is not None:
        res['budgetPayeeID'] = budget_transaction.budget_payee_id

    if budget_transaction.budget_payee_name is not None:
        res['budgetPayeeName'] = budget_transaction.budget_payee_name

    if budget_transaction.categories is not None:
        res['categories'] = to_jsonable(
        budget_transaction.categories,
        expected=[list, BudgetTransactionCategory],
        path='{}.categories'.format(path))

    if budget_transaction.check_number is not None:
        res['checkNumber'] = budget_transaction.check_number

    if budget_transaction.created is not None:
        res['created'] = budget_transaction.created

    if budget_transaction.date is not None:
        res['date'] = budget_transaction.date

    if budget_transaction.id is not None:
        res['id'] = budget_transaction.id

    if budget_transaction.keep is not None:
        res['keep'] = budget_transaction.keep

    if budget_transaction.note is not None:
        res['note'] = budget_transaction.note

    return res


class BudgetTransactionAccount:
    def __init__(
            self,
            amount: Optional[int] = None,
            auth_household_id: Optional[str] = None,
            budget_account_id: Optional[str] = None,
            budget_transaction_id: Optional[str] = None,
            id: Optional[str] = None,
            status: Optional[int] = None) -> None:
        """Initializes with the given values."""
        self.amount = amount

        self.auth_household_id = auth_household_id

        self.budget_account_id = budget_account_id

        self.budget_transaction_id = budget_transaction_id

        self.id = id

        self.status = status

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_transaction_account_to_jsonable.

        :return: JSON-able representation
        """
        return budget_transaction_account_to_jsonable(self)


def new_budget_transaction_account() -> BudgetTransactionAccount:
    """Generates an instance of BudgetTransactionAccount with default values."""
    return BudgetTransactionAccount()


def budget_transaction_account_from_obj(obj: Any, path: str = "") -> BudgetTransactionAccount:
    """
    Generates an instance of BudgetTransactionAccount from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetTransactionAccount
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetTransactionAccount
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_amount = obj.get('amount', None)
    if obj_amount is not None:
        amount_from_obj = from_obj(
            obj_amount,
            expected=[int],
            path=path + '.amount')  # type: Optional[int]
    else:
        amount_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_account_id = obj.get('budgetAccountID', None)
    if obj_budget_account_id is not None:
        budget_account_id_from_obj = from_obj(
            obj_budget_account_id,
            expected=[str],
            path=path + '.budgetAccountID')  # type: Optional[str]
    else:
        budget_account_id_from_obj = None

    obj_budget_transaction_id = obj.get('budgetTransactionID', None)
    if obj_budget_transaction_id is not None:
        budget_transaction_id_from_obj = from_obj(
            obj_budget_transaction_id,
            expected=[str],
            path=path + '.budgetTransactionID')  # type: Optional[str]
    else:
        budget_transaction_id_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_status = obj.get('status', None)
    if obj_status is not None:
        status_from_obj = from_obj(
            obj_status,
            expected=[int],
            path=path + '.status')  # type: Optional[int]
    else:
        status_from_obj = None

    return BudgetTransactionAccount(
        amount=amount_from_obj,
        auth_household_id=auth_household_id_from_obj,
        budget_account_id=budget_account_id_from_obj,
        budget_transaction_id=budget_transaction_id_from_obj,
        id=id_from_obj,
        status=status_from_obj)


def budget_transaction_account_to_jsonable(
        budget_transaction_account: BudgetTransactionAccount,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetTransactionAccount.

    :param budget_transaction_account: instance of BudgetTransactionAccount to be JSON-ized
    :param path: path to the budget_transaction_account used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_transaction_account.amount is not None:
        res['amount'] = budget_transaction_account.amount

    if budget_transaction_account.auth_household_id is not None:
        res['authHouseholdID'] = budget_transaction_account.auth_household_id

    if budget_transaction_account.budget_account_id is not None:
        res['budgetAccountID'] = budget_transaction_account.budget_account_id

    if budget_transaction_account.budget_transaction_id is not None:
        res['budgetTransactionID'] = budget_transaction_account.budget_transaction_id

    if budget_transaction_account.id is not None:
        res['id'] = budget_transaction_account.id

    if budget_transaction_account.status is not None:
        res['status'] = budget_transaction_account.status

    return res


class BudgetTransactionCategory:
    def __init__(
            self,
            amount: Optional[int] = None,
            auth_household_id: Optional[str] = None,
            budget_category_id: Optional[str] = None,
            budget_transaction_id: Optional[str] = None,
            id: Optional[str] = None,
            year_month: Optional[int] = None) -> None:
        """Initializes with the given values."""
        self.amount = amount

        self.auth_household_id = auth_household_id

        self.budget_category_id = budget_category_id

        self.budget_transaction_id = budget_transaction_id

        self.id = id

        self.year_month = year_month

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to budget_transaction_category_to_jsonable.

        :return: JSON-able representation
        """
        return budget_transaction_category_to_jsonable(self)


def new_budget_transaction_category() -> BudgetTransactionCategory:
    """Generates an instance of BudgetTransactionCategory with default values."""
    return BudgetTransactionCategory()


def budget_transaction_category_from_obj(obj: Any, path: str = "") -> BudgetTransactionCategory:
    """
    Generates an instance of BudgetTransactionCategory from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BudgetTransactionCategory
    :param path: path to the object used for debugging
    :return: parsed instance of BudgetTransactionCategory
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_amount = obj.get('amount', None)
    if obj_amount is not None:
        amount_from_obj = from_obj(
            obj_amount,
            expected=[int],
            path=path + '.amount')  # type: Optional[int]
    else:
        amount_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_category_id = obj.get('budgetCategoryID', None)
    if obj_budget_category_id is not None:
        budget_category_id_from_obj = from_obj(
            obj_budget_category_id,
            expected=[str],
            path=path + '.budgetCategoryID')  # type: Optional[str]
    else:
        budget_category_id_from_obj = None

    obj_budget_transaction_id = obj.get('budgetTransactionID', None)
    if obj_budget_transaction_id is not None:
        budget_transaction_id_from_obj = from_obj(
            obj_budget_transaction_id,
            expected=[str],
            path=path + '.budgetTransactionID')  # type: Optional[str]
    else:
        budget_transaction_id_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_year_month = obj.get('yearMonth', None)
    if obj_year_month is not None:
        year_month_from_obj = from_obj(
            obj_year_month,
            expected=[int],
            path=path + '.yearMonth')  # type: Optional[int]
    else:
        year_month_from_obj = None

    return BudgetTransactionCategory(
        amount=amount_from_obj,
        auth_household_id=auth_household_id_from_obj,
        budget_category_id=budget_category_id_from_obj,
        budget_transaction_id=budget_transaction_id_from_obj,
        id=id_from_obj,
        year_month=year_month_from_obj)


def budget_transaction_category_to_jsonable(
        budget_transaction_category: BudgetTransactionCategory,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BudgetTransactionCategory.

    :param budget_transaction_category: instance of BudgetTransactionCategory to be JSON-ized
    :param path: path to the budget_transaction_category used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if budget_transaction_category.amount is not None:
        res['amount'] = budget_transaction_category.amount

    if budget_transaction_category.auth_household_id is not None:
        res['authHouseholdID'] = budget_transaction_category.auth_household_id

    if budget_transaction_category.budget_category_id is not None:
        res['budgetCategoryID'] = budget_transaction_category.budget_category_id

    if budget_transaction_category.budget_transaction_id is not None:
        res['budgetTransactionID'] = budget_transaction_category.budget_transaction_id

    if budget_transaction_category.id is not None:
        res['id'] = budget_transaction_category.id

    if budget_transaction_category.year_month is not None:
        res['yearMonth'] = budget_transaction_category.year_month

    return res


class CalendarEvent:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            calendar_i_calendar_id: Optional[str] = None,
            color: Optional[int] = None,
            created: Optional[str] = None,
            date_end: Optional[str] = None,
            date_start: Optional[str] = None,
            details: Optional[str] = None,
            duration: Optional[int] = None,
            id: Optional[str] = None,
            location: Optional[str] = None,
            name: Optional[str] = None,
            notify_offset: Optional[int] = None,
            participants: Optional[List[str]] = None,
            recurrence: Optional['Recurrence'] = None,
            skip_days: Optional[List[str]] = None,
            time_start: Optional[str] = None,
            time_zone: Optional[str] = None,
            timestamp_end: Optional[str] = None,
            timestamp_start: Optional[str] = None,
            travel_time: Optional[int] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.calendar_i_calendar_id = calendar_i_calendar_id

        self.color = color

        self.created = created

        # end of event or recurrence
        self.date_end = date_end

        # start of event or recurrence
        self.date_start = date_start

        self.details = details

        self.duration = duration

        self.id = id

        self.location = location

        self.name = name

        self.notify_offset = notify_offset

        self.participants = participants

        self.recurrence = recurrence

        self.skip_days = skip_days

        self.time_start = time_start

        self.time_zone = time_zone

        # set by database based on date_start + time_start + duration + travel_time at the right time zone
        self.timestamp_end = timestamp_end

        # set by database based on date_start + time_start at the right time zone
        self.timestamp_start = timestamp_start

        self.travel_time = travel_time

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to calendar_event_to_jsonable.

        :return: JSON-able representation
        """
        return calendar_event_to_jsonable(self)


def new_calendar_event() -> CalendarEvent:
    """Generates an instance of CalendarEvent with default values."""
    return CalendarEvent()


def calendar_event_from_obj(obj: Any, path: str = "") -> CalendarEvent:
    """
    Generates an instance of CalendarEvent from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of CalendarEvent
    :param path: path to the object used for debugging
    :return: parsed instance of CalendarEvent
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_calendar_i_calendar_id = obj.get('calendarICalendarID', None)
    if obj_calendar_i_calendar_id is not None:
        calendar_i_calendar_id_from_obj = from_obj(
            obj_calendar_i_calendar_id,
            expected=[str],
            path=path + '.calendarICalendarID')  # type: Optional[str]
    else:
        calendar_i_calendar_id_from_obj = None

    obj_color = obj.get('color', None)
    if obj_color is not None:
        color_from_obj = from_obj(
            obj_color,
            expected=[int],
            path=path + '.color')  # type: Optional[int]
    else:
        color_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_date_end = obj.get('dateEnd', None)
    if obj_date_end is not None:
        date_end_from_obj = from_obj(
            obj_date_end,
            expected=[str],
            path=path + '.dateEnd')  # type: Optional[str]
    else:
        date_end_from_obj = None

    obj_date_start = obj.get('dateStart', None)
    if obj_date_start is not None:
        date_start_from_obj = from_obj(
            obj_date_start,
            expected=[str],
            path=path + '.dateStart')  # type: Optional[str]
    else:
        date_start_from_obj = None

    obj_details = obj.get('details', None)
    if obj_details is not None:
        details_from_obj = from_obj(
            obj_details,
            expected=[str],
            path=path + '.details')  # type: Optional[str]
    else:
        details_from_obj = None

    obj_duration = obj.get('duration', None)
    if obj_duration is not None:
        duration_from_obj = from_obj(
            obj_duration,
            expected=[int],
            path=path + '.duration')  # type: Optional[int]
    else:
        duration_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_location = obj.get('location', None)
    if obj_location is not None:
        location_from_obj = from_obj(
            obj_location,
            expected=[str],
            path=path + '.location')  # type: Optional[str]
    else:
        location_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_notify_offset = obj.get('notifyOffset', None)
    if obj_notify_offset is not None:
        notify_offset_from_obj = from_obj(
            obj_notify_offset,
            expected=[int],
            path=path + '.notifyOffset')  # type: Optional[int]
    else:
        notify_offset_from_obj = None

    obj_participants = obj.get('participants', None)
    if obj_participants is not None:
        participants_from_obj = from_obj(
            obj_participants,
            expected=[list, str],
            path=path + '.participants')  # type: Optional[List[str]]
    else:
        participants_from_obj = None

    obj_recurrence = obj.get('recurrence', None)
    if obj_recurrence is not None:
        recurrence_from_obj = from_obj(
            obj_recurrence,
            expected=[Recurrence],
            path=path + '.recurrence')  # type: Optional['Recurrence']
    else:
        recurrence_from_obj = None

    obj_skip_days = obj.get('skipDays', None)
    if obj_skip_days is not None:
        skip_days_from_obj = from_obj(
            obj_skip_days,
            expected=[list, str],
            path=path + '.skipDays')  # type: Optional[List[str]]
    else:
        skip_days_from_obj = None

    obj_time_start = obj.get('timeStart', None)
    if obj_time_start is not None:
        time_start_from_obj = from_obj(
            obj_time_start,
            expected=[str],
            path=path + '.timeStart')  # type: Optional[str]
    else:
        time_start_from_obj = None

    obj_time_zone = obj.get('timeZone', None)
    if obj_time_zone is not None:
        time_zone_from_obj = from_obj(
            obj_time_zone,
            expected=[str],
            path=path + '.timeZone')  # type: Optional[str]
    else:
        time_zone_from_obj = None

    obj_timestamp_end = obj.get('timestampEnd', None)
    if obj_timestamp_end is not None:
        timestamp_end_from_obj = from_obj(
            obj_timestamp_end,
            expected=[str],
            path=path + '.timestampEnd')  # type: Optional[str]
    else:
        timestamp_end_from_obj = None

    obj_timestamp_start = obj.get('timestampStart', None)
    if obj_timestamp_start is not None:
        timestamp_start_from_obj = from_obj(
            obj_timestamp_start,
            expected=[str],
            path=path + '.timestampStart')  # type: Optional[str]
    else:
        timestamp_start_from_obj = None

    obj_travel_time = obj.get('travelTime', None)
    if obj_travel_time is not None:
        travel_time_from_obj = from_obj(
            obj_travel_time,
            expected=[int],
            path=path + '.travelTime')  # type: Optional[int]
    else:
        travel_time_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return CalendarEvent(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        calendar_i_calendar_id=calendar_i_calendar_id_from_obj,
        color=color_from_obj,
        created=created_from_obj,
        date_end=date_end_from_obj,
        date_start=date_start_from_obj,
        details=details_from_obj,
        duration=duration_from_obj,
        id=id_from_obj,
        location=location_from_obj,
        name=name_from_obj,
        notify_offset=notify_offset_from_obj,
        participants=participants_from_obj,
        recurrence=recurrence_from_obj,
        skip_days=skip_days_from_obj,
        time_start=time_start_from_obj,
        time_zone=time_zone_from_obj,
        timestamp_end=timestamp_end_from_obj,
        timestamp_start=timestamp_start_from_obj,
        travel_time=travel_time_from_obj,
        updated=updated_from_obj)


def calendar_event_to_jsonable(
        calendar_event: CalendarEvent,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of CalendarEvent.

    :param calendar_event: instance of CalendarEvent to be JSON-ized
    :param path: path to the calendar_event used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if calendar_event.auth_account_id is not None:
        res['authAccountID'] = calendar_event.auth_account_id

    if calendar_event.auth_household_id is not None:
        res['authHouseholdID'] = calendar_event.auth_household_id

    if calendar_event.calendar_i_calendar_id is not None:
        res['calendarICalendarID'] = calendar_event.calendar_i_calendar_id

    if calendar_event.color is not None:
        res['color'] = calendar_event.color

    if calendar_event.created is not None:
        res['created'] = calendar_event.created

    if calendar_event.date_end is not None:
        res['dateEnd'] = calendar_event.date_end

    if calendar_event.date_start is not None:
        res['dateStart'] = calendar_event.date_start

    if calendar_event.details is not None:
        res['details'] = calendar_event.details

    if calendar_event.duration is not None:
        res['duration'] = calendar_event.duration

    if calendar_event.id is not None:
        res['id'] = calendar_event.id

    if calendar_event.location is not None:
        res['location'] = calendar_event.location

    if calendar_event.name is not None:
        res['name'] = calendar_event.name

    if calendar_event.notify_offset is not None:
        res['notifyOffset'] = calendar_event.notify_offset

    if calendar_event.participants is not None:
        res['participants'] = to_jsonable(
        calendar_event.participants,
        expected=[list, str],
        path='{}.participants'.format(path))

    if calendar_event.recurrence is not None:
        res['recurrence'] = to_jsonable(
        calendar_event.recurrence,
        expected=[Recurrence],
        path='{}.recurrence'.format(path))

    if calendar_event.skip_days is not None:
        res['skipDays'] = to_jsonable(
        calendar_event.skip_days,
        expected=[list, str],
        path='{}.skipDays'.format(path))

    if calendar_event.time_start is not None:
        res['timeStart'] = calendar_event.time_start

    if calendar_event.time_zone is not None:
        res['timeZone'] = calendar_event.time_zone

    if calendar_event.timestamp_end is not None:
        res['timestampEnd'] = calendar_event.timestamp_end

    if calendar_event.timestamp_start is not None:
        res['timestampStart'] = calendar_event.timestamp_start

    if calendar_event.travel_time is not None:
        res['travelTime'] = calendar_event.travel_time

    if calendar_event.updated is not None:
        res['updated'] = calendar_event.updated

    return res


class Change:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            created: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            operation: Optional[int] = None,
            table_name: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.created = created

        self.id = id

        self.name = name

        self.operation = operation

        self.table_name = table_name

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to change_to_jsonable.

        :return: JSON-able representation
        """
        return change_to_jsonable(self)


def new_change() -> Change:
    """Generates an instance of Change with default values."""
    return Change()


def change_from_obj(obj: Any, path: str = "") -> Change:
    """
    Generates an instance of Change from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Change
    :param path: path to the object used for debugging
    :return: parsed instance of Change
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_operation = obj.get('operation', None)
    if obj_operation is not None:
        operation_from_obj = from_obj(
            obj_operation,
            expected=[int],
            path=path + '.operation')  # type: Optional[int]
    else:
        operation_from_obj = None

    obj_table_name = obj.get('tableName', None)
    if obj_table_name is not None:
        table_name_from_obj = from_obj(
            obj_table_name,
            expected=[str],
            path=path + '.tableName')  # type: Optional[str]
    else:
        table_name_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return Change(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        created=created_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        operation=operation_from_obj,
        table_name=table_name_from_obj,
        updated=updated_from_obj)


def change_to_jsonable(
        change: Change,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Change.

    :param change: instance of Change to be JSON-ized
    :param path: path to the change used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if change.auth_account_id is not None:
        res['authAccountID'] = change.auth_account_id

    if change.auth_household_id is not None:
        res['authHouseholdID'] = change.auth_household_id

    if change.created is not None:
        res['created'] = change.created

    if change.id is not None:
        res['id'] = change.id

    if change.name is not None:
        res['name'] = change.name

    if change.operation is not None:
        res['operation'] = change.operation

    if change.table_name is not None:
        res['tableName'] = change.table_name

    if change.updated is not None:
        res['updated'] = change.updated

    return res


class CivilDate:
    def __init__(
            self,
            day: Optional[int] = None,
            month: Optional[int] = None,
            year: Optional[int] = None) -> None:
        """Initializes with the given values."""
        self.day = day

        self.month = month

        self.year = year

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to civil_date_to_jsonable.

        :return: JSON-able representation
        """
        return civil_date_to_jsonable(self)


def new_civil_date() -> CivilDate:
    """Generates an instance of CivilDate with default values."""
    return CivilDate()


def civil_date_from_obj(obj: Any, path: str = "") -> CivilDate:
    """
    Generates an instance of CivilDate from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of CivilDate
    :param path: path to the object used for debugging
    :return: parsed instance of CivilDate
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_day = obj.get('day', None)
    if obj_day is not None:
        day_from_obj = from_obj(
            obj_day,
            expected=[int],
            path=path + '.day')  # type: Optional[int]
    else:
        day_from_obj = None

    obj_month = obj.get('month', None)
    if obj_month is not None:
        month_from_obj = from_obj(
            obj_month,
            expected=[int],
            path=path + '.month')  # type: Optional[int]
    else:
        month_from_obj = None

    obj_year = obj.get('year', None)
    if obj_year is not None:
        year_from_obj = from_obj(
            obj_year,
            expected=[int],
            path=path + '.year')  # type: Optional[int]
    else:
        year_from_obj = None

    return CivilDate(
        day=day_from_obj,
        month=month_from_obj,
        year=year_from_obj)


def civil_date_to_jsonable(
        civil_date: CivilDate,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of CivilDate.

    :param civil_date: instance of CivilDate to be JSON-ized
    :param path: path to the civil_date used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if civil_date.day is not None:
        res['day'] = civil_date.day

    if civil_date.month is not None:
        res['month'] = civil_date.month

    if civil_date.year is not None:
        res['year'] = civil_date.year

    return res


class CookMealPlan:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            cook_meal_time_id: Optional[str] = None,
            cook_recipe_id: Optional[str] = None,
            cook_recipe_scale: Optional[str] = None,
            created: Optional[str] = None,
            custom_recipe: Optional[str] = None,
            date: Optional[str] = None,
            id: Optional[str] = None,
            notification_time_cook: Optional[str] = None,
            notification_time_prep: Optional[str] = None,
            time: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.cook_meal_time_id = cook_meal_time_id

        self.cook_recipe_id = cook_recipe_id

        self.cook_recipe_scale = cook_recipe_scale

        self.created = created

        self.custom_recipe = custom_recipe

        self.date = date

        self.id = id

        self.notification_time_cook = notification_time_cook

        self.notification_time_prep = notification_time_prep

        self.time = time

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to cook_meal_plan_to_jsonable.

        :return: JSON-able representation
        """
        return cook_meal_plan_to_jsonable(self)


def new_cook_meal_plan() -> CookMealPlan:
    """Generates an instance of CookMealPlan with default values."""
    return CookMealPlan()


def cook_meal_plan_from_obj(obj: Any, path: str = "") -> CookMealPlan:
    """
    Generates an instance of CookMealPlan from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of CookMealPlan
    :param path: path to the object used for debugging
    :return: parsed instance of CookMealPlan
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_cook_meal_time_id = obj.get('cookMealTimeID', None)
    if obj_cook_meal_time_id is not None:
        cook_meal_time_id_from_obj = from_obj(
            obj_cook_meal_time_id,
            expected=[str],
            path=path + '.cookMealTimeID')  # type: Optional[str]
    else:
        cook_meal_time_id_from_obj = None

    obj_cook_recipe_id = obj.get('cookRecipeID', None)
    if obj_cook_recipe_id is not None:
        cook_recipe_id_from_obj = from_obj(
            obj_cook_recipe_id,
            expected=[str],
            path=path + '.cookRecipeID')  # type: Optional[str]
    else:
        cook_recipe_id_from_obj = None

    obj_cook_recipe_scale = obj.get('cookRecipeScale', None)
    if obj_cook_recipe_scale is not None:
        cook_recipe_scale_from_obj = from_obj(
            obj_cook_recipe_scale,
            expected=[str],
            path=path + '.cookRecipeScale')  # type: Optional[str]
    else:
        cook_recipe_scale_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_custom_recipe = obj.get('customRecipe', None)
    if obj_custom_recipe is not None:
        custom_recipe_from_obj = from_obj(
            obj_custom_recipe,
            expected=[str],
            path=path + '.customRecipe')  # type: Optional[str]
    else:
        custom_recipe_from_obj = None

    obj_date = obj.get('date', None)
    if obj_date is not None:
        date_from_obj = from_obj(
            obj_date,
            expected=[str],
            path=path + '.date')  # type: Optional[str]
    else:
        date_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_notification_time_cook = obj.get('notificationTimeCook', None)
    if obj_notification_time_cook is not None:
        notification_time_cook_from_obj = from_obj(
            obj_notification_time_cook,
            expected=[str],
            path=path + '.notificationTimeCook')  # type: Optional[str]
    else:
        notification_time_cook_from_obj = None

    obj_notification_time_prep = obj.get('notificationTimePrep', None)
    if obj_notification_time_prep is not None:
        notification_time_prep_from_obj = from_obj(
            obj_notification_time_prep,
            expected=[str],
            path=path + '.notificationTimePrep')  # type: Optional[str]
    else:
        notification_time_prep_from_obj = None

    obj_time = obj.get('time', None)
    if obj_time is not None:
        time_from_obj = from_obj(
            obj_time,
            expected=[str],
            path=path + '.time')  # type: Optional[str]
    else:
        time_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return CookMealPlan(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        cook_meal_time_id=cook_meal_time_id_from_obj,
        cook_recipe_id=cook_recipe_id_from_obj,
        cook_recipe_scale=cook_recipe_scale_from_obj,
        created=created_from_obj,
        custom_recipe=custom_recipe_from_obj,
        date=date_from_obj,
        id=id_from_obj,
        notification_time_cook=notification_time_cook_from_obj,
        notification_time_prep=notification_time_prep_from_obj,
        time=time_from_obj,
        updated=updated_from_obj)


def cook_meal_plan_to_jsonable(
        cook_meal_plan: CookMealPlan,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of CookMealPlan.

    :param cook_meal_plan: instance of CookMealPlan to be JSON-ized
    :param path: path to the cook_meal_plan used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if cook_meal_plan.auth_account_id is not None:
        res['authAccountID'] = cook_meal_plan.auth_account_id

    if cook_meal_plan.auth_household_id is not None:
        res['authHouseholdID'] = cook_meal_plan.auth_household_id

    if cook_meal_plan.cook_meal_time_id is not None:
        res['cookMealTimeID'] = cook_meal_plan.cook_meal_time_id

    if cook_meal_plan.cook_recipe_id is not None:
        res['cookRecipeID'] = cook_meal_plan.cook_recipe_id

    if cook_meal_plan.cook_recipe_scale is not None:
        res['cookRecipeScale'] = cook_meal_plan.cook_recipe_scale

    if cook_meal_plan.created is not None:
        res['created'] = cook_meal_plan.created

    if cook_meal_plan.custom_recipe is not None:
        res['customRecipe'] = cook_meal_plan.custom_recipe

    if cook_meal_plan.date is not None:
        res['date'] = cook_meal_plan.date

    if cook_meal_plan.id is not None:
        res['id'] = cook_meal_plan.id

    if cook_meal_plan.notification_time_cook is not None:
        res['notificationTimeCook'] = cook_meal_plan.notification_time_cook

    if cook_meal_plan.notification_time_prep is not None:
        res['notificationTimePrep'] = cook_meal_plan.notification_time_prep

    if cook_meal_plan.time is not None:
        res['time'] = cook_meal_plan.time

    if cook_meal_plan.updated is not None:
        res['updated'] = cook_meal_plan.updated

    return res


class CookMealTime:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            created: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            time: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.created = created

        self.id = id

        self.name = name

        self.time = time

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to cook_meal_time_to_jsonable.

        :return: JSON-able representation
        """
        return cook_meal_time_to_jsonable(self)


def new_cook_meal_time() -> CookMealTime:
    """Generates an instance of CookMealTime with default values."""
    return CookMealTime()


def cook_meal_time_from_obj(obj: Any, path: str = "") -> CookMealTime:
    """
    Generates an instance of CookMealTime from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of CookMealTime
    :param path: path to the object used for debugging
    :return: parsed instance of CookMealTime
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_time = obj.get('time', None)
    if obj_time is not None:
        time_from_obj = from_obj(
            obj_time,
            expected=[str],
            path=path + '.time')  # type: Optional[str]
    else:
        time_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return CookMealTime(
        auth_household_id=auth_household_id_from_obj,
        created=created_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        time=time_from_obj,
        updated=updated_from_obj)


def cook_meal_time_to_jsonable(
        cook_meal_time: CookMealTime,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of CookMealTime.

    :param cook_meal_time: instance of CookMealTime to be JSON-ized
    :param path: path to the cook_meal_time used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if cook_meal_time.auth_household_id is not None:
        res['authHouseholdID'] = cook_meal_time.auth_household_id

    if cook_meal_time.created is not None:
        res['created'] = cook_meal_time.created

    if cook_meal_time.id is not None:
        res['id'] = cook_meal_time.id

    if cook_meal_time.name is not None:
        res['name'] = cook_meal_time.name

    if cook_meal_time.time is not None:
        res['time'] = cook_meal_time.time

    if cook_meal_time.updated is not None:
        res['updated'] = cook_meal_time.updated

    return res


class CookRecipe:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            cook_meal_plan_count: Optional[int] = None,
            cook_meal_plan_last: Optional[str] = None,
            created: Optional[str] = None,
            deleted: Optional[str] = None,
            difficulty: Optional[int] = None,
            directions: Optional[str] = None,
            id: Optional[str] = None,
            image: Optional[str] = None,
            ingredients: Optional[str] = None,
            name: Optional[str] = None,
            notes: Optional[List['CookRecipeNote']] = None,
            public: Optional[bool] = None,
            rating: Optional[int] = None,
            servings: Optional[str] = None,
            short_id: Optional[str] = None,
            source: Optional[str] = None,
            tags: Optional[List[str]] = None,
            time_cook: Optional[int] = None,
            time_prep: Optional[int] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.cook_meal_plan_count = cook_meal_plan_count

        self.cook_meal_plan_last = cook_meal_plan_last

        self.created = created

        self.deleted = deleted

        self.difficulty = difficulty

        self.directions = directions

        self.id = id

        self.image = image

        self.ingredients = ingredients

        self.name = name

        self.notes = notes

        self.public = public

        self.rating = rating

        self.servings = servings

        self.short_id = short_id

        self.source = source

        self.tags = tags

        self.time_cook = time_cook

        self.time_prep = time_prep

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to cook_recipe_to_jsonable.

        :return: JSON-able representation
        """
        return cook_recipe_to_jsonable(self)


def new_cook_recipe() -> CookRecipe:
    """Generates an instance of CookRecipe with default values."""
    return CookRecipe()


def cook_recipe_from_obj(obj: Any, path: str = "") -> CookRecipe:
    """
    Generates an instance of CookRecipe from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of CookRecipe
    :param path: path to the object used for debugging
    :return: parsed instance of CookRecipe
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_cook_meal_plan_count = obj.get('cookMealPlanCount', None)
    if obj_cook_meal_plan_count is not None:
        cook_meal_plan_count_from_obj = from_obj(
            obj_cook_meal_plan_count,
            expected=[int],
            path=path + '.cookMealPlanCount')  # type: Optional[int]
    else:
        cook_meal_plan_count_from_obj = None

    obj_cook_meal_plan_last = obj.get('cookMealPlanLast', None)
    if obj_cook_meal_plan_last is not None:
        cook_meal_plan_last_from_obj = from_obj(
            obj_cook_meal_plan_last,
            expected=[str],
            path=path + '.cookMealPlanLast')  # type: Optional[str]
    else:
        cook_meal_plan_last_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_deleted = obj.get('deleted', None)
    if obj_deleted is not None:
        deleted_from_obj = from_obj(
            obj_deleted,
            expected=[str],
            path=path + '.deleted')  # type: Optional[str]
    else:
        deleted_from_obj = None

    obj_difficulty = obj.get('difficulty', None)
    if obj_difficulty is not None:
        difficulty_from_obj = from_obj(
            obj_difficulty,
            expected=[int],
            path=path + '.difficulty')  # type: Optional[int]
    else:
        difficulty_from_obj = None

    obj_directions = obj.get('directions', None)
    if obj_directions is not None:
        directions_from_obj = from_obj(
            obj_directions,
            expected=[str],
            path=path + '.directions')  # type: Optional[str]
    else:
        directions_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_image = obj.get('image', None)
    if obj_image is not None:
        image_from_obj = from_obj(
            obj_image,
            expected=[str],
            path=path + '.image')  # type: Optional[str]
    else:
        image_from_obj = None

    obj_ingredients = obj.get('ingredients', None)
    if obj_ingredients is not None:
        ingredients_from_obj = from_obj(
            obj_ingredients,
            expected=[str],
            path=path + '.ingredients')  # type: Optional[str]
    else:
        ingredients_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_notes = obj.get('notes', None)
    if obj_notes is not None:
        notes_from_obj = from_obj(
            obj_notes,
            expected=[list, CookRecipeNote],
            path=path + '.notes')  # type: Optional[List['CookRecipeNote']]
    else:
        notes_from_obj = None

    obj_public = obj.get('public', None)
    if obj_public is not None:
        public_from_obj = from_obj(
            obj_public,
            expected=[bool],
            path=path + '.public')  # type: Optional[bool]
    else:
        public_from_obj = None

    obj_rating = obj.get('rating', None)
    if obj_rating is not None:
        rating_from_obj = from_obj(
            obj_rating,
            expected=[int],
            path=path + '.rating')  # type: Optional[int]
    else:
        rating_from_obj = None

    obj_servings = obj.get('servings', None)
    if obj_servings is not None:
        servings_from_obj = from_obj(
            obj_servings,
            expected=[str],
            path=path + '.servings')  # type: Optional[str]
    else:
        servings_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_source = obj.get('source', None)
    if obj_source is not None:
        source_from_obj = from_obj(
            obj_source,
            expected=[str],
            path=path + '.source')  # type: Optional[str]
    else:
        source_from_obj = None

    obj_tags = obj.get('tags', None)
    if obj_tags is not None:
        tags_from_obj = from_obj(
            obj_tags,
            expected=[list, str],
            path=path + '.tags')  # type: Optional[List[str]]
    else:
        tags_from_obj = None

    obj_time_cook = obj.get('timeCook', None)
    if obj_time_cook is not None:
        time_cook_from_obj = from_obj(
            obj_time_cook,
            expected=[int],
            path=path + '.timeCook')  # type: Optional[int]
    else:
        time_cook_from_obj = None

    obj_time_prep = obj.get('timePrep', None)
    if obj_time_prep is not None:
        time_prep_from_obj = from_obj(
            obj_time_prep,
            expected=[int],
            path=path + '.timePrep')  # type: Optional[int]
    else:
        time_prep_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return CookRecipe(
        auth_household_id=auth_household_id_from_obj,
        cook_meal_plan_count=cook_meal_plan_count_from_obj,
        cook_meal_plan_last=cook_meal_plan_last_from_obj,
        created=created_from_obj,
        deleted=deleted_from_obj,
        difficulty=difficulty_from_obj,
        directions=directions_from_obj,
        id=id_from_obj,
        image=image_from_obj,
        ingredients=ingredients_from_obj,
        name=name_from_obj,
        notes=notes_from_obj,
        public=public_from_obj,
        rating=rating_from_obj,
        servings=servings_from_obj,
        short_id=short_id_from_obj,
        source=source_from_obj,
        tags=tags_from_obj,
        time_cook=time_cook_from_obj,
        time_prep=time_prep_from_obj,
        updated=updated_from_obj)


def cook_recipe_to_jsonable(
        cook_recipe: CookRecipe,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of CookRecipe.

    :param cook_recipe: instance of CookRecipe to be JSON-ized
    :param path: path to the cook_recipe used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if cook_recipe.auth_household_id is not None:
        res['authHouseholdID'] = cook_recipe.auth_household_id

    if cook_recipe.cook_meal_plan_count is not None:
        res['cookMealPlanCount'] = cook_recipe.cook_meal_plan_count

    if cook_recipe.cook_meal_plan_last is not None:
        res['cookMealPlanLast'] = cook_recipe.cook_meal_plan_last

    if cook_recipe.created is not None:
        res['created'] = cook_recipe.created

    if cook_recipe.deleted is not None:
        res['deleted'] = cook_recipe.deleted

    if cook_recipe.difficulty is not None:
        res['difficulty'] = cook_recipe.difficulty

    if cook_recipe.directions is not None:
        res['directions'] = cook_recipe.directions

    if cook_recipe.id is not None:
        res['id'] = cook_recipe.id

    if cook_recipe.image is not None:
        res['image'] = cook_recipe.image

    if cook_recipe.ingredients is not None:
        res['ingredients'] = cook_recipe.ingredients

    if cook_recipe.name is not None:
        res['name'] = cook_recipe.name

    if cook_recipe.notes is not None:
        res['notes'] = to_jsonable(
        cook_recipe.notes,
        expected=[list, CookRecipeNote],
        path='{}.notes'.format(path))

    if cook_recipe.public is not None:
        res['public'] = cook_recipe.public

    if cook_recipe.rating is not None:
        res['rating'] = cook_recipe.rating

    if cook_recipe.servings is not None:
        res['servings'] = cook_recipe.servings

    if cook_recipe.short_id is not None:
        res['shortID'] = cook_recipe.short_id

    if cook_recipe.source is not None:
        res['source'] = cook_recipe.source

    if cook_recipe.tags is not None:
        res['tags'] = to_jsonable(
        cook_recipe.tags,
        expected=[list, str],
        path='{}.tags'.format(path))

    if cook_recipe.time_cook is not None:
        res['timeCook'] = cook_recipe.time_cook

    if cook_recipe.time_prep is not None:
        res['timePrep'] = cook_recipe.time_prep

    if cook_recipe.updated is not None:
        res['updated'] = cook_recipe.updated

    return res


class CookRecipeNote:
    def __init__(
            self,
            date: Optional[Any] = None,
            difficulty: Optional[int] = None,
            note: Optional[str] = None,
            rating: Optional[int] = None) -> None:
        """Initializes with the given values."""
        self.date = date

        self.difficulty = difficulty

        self.note = note

        self.rating = rating

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to cook_recipe_note_to_jsonable.

        :return: JSON-able representation
        """
        return cook_recipe_note_to_jsonable(self)


def new_cook_recipe_note() -> CookRecipeNote:
    """Generates an instance of CookRecipeNote with default values."""
    return CookRecipeNote()


def cook_recipe_note_from_obj(obj: Any, path: str = "") -> CookRecipeNote:
    """
    Generates an instance of CookRecipeNote from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of CookRecipeNote
    :param path: path to the object used for debugging
    :return: parsed instance of CookRecipeNote
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    date_from_obj = obj.get('date', None)

    obj_difficulty = obj.get('difficulty', None)
    if obj_difficulty is not None:
        difficulty_from_obj = from_obj(
            obj_difficulty,
            expected=[int],
            path=path + '.difficulty')  # type: Optional[int]
    else:
        difficulty_from_obj = None

    obj_note = obj.get('note', None)
    if obj_note is not None:
        note_from_obj = from_obj(
            obj_note,
            expected=[str],
            path=path + '.note')  # type: Optional[str]
    else:
        note_from_obj = None

    obj_rating = obj.get('rating', None)
    if obj_rating is not None:
        rating_from_obj = from_obj(
            obj_rating,
            expected=[int],
            path=path + '.rating')  # type: Optional[int]
    else:
        rating_from_obj = None

    return CookRecipeNote(
        date=date_from_obj,
        difficulty=difficulty_from_obj,
        note=note_from_obj,
        rating=rating_from_obj)


def cook_recipe_note_to_jsonable(
        cook_recipe_note: CookRecipeNote,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of CookRecipeNote.

    :param cook_recipe_note: instance of CookRecipeNote to be JSON-ized
    :param path: path to the cook_recipe_note used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if cook_recipe_note.date is not None:
        res['date'] = cook_recipe_note.date

    if cook_recipe_note.difficulty is not None:
        res['difficulty'] = cook_recipe_note.difficulty

    if cook_recipe_note.note is not None:
        res['note'] = cook_recipe_note.note

    if cook_recipe_note.rating is not None:
        res['rating'] = cook_recipe_note.rating

    return res


class HealthItem:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            color: Optional[int] = None,
            correlations: Optional[Dict[str, int]] = None,
            created: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            output: Optional[bool] = None,
            total_correlations: Optional[int] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.color = color

        self.correlations = correlations

        self.created = created

        self.id = id

        self.name = name

        self.output = output

        self.total_correlations = total_correlations

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to health_item_to_jsonable.

        :return: JSON-able representation
        """
        return health_item_to_jsonable(self)


def new_health_item() -> HealthItem:
    """Generates an instance of HealthItem with default values."""
    return HealthItem()


def health_item_from_obj(obj: Any, path: str = "") -> HealthItem:
    """
    Generates an instance of HealthItem from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of HealthItem
    :param path: path to the object used for debugging
    :return: parsed instance of HealthItem
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_color = obj.get('color', None)
    if obj_color is not None:
        color_from_obj = from_obj(
            obj_color,
            expected=[int],
            path=path + '.color')  # type: Optional[int]
    else:
        color_from_obj = None

    obj_correlations = obj.get('correlations', None)
    if obj_correlations is not None:
        correlations_from_obj = from_obj(
            obj_correlations,
            expected=[dict, int],
            path=path + '.correlations')  # type: Optional[Dict[str, int]]
    else:
        correlations_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_output = obj.get('output', None)
    if obj_output is not None:
        output_from_obj = from_obj(
            obj_output,
            expected=[bool],
            path=path + '.output')  # type: Optional[bool]
    else:
        output_from_obj = None

    obj_total_correlations = obj.get('totalCorrelations', None)
    if obj_total_correlations is not None:
        total_correlations_from_obj = from_obj(
            obj_total_correlations,
            expected=[int],
            path=path + '.totalCorrelations')  # type: Optional[int]
    else:
        total_correlations_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return HealthItem(
        auth_account_id=auth_account_id_from_obj,
        color=color_from_obj,
        correlations=correlations_from_obj,
        created=created_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        output=output_from_obj,
        total_correlations=total_correlations_from_obj,
        updated=updated_from_obj)


def health_item_to_jsonable(
        health_item: HealthItem,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of HealthItem.

    :param health_item: instance of HealthItem to be JSON-ized
    :param path: path to the health_item used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if health_item.auth_account_id is not None:
        res['authAccountID'] = health_item.auth_account_id

    if health_item.color is not None:
        res['color'] = health_item.color

    if health_item.correlations is not None:
        res['correlations'] = to_jsonable(
        health_item.correlations,
        expected=[dict, int],
        path='{}.correlations'.format(path))

    if health_item.created is not None:
        res['created'] = health_item.created

    if health_item.id is not None:
        res['id'] = health_item.id

    if health_item.name is not None:
        res['name'] = health_item.name

    if health_item.output is not None:
        res['output'] = health_item.output

    if health_item.total_correlations is not None:
        res['totalCorrelations'] = health_item.total_correlations

    if health_item.updated is not None:
        res['updated'] = health_item.updated

    return res


class HealthLog:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            created: Optional[str] = None,
            date: Optional['CivilDate'] = None,
            health_item_id: Optional[str] = None,
            id: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.created = created

        self.date = date

        self.health_item_id = health_item_id

        self.id = id

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to health_log_to_jsonable.

        :return: JSON-able representation
        """
        return health_log_to_jsonable(self)


def new_health_log() -> HealthLog:
    """Generates an instance of HealthLog with default values."""
    return HealthLog()


def health_log_from_obj(obj: Any, path: str = "") -> HealthLog:
    """
    Generates an instance of HealthLog from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of HealthLog
    :param path: path to the object used for debugging
    :return: parsed instance of HealthLog
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_date = obj.get('date', None)
    if obj_date is not None:
        date_from_obj = from_obj(
            obj_date,
            expected=[CivilDate],
            path=path + '.date')  # type: Optional['CivilDate']
    else:
        date_from_obj = None

    obj_health_item_id = obj.get('healthItemID', None)
    if obj_health_item_id is not None:
        health_item_id_from_obj = from_obj(
            obj_health_item_id,
            expected=[str],
            path=path + '.healthItemID')  # type: Optional[str]
    else:
        health_item_id_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return HealthLog(
        auth_account_id=auth_account_id_from_obj,
        created=created_from_obj,
        date=date_from_obj,
        health_item_id=health_item_id_from_obj,
        id=id_from_obj,
        updated=updated_from_obj)


def health_log_to_jsonable(
        health_log: HealthLog,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of HealthLog.

    :param health_log: instance of HealthLog to be JSON-ized
    :param path: path to the health_log used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if health_log.auth_account_id is not None:
        res['authAccountID'] = health_log.auth_account_id

    if health_log.created is not None:
        res['created'] = health_log.created

    if health_log.date is not None:
        res['date'] = to_jsonable(
        health_log.date,
        expected=[CivilDate],
        path='{}.date'.format(path))

    if health_log.health_item_id is not None:
        res['healthItemID'] = health_log.health_item_id

    if health_log.id is not None:
        res['id'] = health_log.id

    if health_log.updated is not None:
        res['updated'] = health_log.updated

    return res


class ID:
    def __init__(
            self,
            id: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.id = id

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to id_to_jsonable.

        :return: JSON-able representation
        """
        return id_to_jsonable(self)


def new_id() -> ID:
    """Generates an instance of ID with default values."""
    return ID()


def id_from_obj(obj: Any, path: str = "") -> ID:
    """
    Generates an instance of ID from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ID
    :param path: path to the object used for debugging
    :return: parsed instance of ID
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return ID(
        id=id_from_obj,
        updated=updated_from_obj)


def id_to_jsonable(
        id: ID,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ID.

    :param id: instance of ID to be JSON-ized
    :param path: path to the id used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if id.id is not None:
        res['id'] = id.id

    if id.updated is not None:
        res['updated'] = id.updated

    return res


class InventoryCollection:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            columns: Optional[Dict[str, str]] = None,
            created: Optional[str] = None,
            grouping: Optional[str] = None,
            icon: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            short_id: Optional[str] = None,
            sort: Optional['InventoryCollectionSort'] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.columns = columns

        self.created = created

        self.grouping = grouping

        self.icon = icon

        self.id = id

        self.name = name

        self.short_id = short_id

        self.sort = sort

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to inventory_collection_to_jsonable.

        :return: JSON-able representation
        """
        return inventory_collection_to_jsonable(self)


def new_inventory_collection() -> InventoryCollection:
    """Generates an instance of InventoryCollection with default values."""
    return InventoryCollection()


def inventory_collection_from_obj(obj: Any, path: str = "") -> InventoryCollection:
    """
    Generates an instance of InventoryCollection from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of InventoryCollection
    :param path: path to the object used for debugging
    :return: parsed instance of InventoryCollection
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_columns = obj.get('columns', None)
    if obj_columns is not None:
        columns_from_obj = from_obj(
            obj_columns,
            expected=[dict, str],
            path=path + '.columns')  # type: Optional[Dict[str, str]]
    else:
        columns_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_grouping = obj.get('grouping', None)
    if obj_grouping is not None:
        grouping_from_obj = from_obj(
            obj_grouping,
            expected=[str],
            path=path + '.grouping')  # type: Optional[str]
    else:
        grouping_from_obj = None

    obj_icon = obj.get('icon', None)
    if obj_icon is not None:
        icon_from_obj = from_obj(
            obj_icon,
            expected=[str],
            path=path + '.icon')  # type: Optional[str]
    else:
        icon_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_sort = obj.get('sort', None)
    if obj_sort is not None:
        sort_from_obj = from_obj(
            obj_sort,
            expected=[InventoryCollectionSort],
            path=path + '.sort')  # type: Optional['InventoryCollectionSort']
    else:
        sort_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return InventoryCollection(
        auth_household_id=auth_household_id_from_obj,
        columns=columns_from_obj,
        created=created_from_obj,
        grouping=grouping_from_obj,
        icon=icon_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        short_id=short_id_from_obj,
        sort=sort_from_obj,
        updated=updated_from_obj)


def inventory_collection_to_jsonable(
        inventory_collection: InventoryCollection,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of InventoryCollection.

    :param inventory_collection: instance of InventoryCollection to be JSON-ized
    :param path: path to the inventory_collection used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if inventory_collection.auth_household_id is not None:
        res['authHouseholdID'] = inventory_collection.auth_household_id

    if inventory_collection.columns is not None:
        res['columns'] = to_jsonable(
        inventory_collection.columns,
        expected=[dict, str],
        path='{}.columns'.format(path))

    if inventory_collection.created is not None:
        res['created'] = inventory_collection.created

    if inventory_collection.grouping is not None:
        res['grouping'] = inventory_collection.grouping

    if inventory_collection.icon is not None:
        res['icon'] = inventory_collection.icon

    if inventory_collection.id is not None:
        res['id'] = inventory_collection.id

    if inventory_collection.name is not None:
        res['name'] = inventory_collection.name

    if inventory_collection.short_id is not None:
        res['shortID'] = inventory_collection.short_id

    if inventory_collection.sort is not None:
        res['sort'] = to_jsonable(
        inventory_collection.sort,
        expected=[InventoryCollectionSort],
        path='{}.sort'.format(path))

    if inventory_collection.updated is not None:
        res['updated'] = inventory_collection.updated

    return res


class InventoryCollectionSort:
    def __init__(
            self,
            invert: Optional[bool] = None,
            property: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.invert = invert

        self.property = property

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to inventory_collection_sort_to_jsonable.

        :return: JSON-able representation
        """
        return inventory_collection_sort_to_jsonable(self)


def new_inventory_collection_sort() -> InventoryCollectionSort:
    """Generates an instance of InventoryCollectionSort with default values."""
    return InventoryCollectionSort()


def inventory_collection_sort_from_obj(obj: Any, path: str = "") -> InventoryCollectionSort:
    """
    Generates an instance of InventoryCollectionSort from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of InventoryCollectionSort
    :param path: path to the object used for debugging
    :return: parsed instance of InventoryCollectionSort
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_invert = obj.get('invert', None)
    if obj_invert is not None:
        invert_from_obj = from_obj(
            obj_invert,
            expected=[bool],
            path=path + '.invert')  # type: Optional[bool]
    else:
        invert_from_obj = None

    obj_property = obj.get('property', None)
    if obj_property is not None:
        property_from_obj = from_obj(
            obj_property,
            expected=[str],
            path=path + '.property')  # type: Optional[str]
    else:
        property_from_obj = None

    return InventoryCollectionSort(
        invert=invert_from_obj,
        property=property_from_obj)


def inventory_collection_sort_to_jsonable(
        inventory_collection_sort: InventoryCollectionSort,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of InventoryCollectionSort.

    :param inventory_collection_sort: instance of InventoryCollectionSort to be JSON-ized
    :param path: path to the inventory_collection_sort used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if inventory_collection_sort.invert is not None:
        res['invert'] = inventory_collection_sort.invert

    if inventory_collection_sort.property is not None:
        res['property'] = inventory_collection_sort.property

    return res


class InventoryItem:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            created: Optional[str] = None,
            id: Optional[str] = None,
            image: Optional[str] = None,
            last_purchased: Optional[str] = None,
            name: Optional[str] = None,
            properties: Optional[Dict[str, str]] = None,
            quantity: Optional[int] = None,
            short_id: Optional[str] = None,
            upc: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.created = created

        self.id = id

        self.image = image

        self.last_purchased = last_purchased

        self.name = name

        self.properties = properties

        self.quantity = quantity

        self.short_id = short_id

        self.upc = upc

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to inventory_item_to_jsonable.

        :return: JSON-able representation
        """
        return inventory_item_to_jsonable(self)


def new_inventory_item() -> InventoryItem:
    """Generates an instance of InventoryItem with default values."""
    return InventoryItem()


def inventory_item_from_obj(obj: Any, path: str = "") -> InventoryItem:
    """
    Generates an instance of InventoryItem from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of InventoryItem
    :param path: path to the object used for debugging
    :return: parsed instance of InventoryItem
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_image = obj.get('image', None)
    if obj_image is not None:
        image_from_obj = from_obj(
            obj_image,
            expected=[str],
            path=path + '.image')  # type: Optional[str]
    else:
        image_from_obj = None

    obj_last_purchased = obj.get('lastPurchased', None)
    if obj_last_purchased is not None:
        last_purchased_from_obj = from_obj(
            obj_last_purchased,
            expected=[str],
            path=path + '.lastPurchased')  # type: Optional[str]
    else:
        last_purchased_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_properties = obj.get('properties', None)
    if obj_properties is not None:
        properties_from_obj = from_obj(
            obj_properties,
            expected=[dict, str],
            path=path + '.properties')  # type: Optional[Dict[str, str]]
    else:
        properties_from_obj = None

    obj_quantity = obj.get('quantity', None)
    if obj_quantity is not None:
        quantity_from_obj = from_obj(
            obj_quantity,
            expected=[int],
            path=path + '.quantity')  # type: Optional[int]
    else:
        quantity_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_upc = obj.get('upc', None)
    if obj_upc is not None:
        upc_from_obj = from_obj(
            obj_upc,
            expected=[str],
            path=path + '.upc')  # type: Optional[str]
    else:
        upc_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return InventoryItem(
        auth_household_id=auth_household_id_from_obj,
        created=created_from_obj,
        id=id_from_obj,
        image=image_from_obj,
        last_purchased=last_purchased_from_obj,
        name=name_from_obj,
        properties=properties_from_obj,
        quantity=quantity_from_obj,
        short_id=short_id_from_obj,
        upc=upc_from_obj,
        updated=updated_from_obj)


def inventory_item_to_jsonable(
        inventory_item: InventoryItem,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of InventoryItem.

    :param inventory_item: instance of InventoryItem to be JSON-ized
    :param path: path to the inventory_item used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if inventory_item.auth_household_id is not None:
        res['authHouseholdID'] = inventory_item.auth_household_id

    if inventory_item.created is not None:
        res['created'] = inventory_item.created

    if inventory_item.id is not None:
        res['id'] = inventory_item.id

    if inventory_item.image is not None:
        res['image'] = inventory_item.image

    if inventory_item.last_purchased is not None:
        res['lastPurchased'] = inventory_item.last_purchased

    if inventory_item.name is not None:
        res['name'] = inventory_item.name

    if inventory_item.properties is not None:
        res['properties'] = to_jsonable(
        inventory_item.properties,
        expected=[dict, str],
        path='{}.properties'.format(path))

    if inventory_item.quantity is not None:
        res['quantity'] = inventory_item.quantity

    if inventory_item.short_id is not None:
        res['shortID'] = inventory_item.short_id

    if inventory_item.upc is not None:
        res['upc'] = inventory_item.upc

    if inventory_item.updated is not None:
        res['updated'] = inventory_item.updated

    return res


class NotesPage:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            color: Optional[int] = None,
            created: Optional[str] = None,
            deleted: Optional[str] = None,
            icon: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            parent_id: Optional[str] = None,
            short_id: Optional[str] = None,
            tags: Optional[List[str]] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.color = color

        self.created = created

        self.deleted = deleted

        self.icon = icon

        self.id = id

        self.name = name

        self.parent_id = parent_id

        self.short_id = short_id

        self.tags = tags

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to notes_page_to_jsonable.

        :return: JSON-able representation
        """
        return notes_page_to_jsonable(self)


def new_notes_page() -> NotesPage:
    """Generates an instance of NotesPage with default values."""
    return NotesPage()


def notes_page_from_obj(obj: Any, path: str = "") -> NotesPage:
    """
    Generates an instance of NotesPage from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of NotesPage
    :param path: path to the object used for debugging
    :return: parsed instance of NotesPage
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_color = obj.get('color', None)
    if obj_color is not None:
        color_from_obj = from_obj(
            obj_color,
            expected=[int],
            path=path + '.color')  # type: Optional[int]
    else:
        color_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_deleted = obj.get('deleted', None)
    if obj_deleted is not None:
        deleted_from_obj = from_obj(
            obj_deleted,
            expected=[str],
            path=path + '.deleted')  # type: Optional[str]
    else:
        deleted_from_obj = None

    obj_icon = obj.get('icon', None)
    if obj_icon is not None:
        icon_from_obj = from_obj(
            obj_icon,
            expected=[str],
            path=path + '.icon')  # type: Optional[str]
    else:
        icon_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_parent_id = obj.get('parentID', None)
    if obj_parent_id is not None:
        parent_id_from_obj = from_obj(
            obj_parent_id,
            expected=[str],
            path=path + '.parentID')  # type: Optional[str]
    else:
        parent_id_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_tags = obj.get('tags', None)
    if obj_tags is not None:
        tags_from_obj = from_obj(
            obj_tags,
            expected=[list, str],
            path=path + '.tags')  # type: Optional[List[str]]
    else:
        tags_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return NotesPage(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        color=color_from_obj,
        created=created_from_obj,
        deleted=deleted_from_obj,
        icon=icon_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        parent_id=parent_id_from_obj,
        short_id=short_id_from_obj,
        tags=tags_from_obj,
        updated=updated_from_obj)


def notes_page_to_jsonable(
        notes_page: NotesPage,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of NotesPage.

    :param notes_page: instance of NotesPage to be JSON-ized
    :param path: path to the notes_page used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if notes_page.auth_account_id is not None:
        res['authAccountID'] = notes_page.auth_account_id

    if notes_page.auth_household_id is not None:
        res['authHouseholdID'] = notes_page.auth_household_id

    if notes_page.color is not None:
        res['color'] = notes_page.color

    if notes_page.created is not None:
        res['created'] = notes_page.created

    if notes_page.deleted is not None:
        res['deleted'] = notes_page.deleted

    if notes_page.icon is not None:
        res['icon'] = notes_page.icon

    if notes_page.id is not None:
        res['id'] = notes_page.id

    if notes_page.name is not None:
        res['name'] = notes_page.name

    if notes_page.parent_id is not None:
        res['parentID'] = notes_page.parent_id

    if notes_page.short_id is not None:
        res['shortID'] = notes_page.short_id

    if notes_page.tags is not None:
        res['tags'] = to_jsonable(
        notes_page.tags,
        expected=[list, str],
        path='{}.tags'.format(path))

    if notes_page.updated is not None:
        res['updated'] = notes_page.updated

    return res


class NotesPageVersion:
    def __init__(
            self,
            body: Optional[str] = None,
            created_by: Optional[str] = None,
            id: Optional[str] = None,
            notes_page_id: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.body = body

        self.created_by = created_by

        self.id = id

        self.notes_page_id = notes_page_id

        # Updated is technically the created field, but the existing merge and query code uses updated and it's hard to justify duplicating all that code for a semantic change.  Alternatively, having a created and updated field seems very redundant as they will always be equal.
        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to notes_page_version_to_jsonable.

        :return: JSON-able representation
        """
        return notes_page_version_to_jsonable(self)


def new_notes_page_version() -> NotesPageVersion:
    """Generates an instance of NotesPageVersion with default values."""
    return NotesPageVersion()


def notes_page_version_from_obj(obj: Any, path: str = "") -> NotesPageVersion:
    """
    Generates an instance of NotesPageVersion from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of NotesPageVersion
    :param path: path to the object used for debugging
    :return: parsed instance of NotesPageVersion
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_body = obj.get('body', None)
    if obj_body is not None:
        body_from_obj = from_obj(
            obj_body,
            expected=[str],
            path=path + '.body')  # type: Optional[str]
    else:
        body_from_obj = None

    obj_created_by = obj.get('createdBy', None)
    if obj_created_by is not None:
        created_by_from_obj = from_obj(
            obj_created_by,
            expected=[str],
            path=path + '.createdBy')  # type: Optional[str]
    else:
        created_by_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_notes_page_id = obj.get('notesPageID', None)
    if obj_notes_page_id is not None:
        notes_page_id_from_obj = from_obj(
            obj_notes_page_id,
            expected=[str],
            path=path + '.notesPageID')  # type: Optional[str]
    else:
        notes_page_id_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return NotesPageVersion(
        body=body_from_obj,
        created_by=created_by_from_obj,
        id=id_from_obj,
        notes_page_id=notes_page_id_from_obj,
        updated=updated_from_obj)


def notes_page_version_to_jsonable(
        notes_page_version: NotesPageVersion,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of NotesPageVersion.

    :param notes_page_version: instance of NotesPageVersion to be JSON-ized
    :param path: path to the notes_page_version used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if notes_page_version.body is not None:
        res['body'] = notes_page_version.body

    if notes_page_version.created_by is not None:
        res['createdBy'] = notes_page_version.created_by

    if notes_page_version.id is not None:
        res['id'] = notes_page_version.id

    if notes_page_version.notes_page_id is not None:
        res['notesPageID'] = notes_page_version.notes_page_id

    if notes_page_version.updated is not None:
        res['updated'] = notes_page_version.updated

    return res


class Permissions:
    def __init__(
            self,
            auth: Optional[int] = None,
            budget: Optional[int] = None,
            calendar: Optional[int] = None,
            cook: Optional[int] = None,
            health: Optional[int] = None,
            inventory: Optional[int] = None,
            notes: Optional[int] = None,
            plan: Optional[int] = None,
            reward: Optional[int] = None,
            secrets: Optional[int] = None,
            shop: Optional[int] = None) -> None:
        """Initializes with the given values."""
        self.auth = auth

        self.budget = budget

        self.calendar = calendar

        self.cook = cook

        self.health = health

        self.inventory = inventory

        self.notes = notes

        self.plan = plan

        self.reward = reward

        self.secrets = secrets

        self.shop = shop

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to permissions_to_jsonable.

        :return: JSON-able representation
        """
        return permissions_to_jsonable(self)


def new_permissions() -> Permissions:
    """Generates an instance of Permissions with default values."""
    return Permissions()


def permissions_from_obj(obj: Any, path: str = "") -> Permissions:
    """
    Generates an instance of Permissions from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Permissions
    :param path: path to the object used for debugging
    :return: parsed instance of Permissions
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth = obj.get('auth', None)
    if obj_auth is not None:
        auth_from_obj = from_obj(
            obj_auth,
            expected=[int],
            path=path + '.auth')  # type: Optional[int]
    else:
        auth_from_obj = None

    obj_budget = obj.get('budget', None)
    if obj_budget is not None:
        budget_from_obj = from_obj(
            obj_budget,
            expected=[int],
            path=path + '.budget')  # type: Optional[int]
    else:
        budget_from_obj = None

    obj_calendar = obj.get('calendar', None)
    if obj_calendar is not None:
        calendar_from_obj = from_obj(
            obj_calendar,
            expected=[int],
            path=path + '.calendar')  # type: Optional[int]
    else:
        calendar_from_obj = None

    obj_cook = obj.get('cook', None)
    if obj_cook is not None:
        cook_from_obj = from_obj(
            obj_cook,
            expected=[int],
            path=path + '.cook')  # type: Optional[int]
    else:
        cook_from_obj = None

    obj_health = obj.get('health', None)
    if obj_health is not None:
        health_from_obj = from_obj(
            obj_health,
            expected=[int],
            path=path + '.health')  # type: Optional[int]
    else:
        health_from_obj = None

    obj_inventory = obj.get('inventory', None)
    if obj_inventory is not None:
        inventory_from_obj = from_obj(
            obj_inventory,
            expected=[int],
            path=path + '.inventory')  # type: Optional[int]
    else:
        inventory_from_obj = None

    obj_notes = obj.get('notes', None)
    if obj_notes is not None:
        notes_from_obj = from_obj(
            obj_notes,
            expected=[int],
            path=path + '.notes')  # type: Optional[int]
    else:
        notes_from_obj = None

    obj_plan = obj.get('plan', None)
    if obj_plan is not None:
        plan_from_obj = from_obj(
            obj_plan,
            expected=[int],
            path=path + '.plan')  # type: Optional[int]
    else:
        plan_from_obj = None

    obj_reward = obj.get('reward', None)
    if obj_reward is not None:
        reward_from_obj = from_obj(
            obj_reward,
            expected=[int],
            path=path + '.reward')  # type: Optional[int]
    else:
        reward_from_obj = None

    obj_secrets = obj.get('secrets', None)
    if obj_secrets is not None:
        secrets_from_obj = from_obj(
            obj_secrets,
            expected=[int],
            path=path + '.secrets')  # type: Optional[int]
    else:
        secrets_from_obj = None

    obj_shop = obj.get('shop', None)
    if obj_shop is not None:
        shop_from_obj = from_obj(
            obj_shop,
            expected=[int],
            path=path + '.shop')  # type: Optional[int]
    else:
        shop_from_obj = None

    return Permissions(
        auth=auth_from_obj,
        budget=budget_from_obj,
        calendar=calendar_from_obj,
        cook=cook_from_obj,
        health=health_from_obj,
        inventory=inventory_from_obj,
        notes=notes_from_obj,
        plan=plan_from_obj,
        reward=reward_from_obj,
        secrets=secrets_from_obj,
        shop=shop_from_obj)


def permissions_to_jsonable(
        permissions: Permissions,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Permissions.

    :param permissions: instance of Permissions to be JSON-ized
    :param path: path to the permissions used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if permissions.auth is not None:
        res['auth'] = permissions.auth

    if permissions.budget is not None:
        res['budget'] = permissions.budget

    if permissions.calendar is not None:
        res['calendar'] = permissions.calendar

    if permissions.cook is not None:
        res['cook'] = permissions.cook

    if permissions.health is not None:
        res['health'] = permissions.health

    if permissions.inventory is not None:
        res['inventory'] = permissions.inventory

    if permissions.notes is not None:
        res['notes'] = permissions.notes

    if permissions.plan is not None:
        res['plan'] = permissions.plan

    if permissions.reward is not None:
        res['reward'] = permissions.reward

    if permissions.secrets is not None:
        res['secrets'] = permissions.secrets

    if permissions.shop is not None:
        res['shop'] = permissions.shop

    return res


class PlanProject:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            budget_category_id: Optional[str] = None,
            color: Optional[int] = None,
            created: Optional[str] = None,
            icon: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            parent_id: Optional[str] = None,
            plan_task_count: Optional[int] = None,
            position: Optional[str] = None,
            shop_item_count: Optional[int] = None,
            short_id: Optional[str] = None,
            tags: Optional[List[str]] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.budget_category_id = budget_category_id

        self.color = color

        self.created = created

        self.icon = icon

        self.id = id

        self.name = name

        self.parent_id = parent_id

        self.plan_task_count = plan_task_count

        self.position = position

        self.shop_item_count = shop_item_count

        self.short_id = short_id

        self.tags = tags

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to plan_project_to_jsonable.

        :return: JSON-able representation
        """
        return plan_project_to_jsonable(self)


def new_plan_project() -> PlanProject:
    """Generates an instance of PlanProject with default values."""
    return PlanProject()


def plan_project_from_obj(obj: Any, path: str = "") -> PlanProject:
    """
    Generates an instance of PlanProject from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of PlanProject
    :param path: path to the object used for debugging
    :return: parsed instance of PlanProject
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_category_id = obj.get('budgetCategoryID', None)
    if obj_budget_category_id is not None:
        budget_category_id_from_obj = from_obj(
            obj_budget_category_id,
            expected=[str],
            path=path + '.budgetCategoryID')  # type: Optional[str]
    else:
        budget_category_id_from_obj = None

    obj_color = obj.get('color', None)
    if obj_color is not None:
        color_from_obj = from_obj(
            obj_color,
            expected=[int],
            path=path + '.color')  # type: Optional[int]
    else:
        color_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_icon = obj.get('icon', None)
    if obj_icon is not None:
        icon_from_obj = from_obj(
            obj_icon,
            expected=[str],
            path=path + '.icon')  # type: Optional[str]
    else:
        icon_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_parent_id = obj.get('parentID', None)
    if obj_parent_id is not None:
        parent_id_from_obj = from_obj(
            obj_parent_id,
            expected=[str],
            path=path + '.parentID')  # type: Optional[str]
    else:
        parent_id_from_obj = None

    obj_plan_task_count = obj.get('planTaskCount', None)
    if obj_plan_task_count is not None:
        plan_task_count_from_obj = from_obj(
            obj_plan_task_count,
            expected=[int],
            path=path + '.planTaskCount')  # type: Optional[int]
    else:
        plan_task_count_from_obj = None

    obj_position = obj.get('position', None)
    if obj_position is not None:
        position_from_obj = from_obj(
            obj_position,
            expected=[str],
            path=path + '.position')  # type: Optional[str]
    else:
        position_from_obj = None

    obj_shop_item_count = obj.get('shopItemCount', None)
    if obj_shop_item_count is not None:
        shop_item_count_from_obj = from_obj(
            obj_shop_item_count,
            expected=[int],
            path=path + '.shopItemCount')  # type: Optional[int]
    else:
        shop_item_count_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_tags = obj.get('tags', None)
    if obj_tags is not None:
        tags_from_obj = from_obj(
            obj_tags,
            expected=[list, str],
            path=path + '.tags')  # type: Optional[List[str]]
    else:
        tags_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return PlanProject(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        budget_category_id=budget_category_id_from_obj,
        color=color_from_obj,
        created=created_from_obj,
        icon=icon_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        parent_id=parent_id_from_obj,
        plan_task_count=plan_task_count_from_obj,
        position=position_from_obj,
        shop_item_count=shop_item_count_from_obj,
        short_id=short_id_from_obj,
        tags=tags_from_obj,
        updated=updated_from_obj)


def plan_project_to_jsonable(
        plan_project: PlanProject,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of PlanProject.

    :param plan_project: instance of PlanProject to be JSON-ized
    :param path: path to the plan_project used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if plan_project.auth_account_id is not None:
        res['authAccountID'] = plan_project.auth_account_id

    if plan_project.auth_household_id is not None:
        res['authHouseholdID'] = plan_project.auth_household_id

    if plan_project.budget_category_id is not None:
        res['budgetCategoryID'] = plan_project.budget_category_id

    if plan_project.color is not None:
        res['color'] = plan_project.color

    if plan_project.created is not None:
        res['created'] = plan_project.created

    if plan_project.icon is not None:
        res['icon'] = plan_project.icon

    if plan_project.id is not None:
        res['id'] = plan_project.id

    if plan_project.name is not None:
        res['name'] = plan_project.name

    if plan_project.parent_id is not None:
        res['parentID'] = plan_project.parent_id

    if plan_project.plan_task_count is not None:
        res['planTaskCount'] = plan_project.plan_task_count

    if plan_project.position is not None:
        res['position'] = plan_project.position

    if plan_project.shop_item_count is not None:
        res['shopItemCount'] = plan_project.shop_item_count

    if plan_project.short_id is not None:
        res['shortID'] = plan_project.short_id

    if plan_project.tags is not None:
        res['tags'] = to_jsonable(
        plan_project.tags,
        expected=[list, str],
        path='{}.tags'.format(path))

    if plan_project.updated is not None:
        res['updated'] = plan_project.updated

    return res


class PlanTask:
    def __init__(
            self,
            assignees: Optional[List[str]] = None,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            color: Optional[int] = None,
            created: Optional[str] = None,
            date_end: Optional[str] = None,
            details: Optional[str] = None,
            done: Optional[bool] = None,
            due_date: Optional[str] = None,
            duration: Optional[int] = None,
            id: Optional[str] = None,
            inventory_item_id: Optional[str] = None,
            last_done_by: Optional[str] = None,
            last_done_date: Optional['CivilDate'] = None,
            name: Optional[str] = None,
            notify: Optional[bool] = None,
            parent_id: Optional[str] = None,
            plan_project_id: Optional[str] = None,
            position: Optional[str] = None,
            recur_on_done: Optional[bool] = None,
            recurrence: Optional['Recurrence'] = None,
            short_id: Optional[str] = None,
            tags: Optional[List[str]] = None,
            template: Optional[bool] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.assignees = assignees

        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.color = color

        self.created = created

        # end of event or recurrence
        self.date_end = date_end

        self.details = details

        self.done = done

        self.due_date = due_date

        self.duration = duration

        self.id = id

        self.inventory_item_id = inventory_item_id

        self.last_done_by = last_done_by

        self.last_done_date = last_done_date

        self.name = name

        self.notify = notify

        self.parent_id = parent_id

        self.plan_project_id = plan_project_id

        self.position = position

        self.recur_on_done = recur_on_done

        self.recurrence = recurrence

        self.short_id = short_id

        self.tags = tags

        self.template = template

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to plan_task_to_jsonable.

        :return: JSON-able representation
        """
        return plan_task_to_jsonable(self)


def new_plan_task() -> PlanTask:
    """Generates an instance of PlanTask with default values."""
    return PlanTask()


def plan_task_from_obj(obj: Any, path: str = "") -> PlanTask:
    """
    Generates an instance of PlanTask from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of PlanTask
    :param path: path to the object used for debugging
    :return: parsed instance of PlanTask
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_assignees = obj.get('assignees', None)
    if obj_assignees is not None:
        assignees_from_obj = from_obj(
            obj_assignees,
            expected=[list, str],
            path=path + '.assignees')  # type: Optional[List[str]]
    else:
        assignees_from_obj = None

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_color = obj.get('color', None)
    if obj_color is not None:
        color_from_obj = from_obj(
            obj_color,
            expected=[int],
            path=path + '.color')  # type: Optional[int]
    else:
        color_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_date_end = obj.get('dateEnd', None)
    if obj_date_end is not None:
        date_end_from_obj = from_obj(
            obj_date_end,
            expected=[str],
            path=path + '.dateEnd')  # type: Optional[str]
    else:
        date_end_from_obj = None

    obj_details = obj.get('details', None)
    if obj_details is not None:
        details_from_obj = from_obj(
            obj_details,
            expected=[str],
            path=path + '.details')  # type: Optional[str]
    else:
        details_from_obj = None

    obj_done = obj.get('done', None)
    if obj_done is not None:
        done_from_obj = from_obj(
            obj_done,
            expected=[bool],
            path=path + '.done')  # type: Optional[bool]
    else:
        done_from_obj = None

    obj_due_date = obj.get('dueDate', None)
    if obj_due_date is not None:
        due_date_from_obj = from_obj(
            obj_due_date,
            expected=[str],
            path=path + '.dueDate')  # type: Optional[str]
    else:
        due_date_from_obj = None

    obj_duration = obj.get('duration', None)
    if obj_duration is not None:
        duration_from_obj = from_obj(
            obj_duration,
            expected=[int],
            path=path + '.duration')  # type: Optional[int]
    else:
        duration_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_inventory_item_id = obj.get('inventoryItemID', None)
    if obj_inventory_item_id is not None:
        inventory_item_id_from_obj = from_obj(
            obj_inventory_item_id,
            expected=[str],
            path=path + '.inventoryItemID')  # type: Optional[str]
    else:
        inventory_item_id_from_obj = None

    obj_last_done_by = obj.get('lastDoneBy', None)
    if obj_last_done_by is not None:
        last_done_by_from_obj = from_obj(
            obj_last_done_by,
            expected=[str],
            path=path + '.lastDoneBy')  # type: Optional[str]
    else:
        last_done_by_from_obj = None

    obj_last_done_date = obj.get('lastDoneDate', None)
    if obj_last_done_date is not None:
        last_done_date_from_obj = from_obj(
            obj_last_done_date,
            expected=[CivilDate],
            path=path + '.lastDoneDate')  # type: Optional['CivilDate']
    else:
        last_done_date_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_notify = obj.get('notify', None)
    if obj_notify is not None:
        notify_from_obj = from_obj(
            obj_notify,
            expected=[bool],
            path=path + '.notify')  # type: Optional[bool]
    else:
        notify_from_obj = None

    obj_parent_id = obj.get('parentID', None)
    if obj_parent_id is not None:
        parent_id_from_obj = from_obj(
            obj_parent_id,
            expected=[str],
            path=path + '.parentID')  # type: Optional[str]
    else:
        parent_id_from_obj = None

    obj_plan_project_id = obj.get('planProjectID', None)
    if obj_plan_project_id is not None:
        plan_project_id_from_obj = from_obj(
            obj_plan_project_id,
            expected=[str],
            path=path + '.planProjectID')  # type: Optional[str]
    else:
        plan_project_id_from_obj = None

    obj_position = obj.get('position', None)
    if obj_position is not None:
        position_from_obj = from_obj(
            obj_position,
            expected=[str],
            path=path + '.position')  # type: Optional[str]
    else:
        position_from_obj = None

    obj_recur_on_done = obj.get('recurOnDone', None)
    if obj_recur_on_done is not None:
        recur_on_done_from_obj = from_obj(
            obj_recur_on_done,
            expected=[bool],
            path=path + '.recurOnDone')  # type: Optional[bool]
    else:
        recur_on_done_from_obj = None

    obj_recurrence = obj.get('recurrence', None)
    if obj_recurrence is not None:
        recurrence_from_obj = from_obj(
            obj_recurrence,
            expected=[Recurrence],
            path=path + '.recurrence')  # type: Optional['Recurrence']
    else:
        recurrence_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_tags = obj.get('tags', None)
    if obj_tags is not None:
        tags_from_obj = from_obj(
            obj_tags,
            expected=[list, str],
            path=path + '.tags')  # type: Optional[List[str]]
    else:
        tags_from_obj = None

    obj_template = obj.get('template', None)
    if obj_template is not None:
        template_from_obj = from_obj(
            obj_template,
            expected=[bool],
            path=path + '.template')  # type: Optional[bool]
    else:
        template_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return PlanTask(
        assignees=assignees_from_obj,
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        color=color_from_obj,
        created=created_from_obj,
        date_end=date_end_from_obj,
        details=details_from_obj,
        done=done_from_obj,
        due_date=due_date_from_obj,
        duration=duration_from_obj,
        id=id_from_obj,
        inventory_item_id=inventory_item_id_from_obj,
        last_done_by=last_done_by_from_obj,
        last_done_date=last_done_date_from_obj,
        name=name_from_obj,
        notify=notify_from_obj,
        parent_id=parent_id_from_obj,
        plan_project_id=plan_project_id_from_obj,
        position=position_from_obj,
        recur_on_done=recur_on_done_from_obj,
        recurrence=recurrence_from_obj,
        short_id=short_id_from_obj,
        tags=tags_from_obj,
        template=template_from_obj,
        updated=updated_from_obj)


def plan_task_to_jsonable(
        plan_task: PlanTask,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of PlanTask.

    :param plan_task: instance of PlanTask to be JSON-ized
    :param path: path to the plan_task used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if plan_task.assignees is not None:
        res['assignees'] = to_jsonable(
        plan_task.assignees,
        expected=[list, str],
        path='{}.assignees'.format(path))

    if plan_task.auth_account_id is not None:
        res['authAccountID'] = plan_task.auth_account_id

    if plan_task.auth_household_id is not None:
        res['authHouseholdID'] = plan_task.auth_household_id

    if plan_task.color is not None:
        res['color'] = plan_task.color

    if plan_task.created is not None:
        res['created'] = plan_task.created

    if plan_task.date_end is not None:
        res['dateEnd'] = plan_task.date_end

    if plan_task.details is not None:
        res['details'] = plan_task.details

    if plan_task.done is not None:
        res['done'] = plan_task.done

    if plan_task.due_date is not None:
        res['dueDate'] = plan_task.due_date

    if plan_task.duration is not None:
        res['duration'] = plan_task.duration

    if plan_task.id is not None:
        res['id'] = plan_task.id

    if plan_task.inventory_item_id is not None:
        res['inventoryItemID'] = plan_task.inventory_item_id

    if plan_task.last_done_by is not None:
        res['lastDoneBy'] = plan_task.last_done_by

    if plan_task.last_done_date is not None:
        res['lastDoneDate'] = to_jsonable(
        plan_task.last_done_date,
        expected=[CivilDate],
        path='{}.lastDoneDate'.format(path))

    if plan_task.name is not None:
        res['name'] = plan_task.name

    if plan_task.notify is not None:
        res['notify'] = plan_task.notify

    if plan_task.parent_id is not None:
        res['parentID'] = plan_task.parent_id

    if plan_task.plan_project_id is not None:
        res['planProjectID'] = plan_task.plan_project_id

    if plan_task.position is not None:
        res['position'] = plan_task.position

    if plan_task.recur_on_done is not None:
        res['recurOnDone'] = plan_task.recur_on_done

    if plan_task.recurrence is not None:
        res['recurrence'] = to_jsonable(
        plan_task.recurrence,
        expected=[Recurrence],
        path='{}.recurrence'.format(path))

    if plan_task.short_id is not None:
        res['shortID'] = plan_task.short_id

    if plan_task.tags is not None:
        res['tags'] = to_jsonable(
        plan_task.tags,
        expected=[list, str],
        path='{}.tags'.format(path))

    if plan_task.template is not None:
        res['template'] = plan_task.template

    if plan_task.updated is not None:
        res['updated'] = plan_task.updated

    return res


class Recurrence:
    def __init__(
            self,
            day: Optional[int] = None,
            month: Optional[int] = None,
            month_week: Optional[int] = None,
            separation: Optional[int] = None,
            weekday: Optional[int] = None,
            weekdays: Optional[List[int]] = None) -> None:
        """Initializes with the given values."""
        self.day = day

        self.month = month

        self.month_week = month_week

        self.separation = separation

        self.weekday = weekday

        self.weekdays = weekdays

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to recurrence_to_jsonable.

        :return: JSON-able representation
        """
        return recurrence_to_jsonable(self)


def new_recurrence() -> Recurrence:
    """Generates an instance of Recurrence with default values."""
    return Recurrence()


def recurrence_from_obj(obj: Any, path: str = "") -> Recurrence:
    """
    Generates an instance of Recurrence from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Recurrence
    :param path: path to the object used for debugging
    :return: parsed instance of Recurrence
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_day = obj.get('day', None)
    if obj_day is not None:
        day_from_obj = from_obj(
            obj_day,
            expected=[int],
            path=path + '.day')  # type: Optional[int]
    else:
        day_from_obj = None

    obj_month = obj.get('month', None)
    if obj_month is not None:
        month_from_obj = from_obj(
            obj_month,
            expected=[int],
            path=path + '.month')  # type: Optional[int]
    else:
        month_from_obj = None

    obj_month_week = obj.get('monthWeek', None)
    if obj_month_week is not None:
        month_week_from_obj = from_obj(
            obj_month_week,
            expected=[int],
            path=path + '.monthWeek')  # type: Optional[int]
    else:
        month_week_from_obj = None

    obj_separation = obj.get('separation', None)
    if obj_separation is not None:
        separation_from_obj = from_obj(
            obj_separation,
            expected=[int],
            path=path + '.separation')  # type: Optional[int]
    else:
        separation_from_obj = None

    obj_weekday = obj.get('weekday', None)
    if obj_weekday is not None:
        weekday_from_obj = from_obj(
            obj_weekday,
            expected=[int],
            path=path + '.weekday')  # type: Optional[int]
    else:
        weekday_from_obj = None

    obj_weekdays = obj.get('weekdays', None)
    if obj_weekdays is not None:
        weekdays_from_obj = from_obj(
            obj_weekdays,
            expected=[list, int],
            path=path + '.weekdays')  # type: Optional[List[int]]
    else:
        weekdays_from_obj = None

    return Recurrence(
        day=day_from_obj,
        month=month_from_obj,
        month_week=month_week_from_obj,
        separation=separation_from_obj,
        weekday=weekday_from_obj,
        weekdays=weekdays_from_obj)


def recurrence_to_jsonable(
        recurrence: Recurrence,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Recurrence.

    :param recurrence: instance of Recurrence to be JSON-ized
    :param path: path to the recurrence used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if recurrence.day is not None:
        res['day'] = recurrence.day

    if recurrence.month is not None:
        res['month'] = recurrence.month

    if recurrence.month_week is not None:
        res['monthWeek'] = recurrence.month_week

    if recurrence.separation is not None:
        res['separation'] = recurrence.separation

    if recurrence.weekday is not None:
        res['weekday'] = recurrence.weekday

    if recurrence.weekdays is not None:
        res['weekdays'] = to_jsonable(
        recurrence.weekdays,
        expected=[list, int],
        path='{}.weekdays'.format(path))

    return res


class Response:
    def __init__(
            self,
            data_hash: Optional[str] = None,
            data_ids: Optional[List['ID']] = None,
            data_total: Optional[int] = None,
            data_type: Optional[str] = None,
            data_value: Optional[List[Any]] = None,
            message: Optional[str] = None,
            request_id: Optional[str] = None,
            status: Optional[int] = None,
            success: Optional[bool] = None) -> None:
        """Initializes with the given values."""
        self.data_hash = data_hash

        self.data_ids = data_ids

        self.data_total = data_total

        self.data_type = data_type

        self.data_value = data_value

        self.message = message

        self.request_id = request_id

        self.status = status

        self.success = success

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to response_to_jsonable.

        :return: JSON-able representation
        """
        return response_to_jsonable(self)


def new_response() -> Response:
    """Generates an instance of Response with default values."""
    return Response()


def response_from_obj(obj: Any, path: str = "") -> Response:
    """
    Generates an instance of Response from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Response
    :param path: path to the object used for debugging
    :return: parsed instance of Response
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_data_hash = obj.get('dataHash', None)
    if obj_data_hash is not None:
        data_hash_from_obj = from_obj(
            obj_data_hash,
            expected=[str],
            path=path + '.dataHash')  # type: Optional[str]
    else:
        data_hash_from_obj = None

    obj_data_ids = obj.get('dataIDs', None)
    if obj_data_ids is not None:
        data_ids_from_obj = from_obj(
            obj_data_ids,
            expected=[list, ID],
            path=path + '.dataIDs')  # type: Optional[List['ID']]
    else:
        data_ids_from_obj = None

    obj_data_total = obj.get('dataTotal', None)
    if obj_data_total is not None:
        data_total_from_obj = from_obj(
            obj_data_total,
            expected=[int],
            path=path + '.dataTotal')  # type: Optional[int]
    else:
        data_total_from_obj = None

    obj_data_type = obj.get('dataType', None)
    if obj_data_type is not None:
        data_type_from_obj = from_obj(
            obj_data_type,
            expected=[str],
            path=path + '.dataType')  # type: Optional[str]
    else:
        data_type_from_obj = None

    obj_data_value = obj.get('dataValue', None)
    if obj_data_value is not None:
        data_value_from_obj = from_obj(
            obj_data_value,
            expected=[list, Any],
            path=path + '.dataValue')  # type: Optional[List[Any]]
    else:
        data_value_from_obj = None

    obj_message = obj.get('message', None)
    if obj_message is not None:
        message_from_obj = from_obj(
            obj_message,
            expected=[str],
            path=path + '.message')  # type: Optional[str]
    else:
        message_from_obj = None

    obj_request_id = obj.get('requestID', None)
    if obj_request_id is not None:
        request_id_from_obj = from_obj(
            obj_request_id,
            expected=[str],
            path=path + '.requestID')  # type: Optional[str]
    else:
        request_id_from_obj = None

    obj_status = obj.get('status', None)
    if obj_status is not None:
        status_from_obj = from_obj(
            obj_status,
            expected=[int],
            path=path + '.status')  # type: Optional[int]
    else:
        status_from_obj = None

    obj_success = obj.get('success', None)
    if obj_success is not None:
        success_from_obj = from_obj(
            obj_success,
            expected=[bool],
            path=path + '.success')  # type: Optional[bool]
    else:
        success_from_obj = None

    return Response(
        data_hash=data_hash_from_obj,
        data_ids=data_ids_from_obj,
        data_total=data_total_from_obj,
        data_type=data_type_from_obj,
        data_value=data_value_from_obj,
        message=message_from_obj,
        request_id=request_id_from_obj,
        status=status_from_obj,
        success=success_from_obj)


def response_to_jsonable(
        response: Response,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Response.

    :param response: instance of Response to be JSON-ized
    :param path: path to the response used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if response.data_hash is not None:
        res['dataHash'] = response.data_hash

    if response.data_ids is not None:
        res['dataIDs'] = to_jsonable(
        response.data_ids,
        expected=[list, ID],
        path='{}.dataIDs'.format(path))

    if response.data_total is not None:
        res['dataTotal'] = response.data_total

    if response.data_type is not None:
        res['dataType'] = response.data_type

    if response.data_value is not None:
        res['dataValue'] = to_jsonable(
        response.data_value,
        expected=[list, Any],
        path='{}.dataValue'.format(path))

    if response.message is not None:
        res['message'] = response.message

    if response.request_id is not None:
        res['requestID'] = response.request_id

    if response.status is not None:
        res['status'] = response.status

    if response.success is not None:
        res['success'] = response.success

    return res


class RewardCard:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            created: Optional[str] = None,
            details: Optional[str] = None,
            id: Optional[str] = None,
            invert: Optional[bool] = None,
            name: Optional[str] = None,
            recipients: Optional[List[str]] = None,
            reward: Optional[str] = None,
            senders: Optional[List[str]] = None,
            short_id: Optional[str] = None,
            stamp_count: Optional[int] = None,
            stamp_goal: Optional[int] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.created = created

        self.details = details

        self.id = id

        self.invert = invert

        self.name = name

        self.recipients = recipients

        self.reward = reward

        self.senders = senders

        self.short_id = short_id

        self.stamp_count = stamp_count

        self.stamp_goal = stamp_goal

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to reward_card_to_jsonable.

        :return: JSON-able representation
        """
        return reward_card_to_jsonable(self)


def new_reward_card() -> RewardCard:
    """Generates an instance of RewardCard with default values."""
    return RewardCard()


def reward_card_from_obj(obj: Any, path: str = "") -> RewardCard:
    """
    Generates an instance of RewardCard from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of RewardCard
    :param path: path to the object used for debugging
    :return: parsed instance of RewardCard
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_details = obj.get('details', None)
    if obj_details is not None:
        details_from_obj = from_obj(
            obj_details,
            expected=[str],
            path=path + '.details')  # type: Optional[str]
    else:
        details_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_invert = obj.get('invert', None)
    if obj_invert is not None:
        invert_from_obj = from_obj(
            obj_invert,
            expected=[bool],
            path=path + '.invert')  # type: Optional[bool]
    else:
        invert_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_recipients = obj.get('recipients', None)
    if obj_recipients is not None:
        recipients_from_obj = from_obj(
            obj_recipients,
            expected=[list, str],
            path=path + '.recipients')  # type: Optional[List[str]]
    else:
        recipients_from_obj = None

    obj_reward = obj.get('reward', None)
    if obj_reward is not None:
        reward_from_obj = from_obj(
            obj_reward,
            expected=[str],
            path=path + '.reward')  # type: Optional[str]
    else:
        reward_from_obj = None

    obj_senders = obj.get('senders', None)
    if obj_senders is not None:
        senders_from_obj = from_obj(
            obj_senders,
            expected=[list, str],
            path=path + '.senders')  # type: Optional[List[str]]
    else:
        senders_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_stamp_count = obj.get('stampCount', None)
    if obj_stamp_count is not None:
        stamp_count_from_obj = from_obj(
            obj_stamp_count,
            expected=[int],
            path=path + '.stampCount')  # type: Optional[int]
    else:
        stamp_count_from_obj = None

    obj_stamp_goal = obj.get('stampGoal', None)
    if obj_stamp_goal is not None:
        stamp_goal_from_obj = from_obj(
            obj_stamp_goal,
            expected=[int],
            path=path + '.stampGoal')  # type: Optional[int]
    else:
        stamp_goal_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return RewardCard(
        auth_household_id=auth_household_id_from_obj,
        created=created_from_obj,
        details=details_from_obj,
        id=id_from_obj,
        invert=invert_from_obj,
        name=name_from_obj,
        recipients=recipients_from_obj,
        reward=reward_from_obj,
        senders=senders_from_obj,
        short_id=short_id_from_obj,
        stamp_count=stamp_count_from_obj,
        stamp_goal=stamp_goal_from_obj,
        updated=updated_from_obj)


def reward_card_to_jsonable(
        reward_card: RewardCard,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of RewardCard.

    :param reward_card: instance of RewardCard to be JSON-ized
    :param path: path to the reward_card used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if reward_card.auth_household_id is not None:
        res['authHouseholdID'] = reward_card.auth_household_id

    if reward_card.created is not None:
        res['created'] = reward_card.created

    if reward_card.details is not None:
        res['details'] = reward_card.details

    if reward_card.id is not None:
        res['id'] = reward_card.id

    if reward_card.invert is not None:
        res['invert'] = reward_card.invert

    if reward_card.name is not None:
        res['name'] = reward_card.name

    if reward_card.recipients is not None:
        res['recipients'] = to_jsonable(
        reward_card.recipients,
        expected=[list, str],
        path='{}.recipients'.format(path))

    if reward_card.reward is not None:
        res['reward'] = reward_card.reward

    if reward_card.senders is not None:
        res['senders'] = to_jsonable(
        reward_card.senders,
        expected=[list, str],
        path='{}.senders'.format(path))

    if reward_card.short_id is not None:
        res['shortID'] = reward_card.short_id

    if reward_card.stamp_count is not None:
        res['stampCount'] = reward_card.stamp_count

    if reward_card.stamp_goal is not None:
        res['stampGoal'] = reward_card.stamp_goal

    if reward_card.updated is not None:
        res['updated'] = reward_card.updated

    return res


class SecretsValue:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            data_encrypted: Optional[List['EncryptionEncryptedValue']] = None,
            deleted: Optional[str] = None,
            id: Optional[str] = None,
            name_encrypted: Optional['EncryptionEncryptedValue'] = None,
            secrets_vault_id: Optional[str] = None,
            short_id: Optional[str] = None,
            tags_encrypted: Optional['EncryptionEncryptedValue'] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.data_encrypted = data_encrypted

        self.deleted = deleted

        self.id = id

        self.name_encrypted = name_encrypted

        self.secrets_vault_id = secrets_vault_id

        self.short_id = short_id

        self.tags_encrypted = tags_encrypted

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to secrets_value_to_jsonable.

        :return: JSON-able representation
        """
        return secrets_value_to_jsonable(self)


def new_secrets_value() -> SecretsValue:
    """Generates an instance of SecretsValue with default values."""
    return SecretsValue()


def secrets_value_from_obj(obj: Any, path: str = "") -> SecretsValue:
    """
    Generates an instance of SecretsValue from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of SecretsValue
    :param path: path to the object used for debugging
    :return: parsed instance of SecretsValue
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_data_encrypted = obj.get('dataEncrypted', None)
    if obj_data_encrypted is not None:
        data_encrypted_from_obj = from_obj(
            obj_data_encrypted,
            expected=[list, EncryptionEncryptedValue],
            path=path + '.dataEncrypted')  # type: Optional[List['EncryptionEncryptedValue']]
    else:
        data_encrypted_from_obj = None

    obj_deleted = obj.get('deleted', None)
    if obj_deleted is not None:
        deleted_from_obj = from_obj(
            obj_deleted,
            expected=[str],
            path=path + '.deleted')  # type: Optional[str]
    else:
        deleted_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name_encrypted = obj.get('nameEncrypted', None)
    if obj_name_encrypted is not None:
        name_encrypted_from_obj = from_obj(
            obj_name_encrypted,
            expected=[EncryptionEncryptedValue],
            path=path + '.nameEncrypted')  # type: Optional['EncryptionEncryptedValue']
    else:
        name_encrypted_from_obj = None

    obj_secrets_vault_id = obj.get('secretsVaultID', None)
    if obj_secrets_vault_id is not None:
        secrets_vault_id_from_obj = from_obj(
            obj_secrets_vault_id,
            expected=[str],
            path=path + '.secretsVaultID')  # type: Optional[str]
    else:
        secrets_vault_id_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_tags_encrypted = obj.get('tagsEncrypted', None)
    if obj_tags_encrypted is not None:
        tags_encrypted_from_obj = from_obj(
            obj_tags_encrypted,
            expected=[EncryptionEncryptedValue],
            path=path + '.tagsEncrypted')  # type: Optional['EncryptionEncryptedValue']
    else:
        tags_encrypted_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return SecretsValue(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        data_encrypted=data_encrypted_from_obj,
        deleted=deleted_from_obj,
        id=id_from_obj,
        name_encrypted=name_encrypted_from_obj,
        secrets_vault_id=secrets_vault_id_from_obj,
        short_id=short_id_from_obj,
        tags_encrypted=tags_encrypted_from_obj,
        updated=updated_from_obj)


def secrets_value_to_jsonable(
        secrets_value: SecretsValue,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of SecretsValue.

    :param secrets_value: instance of SecretsValue to be JSON-ized
    :param path: path to the secrets_value used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if secrets_value.auth_account_id is not None:
        res['authAccountID'] = secrets_value.auth_account_id

    if secrets_value.auth_household_id is not None:
        res['authHouseholdID'] = secrets_value.auth_household_id

    if secrets_value.data_encrypted is not None:
        res['dataEncrypted'] = to_jsonable(
        secrets_value.data_encrypted,
        expected=[list, EncryptionEncryptedValue],
        path='{}.dataEncrypted'.format(path))

    if secrets_value.deleted is not None:
        res['deleted'] = secrets_value.deleted

    if secrets_value.id is not None:
        res['id'] = secrets_value.id

    if secrets_value.name_encrypted is not None:
        res['nameEncrypted'] = to_jsonable(
        secrets_value.name_encrypted,
        expected=[EncryptionEncryptedValue],
        path='{}.nameEncrypted'.format(path))

    if secrets_value.secrets_vault_id is not None:
        res['secretsVaultID'] = secrets_value.secrets_vault_id

    if secrets_value.short_id is not None:
        res['shortID'] = secrets_value.short_id

    if secrets_value.tags_encrypted is not None:
        res['tagsEncrypted'] = to_jsonable(
        secrets_value.tags_encrypted,
        expected=[EncryptionEncryptedValue],
        path='{}.tagsEncrypted'.format(path))

    if secrets_value.updated is not None:
        res['updated'] = secrets_value.updated

    return res


class SecretsVault:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            created: Optional[str] = None,
            icon: Optional[str] = None,
            id: Optional[str] = None,
            keys: Optional[List['SecretsVaultKey']] = None,
            name: Optional[str] = None,
            short_id: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.created = created

        self.icon = icon

        self.id = id

        self.keys = keys

        self.name = name

        self.short_id = short_id

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to secrets_vault_to_jsonable.

        :return: JSON-able representation
        """
        return secrets_vault_to_jsonable(self)


def new_secrets_vault() -> SecretsVault:
    """Generates an instance of SecretsVault with default values."""
    return SecretsVault()


def secrets_vault_from_obj(obj: Any, path: str = "") -> SecretsVault:
    """
    Generates an instance of SecretsVault from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of SecretsVault
    :param path: path to the object used for debugging
    :return: parsed instance of SecretsVault
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_icon = obj.get('icon', None)
    if obj_icon is not None:
        icon_from_obj = from_obj(
            obj_icon,
            expected=[str],
            path=path + '.icon')  # type: Optional[str]
    else:
        icon_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_keys = obj.get('keys', None)
    if obj_keys is not None:
        keys_from_obj = from_obj(
            obj_keys,
            expected=[list, SecretsVaultKey],
            path=path + '.keys')  # type: Optional[List['SecretsVaultKey']]
    else:
        keys_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return SecretsVault(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        created=created_from_obj,
        icon=icon_from_obj,
        id=id_from_obj,
        keys=keys_from_obj,
        name=name_from_obj,
        short_id=short_id_from_obj,
        updated=updated_from_obj)


def secrets_vault_to_jsonable(
        secrets_vault: SecretsVault,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of SecretsVault.

    :param secrets_vault: instance of SecretsVault to be JSON-ized
    :param path: path to the secrets_vault used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if secrets_vault.auth_account_id is not None:
        res['authAccountID'] = secrets_vault.auth_account_id

    if secrets_vault.auth_household_id is not None:
        res['authHouseholdID'] = secrets_vault.auth_household_id

    if secrets_vault.created is not None:
        res['created'] = secrets_vault.created

    if secrets_vault.icon is not None:
        res['icon'] = secrets_vault.icon

    if secrets_vault.id is not None:
        res['id'] = secrets_vault.id

    if secrets_vault.keys is not None:
        res['keys'] = to_jsonable(
        secrets_vault.keys,
        expected=[list, SecretsVaultKey],
        path='{}.keys'.format(path))

    if secrets_vault.name is not None:
        res['name'] = secrets_vault.name

    if secrets_vault.short_id is not None:
        res['shortID'] = secrets_vault.short_id

    if secrets_vault.updated is not None:
        res['updated'] = secrets_vault.updated

    return res


class SecretsVaultKey:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            key: Optional['EncryptionEncryptedValue'] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.key = key

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to secrets_vault_key_to_jsonable.

        :return: JSON-able representation
        """
        return secrets_vault_key_to_jsonable(self)


def new_secrets_vault_key() -> SecretsVaultKey:
    """Generates an instance of SecretsVaultKey with default values."""
    return SecretsVaultKey()


def secrets_vault_key_from_obj(obj: Any, path: str = "") -> SecretsVaultKey:
    """
    Generates an instance of SecretsVaultKey from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of SecretsVaultKey
    :param path: path to the object used for debugging
    :return: parsed instance of SecretsVaultKey
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_key = obj.get('key', None)
    if obj_key is not None:
        key_from_obj = from_obj(
            obj_key,
            expected=[EncryptionEncryptedValue],
            path=path + '.key')  # type: Optional['EncryptionEncryptedValue']
    else:
        key_from_obj = None

    return SecretsVaultKey(
        auth_account_id=auth_account_id_from_obj,
        key=key_from_obj)


def secrets_vault_key_to_jsonable(
        secrets_vault_key: SecretsVaultKey,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of SecretsVaultKey.

    :param secrets_vault_key: instance of SecretsVaultKey to be JSON-ized
    :param path: path to the secrets_vault_key used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if secrets_vault_key.auth_account_id is not None:
        res['authAccountID'] = secrets_vault_key.auth_account_id

    if secrets_vault_key.key is not None:
        res['key'] = to_jsonable(
        secrets_vault_key.key,
        expected=[EncryptionEncryptedValue],
        path='{}.key'.format(path))

    return res


class ShopCategory:
    def __init__(
            self,
            auth_household_id: Optional[str] = None,
            budget_payee_id: Optional[str] = None,
            created: Optional[str] = None,
            id: Optional[str] = None,
            match: Optional[str] = None,
            name: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_household_id = auth_household_id

        self.budget_payee_id = budget_payee_id

        self.created = created

        self.id = id

        self.match = match

        self.name = name

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to shop_category_to_jsonable.

        :return: JSON-able representation
        """
        return shop_category_to_jsonable(self)


def new_shop_category() -> ShopCategory:
    """Generates an instance of ShopCategory with default values."""
    return ShopCategory()


def shop_category_from_obj(obj: Any, path: str = "") -> ShopCategory:
    """
    Generates an instance of ShopCategory from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ShopCategory
    :param path: path to the object used for debugging
    :return: parsed instance of ShopCategory
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_payee_id = obj.get('budgetPayeeID', None)
    if obj_budget_payee_id is not None:
        budget_payee_id_from_obj = from_obj(
            obj_budget_payee_id,
            expected=[str],
            path=path + '.budgetPayeeID')  # type: Optional[str]
    else:
        budget_payee_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_match = obj.get('match', None)
    if obj_match is not None:
        match_from_obj = from_obj(
            obj_match,
            expected=[str],
            path=path + '.match')  # type: Optional[str]
    else:
        match_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return ShopCategory(
        auth_household_id=auth_household_id_from_obj,
        budget_payee_id=budget_payee_id_from_obj,
        created=created_from_obj,
        id=id_from_obj,
        match=match_from_obj,
        name=name_from_obj,
        updated=updated_from_obj)


def shop_category_to_jsonable(
        shop_category: ShopCategory,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ShopCategory.

    :param shop_category: instance of ShopCategory to be JSON-ized
    :param path: path to the shop_category used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if shop_category.auth_household_id is not None:
        res['authHouseholdID'] = shop_category.auth_household_id

    if shop_category.budget_payee_id is not None:
        res['budgetPayeeID'] = shop_category.budget_payee_id

    if shop_category.created is not None:
        res['created'] = shop_category.created

    if shop_category.id is not None:
        res['id'] = shop_category.id

    if shop_category.match is not None:
        res['match'] = shop_category.match

    if shop_category.name is not None:
        res['name'] = shop_category.name

    if shop_category.updated is not None:
        res['updated'] = shop_category.updated

    return res


class ShopItem:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            budget_category_id: Optional[str] = None,
            budget_payee_id: Optional[str] = None,
            cook_meal_plan_id: Optional[str] = None,
            cook_recipe_id: Optional[str] = None,
            created: Optional[str] = None,
            id: Optional[str] = None,
            in_cart: Optional[bool] = None,
            name: Optional[str] = None,
            next_date: Optional[str] = None,
            plan_project_id: Optional[str] = None,
            position: Optional[str] = None,
            price: Optional[int] = None,
            recurrence: Optional['Recurrence'] = None,
            shop_category_id: Optional[str] = None,
            shop_list_id: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.budget_category_id = budget_category_id

        self.budget_payee_id = budget_payee_id

        self.cook_meal_plan_id = cook_meal_plan_id

        self.cook_recipe_id = cook_recipe_id

        self.created = created

        self.id = id

        self.in_cart = in_cart

        self.name = name

        self.next_date = next_date

        self.plan_project_id = plan_project_id

        self.position = position

        self.price = price

        self.recurrence = recurrence

        self.shop_category_id = shop_category_id

        self.shop_list_id = shop_list_id

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to shop_item_to_jsonable.

        :return: JSON-able representation
        """
        return shop_item_to_jsonable(self)


def new_shop_item() -> ShopItem:
    """Generates an instance of ShopItem with default values."""
    return ShopItem()


def shop_item_from_obj(obj: Any, path: str = "") -> ShopItem:
    """
    Generates an instance of ShopItem from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ShopItem
    :param path: path to the object used for debugging
    :return: parsed instance of ShopItem
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_category_id = obj.get('budgetCategoryID', None)
    if obj_budget_category_id is not None:
        budget_category_id_from_obj = from_obj(
            obj_budget_category_id,
            expected=[str],
            path=path + '.budgetCategoryID')  # type: Optional[str]
    else:
        budget_category_id_from_obj = None

    obj_budget_payee_id = obj.get('budgetPayeeID', None)
    if obj_budget_payee_id is not None:
        budget_payee_id_from_obj = from_obj(
            obj_budget_payee_id,
            expected=[str],
            path=path + '.budgetPayeeID')  # type: Optional[str]
    else:
        budget_payee_id_from_obj = None

    obj_cook_meal_plan_id = obj.get('cookMealPlanID', None)
    if obj_cook_meal_plan_id is not None:
        cook_meal_plan_id_from_obj = from_obj(
            obj_cook_meal_plan_id,
            expected=[str],
            path=path + '.cookMealPlanID')  # type: Optional[str]
    else:
        cook_meal_plan_id_from_obj = None

    obj_cook_recipe_id = obj.get('cookRecipeID', None)
    if obj_cook_recipe_id is not None:
        cook_recipe_id_from_obj = from_obj(
            obj_cook_recipe_id,
            expected=[str],
            path=path + '.cookRecipeID')  # type: Optional[str]
    else:
        cook_recipe_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_in_cart = obj.get('inCart', None)
    if obj_in_cart is not None:
        in_cart_from_obj = from_obj(
            obj_in_cart,
            expected=[bool],
            path=path + '.inCart')  # type: Optional[bool]
    else:
        in_cart_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_next_date = obj.get('nextDate', None)
    if obj_next_date is not None:
        next_date_from_obj = from_obj(
            obj_next_date,
            expected=[str],
            path=path + '.nextDate')  # type: Optional[str]
    else:
        next_date_from_obj = None

    obj_plan_project_id = obj.get('planProjectID', None)
    if obj_plan_project_id is not None:
        plan_project_id_from_obj = from_obj(
            obj_plan_project_id,
            expected=[str],
            path=path + '.planProjectID')  # type: Optional[str]
    else:
        plan_project_id_from_obj = None

    obj_position = obj.get('position', None)
    if obj_position is not None:
        position_from_obj = from_obj(
            obj_position,
            expected=[str],
            path=path + '.position')  # type: Optional[str]
    else:
        position_from_obj = None

    obj_price = obj.get('price', None)
    if obj_price is not None:
        price_from_obj = from_obj(
            obj_price,
            expected=[int],
            path=path + '.price')  # type: Optional[int]
    else:
        price_from_obj = None

    obj_recurrence = obj.get('recurrence', None)
    if obj_recurrence is not None:
        recurrence_from_obj = from_obj(
            obj_recurrence,
            expected=[Recurrence],
            path=path + '.recurrence')  # type: Optional['Recurrence']
    else:
        recurrence_from_obj = None

    obj_shop_category_id = obj.get('shopCategoryID', None)
    if obj_shop_category_id is not None:
        shop_category_id_from_obj = from_obj(
            obj_shop_category_id,
            expected=[str],
            path=path + '.shopCategoryID')  # type: Optional[str]
    else:
        shop_category_id_from_obj = None

    obj_shop_list_id = obj.get('shopListID', None)
    if obj_shop_list_id is not None:
        shop_list_id_from_obj = from_obj(
            obj_shop_list_id,
            expected=[str],
            path=path + '.shopListID')  # type: Optional[str]
    else:
        shop_list_id_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return ShopItem(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        budget_category_id=budget_category_id_from_obj,
        budget_payee_id=budget_payee_id_from_obj,
        cook_meal_plan_id=cook_meal_plan_id_from_obj,
        cook_recipe_id=cook_recipe_id_from_obj,
        created=created_from_obj,
        id=id_from_obj,
        in_cart=in_cart_from_obj,
        name=name_from_obj,
        next_date=next_date_from_obj,
        plan_project_id=plan_project_id_from_obj,
        position=position_from_obj,
        price=price_from_obj,
        recurrence=recurrence_from_obj,
        shop_category_id=shop_category_id_from_obj,
        shop_list_id=shop_list_id_from_obj,
        updated=updated_from_obj)


def shop_item_to_jsonable(
        shop_item: ShopItem,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ShopItem.

    :param shop_item: instance of ShopItem to be JSON-ized
    :param path: path to the shop_item used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if shop_item.auth_account_id is not None:
        res['authAccountID'] = shop_item.auth_account_id

    if shop_item.auth_household_id is not None:
        res['authHouseholdID'] = shop_item.auth_household_id

    if shop_item.budget_category_id is not None:
        res['budgetCategoryID'] = shop_item.budget_category_id

    if shop_item.budget_payee_id is not None:
        res['budgetPayeeID'] = shop_item.budget_payee_id

    if shop_item.cook_meal_plan_id is not None:
        res['cookMealPlanID'] = shop_item.cook_meal_plan_id

    if shop_item.cook_recipe_id is not None:
        res['cookRecipeID'] = shop_item.cook_recipe_id

    if shop_item.created is not None:
        res['created'] = shop_item.created

    if shop_item.id is not None:
        res['id'] = shop_item.id

    if shop_item.in_cart is not None:
        res['inCart'] = shop_item.in_cart

    if shop_item.name is not None:
        res['name'] = shop_item.name

    if shop_item.next_date is not None:
        res['nextDate'] = shop_item.next_date

    if shop_item.plan_project_id is not None:
        res['planProjectID'] = shop_item.plan_project_id

    if shop_item.position is not None:
        res['position'] = shop_item.position

    if shop_item.price is not None:
        res['price'] = shop_item.price

    if shop_item.recurrence is not None:
        res['recurrence'] = to_jsonable(
        shop_item.recurrence,
        expected=[Recurrence],
        path='{}.recurrence'.format(path))

    if shop_item.shop_category_id is not None:
        res['shopCategoryID'] = shop_item.shop_category_id

    if shop_item.shop_list_id is not None:
        res['shopListID'] = shop_item.shop_list_id

    if shop_item.updated is not None:
        res['updated'] = shop_item.updated

    return res


class ShopList:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            budget_category_id: Optional[str] = None,
            created: Optional[str] = None,
            icon: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            shop_item_count: Optional[int] = None,
            short_id: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.budget_category_id = budget_category_id

        self.created = created

        self.icon = icon

        self.id = id

        self.name = name

        self.shop_item_count = shop_item_count

        self.short_id = short_id

        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to shop_list_to_jsonable.

        :return: JSON-able representation
        """
        return shop_list_to_jsonable(self)


def new_shop_list() -> ShopList:
    """Generates an instance of ShopList with default values."""
    return ShopList()


def shop_list_from_obj(obj: Any, path: str = "") -> ShopList:
    """
    Generates an instance of ShopList from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ShopList
    :param path: path to the object used for debugging
    :return: parsed instance of ShopList
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_budget_category_id = obj.get('budgetCategoryID', None)
    if obj_budget_category_id is not None:
        budget_category_id_from_obj = from_obj(
            obj_budget_category_id,
            expected=[str],
            path=path + '.budgetCategoryID')  # type: Optional[str]
    else:
        budget_category_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_icon = obj.get('icon', None)
    if obj_icon is not None:
        icon_from_obj = from_obj(
            obj_icon,
            expected=[str],
            path=path + '.icon')  # type: Optional[str]
    else:
        icon_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_shop_item_count = obj.get('shopItemCount', None)
    if obj_shop_item_count is not None:
        shop_item_count_from_obj = from_obj(
            obj_shop_item_count,
            expected=[int],
            path=path + '.shopItemCount')  # type: Optional[int]
    else:
        shop_item_count_from_obj = None

    obj_short_id = obj.get('shortID', None)
    if obj_short_id is not None:
        short_id_from_obj = from_obj(
            obj_short_id,
            expected=[str],
            path=path + '.shortID')  # type: Optional[str]
    else:
        short_id_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return ShopList(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        budget_category_id=budget_category_id_from_obj,
        created=created_from_obj,
        icon=icon_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        shop_item_count=shop_item_count_from_obj,
        short_id=short_id_from_obj,
        updated=updated_from_obj)


def shop_list_to_jsonable(
        shop_list: ShopList,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ShopList.

    :param shop_list: instance of ShopList to be JSON-ized
    :param path: path to the shop_list used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if shop_list.auth_account_id is not None:
        res['authAccountID'] = shop_list.auth_account_id

    if shop_list.auth_household_id is not None:
        res['authHouseholdID'] = shop_list.auth_household_id

    if shop_list.budget_category_id is not None:
        res['budgetCategoryID'] = shop_list.budget_category_id

    if shop_list.created is not None:
        res['created'] = shop_list.created

    if shop_list.icon is not None:
        res['icon'] = shop_list.icon

    if shop_list.id is not None:
        res['id'] = shop_list.id

    if shop_list.name is not None:
        res['name'] = shop_list.name

    if shop_list.shop_item_count is not None:
        res['shopItemCount'] = shop_list.shop_item_count

    if shop_list.short_id is not None:
        res['shortID'] = shop_list.short_id

    if shop_list.updated is not None:
        res['updated'] = shop_list.updated

    return res


class TableNotify:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            id: Optional[str] = None,
            operation: Optional[int] = None,
            table: Optional[str] = None,
            updated: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.id = id

        self.operation = operation

        self.table = table

        # Updated is the old timestamp when the operation is an update.
        self.updated = updated

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to table_notify_to_jsonable.

        :return: JSON-able representation
        """
        return table_notify_to_jsonable(self)


def new_table_notify() -> TableNotify:
    """Generates an instance of TableNotify with default values."""
    return TableNotify()


def table_notify_from_obj(obj: Any, path: str = "") -> TableNotify:
    """
    Generates an instance of TableNotify from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of TableNotify
    :param path: path to the object used for debugging
    :return: parsed instance of TableNotify
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_operation = obj.get('operation', None)
    if obj_operation is not None:
        operation_from_obj = from_obj(
            obj_operation,
            expected=[int],
            path=path + '.operation')  # type: Optional[int]
    else:
        operation_from_obj = None

    obj_table = obj.get('table', None)
    if obj_table is not None:
        table_from_obj = from_obj(
            obj_table,
            expected=[str],
            path=path + '.table')  # type: Optional[str]
    else:
        table_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    return TableNotify(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        id=id_from_obj,
        operation=operation_from_obj,
        table=table_from_obj,
        updated=updated_from_obj)


def table_notify_to_jsonable(
        table_notify: TableNotify,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of TableNotify.

    :param table_notify: instance of TableNotify to be JSON-ized
    :param path: path to the table_notify used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if table_notify.auth_account_id is not None:
        res['authAccountID'] = table_notify.auth_account_id

    if table_notify.auth_household_id is not None:
        res['authHouseholdID'] = table_notify.auth_household_id

    if table_notify.id is not None:
        res['id'] = table_notify.id

    if table_notify.operation is not None:
        res['operation'] = table_notify.operation

    if table_notify.table is not None:
        res['table'] = table_notify.table

    if table_notify.updated is not None:
        res['updated'] = table_notify.updated

    return res


class EncryptionEncryptedValue:
    def __init__(
            self,
            ciphertext: Optional[str] = None,
            encryption: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.ciphertext = ciphertext

        self.encryption = encryption

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to encryption_encrypted_value_to_jsonable.

        :return: JSON-able representation
        """
        return encryption_encrypted_value_to_jsonable(self)


def new_encryption_encrypted_value() -> EncryptionEncryptedValue:
    """Generates an instance of EncryptionEncryptedValue with default values."""
    return EncryptionEncryptedValue()


def encryption_encrypted_value_from_obj(obj: Any, path: str = "") -> EncryptionEncryptedValue:
    """
    Generates an instance of EncryptionEncryptedValue from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of EncryptionEncryptedValue
    :param path: path to the object used for debugging
    :return: parsed instance of EncryptionEncryptedValue
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_ciphertext = obj.get('ciphertext', None)
    if obj_ciphertext is not None:
        ciphertext_from_obj = from_obj(
            obj_ciphertext,
            expected=[str],
            path=path + '.ciphertext')  # type: Optional[str]
    else:
        ciphertext_from_obj = None

    obj_encryption = obj.get('encryption', None)
    if obj_encryption is not None:
        encryption_from_obj = from_obj(
            obj_encryption,
            expected=[str],
            path=path + '.encryption')  # type: Optional[str]
    else:
        encryption_from_obj = None

    return EncryptionEncryptedValue(
        ciphertext=ciphertext_from_obj,
        encryption=encryption_from_obj)


def encryption_encrypted_value_to_jsonable(
        encryption_encrypted_value: EncryptionEncryptedValue,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of EncryptionEncryptedValue.

    :param encryption_encrypted_value: instance of EncryptionEncryptedValue to be JSON-ized
    :param path: path to the encryption_encrypted_value used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if encryption_encrypted_value.ciphertext is not None:
        res['ciphertext'] = encryption_encrypted_value.ciphertext

    if encryption_encrypted_value.encryption is not None:
        res['encryption'] = encryption_encrypted_value.encryption

    return res


class ModelsCalendarICalendar:
    def __init__(
            self,
            auth_account_id: Optional[str] = None,
            auth_household_id: Optional[str] = None,
            created: Optional[str] = None,
            ics: Optional[str] = None,
            id: Optional[str] = None,
            name: Optional[str] = None,
            updated: Optional[str] = None,
            url: Optional[str] = None) -> None:
        """Initializes with the given values."""
        self.auth_account_id = auth_account_id

        self.auth_household_id = auth_household_id

        self.created = created

        self.ics = ics

        self.id = id

        # * If name is not specified, the ICS will be parsed, CalendarEvents created, but no CalendarICalendar will be created/associated with them.
        self.name = name

        self.updated = updated

        self.url = url

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to models_calendar_i_calendar_to_jsonable.

        :return: JSON-able representation
        """
        return models_calendar_i_calendar_to_jsonable(self)


def new_models_calendar_i_calendar() -> ModelsCalendarICalendar:
    """Generates an instance of ModelsCalendarICalendar with default values."""
    return ModelsCalendarICalendar()


def models_calendar_i_calendar_from_obj(obj: Any, path: str = "") -> ModelsCalendarICalendar:
    """
    Generates an instance of ModelsCalendarICalendar from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ModelsCalendarICalendar
    :param path: path to the object used for debugging
    :return: parsed instance of ModelsCalendarICalendar
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_auth_account_id = obj.get('authAccountID', None)
    if obj_auth_account_id is not None:
        auth_account_id_from_obj = from_obj(
            obj_auth_account_id,
            expected=[str],
            path=path + '.authAccountID')  # type: Optional[str]
    else:
        auth_account_id_from_obj = None

    obj_auth_household_id = obj.get('authHouseholdID', None)
    if obj_auth_household_id is not None:
        auth_household_id_from_obj = from_obj(
            obj_auth_household_id,
            expected=[str],
            path=path + '.authHouseholdID')  # type: Optional[str]
    else:
        auth_household_id_from_obj = None

    obj_created = obj.get('created', None)
    if obj_created is not None:
        created_from_obj = from_obj(
            obj_created,
            expected=[str],
            path=path + '.created')  # type: Optional[str]
    else:
        created_from_obj = None

    obj_ics = obj.get('ics', None)
    if obj_ics is not None:
        ics_from_obj = from_obj(
            obj_ics,
            expected=[str],
            path=path + '.ics')  # type: Optional[str]
    else:
        ics_from_obj = None

    obj_id = obj.get('id', None)
    if obj_id is not None:
        id_from_obj = from_obj(
            obj_id,
            expected=[str],
            path=path + '.id')  # type: Optional[str]
    else:
        id_from_obj = None

    obj_name = obj.get('name', None)
    if obj_name is not None:
        name_from_obj = from_obj(
            obj_name,
            expected=[str],
            path=path + '.name')  # type: Optional[str]
    else:
        name_from_obj = None

    obj_updated = obj.get('updated', None)
    if obj_updated is not None:
        updated_from_obj = from_obj(
            obj_updated,
            expected=[str],
            path=path + '.updated')  # type: Optional[str]
    else:
        updated_from_obj = None

    obj_url = obj.get('url', None)
    if obj_url is not None:
        url_from_obj = from_obj(
            obj_url,
            expected=[str],
            path=path + '.url')  # type: Optional[str]
    else:
        url_from_obj = None

    return ModelsCalendarICalendar(
        auth_account_id=auth_account_id_from_obj,
        auth_household_id=auth_household_id_from_obj,
        created=created_from_obj,
        ics=ics_from_obj,
        id=id_from_obj,
        name=name_from_obj,
        updated=updated_from_obj,
        url=url_from_obj)


def models_calendar_i_calendar_to_jsonable(
        models_calendar_i_calendar: ModelsCalendarICalendar,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ModelsCalendarICalendar.

    :param models_calendar_i_calendar: instance of ModelsCalendarICalendar to be JSON-ized
    :param path: path to the models_calendar_i_calendar used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if models_calendar_i_calendar.auth_account_id is not None:
        res['authAccountID'] = models_calendar_i_calendar.auth_account_id

    if models_calendar_i_calendar.auth_household_id is not None:
        res['authHouseholdID'] = models_calendar_i_calendar.auth_household_id

    if models_calendar_i_calendar.created is not None:
        res['created'] = models_calendar_i_calendar.created

    if models_calendar_i_calendar.ics is not None:
        res['ics'] = models_calendar_i_calendar.ics

    if models_calendar_i_calendar.id is not None:
        res['id'] = models_calendar_i_calendar.id

    if models_calendar_i_calendar.name is not None:
        res['name'] = models_calendar_i_calendar.name

    if models_calendar_i_calendar.updated is not None:
        res['updated'] = models_calendar_i_calendar.updated

    if models_calendar_i_calendar.url is not None:
        res['url'] = models_calendar_i_calendar.url

    return res


class UuidNullUUID:
    def __init__(
            self,
            uuid: Optional[str] = None,
            valid: Optional[bool] = None) -> None:
        """Initializes with the given values."""
        self.uuid = uuid

        # Valid is true if UUID is not NULL
        self.valid = valid

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to uuid_null_u_u_id_to_jsonable.

        :return: JSON-able representation
        """
        return uuid_null_u_u_id_to_jsonable(self)


def new_uuid_null_u_u_id() -> UuidNullUUID:
    """Generates an instance of UuidNullUUID with default values."""
    return UuidNullUUID()


def uuid_null_u_u_id_from_obj(obj: Any, path: str = "") -> UuidNullUUID:
    """
    Generates an instance of UuidNullUUID from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of UuidNullUUID
    :param path: path to the object used for debugging
    :return: parsed instance of UuidNullUUID
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    obj_uuid = obj.get('uuid', None)
    if obj_uuid is not None:
        uuid_from_obj = from_obj(
            obj_uuid,
            expected=[str],
            path=path + '.uuid')  # type: Optional[str]
    else:
        uuid_from_obj = None

    obj_valid = obj.get('valid', None)
    if obj_valid is not None:
        valid_from_obj = from_obj(
            obj_valid,
            expected=[bool],
            path=path + '.valid')  # type: Optional[bool]
    else:
        valid_from_obj = None

    return UuidNullUUID(
        uuid=uuid_from_obj,
        valid=valid_from_obj)


def uuid_null_u_u_id_to_jsonable(
        uuid_null_u_u_id: UuidNullUUID,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of UuidNullUUID.

    :param uuid_null_u_u_id: instance of UuidNullUUID to be JSON-ized
    :param path: path to the uuid_null_u_u_id used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if uuid_null_u_u_id.uuid is not None:
        res['uuid'] = uuid_null_u_u_id.uuid

    if uuid_null_u_u_id.valid is not None:
        res['valid'] = uuid_null_u_u_id.valid

    return res


class RemoteCaller:
    """Executes the remote calls to the server."""

    def __init__(
        self,
        url_prefix: str,
        auth: Optional[requests.auth.AuthBase] = None,
        session: Optional[requests.Session] = None) -> None:
        self.url_prefix = url_prefix
        self.auth = auth
        self.session = session

        if not self.session:
            self.session = requests.Session()
            self.session.auth = self.auth

    def auth_accounts_read(self) -> Any:
        """
        Send a get request to /api/v1/auth/accounts.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/accounts'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_create(
            self,
            body: 'AuthAccount') -> Any:
        """
        Send a post request to /api/v1/auth/accounts.

        :param body: AuthAccount

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/accounts'

        data = to_jsonable(
            body,
            expected=[AuthAccount])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/auth/accounts/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/accounts/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_account_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/auth/accounts/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/accounts/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_update(
            self,
            body: 'AuthAccount',
            id: str) -> Any:
        """
        Send a put request to /api/v1/auth/accounts/{id}.

        :param body: AuthAccount
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/accounts/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[AuthAccount])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_keys_update(
            self,
            body: 'AuthAccount',
            id: str) -> Any:
        """
        Send a put request to /api/v1/auth/accounts/{id}/keys.

        :param body: AuthAccount
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/accounts/',
            str(id),
            '/keys'])

        data = to_jsonable(
            body,
            expected=[AuthAccount])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_t_o_t_p_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/auth/accounts/{id}/totp.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/accounts/',
            str(id),
            '/totp'])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_t_o_t_p_create(
            self,
            id: str) -> Any:
        """
        Send a post request to /api/v1/auth/accounts/{id}/totp.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/accounts/',
            str(id),
            '/totp'])

        resp = self.session.request(
            method='post',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_t_o_t_p_update(
            self,
            body: 'AuthAccount',
            id: str) -> Any:
        """
        Send a put request to /api/v1/auth/accounts/{id}/totp.

        :param body: AuthAccount
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/accounts/',
            str(id),
            '/totp'])

        data = to_jsonable(
            body,
            expected=[AuthAccount])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_households_read(self) -> Any:
        """
        Send a get request to /api/v1/auth/households.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/households'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_household_create(
            self,
            body: 'AuthHousehold') -> Any:
        """
        Send a post request to /api/v1/auth/households.

        :param body: AuthHousehold

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/households'

        data = to_jsonable(
            body,
            expected=[AuthHousehold])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_household_member_delete(
            self,
            auth_account_id: str,
            auth_household_id: str) -> 'Response':
        """
        Send a delete request to /api/v1/auth/households/{auth_household_id}/members/{auth_account_id}.

        :param auth_account_id: AuthAccountID
        :param auth_household_id: AuthHouseholdID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/households/',
            str(auth_household_id),
            '/members/',
            str(auth_account_id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_household_member_update(
            self,
            auth_account_id: str,
            auth_household_id: str,
            body: 'AuthAccount') -> 'Response':
        """
        Send a put request to /api/v1/auth/households/{auth_household_id}/members/{auth_account_id}.

        :param auth_account_id: AuthAccountID
        :param auth_household_id: AuthHouseholdID
        :param body: AuthAccount

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/households/',
            str(auth_household_id),
            '/members/',
            str(auth_account_id)])

        data = to_jsonable(
            body,
            expected=[AuthAccount])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_household_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/auth/households/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/households/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_household_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/auth/households/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/households/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_household_update(
            self,
            body: 'AuthHousehold',
            id: str) -> Any:
        """
        Send a put request to /api/v1/auth/households/{id}.

        :param body: AuthHousehold
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/households/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[AuthHousehold])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_household_invite_create(
            self,
            body: 'AuthAccount',
            id: str) -> 'Response':
        """
        Send a post request to /api/v1/auth/households/{id}/invites.

        :param body: AuthAccountAuthHousehold
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/households/',
            str(id),
            '/invites'])

        data = to_jsonable(
            body,
            expected=[AuthAccount])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_household_invite_delete(
            self,
            id: str,
            token: str) -> 'Response':
        """
        Send a delete request to /api/v1/auth/households/{id}/invites/{token}.

        :param id: ID
        :param token: Token

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/households/',
            str(id),
            '/invites/',
            str(token)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_household_invite_accept(
            self,
            id: str,
            token: str) -> 'Response':
        """
        Send a get request to /api/v1/auth/households/{id}/invites/{token}.

        :param id: ID
        :param token: Token

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/households/',
            str(id),
            '/invites/',
            str(token)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_session_delete_all(self) -> 'Response':
        """
        Send a delete request to /api/v1/auth/sessions.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/sessions'

        resp = self.session.request(method='delete', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_session_read(self) -> Any:
        """
        Send a get request to /api/v1/auth/sessions.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/sessions'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_session_create(
            self,
            body: 'AuthSession') -> Any:
        """
        Send a post request to /api/v1/auth/sessions.

        :param body: AuthSession

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/sessions'

        data = to_jsonable(
            body,
            expected=[AuthSession])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_session_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/auth/sessions/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/sessions/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def auth_session_update(
            self,
            body: 'AuthSession',
            id: str) -> Any:
        """
        Send a put request to /api/v1/auth/sessions/{id}.

        :param body: AuthSession
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/sessions/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[AuthSession])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_sign_in_read(self) -> Any:
        """
        Send a get request to /api/v1/auth/signin.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/signin'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_sign_in_create(
            self,
            body: 'AuthAccount') -> Any:
        """
        Requires emailAddress and password

        :param body: AuthAccount

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/signin'

        data = to_jsonable(
            body,
            expected=[AuthAccount])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_verify_read(
            self,
            body: 'AuthAccount') -> Any:
        """
        Send a get request to /api/v1/auth/verify.

        :param body: AuthAccount

        :return: OK
        """
        url = self.url_prefix + '/api/v1/auth/verify'

        data = to_jsonable(
            body,
            expected=[AuthAccount])


        resp = self.session.request(
            method='get',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def auth_account_verify_update(
            self,
            id: str,
            token: str) -> 'Response':
        """
        Send a put request to /api/v1/auth/verify/{id}/{token}.

        :param id: ID
        :param token: Verification token

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/auth/verify/',
            str(id),
            '/',
            str(token)])

        resp = self.session.request(
            method='put',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def bookmarks_read(self) -> Any:
        """
        Send a get request to /api/v1/bookmarks.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/bookmarks'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def bookmark_create(
            self,
            body: 'Bookmark') -> Any:
        """
        Send a post request to /api/v1/bookmarks.

        :param body: Bookmark

        :return: OK
        """
        url = self.url_prefix + '/api/v1/bookmarks'

        data = to_jsonable(
            body,
            expected=[Bookmark])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def bookmark_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/bookmarks/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/bookmarks/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def bookmark_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/bookmarks/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/bookmarks/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def bookmark_update(
            self,
            body: 'Bookmark',
            id: str) -> Any:
        """
        Send a put request to /api/v1/bookmarks/{id}.

        :param body: Bookmark
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/bookmarks/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[Bookmark])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_accounts_read(self) -> Any:
        """
        Send a get request to /api/v1/budget/accounts.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/accounts'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_account_create(
            self,
            body: 'BudgetAccount') -> Any:
        """
        Send a post request to /api/v1/budget/accounts.

        :param body: BudgetAccount

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/accounts'

        data = to_jsonable(
            body,
            expected=[BudgetAccount])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_account_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/budget/accounts/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/accounts/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def budget_account_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/budget/accounts/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/accounts/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_account_update(
            self,
            body: 'BudgetAccount',
            id: str) -> Any:
        """
        Send a put request to /api/v1/budget/accounts/{id}.

        :param body: BudgetAccount
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/accounts/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[BudgetAccount])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_account_reconcile(
            self,
            id: str) -> Any:
        """
        Send a post request to /api/v1/budget/accounts/{id}/reconcile.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/accounts/',
            str(id),
            '/reconcile'])

        resp = self.session.request(
            method='post',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_transactions_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/budget/accounts/{id}/transactions.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/accounts/',
            str(id),
            '/transactions'])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_categories_read(self) -> Any:
        """
        Send a get request to /api/v1/budget/categories.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/categories'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_category_create(
            self,
            body: 'BudgetCategory') -> Any:
        """
        Send a post request to /api/v1/budget/categories.

        :param body: BudgetCategory

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/categories'

        data = to_jsonable(
            body,
            expected=[BudgetCategory])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_category_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/budget/categories/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/categories/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def budget_category_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/budget/categories/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/categories/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_category_update(
            self,
            body: 'BudgetCategory',
            id: str) -> Any:
        """
        Send a put request to /api/v1/budget/categories/{id}.

        :param body: BudgetCategory
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/categories/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[BudgetCategory])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_transactions_read_category(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/budget/categories/{id}/transactions.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/categories/',
            str(id),
            '/transactions'])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_month_category_create(
            self,
            body: 'BudgetMonthCategory') -> Any:
        """
        Send a post request to /api/v1/budget/month-categories.

        :param body: BudgetMonthCategory

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/month-categories'

        data = to_jsonable(
            body,
            expected=[BudgetMonthCategory])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_month_category_update(
            self,
            body: 'BudgetMonthCategory') -> Any:
        """
        Send a put request to /api/v1/budget/month-categories.

        :param body: BudgetMonthCategory

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/month-categories'

        data = to_jsonable(
            body,
            expected=[BudgetMonthCategory])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_month_read(
            self,
            year_month: str) -> Any:
        """
        Send a get request to /api/v1/budget/months/{yearMonth}.

        :param year_month: yearMonth

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/months/',
            str(year_month)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_payees_read(self) -> Any:
        """
        Send a get request to /api/v1/budget/payees.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/payees'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_payee_create(
            self,
            body: 'BudgetPayee') -> Any:
        """
        Send a post request to /api/v1/budget/payees.

        :param body: BudgetPayee

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/payees'

        data = to_jsonable(
            body,
            expected=[BudgetPayee])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_payee_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/budget/payees/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/payees/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def budget_payee_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/budget/payees/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/payees/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_payee_update(
            self,
            body: 'BudgetPayee',
            id: str) -> Any:
        """
        Send a put request to /api/v1/budget/payees/{id}.

        :param body: BudgetPayee
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/payees/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[BudgetPayee])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_transactions_read_payee(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/budget/payees/{id}/transactions.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/payees/',
            str(id),
            '/transactions'])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_recurrences_read(self) -> Any:
        """
        Send a get request to /api/v1/budget/recurrences.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/recurrences'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_recurrence_create(
            self,
            body: 'BudgetRecurrence') -> Any:
        """
        Send a post request to /api/v1/budget/recurrences.

        :param body: BudgetRecurrence

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/recurrences'

        data = to_jsonable(
            body,
            expected=[BudgetRecurrence])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_recurrence_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/budget/recurrences/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/recurrences/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def budget_recurrence_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/budget/recurrences/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/recurrences/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_recurrence_update(
            self,
            body: 'BudgetRecurrence',
            id: str) -> Any:
        """
        Send a put request to /api/v1/budget/recurrences/{id}.

        :param body: BudgetRecurrence
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/recurrences/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[BudgetRecurrence])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_transaction_create(
            self,
            body: 'BudgetTransaction') -> Any:
        """
        Send a post request to /api/v1/budget/transactions.

        :param body: BudgetTransaction

        :return: OK
        """
        url = self.url_prefix + '/api/v1/budget/transactions'

        data = to_jsonable(
            body,
            expected=[BudgetTransaction])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def budget_transaction_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/budget/transactions/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/transactions/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def budget_transaction_update(
            self,
            body: 'BudgetTransaction',
            id: str) -> Any:
        """
        Send a put request to /api/v1/budget/transactions/{id}.

        :param body: BudgetTransaction
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/budget/transactions/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[BudgetTransaction])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def calendar_events_read(self) -> Any:
        """
        Send a get request to /api/v1/calendar/events.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/calendar/events'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def calendar_event_create(
            self,
            body: 'CalendarEvent') -> Any:
        """
        Send a post request to /api/v1/calendar/events.

        :param body: CalendarEvent

        :return: OK
        """
        url = self.url_prefix + '/api/v1/calendar/events'

        data = to_jsonable(
            body,
            expected=[CalendarEvent])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def calendar_event_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/calendar/events/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/calendar/events/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def calendar_event_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/calendar/events/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/calendar/events/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def calendar_event_update(
            self,
            body: 'CalendarEvent',
            id: str) -> Any:
        """
        Send a put request to /api/v1/calendar/events/{id}.

        :param body: CalendarEvent
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/calendar/events/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[CalendarEvent])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def calendar_i_calendars_read(self) -> Any:
        """
        Send a get request to /api/v1/calendar/icalendars.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/calendar/icalendars'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def calendar_i_calendar_create(
            self,
            body: 'ModelsCalendarICalendar') -> Any:
        """
        Send a post request to /api/v1/calendar/icalendars.

        :param body: CalendarICalendar

        :return: OK
        """
        url = self.url_prefix + '/api/v1/calendar/icalendars'

        data = to_jsonable(
            body,
            expected=[ModelsCalendarICalendar])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def calendar_i_calendar_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/calendar/icalendars/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/calendar/icalendars/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def calendar_i_calendar_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/calendar/icalendars/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/calendar/icalendars/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def calendar_i_calendar_update(
            self,
            body: 'ModelsCalendarICalendar',
            id: str) -> Any:
        """
        Send a put request to /api/v1/calendar/icalendars/{id}.

        :param body: CalendarICalendar
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/calendar/icalendars/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[ModelsCalendarICalendar])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def changes_read(self) -> Any:
        """
        Send a get request to /api/v1/changes.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/changes'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def change_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/changes/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/changes/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_meal_plans_read(self) -> Any:
        """
        Send a get request to /api/v1/cook/meal-plans.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/cook/meal-plans'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_meal_plan_create(
            self,
            body: 'CookMealPlan') -> Any:
        """
        Send a post request to /api/v1/cook/meal-plans.

        :param body: CookMealPlan

        :return: OK
        """
        url = self.url_prefix + '/api/v1/cook/meal-plans'

        data = to_jsonable(
            body,
            expected=[CookMealPlan])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_meal_plan_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/cook/meal-plans/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/meal-plans/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def cook_meal_plan_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/cook/meal-plans/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/meal-plans/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_meal_plan_update(
            self,
            body: 'CookMealPlan',
            id: str) -> Any:
        """
        Send a put request to /api/v1/cook/meal-plans/{id}.

        :param body: CookMealPlan
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/meal-plans/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[CookMealPlan])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_meal_times_read(self) -> Any:
        """
        Send a get request to /api/v1/cook/meal-times.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/cook/meal-times'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_meal_time_create(
            self,
            body: 'CookMealTime') -> Any:
        """
        Send a post request to /api/v1/cook/meal-times.

        :param body: CookMealTime

        :return: OK
        """
        url = self.url_prefix + '/api/v1/cook/meal-times'

        data = to_jsonable(
            body,
            expected=[CookMealTime])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_meal_time_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/cook/meal-times/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/meal-times/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def cook_meal_time_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/cook/meal-times/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/meal-times/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_meal_time_update(
            self,
            body: 'CookMealTime',
            id: str) -> Any:
        """
        Send a put request to /api/v1/cook/meal-times/{id}.

        :param body: CookMealTime
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/meal-times/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[CookMealTime])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_recipes_read(self) -> Any:
        """
        Send a get request to /api/v1/cook/recipes.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/cook/recipes'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_recipe_create(
            self,
            body: 'CookRecipe') -> Any:
        """
        Send a post request to /api/v1/cook/recipes.

        :param body: CookRecipe

        :return: OK
        """
        url = self.url_prefix + '/api/v1/cook/recipes'

        data = to_jsonable(
            body,
            expected=[CookRecipe])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_recipe_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/cook/recipes/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/recipes/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def cook_recipe_read(
            self,
            id: str) -> Any:
        """
        Can read recipes marked public unauthenticated

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/recipes/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def cook_recipe_update(
            self,
            body: 'CookRecipe',
            id: str) -> Any:
        """
        Send a put request to /api/v1/cook/recipes/{id}.

        :param body: CookRecipe
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/cook/recipes/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[CookRecipe])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_items_read(self) -> Any:
        """
        Send a get request to /api/v1/health/items.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/health/items'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_item_create(
            self,
            body: 'HealthItem') -> Any:
        """
        Send a post request to /api/v1/health/items.

        :param body: HealthItem

        :return: OK
        """
        url = self.url_prefix + '/api/v1/health/items'

        data = to_jsonable(
            body,
            expected=[HealthItem])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_items_init(self) -> Any:
        """
        Send a put request to /api/v1/health/items.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/health/items'

        resp = self.session.request(method='put', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_item_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/health/items/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/health/items/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def health_item_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/health/items/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/health/items/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_item_update(
            self,
            body: 'HealthItem',
            id: str) -> Any:
        """
        Send a put request to /api/v1/health/items/{id}.

        :param body: HealthItem
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/health/items/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[HealthItem])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_logs_read(self) -> Any:
        """
        Send a get request to /api/v1/health/logs.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/health/logs'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_log_create(
            self,
            body: 'HealthLog') -> Any:
        """
        Send a post request to /api/v1/health/logs.

        :param body: HealthLog

        :return: OK
        """
        url = self.url_prefix + '/api/v1/health/logs'

        data = to_jsonable(
            body,
            expected=[HealthLog])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_log_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/health/logs/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/health/logs/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def health_log_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/health/logs/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/health/logs/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def health_log_update(
            self,
            body: 'HealthLog',
            id: str) -> Any:
        """
        Send a put request to /api/v1/health/logs/{id}.

        :param body: HealthLog
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/health/logs/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[HealthLog])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def inventory_collections_read(self) -> Any:
        """
        Send a get request to /api/v1/inventory/collections.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/inventory/collections'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def inventory_collection_create(
            self,
            body: 'InventoryCollection') -> Any:
        """
        Send a post request to /api/v1/inventory/collections.

        :param body: InventoryCollection

        :return: OK
        """
        url = self.url_prefix + '/api/v1/inventory/collections'

        data = to_jsonable(
            body,
            expected=[InventoryCollection])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def inventory_collection_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/inventory/collections/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/inventory/collections/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def inventory_collection_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/inventory/collections/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/inventory/collections/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def inventory_collection_update(
            self,
            body: 'InventoryCollection',
            id: str) -> Any:
        """
        Send a put request to /api/v1/inventory/collections/{id}.

        :param body: InventoryCollection
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/inventory/collections/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[InventoryCollection])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def inventory_items_read(self) -> Any:
        """
        Send a get request to /api/v1/inventory/items.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/inventory/items'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def inventory_item_create(
            self,
            body: 'InventoryItem') -> Any:
        """
        Send a post request to /api/v1/inventory/items.

        :param body: InventoryItem

        :return: OK
        """
        url = self.url_prefix + '/api/v1/inventory/items'

        data = to_jsonable(
            body,
            expected=[InventoryItem])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def inventory_item_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/inventory/items/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/inventory/items/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def inventory_item_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/inventory/items/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/inventory/items/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def inventory_item_update(
            self,
            body: 'InventoryItem',
            id: str) -> Any:
        """
        Send a put request to /api/v1/inventory/items/{id}.

        :param body: InventoryItem
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/inventory/items/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[InventoryItem])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def notes_page_versions_read(self) -> Any:
        """
        Send a get request to /api/v1/notes/page-versions.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/notes/page-versions'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def notes_page_version_create(
            self,
            body: 'NotesPageVersion') -> Any:
        """
        Send a post request to /api/v1/notes/page-versions.

        :param body: NotesPageVersion

        :return: OK
        """
        url = self.url_prefix + '/api/v1/notes/page-versions'

        data = to_jsonable(
            body,
            expected=[NotesPageVersion])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def notes_page_version_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/notes/page-versions/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/notes/page-versions/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def notes_page_version_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/notes/page-versions/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/notes/page-versions/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def notes_pages_read(self) -> Any:
        """
        Send a get request to /api/v1/notes/pages.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/notes/pages'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def notes_page_create(
            self,
            body: 'NotesPage') -> Any:
        """
        Send a post request to /api/v1/notes/pages.

        :param body: NotesPage

        :return: OK
        """
        url = self.url_prefix + '/api/v1/notes/pages'

        data = to_jsonable(
            body,
            expected=[NotesPage])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def notes_page_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/notes/pages/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/notes/pages/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def notes_page_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/notes/pages/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/notes/pages/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def notes_page_update(
            self,
            body: 'NotesPage',
            id: str) -> Any:
        """
        Send a put request to /api/v1/notes/pages/{id}.

        :param body: NotesPage
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/notes/pages/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[NotesPage])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def plan_projects_read(self) -> Any:
        """
        Send a get request to /api/v1/plan/projects.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/plan/projects'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def plan_project_create(
            self,
            body: 'PlanProject') -> Any:
        """
        Send a post request to /api/v1/plan/projects.

        :param body: PlanProject

        :return: OK
        """
        url = self.url_prefix + '/api/v1/plan/projects'

        data = to_jsonable(
            body,
            expected=[PlanProject])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def plan_project_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/plan/projects/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/plan/projects/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def plan_project_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/plan/projects/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/plan/projects/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def plan_project_update(
            self,
            body: 'PlanProject',
            id: str) -> Any:
        """
        Send a put request to /api/v1/plan/projects/{id}.

        :param body: PlanProject
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/plan/projects/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[PlanProject])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def plan_tasks_read(self) -> Any:
        """
        Send a get request to /api/v1/plan/tasks.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/plan/tasks'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def plan_task_create(
            self,
            body: 'PlanTask') -> Any:
        """
        Send a post request to /api/v1/plan/tasks.

        :param body: PlanTask

        :return: OK
        """
        url = self.url_prefix + '/api/v1/plan/tasks'

        data = to_jsonable(
            body,
            expected=[PlanTask])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def plan_task_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/plan/tasks/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/plan/tasks/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def plan_task_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/plan/tasks/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/plan/tasks/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def plan_task_update(
            self,
            body: 'PlanTask',
            id: str) -> Any:
        """
        Send a put request to /api/v1/plan/tasks/{id}.

        :param body: PlanTask
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/plan/tasks/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[PlanTask])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def reward_cards_read(self) -> Any:
        """
        Send a get request to /api/v1/reward/cards.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/reward/cards'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def reward_card_create(
            self,
            body: 'RewardCard') -> Any:
        """
        Send a post request to /api/v1/reward/cards.

        :param body: RewardCard

        :return: OK
        """
        url = self.url_prefix + '/api/v1/reward/cards'

        data = to_jsonable(
            body,
            expected=[RewardCard])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def reward_card_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/reward/cards/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/reward/cards/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def reward_card_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/reward/cards/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/reward/cards/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def reward_card_update(
            self,
            body: 'RewardCard',
            id: str) -> Any:
        """
        Send a put request to /api/v1/reward/cards/{id}.

        :param body: RewardCard
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/reward/cards/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[RewardCard])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def secrets_values_read(self) -> Any:
        """
        Send a get request to /api/v1/secrets/values.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/secrets/values'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def secrets_value_create(
            self,
            body: 'SecretsValue') -> Any:
        """
        Send a post request to /api/v1/secrets/values.

        :param body: SecretsValue

        :return: OK
        """
        url = self.url_prefix + '/api/v1/secrets/values'

        data = to_jsonable(
            body,
            expected=[SecretsValue])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def secrets_value_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/secrets/values/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/secrets/values/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def secrets_value_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/secrets/values/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/secrets/values/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def secrets_value_update(
            self,
            body: 'SecretsValue',
            id: str) -> Any:
        """
        Send a put request to /api/v1/secrets/values/{id}.

        :param body: SecretsValue
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/secrets/values/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[SecretsValue])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def secrets_vaults_read(self) -> Any:
        """
        Send a get request to /api/v1/secrets/vaults.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/secrets/vaults'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def secrets_vault_create(
            self,
            body: 'SecretsVault') -> Any:
        """
        Send a post request to /api/v1/secrets/vaults.

        :param body: SecretsVault

        :return: OK
        """
        url = self.url_prefix + '/api/v1/secrets/vaults'

        data = to_jsonable(
            body,
            expected=[SecretsVault])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def secrets_vault_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/secrets/vaults/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/secrets/vaults/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def secrets_vault_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/secrets/vaults/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/secrets/vaults/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def secrets_vault_update(
            self,
            body: 'SecretsVault',
            id: str) -> Any:
        """
        Send a put request to /api/v1/secrets/vaults/{id}.

        :param body: SecretsVault
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/secrets/vaults/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[SecretsVault])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_categories_read(self) -> Any:
        """
        Send a get request to /api/v1/shop/categories.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/shop/categories'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_category_create(
            self,
            body: 'ShopCategory') -> Any:
        """
        Send a post request to /api/v1/shop/categories.

        :param body: ShopCategory

        :return: OK
        """
        url = self.url_prefix + '/api/v1/shop/categories'

        data = to_jsonable(
            body,
            expected=[ShopCategory])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_category_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/shop/categories/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/categories/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def shop_category_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/shop/categories/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/categories/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_category_update(
            self,
            body: 'ShopCategory',
            id: str) -> Any:
        """
        Send a put request to /api/v1/shop/categories/{id}.

        :param body: ShopCategory
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/categories/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[ShopCategory])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_items_read(self) -> Any:
        """
        Send a get request to /api/v1/shop/items.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/shop/items'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_item_create(
            self,
            body: 'ShopItem') -> Any:
        """
        Send a post request to /api/v1/shop/items.

        :param body: ShopItem

        :return: OK
        """
        url = self.url_prefix + '/api/v1/shop/items'

        data = to_jsonable(
            body,
            expected=[ShopItem])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_item_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/shop/items/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/items/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def shop_item_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/shop/items/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/items/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_item_update(
            self,
            body: 'ShopItem',
            id: str) -> Any:
        """
        Send a put request to /api/v1/shop/items/{id}.

        :param body: ShopItem
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/items/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[ShopItem])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_lists_read(self) -> Any:
        """
        Send a get request to /api/v1/shop/lists.

        :return: OK
        """
        url = self.url_prefix + '/api/v1/shop/lists'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_list_create(
            self,
            body: 'ShopList') -> Any:
        """
        Send a post request to /api/v1/shop/lists.

        :param body: ShopList

        :return: OK
        """
        url = self.url_prefix + '/api/v1/shop/lists'

        data = to_jsonable(
            body,
            expected=[ShopList])


        resp = self.session.request(
            method='post',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_list_delete(
            self,
            id: str) -> 'Response':
        """
        Send a delete request to /api/v1/shop/lists/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/lists/',
            str(id)])

        resp = self.session.request(
            method='delete',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Response])

    def shop_list_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/shop/lists/{id}.

        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/lists/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def shop_list_update(
            self,
            body: 'ShopList',
            id: str) -> Any:
        """
        Send a put request to /api/v1/shop/lists/{id}.

        :param body: ShopList
        :param id: ID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/shop/lists/',
            str(id)])

        data = to_jsonable(
            body,
            expected=[ShopList])


        resp = self.session.request(
            method='put',
            url=url,
            json=data,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])

    def s_s_e_read(
            self,
            id: str) -> Any:
        """
        Send a get request to /api/v1/sse/{id}.

        :param id: AuthSessionID

        :return: OK
        """
        url = "".join([
            self.url_prefix,
            '/api/v1/sse/',
            str(id)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[Any])


# Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
