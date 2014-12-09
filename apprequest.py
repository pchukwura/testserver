from flask import Flask, request
from flask import Response

import datetime, json, pytz

app = Flask(__name__)
app.debug = True


@app.route('/workouts/')
def get_workout():
	sport = request.args.get('sport', 'basketball')
	workout_date = request.args.get('date')

	if workout_date is None or len(workout_date) == 0:
		return Response('Missing date parameter', status=400)


	f = open('workouts.json', 'r')
	workout_json = f.read()
	print 'FILE: {0}'.format(workout_json)
	f.close()

	workout_dict = json.loads(workout_json)

	todays_workouts = workout_dict[workout_date]

	print workout_dict

	if todays_workouts is None:
		return Response(json.dumps({}), status=200, mimetype='application/json')

	workout = todays_workouts[sport]
	return Response(json.dumps(workout), status=200, mimetype='application/json')



# @app.route("/workouts/", methods=['POST', 'GET'])
# def fetch_workout():
# 	sport = request.args.get('sport', 'basketball')

# 	basketball_workout = {'id' : 'bbb', 'sport' : 'basketball', 'name' : 'Basketball Workout', 'description' : 'This is an example basketball workout',
# 		'details' : 'These are example details', 'date' : datetime.datetime.now(pytz.utc).isoformat(),
# 		'coverImgURL' : 'http://greatiphonewallpapers.com/uploads/iPhone%20Wallpaper/Sports/Air%20jordan%207.jpg'}

# 	baseball_workout = {'id' : 'aaa', 'sport' : 'baseball', 'name' : 'Baseball Workout', 'description' : 'This is an example baseball workout',
# 		'details' : 'These are example details', 'date' : datetime.datetime.now(pytz.utc).isoformat(),
# 		'coverImgURL' : 'http://greatiphonewallpapers.com/uploads/iPhone%20Wallpaper/Sports/Air%20jordan%207.jpg'}

# 	football_workout = {'id' : 'fff', 'sport' : 'football', 'name' : 'Baseball Workout', 'description' : 'This is an example football workout',
# 		'details' : 'These are example details', 'date' : datetime.datetime.now(pytz.utc).isoformat(),
# 		'coverImgURL' : 'http://greatiphonewallpapers.com/uploads/iPhone%20Wallpaper/Sports/Air%20jordan%207.jpg'}

# 	drills = [{'id' : '111', 'name' : 'Burpees', 'duration' : 90,
# 		'coverImgURL' : 'http://1.bp.blogspot.com/-I9tIS9p7mk8/Uz1ctF7DOTI/AAAAAAAAWYA/n1QKC7xzxKA/s1600/re2pect-jordan-brand-pays-tribute-to-derek-jeter-last-season-01.jpg'}]

# 	drills.append({'id' : '333', 'name' : 'Pushups', 'duration' : 30,
# 		'coverImgURL' : 'http://sports.cbsimg.net/images/visual/whatshot/02152013b_michael_jordan.jpg'})

# 	drills.append({'id' : '222', 'name' : 'Jumping Jacks', 'duration' : 120,
# 		'coverImgURL' : 'http://sports.cbsimg.net/images/visual/whatshot/02152013b_michael_jordan.jpg'})


# 	basketball_workout['drills'] = drills
# 	baseball_workout['drills'] = drills
# 	football_workout['drills'] = drills

# 	sport_workouts = {'basketball' : {'workouts' : [basketball_workout]}, 'baseball' : {'workouts' : [baseball_workout]},
# 		'football' : {'workouts' : [football_workout]}}

# 	selected_workout = sport_workouts.get(sport)
# 	if selected_workout is None:
# 		workouts = sport_workouts['basketball']
# 	else:
# 		workouts = selected_workout
	

	
# 	return Response(json.dumps(workouts), status=200, mimetype='application/json')

@app.route("/user/workout/", methods=['POST'])
def workout_complete():
	user_id = request.form.get('userID')
	workout_id = request.form.get('workoutID')

	print workout_id
	return Response(json.dumps({}), status=200, mimetype='application/json')


if __name__ == '__main__':
	app.run()