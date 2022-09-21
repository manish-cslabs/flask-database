import json
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api = Api(app)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='name of video is required', required=True)
video_put_args.add_argument('views', type=str, help='views of video is required', required=True)
video_put_args.add_argument('likes', type=str, help='likes of video is required', required=True)

videos ={}

def abortIfNotExists(videoId):
    if videoId not in videos:
        abort(404, message ="video id not found")

def abortIfAlraedyExists(videoId):
    if videoId in videos:
        abort(409, message ="video with same id already exists")

class Video(Resource):
    def get(self, videoId):
        abortIfNotExists(videoId)
        return videos[videoId]

    def put(self, videoId):
        abortIfAlraedyExists(videoId)
        args = video_put_args.parse_args()
        videos[videoId] = args
        return videos[videoId], 201

    def delete(self, videoId):
        abortIfNotExists(videoId)
        del videos[videoId]
        return '', 204

api.add_resource(Video, "/video/<int:videoId>")



if __name__ == '__main__':
    app.run(debug=True)