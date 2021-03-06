<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Enterprise Windows Leveling</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a> | <a href="/change_password">Change Password</a>
%end

<h1>Enterprise Windows Leveling Test Generator</h1>

<b>Questions in Database:</b>
<table>
	%for topic, count, l1, l2, l3 in question_counts:
	<tr><td>{{topic}}: </td><td>{{count}} </td><td>(L1: {{l1}}, L2: {{l2}}, L3: {{l3}})</td></tr>
	%end
	<tr><td>Total: </td><td>{{sum([item[1] for item in question_counts])}}</td></tr>
</table>
<br />
<a href="/newquestion"><b>Add Question to the Database</b></a><br />
<a href="/test/all"><b>View all questions</b></a><br />
<a href="/test/saved/all"><b>List of all saved tests</b></a><br /><br />

<b>Generate Test from Template:</b><br />
<ul>
%for test in test_types:
	<li><a href="/test/{{test['_id']}}">{{test['name']}}</a> | {{test['username']}} | <a href="/test/custom/{{test['_id']}}">Edit</a> | <a href="/test/remove/{{test['_id']}}">Remove</a></li>
%end
	<li><a href="/test/custom">Create New Template</a></li>
</ul>
<br />


</body>
</html>

