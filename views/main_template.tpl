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

<a href="/newquestion"><b>Add Question to the Database</b></a><br />
<a href="/test/all"><b>View all questions</b></a><br />
<a href="/test/saved/all"><b>List of all saved tests</b></a><br />

<b>Generate Test from Template:</b><br /><br />
<ul>
%for test in test_types:
	<li><a href="/test/{{test['_id']}}">{{test['name']}}</a> | <a href="/test/remove/{{test['_id']}}">Remove</a></li>
%end
	<li><a href="/test/custom">Custom Test</a></li>
</ul>
<br />


</body>
</html>

