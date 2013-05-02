<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Saved Leveling Tests</title>
</head>
<body>
%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
<a href="/">Home</a>

<h1>Enterprise Windows Leveling Test Generator</h1><br />

The following tests are frozen exactly as originally generated.

<table borders="1">
	<tr><th>Number</th><th>Template</th><th>Created By</th><th>Timestamp</th><th>Level</th><th>% Top Level Questions</th><th>Permalink</th></tr>
	%for i, test in enumerate(tests):
		<tr><td>{{i+1}}</td><td>{{test['template']}}</td><td>{{test['username']}}</td><td>{{test['timestamp']}}</td><td>{{test['level']}}</td><td>{{test['pct_top']}}</td><td><a href="http://leveling.rstnt.com/test/saved/{{test['_id']}}">Test {{i+1}}</a></td></tr>
	%end
</table>

</body>
</html>
