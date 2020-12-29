from flask import Blueprint, request
from functools import wraps
from trailhead_scraper import (
    fetch_profile_data,
    fetch_rank_data,
    fetch_awards,
)

# initialize the flask blueprint
bp = Blueprint("api", __name__)


def check_username_provided(f):
    """Verify that a username parameter has been provided in the request URL.

    Args:
        f (function): The function that will be executed if the username is provided.

    Returns:
        function: The wrapper function.
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        if "username" not in request.args:
            return {"error": "Username not provided"}, 400

        return f(*args, **kwargs)

    return wrapper


@bp.route("/profile")
@check_username_provided
def profile():
    """Retrieve Trailhead profile data for the specified username.

    Returns:
        dict: The profile data as a dictionary.
    """
    try:
        username = request.args.get("username", type=str)
        return fetch_profile_data(username)
    except Exception as e:
        return {"error": str(e)}, 400


@bp.route("/rank")
@check_username_provided
def rank():
    """Retrieve the rank information for the specified username or user id.

    Returns:
        dict: The rank information as a dictionary.
    """
    try:
        username = request.args.get("username", type=str)
        uid = request.args.get("uid", default=None, type=str)
        return fetch_rank_data(username, user_id=uid)
    except Exception as e:
        return {"error": str(e)}, 400


@bp.route("/awards")
@check_username_provided
def awards():
    """Retrieve a list of awards for the specified username or user id.

    Returns:
        dict: A dictionary containing the list of awards related to the user.
    """
    try:
        username = request.args.get("username", type=str)
        uid = request.args.get("uid", default=None, type=str)
        lim = request.args.get("limit", default=None, type=int)
        return {
            "awards": fetch_awards(username, user_id=uid, limit=lim),
        }
    except Exception as e:
        return {"error": str(e)}, 400
