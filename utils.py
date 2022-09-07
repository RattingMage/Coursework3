import json


def get_comments_all():
    """
    Выгружает комментарии из JSON в list
    :return:
    """
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_all():
    """
    Выгружает посты из JSON в list
    :return:
    """
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    result = []
    posts = get_posts_all()
    for post in posts:
        if post['poster_name'] == user_name:
            result.append(post)
    if not result:
        raise ValueError
    else:
        return result


def get_comments_by_post_id(post_id):
    result = []
    comments = get_comments_all()
    for comment in comments:
        if comment['post_id'] == post_id:
            result.append(comment)
    if not result:
        raise ValueError
    else:
        return result


def search_for_posts(query):
    result = []
    answer = []
    st = ''
    counter = 0
    posts = get_posts_all()
    for post in posts:
        for sym in post['content']:
            if sym.isalpha():
                st += sym
            else:
                if len(st):
                    result.append(st)
                result.append(sym)
                st = ''
        if query in result and counter <= 10:
            answer.append(post)
            result = []
            counter += 1
        else:
            result = []
    return answer


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post


def good_count_comments(count):
    if count == 1:
        return "1 комментарий"
    if 2 <= count <= 4:
        return f"{count} комментария"
    if 5 <= count <= 20:
        return f"{count} комментариев"
    if count % 10 == 1:
        return f"{count} комментарий"
    if 2 <= count % 10 <= 4:
        return f"{count} комментария"
    if 5 <= count % 10 <= 9:
        return f"{count} комментариев"
    if count % 10 == 0:
        return f"{count} комментариев"
