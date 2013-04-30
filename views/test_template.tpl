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
Test Description: {{description}}<br />
Total Questions: {{sum(len(q) for q in questions.values())}}

%for section in questions.keys():
<hr />
<h3>{{section}} - {{len(questions[section])}} questions</h3>
<ol>
	%for question in questions[section]:
	<li>Q: [Level(s) {{', '.join(question['levels'])}}] {{question['question']}}<br />A: {{question['answer']}}<br />Notes: <br /><br /><br /><br /><br /></li>
	%end
</ol>
%end


</body>
</html>

