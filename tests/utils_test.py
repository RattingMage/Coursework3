from utils import *
import pytest


def test_load_json():
    assert type(get_posts_all()) == list
    assert len(get_posts_all()) > 0


def test_get_posts_by_user():
    assert type(get_posts_by_user("leo")) == list
    assert len(get_posts_by_user("leo")) >= 0


def test_get_comments_by_post_id():
    assert type(get_comments_by_post_id(1)) == list
    assert len(get_comments_by_post_id(1)) >= 0


def test_search_for_posts():
    assert type(search_for_posts('еда')) == list
    assert len(search_for_posts('еда')) >= 0


def test_get_post_by_pk():
    assert type(get_post_by_pk(1)) == dict
