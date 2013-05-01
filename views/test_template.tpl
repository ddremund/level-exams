<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Leveling Test: {{description}}</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
<a href="/">Home</a>

<h1>Enterprise Windows Leveling Test</h1><br />
Test Description: {{description}}<br />
Created by: {{username}}<br />
Candidate Name:<br />
<br /><br />

<table>
	<tr align="left"><th>Topic</th><th>Questions</th></tr>
	%for topic in questions.keys():
	<tr><td>{{topic}}</td><td>{{len(questions[topic])}}</td></tr>
	%end
	<tr><td>Total</td><td>{{sum(len(q) for q in questions.values())}}</td></tr>
</table>

%for topic in questions.keys():
<hr />
<h3>{{topic}} - {{len(questions[topic])}} questions</h3>
<ol>
	%for question in questions[topic]:
	<li><b>Q:</b> [Level {{'/'.join(question['levels'])}}] {{!"<br />".join(question['question'].split('\n'))}}<br />Image URL: {{question['image_url']}}<br /><br /><b>A:</b> {{!"<br />".join(question['answer'].split('\n'))}}<br /><a href="/question/{{question['_id']}}">Edit Question</a> | <a href="/question/remove/{{question['_id']}}">Delete Question from Database</a><br /><b>Notes:</b> <br /><br /><br /><br /><br /></li>
	%end
</ol>
%end

<hr />
<br />
Images:<br /><br />
%for topic in questions.keys():
	%for i, question in enumerate(questions[topic]):
		%if not question["image_url"] == "":
			Image for {{topic}} question #{{i + 1}}: {{question["image_url"]}}<br />
			<img src="{{!question['image_url']}}" /><br />
		%end
	%end
%end

</body>
</html>
