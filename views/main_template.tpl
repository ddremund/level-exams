<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Leveling</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end

<h1>Enterprise Leveling Test Generator</h1>

Generate Test:<br />
<ul>
%for test in test_types:
<li><a href="/test/{{test['id']}}">{{test['name']}}</a></li>
%end
<li><a href="/test/custom">Custom Test</li>
</ul>

</body>
</html>

