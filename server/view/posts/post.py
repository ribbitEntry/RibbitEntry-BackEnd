from flask_restful import Resource
from flasgger import swag_from
from flask import request
from datetime import datetime
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.docs.posts import POST_POST, POST_DELETE
from server.extensions import db
from server.model.user import User
from server.model.post import Post
from server.view import unicode_safe_json_dumps, upload_files


class Posts(Resource):

    @swag_from(POST_POST)
    @jwt_required
    def post(self):
        userId = get_jwt_identity()
        content = request.form['content']
        nowaday = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 파일 유무 확인
        try:
            files = request.files.getlist("file")
        except:
            files = None

        if User.query.filter(User.id == userId).first():

            if content:
                post = Post(content=content, user=userId, date=nowaday)
                db.session.add(post)
                db.session.commit()
                print(nowaday)
                print(post)
                print(nowaday == post.date)

                if files:
                    before_post = Post.query.filter(Post.user == userId, Post.date == nowaday, Post.content == content).first()
                    postId = before_post.post_id

                    # 파일 업로드 및 링크 리스트 반환
                    urls = upload_files(files, userId, postId)
                    before_post.image = ','.join(urls)
                    db.session.commit()

                return unicode_safe_json_dumps({'status': '글 작성 완료'}, 201)

            else:
                return unicode_safe_json_dumps({'status': '내용을 작성해주세요'}, 400)

        else:
            return unicode_safe_json_dumps({'status': '일치하지 않는 인증 정보입니다.'}, 401)

    @swag_from(POST_DELETE)
    @jwt_required
    def delete(self):
        post_id = request.json['post_id']

        if Post.query.filter(Post.post_id == post_id):
            Post.query.filter(Post.post_id == post_id).delete()
            db.session.commit()
            return unicode_safe_json_dumps({'status': '글이 삭제되었습니다.'}, 200)
        else:
            unicode_safe_json_dumps({'status': '없는 글입니다.'}, 400)
