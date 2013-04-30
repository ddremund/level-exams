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
<h3>{{section}}</h3>
<ol>
	%for question in questions[section]:
	<li>Q: {{question['question']}}<br />A: {{question['answer'}}</li>
	%end
</ol>
%end


</body>
</html>

