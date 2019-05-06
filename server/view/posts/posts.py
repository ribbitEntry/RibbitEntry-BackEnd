import os

from flask import request, current_app
from flasgger import swag_from
from datetime import datetime
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.view import upload_files
from server.model.user import User
from server.model.post import Post
from server.extensions import db
from docs import POSTS_POST, POST_ELEMENT_DELETE, POST_ELEMENT_GET
from server.view import unicode_safe_json_dumps


# postId를 불러오지 않는 클래스 선언
class Posts(Resource):

    @swag_from(POSTS_POST)
    @jwt_required
    def post(self):
        userId = get_jwt_identity()
        content = request.form['content']
        nowaday = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 파일 유무 확인
        files = []
        try:
            first_file = request.files.get('file[1]')
            files.append(first_file)
        except:
            first_file = None
        try:
            second_file = request.files.get('file[2]')
            files.append(second_file)
        except:
            second_file = None
        try:
            third_file = request.files.get('file[3]')
            files.append(third_file)
        except:
            third_file = None
        try:
            fourth_file = request.files.get('file[4]')
            files.append(fourth_file)
        except:
            fourth_file = None

        if User.query.filter(User.id == userId).first():

            if content:
                post = Post(content=content, user=userId, date=nowaday)
                db.session.add(post)
                db.session.commit()

                if files:
                    before_post = Post.query.filter(
                        Post.user == userId,
                        Post.date == nowaday,
                        Post.content == content
                    ).first()
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


# postId를 받아오는 GET, DELETE 메소드를 위한 클래스 선언
class PostElement(Resource):

    @swag_from(POST_ELEMENT_GET)
    @jwt_required
    def get(self, postId):
        pass

    @swag_from(POST_ELEMENT_DELETE)
    @jwt_required
    def delete(self, postId):

        # 계정 확인 커리문 필요(본인의 게시물만 삭제 가능)
        userId = get_jwt_identity()
        post = Post.query.filter(Post.post_id == postId).first()

        if User.query.filter(User.id == userId).first():
            if post.user == userId:
                post.delete()
                db.session.commit()
                path = current_app.config['UPLOAD_FOLDER_PATH'] + '/{}/{}/'.format(userId, postId)
                if os.path.exists(path):
                    os.rmdir(path)
                return unicode_safe_json_dumps({'status': '글이 삭제되었습니다.'}), 200
            else:
                return unicode_safe_json_dumps({'status': 'invalid post info'}), 404
        else:
            return unicode_safe_json_dumps({'status': '없는 글입니다.'}), 400
