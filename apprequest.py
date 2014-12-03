from flask import Flask, request
from flask import Response

import datetime, json, pytz

app = Flask(__name__)
app.debug = True

@app.route("/workouts/", methods=['POST', 'GET'])
def fetch_workout():
	workout = {'id' : 'ccc', 'sport' : 'basketball', 'name' : 'Test Workout', 'description' : 'This is an example workout',
		'details' : 'These are example details', 'date' : datetime.datetime.now(pytz.utc).isoformat(),
		'coverImgURL' : 'http://greatiphonewallpapers.com/uploads/iPhone%20Wallpaper/Sports/Air%20jordan%207.jpg'}

	drills = [{'id' : '111', 'name' : 'Planking', 'duration' : 90,
		'coverImgURL' : 'http://1.bp.blogspot.com/-I9tIS9p7mk8/Uz1ctF7DOTI/AAAAAAAAWYA/n1QKC7xzxKA/s1600/re2pect-jordan-brand-pays-tribute-to-derek-jeter-last-season-01.jpg'}]

	drills.append({'id' : '333', 'name' : 'Sit-Ups', 'duration' : 30,
		'coverImgURL' : 'http://sports.cbsimg.net/images/visual/whatshot/02152013b_michael_jordan.jpg'})

	drills.append({'id' : '222', 'name' : 'Jumping Jacks', 'duration' : 120,
		'coverImgURL' : 'http://sports.cbsimg.net/images/visual/whatshot/02152013b_michael_jordan.jpg'})




	workout['drills'] = drills
	workouts = {'workouts' : [workout]}
	

	
	return Response(json.dumps(workouts), status=200, mimetype='application/json')

@app.route("/user/workout/", methods=['POST'])
def workout_complete():
	user_id = request.form.get('userID')
	workout_id = request.form.get('workoutID')

	print workout_id
	return Response(json.dumps({}), status=200, mimetype='application/json')


if __name__ == '__main__':
	app.run()