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


</body>
</html>

