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

<h1>Enterprise Windows Leveling Test</h1><br />
Test Description: {{description}}<br /><br />

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
	<li>Q: [Level(s) {{', '.join(question['levels'])}}] {{question['question']}}<br />A: {{question['answer']}}<br />Notes: <br /><br /><br /><br /><br /></li>
	%end
</ol>
%end


</body>
</html>

