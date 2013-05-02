<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Enterprise Windows Leveling</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
<a href="/">Home</a>

<h1>Enterprise Windows Leveling Test Generator</h1>

<b>Generate Test from Template:</b><br />
<ul>
%for test in test_types:
	<li><a href="/test/{{test['_id']}}">{{test['name']}}</a> | <a href="/test/remove/{{test['_id']}}">Remove</a></li>
%end
	<li><a href="/test/custom">Custom Test</li>
	<li><a href="/test/all">All Questions</li>
</ul>
<br />
<a href="/newquestion">Add Question</a>

</body>
</html>

