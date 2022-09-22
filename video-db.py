import json
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Api: for restful api creation
# Resource: used while creating class for RESTful functions
# reqparse: ReqParse is used to parse request parameters sent with requests
# abort: is used to abort the request when excepion is encountered
# fields: used to define variable type in serializable object
# marshal_with: used toserialize and unserialize objects
# SQLAlchemy: object relational mapping library

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True

db = SQLAlchemy(app)
# defining trable structues
class VideoModel(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    views= db.Column(db.Integer, nullable=False)
    likes= db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"


# db.create_all()
# for request variabole data parsing
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='name of video is required', required=True)
video_put_args.add_argument('views', type=int, help='views of video is required', required=True)
video_put_args.add_argument('likes', type=int, help='likes of video is required', required=True)

video_update_args=reqparse.RequestParser()
video_update_args.add_argument('name', type=str, help='name of video is required')
video_update_args.add_argument('views', type=int, help='views of video is required')
video_update_args.add_argument('likes', type=int, help='likes of video is required')

# in order to serialize the object
resourceFields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}

class Video(Resource):
    # in order to serialize the object
    @marshal_with(resourceFields)
    def get(self, videoId):
        # result = VideoModel.query.get(videoId)
        result = VideoModel.query.filter_by(id=videoId).first()
        if not result:
            abort(404, message="Video not found with that id")
        return result

    @marshal_with(resourceFields)
    def put(self, videoId):
        args = video_put_args.parse_args()
        result= VideoModel.query.filter_by(id=videoId).first()
        if result:
            abort(409, message="VideoId is already in use")

        video = VideoModel(id=videoId, name=args['name'], views = args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resourceFields)
    def patch(self, videoId):
        # args = video_put_args.parse_args()
        args = video_update_args.parse_args()
        result= VideoModel.query.filter_by(id=videoId).first()
        if not result:
            abort(404, message="Video not found with that id, cant update")
        if args["name"]:
            result.name = args["name"]
        if args["views"]:
            result.views = args["views"]
        if args["likes"]:
            result.likes = args["likes"]

        db.session.commit()
        return result

    def delete(self, videoId):
        result= VideoModel.query.filter_by(id=videoId).first()
        if not result:
            abort(404, message="Video not found with that id, cant delte")
        VideoModel.query.filter_by(id=videoId).delete()
        db.session.commit()

        return '', 204



api.add_resource(Video, "/video/<int:videoId>")



if __name__ == '__main__':
    app.run(debug=True)