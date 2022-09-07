import pytest
from app import view_api_post, view_api_index


def test_view_api_index():
    assert type(view_api_index()) == list
    posts = view_api_index()
    assert posts[0]["pk"] == 1


def test_view_api_post():
    assert type(view_api_post()) == dict
    post = view_api_post()
    assert post["pk"] == 1
