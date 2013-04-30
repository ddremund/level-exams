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

<h1>Enterprise Windows Leveling Test Generator</h1>

Generate Test:<br />
<ul>
%for test in test_types:
<li><a href="/test/{{test['_id']}}">{{test['name']}}</a></li>
%end
<li><a href="/test/custom">Custom Test</li>
<li><a href="/test/all">All Questions</li>
</ul>

</body>
</html>

